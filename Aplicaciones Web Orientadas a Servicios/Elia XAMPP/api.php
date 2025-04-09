<?php
#aqui declaramos los headers
header("Content-Type: application/json");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Accept-Charset: UTF-8");
 
//importo el archivo de conexion
include "conn.php";
//guardo una variable con el metodo
$method = $_SERVER['REQUEST_METHOD'];

switch($method){
    case 'GET':
        $query = "SELECT * FROM students";
        break;
    case 'POST':
        echo "Este es el metodo POST";
        break;
    case 'PUT':
        echo "Este es el metodo PUT";
        break;
    case 'DELETE':
        echo "Este es el metodo DELETE";
        break;
    default:
        echo "Metodo no reconocido";
        break;

}

?>