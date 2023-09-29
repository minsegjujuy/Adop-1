import React, { useState, useEffect } from "react";
import { BASE_APP } from "../../../../utils/contants";
import { Button, Form, Checkbox } from "semantic-ui-react";
import { useVigilancia, useAuth } from "../../../../hooks";
import { MapView } from "../../Mapa/react-leaflet";
import { useFormik } from "formik";
import * as Yup from "yup";
// import { useAuth} from "../../hooks";
import { toast } from "react-toastify";
import Swal from "sweetalert2";
import "./AddVigilancia.scss";
export function AddVigilancia(props) {
  const [position, setposition] = useState({
    lat: -24.715631490415,
    lng: -65.0051351026728,
  });
  const { addHorarios } = props;
  const { auth } = useAuth();
  const [formHorario, setformHorario] = useState(null);

  const {
    addVigilancia,
    get_regionales,
    get_jurisdicciones,
    get_motivos,
    get_tipo_servicios,
    get_recursos,
  } = useVigilancia();
  // const {auth}=useAuth();
  // const {actualizar_contra,actualizar_contra_admin} =useContrasena();

  const [regional, setRegional] = useState(null);
  const [jurisdiccion, setJurisdiccion] = useState(null);
  const [motivo, setMotivo] = useState(null);
  const [tipo_servicio, setTipoServocio] = useState(null);
  const [recurso, setRecurso] = useState(null);

  useEffect(() => {
    buscarRegionales();
    buscarMotivos();
    buscarTipoServocios();
    buscarRecursos();
    if (auth.usuario.unidad_regional === null) {
      buscarJurisdicciones(0);
    } else {
      buscarJurisdicciones(auth.usuario.unidad_regional);
    }
  }, []);

  const buscarRegionales = async () => {
    const options = await get_regionales();
    setRegional(options.map((option) => option));
  };
  const buscarJurisdicciones = async (id) => {
    const options = await get_jurisdicciones(id);

    setJurisdiccion(options.map((option) => option));
  };
  const buscarMotivos = async () => {
    const options = await get_motivos();
    setMotivo(options.map((option) => option));
  };
  const buscarTipoServocios = async () => {
    const options = await get_tipo_servicios();
    setTipoServocio(options.map((option) => option));
  };
  const buscarRecursos = async () => {
    const options = await get_recursos();
    setRecurso(options.map((option) => option));
  };

  const regionales = regional?.map((res, index) => ({
    value: res.id,
    key: `${index}`,
    text: res.unidad_regional,
  }));
  const jurisdicciones = jurisdiccion?.map((res, index) => ({
    value: res.id,
    key: `${index}`,
    text: res.jurisdiccion,
  }));
  const motivos = motivo?.map((res, index) => ({
    value: res.id,
    key: `${index}`,
    text: res.motivo,
  }));
  const tipos_servicios = tipo_servicio?.map((res, index) => ({
    value: res.id,
    key: `${index}`,
    text: res.tipo_servicio,
  }));
  const recursos = recurso?.map((res, index) => ({
    value: res.id,
    key: `${index}`,
    text: res.tipo_recurso,
  }));

  const formik = useFormik({
    initialValues: initialValues(auth),
    validationSchema: Yup.object(validationSchema()),
    onSubmit: async (formValue) => {
      try {
        const objeto = {
          fk_jurisdiccion: formValue.juridiccion,
          fk_motivo: formValue.motivo,
          fk_tipo_servicio: formValue.tipo_servicio,
          // fk_tipo_recurso: formValue.recursos,
          fk_unidad_regional: formValue.regional,
          objetivo: formValue.objetivo,
          cant_dias: 0,
          fecha_inicio: formValue.fecha_inicio,
          fecha_fin: formValue.fecha_fin,
          destino: formValue.destino,
          latitud: position.lat.toFixed(6),
          longitud: position.lng.toFixed(6),
        };
        if (formValue.fecha_indefinida === true) {
          objeto.fecha_fin = null;
        }

        console.log(formHorario);
        console.log(objeto);
        console.log(jurisdicciones);
        const response = await addVigilancia(objeto);

        if (response.msj) {
          Swal.fire({
            title: "Exito!",
            text: response.msj,
            icon: "success",
            timer: 3000,
            showConfirmButton: true,
          });
          window.location.replace(`${BASE_APP}/admin/vigilancia`);
        } else {
          Swal.fire({
            title: "Algunos datos ingresados no son validos!",
            text: response.msj,
            icon: "error",
            showConfirmButton: true,
          });
        }
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <Form onSubmit={formik.handleSubmit}>
      {auth?.usuario?.rol === 3 && (
        <div className="field">
          <label>Regional</label>
          <div className="disable">
            <Form.Input
              name="regional"
              value={formik.values.regional}
              // placeholder={`UNIDAD REGIONAL ${formik.values.regional}`}
              // onChange={buscarJurisdicciones(formik.values.regional)}
              error={formik.errors.regional}
            />
          </div>
        </div>
      )}
      {auth?.usuario?.rol === 1 && (
        <div className="field">
          <label>Regional</label>

          <Form.Select
            fluid
            name="regional"
            options={regionales ? regionales : 0}
            placeholder="Seleccione la regional"
            value={formik.values.regional}
            onChange={(_, data) => {
              formik.setFieldValue("regional", data.value);
              buscarJurisdicciones(data.value);
            }}
            // onChange = {(event) => console.log(event)}
          />
        </div>
      )}
      <div className="two fields">
        <div className="field">
          <label>Juridiccion</label>
          <Form.Select
            search
            name="juridiccion"
            options={jurisdicciones ? jurisdicciones : 0}
            placeholder="Seleccione la juridiccion"
            value={formik.values.juridiccion}
            onChange={(_, data) =>
              formik.setFieldValue("juridiccion", data.value)
            }
          />
        </div>
        <div className="field">
          <label>Motivo</label>
          <div className="field">
            <Form.Select
              name="motivo"
              options={motivos ? motivos : 0}
              placeholder="Seleccione el motivo"
              value={formik.values.motivo}
              onChange={(_, data) => formik.setFieldValue("motivo", data.value)}
            />
          </div>
        </div>
      </div>
      <div className="field">
        <label>Tipo Servicio</label>
        <div className="fields">
          <Form.Select
            name="tipo_servicio"
            options={tipos_servicios ? tipos_servicios : 0}
            placeholder="Seleccione el tipo de servicio "
            value={formik.values.tipo_servicio}
            onChange={(_, data) =>
              formik.setFieldValue("tipo_servicio", data.value)
            }
          />
        </div>
      </div>
      <div className="two fields">
        <div className="field">
          <label>Objetivo</label>
          <Form.TextArea
            name="objetivo"
            placeholder="Escriba un objetivo"
            value={formik.values.objetivo}
            onChange={formik.handleChange}
            error={formik.errors.objetivo}
          />
        </div>
      </div>
      <h4 className="ui dividing header">Fechas de vigilancia</h4>
      <div className="two fields">
        <div className="field">
          <label>Fecha de inicio</label>
          <Form.Input
            name="fecha_inicio"
            type="date"
            value={formik.values.fecha_inicio}
            onChange={formik.handleChange}
            error={formik.errors.fecha_inicio}
          />
        </div>
        <div className="two fields">
          {formik.values.fecha_indefinida === false && (
            <div className="field">
              <label>Fecha fin de vigilancia</label>
              <Form.Input
                name="fecha_fin"
                type="date"
                value={formik.values.fecha_fin}
                onChange={formik.handleChange}
                error={formik.errors.fecha_fin}
              />
            </div>
          )}
          <div className="field">
            <label>Fecha de fin de vigilancia indefinida</label>
            <div className="field">
              <div className="add-edit-user-form__staff">
                <Checkbox
                  toggle
                  checked={formik.values.fecha_indefinida}
                  onChange={(_, data) => {
                    formik.setFieldValue("fecha_indefinida", data.checked);
                  }}
                />{" "}
                Indefinida
              </div>
            </div>
          </div>
        </div>
      </div>

      <h4 className="ui dividing header">Recursos</h4>
      <div className="two fields">
        <div className="field">
          <label>Destino</label>
          <Form.Input
            name="destino"
            placeholder="Indique el destino"
            value={formik.values.destino}
            onChange={formik.handleChange}
            error={formik.errors.destino}
          />
        </div>
        <div className="field">
          <label>Recursos</label>
          <div className="field">
            <Form.Select
              name="recursos"
              options={recursos}
              placeholder="Seleccione los recursos "
              value={formik.values.recursos}
              onChange={(_, data) => formik.setFieldValue("recursos", data.value)}
              multiple={true}
            />
          </div>
        </div>
      </div>
      <h4 className="ui dividing header">Ubicacion de la vigilancia</h4>
      <div className="two fields">
        <MapView position={position} setposition={setposition} />
      </div>

      <div className="boton_crear_vigilancia">
        <Button
          className="positive button"
          type="submit"
          content={"Crear Vigilancia"}
        />
      </div>
    </Form>
  );
}

function initialValues(auth) {
  return {
    regional: auth?.usuario?.rol === 3 ? auth.usuario.unidad_regional : "",
    juridiccion: "",
    motivo: "",
    tipo_servicio: "",
    objetivo: "",
    cantidad_dias: 0,
    fecha_inicio: "",
    fecha_fin: null,
    fecha_indefinida: false,
    // hora_inicio:"",
    // hora_fin:"",
    destino: "",
    recursos: [],
    latitud: "",
    longitud: "",
    file: "",
  };
}

function validationSchema() {
  return {
    juridiccion: Yup.number().required("Seleccione una Juridiccion"),
    // motivo: Yup.number().required("Seleccione un Motivo"),
    // tipo_servicio: Yup.number().required("Seleccione un Tipo de Servicio"),
    // Objetivo:Yup.string().required("Escriba un objetivo para la vigilancia"),
    // fecha_inicio: Yup.date().required("La fecha de inicio es requerida"),
    // destino: Yup.string().required("Escriba un destino"),
    // recursos: Yup.number().required("Seleccione un recurso")
  };
}
