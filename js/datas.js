function guardarDatos() {
    const datos = {
        nombre: document.getElementById('nombre').value,
        apellido: document.getElementById('apellido').value,
        documento: document.getElementById('documento').value,
        direccion: document.getElementById('direccion').value,
        correo: document.getElementById('correo').value,
        mensaje: document.getElementById('mensaje').value,
        estadoCivil: document.querySelector('input[name="estado-civil"]:checked')?.value || 'No especificado',
        paisNacimiento: document.getElementById('pais-nacimiento').value,
        mensajeAdicional: document.getElementById('mensaje-adicional').value
    };

    console.log(JSON.stringify(datos, null, 2));
}