async function guardarDatos() {
    // Obtener los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const direccion = document.getElementById('direccion').value;
    const correo = document.getElementById('correo').value;
    const mensaje = document.getElementById('mensaje-adicional').value;

    // Validar campos requeridos
    if (!nombre || !apellido || !direccion || !correo) {
        alert('Por favor complete todos los campos requeridos');
        return;
    }

    // Crear objeto con los datos
    const clienteData = {
        nombre,
        apellido,
        direccion,
        correo,
        mensaje,
        fecha: new Date().toISOString()
    };

    
}