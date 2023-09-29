import {
  //* Jurisdicciones
  getJurisdicciones,

  //* Unidades Regionales
  getRegionales,

  //* Motivos
  getMotivos,

  //* Tipos Recursos
  getTipoRecursos,

  //* Tipo Servicios
  getTipoServicios,

  //* Vigilancias
  addVigilanciaApi,
  getVigilancias,
  deleteVigilanciaApi,

  //* Turnos
  addTurnosApi,
  getTurno,
  getTurnosApi,
  deleteHistorialApi,

  //* Documentos
  addDocumentoVigilancia,
  getDocumentosVigilancia,
  getDocumentoVigilancia,
  updateDocumentoVigilancia,
  deleteDocumentoVigilancia,

  //* Personal
  getPersonal,
  asignarPersonal,
} from "../api/vigilancia";
import { useState } from "react";
import { useAuth } from "../hooks";

export function useVigilancia() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [vigilancias, setVigilancias] = useState(null);
  const [historial, setHistorial] = useState([]);
  // const [personal, setPersonal] = useState(null);
  const [turno, setTurno] = useState(null);
  const { auth } = useAuth();

  //* Jurisdicciones
  const get_jurisdicciones = async (id) => {
    try {
      setLoading(true);
      const resultado = await getJurisdicciones(auth.token, id);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Unidades Regionales
  const get_regionales = async () => {
    try {
      setLoading(true);
      const resultado = await getRegionales(auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Motivos
  const get_motivos = async () => {
    try {
      setLoading(true);
      const resultado = await getMotivos(auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Tipo Regursos
  const get_recursos = async () => {
    try {
      setLoading(true);
      const resultado = await getTipoRecursos(auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Tipo Servicios
  const get_tipo_servicios = async () => {
    try {
      setLoading(true);
      const resultado = await getTipoServicios(auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Vigilancias
  const addVigilancia = async (data) => {
    try {
      setLoading(true);
      const resultado = await addVigilanciaApi(data, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const get_vigilancia = async (data) => {
    try {
      setLoading(true);
      const resultado = await getVigilancias(auth.token);
      setLoading(false);
      setVigilancias(resultado);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const deleteVigilancia = async (id) => {
    try {
      setLoading(true);
      await deleteVigilanciaApi(id, auth.token);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Turnos
  const add_turnos = async (data, fk_vigilancia) => {
    try {
      setLoading(true);
      const resultado = await addTurnosApi(data, fk_vigilancia, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const get_turno = async (id) => {
    try {
      setLoading(true);
      const resultado = await getTurno(auth.token, id);
      setTurno(resultado);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const get_turnos = async (id) => {
    try {
      setLoading(true);
      const resultado = await getTurnosApi(id, auth.token);
      setLoading(false);
      setHistorial(resultado.turnos);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const deleteHistorial = async (id, id_turno) => {
    try {
      setLoading(true);
      await deleteHistorialApi(id, id_turno, auth.token);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Documentos
  const add_documentos = async (data) => {
    try {
      setLoading(true);
      const resultado = await addDocumentoVigilancia(data, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const get_documentos = async (fk_vigilancia) => {
    try {
      setLoading(true);
      const resultado = await getDocumentosVigilancia(fk_vigilancia, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const get_documento = async (fk_vigilancia, id_documento) => {
    try {
      setLoading(true);
      const resultado = await getDocumentoVigilancia(fk_vigilancia, id_documento, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const delete_documento = async (id, fk_vigilancia) => {
    try {
      setLoading(true);
      const resultado = await deleteDocumentoVigilancia(fk_vigilancia ,id ,auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const update_documento = async (data, id, fk_vigilancia) => {
    try {
      setLoading(true);
      const resultado = await updateDocumentoVigilancia(data, id, fk_vigilancia, auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  //* Personal
  const get_personal = async (data) => {
    try {
      setLoading(true);
      const resultado = await getPersonal(auth.token);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };
  const asignar_personal = async (data, id) => {
    try {
      setLoading(true);
      const resultado = await asignarPersonal(data, auth.token, id);
      setLoading(false);
      return resultado;
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  return {
    loading,
    error,
    vigilancias,
    turno,
    historial,
    auth,

    //* Jurisdicciones
    get_jurisdicciones,
    
    //* Unidades Regionales
    get_regionales,
    
    //* Motivos
    get_motivos,
    
    //* Tipo Recursos
    get_recursos,
    
    //* Tipo Servicios
    get_tipo_servicios,
    
    //* Vigilancias
    addVigilancia,
    get_vigilancia,
    deleteVigilancia,
    
    //* Turnos
    add_turnos,
    get_turno,
    get_turnos,
    deleteHistorial,
    
    //* Documentos
    add_documentos,
    get_documentos,
    get_documento,
    delete_documento,
    update_documento,
    
    //* Personal
    get_personal,
    asignar_personal,
  };
}
