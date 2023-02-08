import React from 'react'
import {HeaderPage,TableUsers,AddUser} from "../../components/Admin/"
import {useUser} from "../../hooks"
import {Button} from "semantic-ui-react"
import {ModalBasic} from "../../components/Common/ModalBasic"
import { useEffect,useState } from 'react'
import "./UserAdmin.scss"
import Swal from "sweetalert2";

export function UserAdmin() {
    const {getUsers,loading,users,setUsers,deleteUser} = useUser()
    const [titleModal, setTitleModal] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [contentModal, setContentModal] = useState(null);
    const [refetch, setRefetch] = useState(false)
    
    console.log(users)
    useEffect(() => {
        getUsers();
      }, []);
      
      
    const openCloseModal = () => {
        setShowModal((prev) => !prev);
      };
      const onRefetch = () => setRefetch((prev) => !prev);

      const addUser = () => {
        setTitleModal("Nuevo Usuario");
        setContentModal(
          <AddUser
            onClose={openCloseModal}
            Refetch = {onRefetch}
            // addUser={addUser}
          />
        );
        openCloseModal();
      };
      const onDeleteUser = async (data) => {
        try {
          Swal.fire({
            icon: "question",
            iconColor: "lightblue",
            title: "Eliminar Usuario",
            text: "¿Estas seguro que quieres eliminar este empleado?",
            showCancelButton: true,
            showConfirmButton: true,
            confirmButtonText: "confirmar",
            cancelButtonText: "cancelar",
            reverseButtons: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
          }).then(async (result) => {
            if (result.isConfirmed) {
              await deleteUser(data.id);
              console.log("hola mundo")
              // window.location.reload()
              // setUsers(null);
    
              Swal.fire({
                title: "Empleado Eliminado!",
                text: "El empleado fue eliminado",
                icon: "success",
                showConfirmButton: true,
                timer: 3000,
              });
            }
          });
        } catch (error) {
          console.error(error);
        }
      };
    
  return (
    <>
          
          <HeaderPage title="USUARIOS"/>
          <div className='header-page-usuarios'>
          {/* <Button 
          type="button"
          content={"Recargar"}
          onClick={() => {
           window.location.reload();
          }}
          primary
          fluid
          /> */}
              <div className='agregar'>
              <Button positive onClick={()=>addUser()}>
                {"Agregar Usuario"}
              </Button>
              </div>
         </div>
      <TableUsers users={users}
                  onDeleteUser={onDeleteUser}
      />
      <ModalBasic
            show={showModal}
            title={titleModal}
            children={contentModal}
            onClose={openCloseModal}
          />
    </>
  )
}
