// Espera a que el contenido del DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function() {
    // Variables globales para almacenar las opciones seleccionadas por el usuario
    let destino = '';
    let interes = '';
    let presupuesto = '';
    let clima = '';
    let epoca = '';

    /**
     * Evento que detecta cambios en la selección de destino y actualiza los intereses disponibles.
     */
    document.querySelector('#destino').addEventListener('change', function(event) {
        destino = event.target.value;
        actualizarIntereses(destino);
    });

    /**
     * Actualiza las opciones del selector de intereses según el destino seleccionado.
     * @param {string} destino - El destino seleccionado por el usuario.
     */
    function actualizarIntereses(destino) {
        let intereses = [];

        // Define los intereses según el destino elegido
        switch(destino) {
            case 'paris':
                intereses = ['Arte', 'Historia', 'Cultura', 'Gastronomía'];
                break;
            case 'hongkong':
                intereses = ['Compras', 'Tecnología', 'Cultura', 'Historia'];
                break;
            case 'tokyo':
                intereses = ['Tecnología', 'Cultura', 'Comida', 'Arte'];
                break;
            case 'cancun':
                intereses = ['Playa', 'Relax', 'Aventura', 'Historia'];
                break;
            case 'amsterdam':
                intereses = ['Arte', 'Cultura', 'Historia', 'Naturaleza'];
                break;
            default:
                intereses = [];
        }

        // Selecciona el elemento HTML donde se actualizarán los intereses
        let interesSelect = document.querySelector('#interes');
        interesSelect.innerHTML = '<option value="" disabled selected>Elige un interés</option>';

        // Agrega las opciones dinámicamente al selector de intereses
        intereses.forEach(function(interest) {
            let option = document.createElement('option');
            option.value = interest.toLowerCase();
            option.textContent = interest;
            interesSelect.appendChild(option);
        });
    }

    // Captura los valores seleccionados por el usuario en cada filtro
    document.querySelector('#interes').addEventListener('change', function(event) {
        interes = event.target.value;
    });

    document.querySelector('#presupuesto').addEventListener('change', function(event) {
        presupuesto = event.target.value;
    });

    document.querySelector('#clima').addEventListener('change', function(event) {
        clima = event.target.value;
    });

    document.querySelector('#epoca').addEventListener('change', function(event) {
        epoca = event.target.value;
    });

    /**
     * Evento que se activa al hacer clic en el botón de búsqueda.
     * Llama a la función para obtener los resultados basados en los filtros seleccionados.
     */
    document.querySelector('#buscar-btn').addEventListener('click', function(event) {
        event.preventDefault();
        obtenerResultados();
    });

    /**
     * Valida la entrada del usuario y envía la solicitud al backend.
     */
    function obtenerResultados() {
        if (!destino || !interes || !presupuesto || !clima || !epoca) {
            alert('Por favor selecciona todos los filtros.');
            return;
        }

        // Crear objeto con los datos seleccionados
        let datos = {
            destino: destino,
            interes: interes,
            presupuesto: presupuesto,
            clima: clima,
            epoca: epoca
        };

        console.log("Enviando datos:", datos);

        // Enviar los datos al backend mediante una solicitud HTTP POST
        fetch("http://localhost/travel_recommendation/backend.php", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Datos recibidos:", data);
            mostrarResultados(data);
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
            alert('Hubo un error al obtener la información.');
        });
    }

    /**
     * Muestra los resultados obtenidos en la interfaz.
     * @param {Object} data - Datos recibidos del backend.
     */
    function mostrarResultados(data) {
        // Limpia los resultados previos
        document.querySelector('#recomendaciones').innerHTML = '';

        // Mostrar recomendaciones basadas en el destino, interés, presupuesto, clima y época
        if (data.recomendaciones && data.recomendaciones.length > 0) {
            let recomendacionesContainer = document.querySelector('#recomendaciones');
            let ul = document.createElement('ul');
            data.recomendaciones.forEach(function(recomendacion) {
                let li = document.createElement('li');
                li.textContent = recomendacion;
                ul.appendChild(li);
            });
            recomendacionesContainer.appendChild(ul);
        } else {
            document.querySelector('#recomendaciones').innerHTML = '<p>No hay recomendaciones disponibles.</p>';
        }

        // Mostrar imágenes
        if (data.imagenes && data.imagenes.length > 0) {
            let imagenesList = document.querySelector('#imagenes');
            imagenesList.innerHTML = ''; // Limpiar imágenes anteriores
            data.imagenes.forEach(function(imagenUrl) {
                if (imagenUrl.startsWith('http')) {
                    let img = document.createElement('img');
                    img.src = imagenUrl;
                    img.alt = 'Imagen relacionada';
                    img.classList.add('imagen-interes');
                    imagenesList.appendChild(img);
                }
            });
        } else {
            document.querySelector('#imagenes').innerHTML = '<p>No hay imágenes disponibles para este interés.</p>';
        }

        // Generar mapa interactivo con la ubicación del destino
        if (data.lat && data.lng) {
            const mapContainer = document.getElementById('map');
            
            // Eliminar mapa anterior si existe
            if (mapContainer._leaflet_id) {
                mapContainer.remove();
                const newMapContainer = document.createElement('div');
                newMapContainer.id = 'map';
                newMapContainer.style.height = '400px';
                document.querySelector('#resultados').appendChild(newMapContainer);
            }

            // Crear y configurar el mapa
            const map = L.map('map').setView([data.lat, data.lng], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            L.marker([data.lat, data.lng]).addTo(map)
                .bindPopup(`<b>${destino}</b>`)
                .openPopup();
        } else {
            console.error('No se pudieron obtener las coordenadas del destino.');
        }
    }
});