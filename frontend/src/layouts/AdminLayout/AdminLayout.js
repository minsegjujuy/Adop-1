import React, { Children,useEffect, useState } from "react";
import "./AdminLayout.scss";
import {logoutApi} from "../../api/user"
import {removeToken} from "../../api/token"
import { LoginAdmin } from "../../pages/Admin";
import { useAuth } from "../../hooks";
import { TopMenu, SideBarMenu } from "../../components/Admin";

export function AdminLayout(props) {
   const { children } = props;
   const {auth,setAuth} = useAuth();
   const {logueado,setLogueado}=useState(true);
  console.log(auth)
  console.log(document.referrer)
  const [logueo,setLogueo]= useState(document.referrer? true:false)
  console.log(logueo)
  // useEffect(() => {
  //   if(logueo===false){
  //     removeToken();
  //     setAuth(null);
  //     logoutApi(auth.token);
  //     setLogueo(true)
  //   }
  
  // }, []);
  if ((!auth || logueo===false)){
    // removeToken();
    // setAuth(null);
    // logoutApi(auth.token);
  // window.location.replace("http://localhost:3000/login")
   return <LoginAdmin />;
  }
  return (
    <div className="admin-layout">
      <div className="admin-layout__menu">
        <TopMenu />
      </div>

      <div className="admin-layout__main-content">
        <SideBarMenu >
          {children}
        </SideBarMenu>
       
      </div>
    </div>
  );
}
