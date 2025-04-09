<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

include("conexion.php");

// Recibir los datos del cliente
$data = json_decode(file_get_contents("php://input"), true);

if (!$data) {
    echo json_encode(["error" => "No se recibieron datos"]);
    exit();
}

$requiredFields = ['destino', 'interes', 'presupuesto', 'clima', 'epoca'];
foreach ($requiredFields as $field) {
    if (!isset($data[$field])) {
        echo json_encode(["error" => "Falta el parámetro: $field"]);
        exit();
    }
}

// Escapar los valores recibidos para mayor seguridad
$destino = $conexion->real_escape_string($data["destino"]);
$interes = $conexion->real_escape_string($data["interes"]);
$presupuesto = $conexion->real_escape_string($data["presupuesto"]);
$clima = $conexion->real_escape_string($data["clima"]);
$epoca = $conexion->real_escape_string($data["epoca"]);

// 🔹 **Consulta de recomendaciones basadas en parámetros**
$sqlRecomendaciones = "SELECT TextoRecomendacion FROM Recomendaciones 
WHERE DestinoID = (SELECT DestinoID FROM Destinos WHERE nombre LIKE ?)
AND (Interes = ? OR Interes IS NULL)
AND (Clima = ? OR Clima IS NULL)
AND (Epoca = ? OR Epoca IS NULL)
AND (Presupuesto = ? OR Presupuesto IS NULL)";

$stmt = $conexion->prepare($sqlRecomendaciones);
$likeDestino = "%$destino%";
$stmt->bind_param("sssss", $likeDestino, $interes, $clima, $epoca, $presupuesto);
$stmt->execute();
$resultado = $stmt->get_result();

$recomendaciones = [];
while ($fila = $resultado->fetch_assoc()) {
    $recomendaciones[] = $fila['TextoRecomendacion'];
}
$stmt->close();

if (empty($recomendaciones)) {
    echo json_encode(["error" => "No se encontraron recomendaciones para tus preferencias."]);
    exit();
}

// 🔹 **API de Unsplash para imágenes del destino**
$unsplashAPIKey = 'jUf_oINdMapNlhQnVSwcwSu2xmVh7S8fISMqbC7fU34';
$unsplashAPIUrl = "https://api.unsplash.com/search/photos?query=$destino+$interes&client_id=$unsplashAPIKey";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $unsplashAPIUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$unsplashResponse = curl_exec($ch);
curl_close($ch);

$unsplashData = json_decode($unsplashResponse, true);
$imagenes = [];

if (isset($unsplashData['results']) && is_array($unsplashData['results'])) {
    $contador = 0;
    foreach ($unsplashData['results'] as $photo) {
        if ($contador >= 4) break;
        $imagenes[] = $photo['urls']['regular'];
        $contador++;
    }
} else {
    $imagenes[] = "No se pudieron obtener imágenes.";
}

// 🔹 **Consulta de coordenadas desde OpenWeatherMap**
function getCoordinates($city, $apiKey) {
    $url = "https://api.openweathermap.org/geo/1.0/direct?q=$city&limit=1&appid=$apiKey";
    $response = @file_get_contents($url);

    if ($response === false) {
        return null;
    }

    $data = json_decode($response, true);
    if (isset($data[0]['lat'])) {
        return [
            'lat' => $data[0]['lat'],
            'lng' => $data[0]['lon']
        ];
    }
    return null;
}

$apiKeyWeather = '604b154fc8aa01160720a3689b1def0f';
$coordinates = getCoordinates($destino, $apiKeyWeather);

// 🔹 **Construcción de la respuesta JSON**
$response = [
    'destino' => $destino,
    'imagenes' => $imagenes,
    'recomendaciones' => $recomendaciones,
    'lat' => $coordinates['lat'] ?? 0,
    'lng' => $coordinates['lng'] ?? 0
];

echo json_encode($response);
?>