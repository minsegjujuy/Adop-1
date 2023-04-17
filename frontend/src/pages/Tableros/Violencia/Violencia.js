import React from "react";
import { HeaderPage } from "../../../components/Admin";
import "./Violencia.scss";


export function Violencia() {

  return (
    <>
      <HeaderPage title="Violencia General" />
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
          title="Tablero General final - violencia"
          width="1300" 
          height="800" 
          src="https://app.powerbi.com/view?r=eyJrIjoiYjBlMjljZWUtYWYxZS00ZjNlLWI0NGYtZTVlOTBiYjc5MmJiIiwidCI6ImFlMzg5MGQyLTdhYjYtNDk4NC05NGIwLWQ2NmMzYmE0ZTEzOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>

    </>
  );
}
