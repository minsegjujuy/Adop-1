import React, { Children } from "react";
import "./AdminLayout.scss";
import { LoginAdmin } from "../../pages/Admin";
import { useAuth } from "../../hooks";
import { TopMenu, SideBarMenu } from "../../components/Admin";

export function AdminLayout(props) {
   const { children } = props;
   const {auth} = useAuth();
  console.log(auth)
  if (!auth) return <LoginAdmin />;
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
