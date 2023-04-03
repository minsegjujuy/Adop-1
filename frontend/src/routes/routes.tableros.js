import {AdminLayout} from "../layouts/AdminLayout"
// import { Home } from "../pages/Client";
import {Tableros} from "../pages/Tableros"; 
import {CargaVigilancia} from "../pages/Vigilancia"
import {LoginAdmin} from "../pages/Admin/LoginAdmin"



const routerTableros = [
  {
    path: "/admin/tableros",
    layout: AdminLayout,
    component: Tableros,
  },
//   {
//     path: "/admin/carga/vigilancia",
//     layout: AdminLayout,
//     component: CargaVigilancia,
//   }
];

export default routerTableros;
