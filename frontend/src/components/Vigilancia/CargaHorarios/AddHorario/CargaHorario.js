import { useFormik } from "formik";
import { Form, Button, Checkbox } from "semantic-ui-react";
import { useVigilancia } from "../../../../hooks";
import Swal from "sweetalert2";
import * as Yup from "yup";
import "./CargaHorario.scss";

export const CargaHorario = (props) => {
  const { onClose, fecha_fin, fecha_inicio, id } = props;
  const { add_turnos } = useVigilancia();
  let turnos = [];
  const horarios = [
    { key: "1", text: "8 horas", value: 8 },
    { key: "2", text: "12 horas", value: 12 },
    { key: "3", text: "16 horas", value: 16 },
  ];

  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: Yup.object(newSchema()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
        if (formValue.lunes === true) {
          turnos.push("lunes");
        }
        if (formValue.martes === true) {
          turnos.push("martes");
        }
        if (formValue.miercoles === true) {
          turnos.push("miercoles");
        }
        if (formValue.jueves === true) {
          turnos.push("jueves");
        }
        if (formValue.viernes === true) {
          turnos.push("viernes");
        }
        if (formValue.sabado === true) {
          turnos.push("sabado");
        }
        if (formValue.domingo === true) {
          turnos.push("domingo");
        }

        const formValue2 = {
          turno: formValue.diario === true ? null : turnos,
          dia_completo: formValue.turno_completo,
          fecha_fin: fecha_fin,
          fecha_inicio: fecha_inicio,
          fk_vigilancia: id,
          diario: formValue.diario,
          hora_inicio: formValue.turno_completo ? null : formValue.hora_inicio,
          duracion: formValue.turno_completo ? null : formValue.duracion,
        };

        const response = await add_turnos(formValue2);
        if (response.msj) {
          Swal.fire({
            title: "Exito!",
            text: response.msj,
            icon: "success",
            timer: 3000,
            showConfirmButton: true,
          });
          window.location.replace("http://localhost:3000/admin/vigilancia");
        } else {
          Swal.fire({
            title: "Algunos datos ingresados no son validos!",
            text: response.msj,
            icon: "error",
            showConfirmButton: true,
          });
        }
        onClose();
      } catch (error) {}
    },
  });

  return (
    <Form className="add-edit-use-form" onSubmit={formik.handleSubmit}>
      <div>
        {!formik.values.diario && (
          <div className="seven fields">
            <div className="field">
              <label>Lunes </label>
              <div className="field">
                <Checkbox
                  checked={formik.values.lunes}
                  onChange={(event, data) =>
                    formik.setFieldValue("lunes", data.checked)
                  }
                />
              </div>
            </div>

            <div className="field">
              <label>Martes</label>
              <Checkbox
                checked={formik.values.martes}
                onChange={(event, data) =>
                  formik.setFieldValue("martes", data.checked)
                }
              />
            </div>

            <div className="field">
              <label>Miercoles</label>
              <Checkbox
                checked={formik.values.miercoles}
                onChange={(event, data) =>
                  formik.setFieldValue("miercoles", data.checked)
                }
              />
            </div>

            <div className="field">
              <label>Jueves</label>
              <div className="field">
                <Checkbox
                  checked={formik.values.jueves}
                  onChange={(event, data) =>
                    formik.setFieldValue("jueves", data.checked)
                  }
                />
              </div>
            </div>

            <div className="field">
              <label>Viernes</label>
              <Checkbox
                checked={formik.values.viernes}
                onChange={(event, data) =>
                  formik.setFieldValue("viernes", data.checked)
                }
              />
            </div>

            <div className="field">
              <label>Sabado</label>
              <Checkbox
                checked={formik.values.sabado}
                onChange={(event, data) =>
                  formik.setFieldValue("sabado", data.checked)
                }
              />
            </div>

            <div className="field">
              <label>Domingo</label>
              <Checkbox
                checked={formik.values.domingo}
                onChange={(event, data) =>
                  formik.setFieldValue("domingo", data.checked)
                }
              />
            </div>
          </div>
        )}
        <div className="field">
          <label>Vigilancia Diaria</label>
          <Checkbox
            toggle
            checked={formik.values.diario}
            onChange={(_, data) => {
              formik.setFieldValue("diario", data.checked);
            }}
          />
        </div>

        <div className="three fields">
          <div className="field">
            <label>Dia completo </label>

            <div className="field">
              <Checkbox
                toggle
                checked={formik.values.turno_completo}
                onChange={(_, data) => {
                  formik.setFieldValue("turno_completo", data.checked);
                }}
              />{" "}
            </div>
          </div>
          {formik.values.turno_completo === false && (
            <div className="field">
              <label>Hora de inicio</label>
              <Form.Input
                name="hora_inicio"
                type="time"
                placeholder="Ingrese hora inicio"
                value={formik.values.hora_inicio}
                onChange={formik.handleChange}
                error={formik.errors.hora_inicio}
              />
            </div>
          )}
          {formik.values.turno_completo === false && (
            <div className="field">
              <label>Duracion del Turno</label>
              <div className="field">
                <Form.Select
                  fluid
                  name="duracion"
                  options={horarios}
                  placeholder="Seleccione"
                  value={formik.values.duracion}
                  onChange={(_, data) =>
                    formik.setFieldValue("duracion", data.value)
                  }
                />
                {/* <Form.Input
                  name="hora_fin"
                  type="time"
                  placeholder="Ingrese hora final"
                  value={formik.values.hora_fin}
                  onChange={formik.handleChange}
                  error={formik.errors.hora_fin}
                /> */}
              </div>
            </div>
          )}
        </div>
      </div>
      <Button type="submit" primary fluid content={"Asignar "} />
    </Form>
  );
};

function initialValues(Turnos) {
  return {
    lunes: false,
    martes: false,
    miercoles: false,
    jueves: false,
    viernes: false,
    sabado: false,
    domingo: false,
    turno_completo: false,
    diario: false,
    hora_inicio: "",
    duracion: "",
  };
}
function newSchema() {
  return {
    hora_inicial: Yup.string(),
  };
}
