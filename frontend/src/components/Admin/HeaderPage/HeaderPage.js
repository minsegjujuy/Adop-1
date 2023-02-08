import React from 'react'

export function HeaderPage(props) {
   const {title} = props;
  return (
    <>
       <div className="header-page-admin">
      <h2>{title}</h2>
    </div>
    </>
  )
}
