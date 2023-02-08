import { ClientLayout } from "../layouts/ClientLayout";
import { Home } from "../pages/Client";

const routesPanel = [
  {
    path: "/admin/panel",
    layout: ClientLayout,
    component: Home,
  },
];
export default routesPanel;
