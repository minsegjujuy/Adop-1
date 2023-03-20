import {AdminLayout} from "../layouts/AdminLayout"
// import { Home } from "../pages/Client";
import { HomeAdmin,UserAdmin} from "../pages/Admin"; 
import {LoginAdmin} from "../pages/Admin/LoginAdmin"



const routerLogin = [
  {
    path: "/",
    layout: AdminLayout,
    component: HomeAdmin,
  },
  {
    path: "/admin/users",
    layout: AdminLayout,
    component: UserAdmin,
  },
];

export default routerLogin;
