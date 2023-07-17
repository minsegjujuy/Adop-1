import React from "react";
import { HeaderPage } from "../../../components/Admin";
import "./Contravencion.scss";

export function Contravencion() {
 
  return (
    <>
      <HeaderPage title="Contravencion General" />
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
          title="Contravencion General"
          width="1300" 
         height="800" 
          src="https://app.powerbi.com/view?r=eyJrIjoiNzMyNmM0ZTgtNzYyMi00YmVmLWE2YzgtZWM5OGEzZTMxYWM2IiwidCI6ImFlMzg5MGQyLTdhYjYtNDk4NC05NGIwLWQ2NmMzYmE0ZTEzOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>
     
    </>
  );
}
