import {AdminLayout} from "../layouts/AdminLayout"
import {Escuelas,Propiedad,Contravencion,Violencia} from "../pages/Tableros"; 




const routerTableros = [
  {
    path: "/admin/tableros/escuelas",
    layout: AdminLayout,
    component: Escuelas,
  },
  {
    path: "/admin/tableros/propiedad",
    layout: AdminLayout,
    component: Propiedad,
  },
  {
    path: "/admin/tableros/contravencion",
    layout: AdminLayout,
    component: Contravencion,
  },
  {
    path: "/admin/tableros/violencia",
    layout: AdminLayout,
    component: Violencia,
  }

];

export default routerTableros;
