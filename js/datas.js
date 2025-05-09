document.addEventListener("DOMContentLoaded",function(){


document.getElementById("frm").addEventListener('submit',async function(event){
 event.preventDefault()
 let nombre=document.getElementById("nombre").value
 let apellido=document.getElementById("apellido").value
 let direccion=document.getElementById("direccion").value
 let correo=document.getElementById("correo").value
 let mensaje=document.getElementById("mensaje-adicional").value


 let respuesta=await fetch('http://127.0.0.1:5000/insertar',{

    method:'POST',
    headers:{
        'Content-Type':'application/json'
    },
    body:JSON.stringify({nombre,apellido,direccion,correo,mensaje})
 })
 console.log("La respuesta "+ respuesta)
 let data=await respuesta.json()
 console.log(data)
 if (data.mensaje=="Clientes insertado de forma correcta")
    alert("Cliente registrado correctamente")
    Swal.fire({
    title:"Registro de clientes",
    text:"Registro exitoso",
    icon:"success"
   })

})
})