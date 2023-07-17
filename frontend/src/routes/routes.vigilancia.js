import {AdminLayout} from "../layouts/AdminLayout"
import { HomeAdmin} from "../pages/Admin"; 
import {CargaVigilancia,AsignarPersonal} from "../pages/Vigilancia"



const routerVigilancia = [
  {
    path: "/admin/vigilancia",
    layout: AdminLayout,
    component: HomeAdmin,
  },{
    path: "/admin/carga/vigilancia",
    layout: AdminLayout,
    component: CargaVigilancia,
  },
  {
    path: "/admin/carga/vigilancia/personal",
    layout: AdminLayout,
    component: AsignarPersonal,
  }
];

export default routerVigilancia;
