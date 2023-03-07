import {AdminLayout} from "../layouts/AdminLayout"
// import { Home } from "../pages/Client";
import { HomeAdmin,UserAdmin} from "../pages/Admin"; 
import {CargaVigilancia} from "../pages/Vigilancia"
import {LoginAdmin} from "../pages/Admin/LoginAdmin"



const routerVigilancia = [
  {
    path: "/admin/vigilancia",
    layout: AdminLayout,
    component: HomeAdmin,
  },{
    path: "/admin/carga/vigilancia",
    layout: AdminLayout,
    component: CargaVigilancia,
  }
];

export default routerVigilancia;
