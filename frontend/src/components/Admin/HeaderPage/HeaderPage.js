import React from 'react'
import "./HeaderPage.scss"

export function HeaderPage(props) {
   const {title,regional} = props;
  return (
    <>
       <div className="header-page-admin">
      <h1 >{title} {regional? `UNIDAD REGIONAL  ${regional}`:null}</h1>
    </div>
    <hr/>
    <br/>
    </>
  )
}
