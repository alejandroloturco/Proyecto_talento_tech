document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("cuestionarioForm").addEventListener("submit", async function (event) {
        event.preventDefault();

        // Obtener todos los valores seleccionados del cuestionario
        const form = event.target;
        const formData = new FormData(form);
        const respuestas = {};

        // Recoger solo los campos definidos en el HTML
        const campos = [
            "registrado",
            "reutiliza_aceite",
            "tira_aceite",
            "conoce_puntos",
            "sabe_contaminacion",
            "dispuesto_entregar",
            "interes_reciclaje",
            "cocina_casa",
            "uso_aceite",
            "separa_residuos",
            "recipiente_especial",
            "tipo_recoleccion",
            "pago_servicio"
        ];

        campos.forEach(campo => {
            respuestas[campo] = formData.get(campo);
        });

        try {
            const respuesta = await fetch("http://127.0.0.1:5000/insertar_cuestionario", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(respuestas)
            });

            const data = await respuesta.json();
            console.log(data);

            if (data.mensaje === "Clientes insertado de forma correcta") {
                Swal.fire({
                    title: "Cuestionario enviado",
                    text: "¡Gracias por participar!",
                    icon: "success"
                });
            } else {
                Swal.fire({
                    title: "Error",
                    text: "No se pudo guardar el cuestionario",
                    icon: "error"
                });
            }
        } catch (error) {
            console.error("Error al enviar el formulario:", error);
            Swal.fire({
                title: "Error de conexión",
                text: "No se pudo conectar con el servidor",
                icon: "error"
            });
        }
    });
});
