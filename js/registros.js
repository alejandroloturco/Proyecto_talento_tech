document.addEventListener("DOMContentLoaded",function(){


    document.getElementById("registroForm").addEventListener('submit',async function(event){
     event.preventDefault()
     let nombre=document.getElementById("nombre").value
     let correo=document.getElementById("email").value
     let contraseña=document.getElementById("password").value
     let contraseña2=document.getElementById("confirm-password").value
     
    
    
     let respuesta=await fetch('http://127.0.0.1:5000/insertar_registros',{
    
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({nombre,correo,contraseña,contraseña2})
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