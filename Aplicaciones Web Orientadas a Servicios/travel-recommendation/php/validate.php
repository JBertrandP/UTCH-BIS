<?php
header('Content-Type: application/json');

$data = json_decode(file_get_contents('php://input'), true);

$interests = $data['interests'];
$budget = $data['budget'];
$weather = $data['weather'];
$season = $data['season'];

// Validación básica en el backend
if (empty($interests) || empty($budget) || empty($weather) || empty($season)) {
    echo json_encode(['error' => 'Todos los campos son obligatorios.']);
    exit;
}

// Obtener información del clima usando OpenWeatherMap
$weatherApiKey = '604b154fc8aa01160720a3689b1def0f';
$city = urlencode($interests); // Usamos los intereses como ciudad de búsqueda
$weatherUrl = "https://api.openweathermap.org/data/2.5/weather?q={$city}&appid={$weatherApiKey}&units=metric&lang=es";

$weatherData = json_decode(file_get_contents($weatherUrl), true);

if (!$weatherData) {
    echo json_encode(['error' => 'No se pudo obtener información del clima.']);
    exit;
}

$weatherDescription = $weatherData['weather'][0]['description'];
$temperature = $weatherData['main']['temp'];

// Obtener información del país usando Restcountries
$countryCode = $weatherData['sys']['country']; // Código de país desde OpenWeatherMap
$countryUrl = "https://restcountries.com/v3.1/alpha/{$countryCode}";
$countryData = json_decode(file_get_contents($countryUrl), true);

if (!$countryData) {
    echo json_encode(['error' => 'No se pudo obtener información del país.']);
    exit;
}

$countryName = $countryData[0]['name']['common'];
$currency = array_keys($countryData[0]['currencies'])[0];
$language = array_keys($countryData[0]['languages'])[0];

// Obtener fotos del destino usando Unsplash
$unsplashApiKey = 'jUf_oINdMapNlhQnVSwcwSu2xmVh7S8fISMqbC7fU34';
$unsplashUrl = "https://api.unsplash.com/search/photos?query={$city}&client_id={$unsplashApiKey}";
$unsplashData = json_decode(file_get_contents($unsplashUrl), true);

if (!$unsplashData) {
    echo json_encode(['error' => 'No se pudo obtener fotos del destino.']);
    exit;
}

$photoUrl = $unsplashData['results'][0]['urls']['regular'];

// Obtener consejos de viaje usando Wikipedia API
$wikipediaUrl = "https://es.wikipedia.org/api/rest_v1/page/summary/{$city}";
$wikipediaData = json_decode(file_get_contents($wikipediaUrl), true);

if (!$wikipediaData) {
    echo json_encode(['error' => 'No se pudo obtener consejos de viaje.']);
    exit;
}

$travelTips = $wikipediaData['extract'];

// Preparar la respuesta con la información obtenida
$recommendations = [
    [
        'name' => $city,
        'description' => "Un destino con clima {$weatherDescription} y temperatura de {$temperature}°C.",
        'image' => $photoUrl,
        'tips' => "Moneda: {$currency}, Idioma: {$language}. {$travelTips}",
        'lat' => $weatherData['coord']['lat'],
        'lng' => $weatherData['coord']['lon']
    ]
];

echo json_encode($recommendations);
?>