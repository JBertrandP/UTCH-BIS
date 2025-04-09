<?php
// Configura la respuesta como JSON
header("Content-Type: application/json");

// Incluye la configuración de la base de datos
include_once '../config/database.php';

// Verifica que sea una solicitud POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(["error" => "Método no permitido"]);
    exit;
}

// Verifica que se ha proporcionado un ID
if (!isset($_POST['id']) || empty($_POST['id'])) {
    echo json_encode(["error" => "ID no proporcionado o inválido"]);
    exit;
}

$id = intval($_POST['id']);

// Verifica si se ha subido un archivo
if (isset($_FILES['archivo']) && $_FILES['archivo']['error'] === UPLOAD_ERR_OK) {
    // Define las extensiones permitidas
    $allowedExtensions = ['mp3', 'mp4'];
    // Obtiene la extensión del archivo subido
    $fileExtension = strtolower(pathinfo($_FILES['archivo']['name'], PATHINFO_EXTENSION));
    
    // Verifica si el archivo tiene una extensión permitida
    if (!in_array($fileExtension, $allowedExtensions)) {
        echo json_encode(["error" => "Solo se permiten archivos MP3 y MP4"]);
        exit;
    }
    
    // Define el directorio donde se almacenarán los archivos subidos
    $uploadDir = '../uploads/';
    
    // Si el directorio no existe, lo crea
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }
    
    // Genera un nombre único para el archivo subido
    $fileName = uniqid('song_', true) . '.' . $fileExtension;
    $uploadFile = $uploadDir . $fileName;
    
    // Intenta mover el archivo subido al directorio
    if (move_uploaded_file($_FILES['archivo']['tmp_name'], $uploadFile)) {
        $archivo = 'uploads/' . $fileName; // Guarda la ruta del archivo en la variable
        
        // Actualiza solo el campo 'archivo' en la base de datos
        $query = "UPDATE canciones SET archivo='$archivo' WHERE id=$id";
        
        // Ejecuta la consulta y verifica si fue exitosa
        if ($conn->query($query)) {
            echo json_encode(["message" => "Archivo de canción actualizado"]);
        } else {
            echo json_encode(["error" => $conn->error]);
        }
    } else {
        echo json_encode(["error" => "Error al subir el archivo"]);
    }
} else {
    echo json_encode(["error" => "No se subió ningún archivo"]);
}
?>