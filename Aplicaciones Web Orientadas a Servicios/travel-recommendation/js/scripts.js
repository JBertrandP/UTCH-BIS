// Función para obtener la ubicación actual del usuario
function getCurrentLocation() {
    return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    resolve({
                        lat: position.coords.latitude,
                        lng: position.coords.longitude
                    });
                },
                (error) => {
                    reject("Error al obtener la ubicación: " + error.message);
                }
            );
        } else {
            reject("Geolocalización no es soportada por este navegador.");
        }
    });
}

// Función para calcular la distancia entre dos puntos usando la fórmula de Haversine
function calculateDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Radio de la Tierra en km
    const dLat = (lat2 - lat1) * (Math.PI / 180);
    const dLon = (lon2 - lon1) * (Math.PI / 180);
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c; // Distancia en km
    return distance.toFixed(2); // Redondeamos a 2 decimales
}

// Función para mostrar las recomendaciones en la página
function showRecommendations(data) {
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = '';

    data.forEach(place => {
        const placeDiv = document.createElement('div');
        placeDiv.className = 'place';
        placeDiv.innerHTML = `
            <h2>${place.name}</h2>
            <p>${place.description}</p>
            <img src="${place.image}" alt="${place.name}">
            <p>Consejos: ${place.tips}</p>
        `;
        recommendationsDiv.appendChild(placeDiv);
    });

    initMap(data);
}

// Función para inicializar el mapa y mostrar los marcadores
function initMap(places) {
    const map = L.map('map').setView([19.4326, -99.1332], 10); // Coordenadas iniciales (Ciudad de México)

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    places.forEach(place => {
        // Centrar el mapa en el lugar recomendado
        map.setView([place.lat, place.lng], 10);

        // Agregar un marcador en el lugar recomendado
        L.marker([place.lat, place.lng])
            .addTo(map)
            .bindPopup(place.name);
    });
}

// Manejar el envío del formulario
document.getElementById('travelForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const interests = document.getElementById('interests').value;
    const budget = document.getElementById('budget').value;
    const weather = document.getElementById('weather').value;
    const season = document.getElementById('season').value;

    // Validación básica en el frontend
    if (!interests || !budget || !weather || !season) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    try {
        // Obtener la ubicación actual del usuario
        const userLocation = await getCurrentLocation();

        // Llamada al backend para validación y procesamiento
        const response = await fetch('php/validate.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                interests: interests,
                budget: budget,
                weather: weather,
                season: season
            })
        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
        } else {
            // Calcular la distancia entre la ubicación actual y el destino recomendado
            const destination = data[0]; // Tomamos el primer destino recomendado
            const distance = calculateDistance(
                userLocation.lat,
                userLocation.lng,
                destination.lat,
                destination.lng
            );

            // Mostrar la distancia en la descripción
            destination.description += ` Distancia: ${distance} km desde tu ubicación actual.`;

            // Mostrar las recomendaciones
            showRecommendations([destination]);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Hubo un error al procesar tu solicitud.');
    }
});