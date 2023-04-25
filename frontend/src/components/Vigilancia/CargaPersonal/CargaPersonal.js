// import React, { useState ,useEffect} from "react";
// import { Button, Form, Icon,Checkbox, Input } from "semantic-ui-react";
// import { useFormik } from "formik";
// import * as Yup from "yup";
// // import { useAuth} from "../../hooks";
// import { toast, Flip } from "react-toastify";
// import Swal from "sweetalert2";
// import "./CargaPersonal.scss"
// export function CargaPersonal(props) {
    
   
//   const formik = useFormik({
//     initialValues: initialValues(),
//     validationSchema: Yup.object(validationSchema()),
//     onSubmit: async (formValue) => {
//       try {
//        console.log(formValue)
//       } catch (error) {
      
//         toast.error(error.message);
//       }
//     },
//   });

//   return (
//    <Form>
//     <div class="ui form">
//     <div class="two fields">
//       <div class="field">
//         <label>First Name</label>
//         <Input
//          placeholder="Read Only"
//           readonly="" type="text"/>
//       </div>
//       <div class="field">
//         <label>Last Name</label>
//         <Input
//          placeholder="Read Only"
//           readonly="" type="text"/>
//       </div>
//     </div>
//   </div>
//   </Form> 
//   );
// }

// function initialValues() {
//   return {
//     fecha:""
//   }
// }

// function validationSchema() {
//   return {
//     // password: Yup.string().required(true),
//     // nuevacontraseña: Yup.string().required(true),
//   };
// }
