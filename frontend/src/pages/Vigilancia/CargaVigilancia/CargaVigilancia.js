import React from 'react'
import {HeaderPage} from "../../../components/Admin"
import {Button} from "semantic-ui-react"
import {AddVigilancia} from "../../../components/Vigilancia/CargaVigilancia"
import {TableVigilancia} from "../../../components/Vigilancia/TableVigilancia"
import {CargaHorario} from "../../../components/Vigilancia/CargaHorarios"
import {ModalBasic} from "../../../components/Common/ModalBasic"
import {useVigilancia,useAuth} from "../../../hooks"
import { useEffect,useState } from 'react'
import "./CargaVigilancia.scss"
import Swal from "sweetalert2";

export function CargaVigilancia() {
  console.log("hola mundo")
    // const {getUsers,loading,users,setUsers,deleteUser,getempleadoId,auth} = useUser()
    const {get_vigilancia,vigilancias} = useVigilancia()
    const {auth} = useAuth();
    const [titleModal, setTitleModal] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [contentModal, setContentModal] = useState(null);
    const [refetch, setRefetch] = useState(false)

    // useEffect(() => {
    //     get_vigilancia();
    //   }, []);
      
      
    const openCloseModal = () => {
        setShowModal((prev) => !prev);
      };
      const onRefetch = () => setRefetch((prev) => !prev);

      // const addHorarios = (cantidad_dias,setformHorario) => {
      //   setTitleModal("Agregar Horarios");
      //   console.log(cantidad_dias)
      //   setContentModal(
      //     <CargaHorario
      //       onClose={openCloseModal}
      //       Refetch = {onRefetch}
      //       cantidad_dias={cantidad_dias}
      //       setformHorario={setformHorario}
      //       // addUser={addUser}
      //     />
      //   );
      //   openCloseModal();
      // };
      
    //   const onDeleteUser = async (data) => {
    //     try {
    //       Swal.fire({
    //         icon: "question",
    //         iconColor: "lightblue",
    //         title: "Eliminar Usuario",
    //         text: "¿Estas seguro que quieres eliminar este empleado?",
    //         showCancelButton: true,
    //         showConfirmButton: true,
    //         confirmButtonText: "confirmar",
    //         cancelButtonText: "cancelar",
    //         reverseButtons: true,
    //         confirmButtonColor: "#3085d6",
    //         cancelButtonColor: "#d33",
    //       }).then(async (result) => {
    //         if (result.isConfirmed) {
    //           await deleteUser(data.id);
    //           console.log("hola mundo")
    //           window.location.reload()
    //           // setUsers(null);
    
    //           Swal.fire({
    //             title: "Empleado Eliminado!",
    //             text: "El empleado fue eliminado",
    //             icon: "success",
    //             showConfirmButton: true,
    //             timer: 3000,
    //           });
    //         }
    //       });
    //     } catch (error) {
    //       console.error(error);
    //     }
    //   };
    
  return (
    <>
          
          <HeaderPage title="CARGA DE VIGILANCIA"/>
          <div className='header-page-usuarios'>
          
              {/* <div className='agregar'>
              <Button positive onClick={()=>console.log("hola mundo")}>
                {"AGREGAR"}
              </Button>
              </div>
               */}
         </div>
      {/* <TableVigilancia 
                    vigilancias={vigilancias}
                    // onDeleteUser={onDeleteUser}
      /> */}
      <div className='form-vigilancia'>
      <AddVigilancia
      />
      </div>
      <ModalBasic
            show={showModal}
            title={titleModal}
            children={contentModal}
            onClose={openCloseModal}
          />
    </>
  )
}
