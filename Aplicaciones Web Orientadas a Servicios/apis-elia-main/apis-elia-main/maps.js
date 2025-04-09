function initMap() {
    // Mapa centrado en Chihuahua, México
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 28.632, lng: -106.0691 }, // Coordenadas de Chihuahua
        zoom: 12,
    });

    // Veterinarias en Chihuahua
    const veterinarias = [
        { lat: 28.633242, lng: -106.089305, name: "Veterinaria Canina y Felina" },
        { lat: 28.636237, lng: -106.091654, name: "Clínica Veterinaria Chihuahua" },
        { lat: 28.626544, lng: -106.089141, name: "Hospital Veterinario Chihuahua" },
        { lat: 28.678903, lng: -106.122623, name: "Clínica Veterinaria Del Parque" },
    ];

    // Agregar marcadores para cada veterinaria
    veterinarias.forEach(function (veterinaria) {
        const marker = new google.maps.Marker({
            position: { lat: veterinaria.lat, lng: veterinaria.lng },
            map: map,
            title: veterinaria.name,
        });

        // Crear un InfoWindow con el nombre de la veterinaria
        const infoWindow = new google.maps.InfoWindow({
            content: veterinaria.name,
        });

        // Asociar el InfoWindow al marcador
        marker.addListener("click", function () {
            infoWindow.open(map, marker);
        });
    });
}

  