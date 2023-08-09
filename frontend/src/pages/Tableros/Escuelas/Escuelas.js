import React from "react";
import { HeaderPage } from "../../../components/Admin";
import "./Escuelas.scss";

export function Escuelas() {
  return (
    <>
      <HeaderPage title="VIGILANCIA Y ESCUELAS" />
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
          title="ADOP - Vigilancia y Escuelas"
          width="1300"
          height="800"
          src="https://app.powerbi.com/view?r=eyJrIjoiNmNkYWM0YjQtZDUyMC00MjdmLWJkZjUtNGUzMjBiMDY0NTI5IiwidCI6ImFlMzg5MGQyLTdhYjYtNDk4NC05NGIwLWQ2NmMzYmE0ZTEzOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>
    </>
  );
}
