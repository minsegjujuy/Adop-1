import routerLogin from "./routes.client";
import routesPanel from "./routes.panel";
import routerVigilancia from "./routes.vigilancia";
import routerTableros from "./routes.tableros";
// import { Error404, MensajeEmailVerificado,MensajeEmailVencido } from "../pages";
// import { Error404Layout, EmailVerificado,EmailVencido } from "../layouts";

const routes = [
  ...routerLogin,
  ...routesPanel,
  ...routerVigilancia,
  ...routerTableros,
  // {
  //   path: "/validado",
  //   layout: EmailVerificado,
  //   component: MensajeEmailVerificado,
  // },
  // {
  //   path: "/vencido",
  //   layout: EmailVencido,
  //   component: MensajeEmailVencido,
  // },
  // {
  //   path: "*",
  //   layout: Error404Layout,
  //   component: Error404,
  // },
];

export default routes;
