import React from "react";
import { HeaderPage } from "../../../components/Admin";
import "./Propiedad.scss";

export function Propiedad() {
  return (
    <>
      <HeaderPage title="Analisis de Propiedad 2022" />
      <div className="header-page-usuarios">
        {/* <div className='agregar'>
              <Button positive onClick={()=>console.log("hola mundo")}>
                {"AGREGAR"}
              </Button>
              </div>
               */}
      </div>
      <div className="vigilancia_escuelas">
        <iframe
          title="Analisis-Propiedad-2022"
          width="1300"
          height="800"
          src="https://app.powerbi.com/view?r=eyJrIjoiMzk5OTNmNjItNmMwMC00Y2UyLWFkZDgtMWFlNzY2YjVjNjEyIiwidCI6ImFlMzg5MGQyLTdhYjYtNDk4NC05NGIwLWQ2NmMzYmE0ZTEzOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>
    </>
  );
}
