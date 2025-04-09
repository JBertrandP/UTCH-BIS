<?php
// Configura la respuesta como JSON
header("Content-Type: application/json");

// Incluye la configuración de la base de datos
include_once '../config/database.php';

// Obtiene el método HTTP de la solicitud (GET, POST, PUT, DELETE)
$method = $_SERVER['REQUEST_METHOD'];

// Se realiza una acción diferente dependiendo del método HTTP
switch ($method) {

    // Cuando se hace una solicitud GET, obtenemos todas las canciones
    case 'GET':
        // Consulta SQL para seleccionar todas las canciones
        $query = "SELECT * FROM canciones";
        
        // Ejecuta la consulta
        $result = $conn->query($query);

        // Si la consulta es exitosa
        if ($result) {
            $canciones = []; // Array para almacenar las canciones

            // Recorre todas las filas obtenidas en la consulta
            while ($row = $result->fetch_assoc()) {
                $canciones[] = $row; // Agrega la canción al array
            }

            // Devuelve todas las canciones en formato JSON
            echo json_encode($canciones);
        } else {
            // Si ocurre un error, devuelve el error en formato JSON
            echo json_encode(["error" => "Error en la consulta: " . $conn->error]);
        }
        break;

    // Cuando se hace una solicitud POST, agregamos una nueva canción
    case 'POST':
        // Obtiene los datos enviados desde el formulario o body
        $titulo = $_POST['titulo'];
        $artista = $_POST['artista'];
        $genero = $_POST['genero'];

        // Verifica si se ha subido un archivo
        if (isset($_FILES['archivo']) && $_FILES['archivo']['error'] === UPLOAD_ERR_OK) {
            // Define las extensiones permitidas
            $allowedExtensions = ['mp3', 'mp4'];
            // Obtiene la extensión del archivo subido
            $fileExtension = strtolower(pathinfo($_FILES['archivo']['name'], PATHINFO_EXTENSION));
            // Define los tipos MIME permitidos
            $allowedMimeTypes = ['audio/mpeg', 'video/mp4'];
            // Obtiene el tipo MIME del archivo subido
            $fileMimeType = mime_content_type($_FILES['archivo']['tmp_name']);

            // Verifica si la extensión y tipo MIME del archivo son válidos
            if (!in_array($fileExtension, $allowedExtensions) || !in_array($fileMimeType, $allowedMimeTypes)) {
                echo json_encode(["error" => "Solo se permiten archivos MP3 y MP4 válidos"]);
                exit; // Sale si el archivo no es válido
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
            } else {
                echo json_encode(["error" => "Error al subir el archivo"]);
                exit; // Sale si no se puede mover el archivo
            }
        } else {
            echo json_encode(["error" => "No se subió ningún archivo"]);
            exit; // Sale si no se sube ningún archivo
        }

        // Realiza la consulta para insertar la nueva canción en la base de datos
        $query = "INSERT INTO canciones (titulo, artista, genero, archivo) VALUES ('$titulo', '$artista', '$genero', '$archivo')";

        // Ejecuta la consulta y verifica si fue exitosa
        if ($conn->query($query)) {
            echo json_encode(["message" => "Canción agregada"]);
        } else {
            echo json_encode(["error" => $conn->error]);
        }
        break;

    // Cuando se hace una solicitud PUT, actualizamos una canción
    case 'PUT':
        // Obtiene los datos enviados en el body de la solicitud PUT
        parse_str(file_get_contents("php://input"), $data);

        // Verifica si los datos se recibieron correctamente
        if (!is_array($data) || empty($data)) {
            echo json_encode(["error" => "No se recibieron datos para actualizar"]);
            exit;
        }

        // Debug: Muestra los datos recibidos
        error_log(print_r($data, true));

        // Verifica que el ID esté presente y no esté vacío
        if (!isset($data['id']) || empty($data['id'])) {
            echo json_encode(["error" => "ID no proporcionado o inválido"]);
            exit; // Sale si el ID no está presente o es inválido
        }

        // Convierte el ID a un entero para prevenir inyecciones SQL
        $id = intval($data['id']);

        // Extrae los otros datos necesarios para la actualización
        $titulo = isset($data['titulo']) ? $data['titulo'] : '';
        $artista = isset($data['artista']) ? $data['artista'] : '';
        $genero = isset($data['genero']) ? $data['genero'] : '';

        // Verifica que los datos esenciales estén presentes
        if (empty($titulo) || empty($artista) || empty($genero)) {
            echo json_encode(["error" => "Faltan datos requeridos para la actualización"]);
            exit;
        }

        // Si no se está actualizando el archivo, mantiene el archivo existente
        $query = "SELECT archivo FROM canciones WHERE id=$id";
        $result = $conn->query($query);

        // Si la canción existe, obtiene su archivo actual
        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $archivo = $row['archivo'];
        } else {
            echo json_encode(["error" => "Canción no encontrada"]);
            exit; // Sale si no se encuentra la canción
        }

        // Realiza la consulta para actualizar la canción en la base de datos
        $query = "UPDATE canciones SET titulo='$titulo', artista='$artista', genero='$genero' WHERE id=$id";

        // Ejecuta la consulta y verifica si fue exitosa
        if ($conn->query($query)) {
            echo json_encode(["message" => "Canción actualizada"]);
        } else {
            echo json_encode(["error" => $conn->error]);
        }
        break;

    // Cuando se hace una solicitud DELETE, eliminamos una canción
    case 'DELETE':
        // Obtiene el ID de la canción a eliminar
        $id = $_GET['id'];

        // Realiza la consulta para eliminar la canción
        $query = "DELETE FROM canciones WHERE id=$id";

        // Ejecuta la consulta y verifica si fue exitosa
        if ($conn->query($query)) {
            echo json_encode(["message" => "Canción eliminada"]);
        } else {
            echo json_encode(["error" => $conn->error]);
        }
        break;

    // Si se recibe un método HTTP no soportado, se muestra un error
    default:
        echo json_encode(["error" => "Método no soportado"]);
        break;
}
?>