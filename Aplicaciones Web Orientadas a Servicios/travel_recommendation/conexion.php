<?php
// Parámetros de conexión a la base de datos
$servidor = "localhost"; // Dirección del servidor 
$usuario = "root"; // Usuario de la base de datos 
$contrasena = ""; // Contraseña del usuario
$base_datos = "travel_recommendation"; // Nombre de la base de datos

// Crear la conexión
$conexion = new mysqli($servidor, $usuario, $contrasena, $base_datos);

// Verificar la conexión
if ($conexion->connect_error) {
    die("Error en la conexión: " . $conexion->connect_error);
}

// Establecer el conjunto de caracteres a UTF-8 para admitir acentos y caracteres especiales
$conexion->set_charset("utf8");

// Opcional: mensaje de conexión exitosa (puedes comentarlo después de probar)
// echo "Conexión exitosa";

?>
