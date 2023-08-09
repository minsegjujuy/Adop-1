import React, { Children, useEffect, useState } from "react";
import "./AdminLayout.scss";
import { logoutApi } from "../../api/user";
import { removeToken } from "../../api/token";
import { LoginAdmin } from "../../pages/Admin";
import { useAuth } from "../../hooks";
import { TopMenu, SideBarMenu } from "../../components/Admin";

export function AdminLayout(props) {
  const { children } = props;
  const { auth, logout } = useAuth();
  console.log(auth);
  const [logueo, setLogueo] = useState(document.referrer ? true : false);

  if (!auth) {
    console.log("hola mundo");
    return <LoginAdmin />;
  }
  // } else {
  //   if (logueo === false && performance.navigation.type === 0) {
  //     console.log("hola2")
  //     if (localStorage.length !== 0) {
  //       console.log("hola3")
  //       logout();
  //     } else {
  //       console.log("hola4")
  //       return <LoginAdmin />;
  //     }
  //   }
  // }
  return (
    <div className="trancision">
      <div className="admin-layout">
        <div className="admin-layout__menu">
          <TopMenu />
        </div>

        <div className="admin-layout__main-content">
          <SideBarMenu>{children}</SideBarMenu>
        </div>
        {/* <div className="admin-layout__footer">
        <Footer/>
      </div> */}
      </div>
    </div>
  );
}
