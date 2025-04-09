<?php
$host = "localhost:3306";
$user = "root";
$password = "";
$conn;
echo "cancer";
try {
    $conn = new PDO("mysql:host=$host;dbname=mibasesita", $user, $password); //hago una nueva instancia de conexion PDO con parametros
    echo "<br>";
    echo "Conectado Correctamente";

    $name = $_POST['name'];
    $age = $_POST['age'];
    $matricula = $_POST['matricula'];

    echo $name;

    $insert = "INSERT INTO students (name, age, matricula)
    VALUES (:name, :number, :elemento)";
    //aqui el query no es ejecutado solo se le envia a la base
    $ress = $conn->prepare($insert); //esto lo hacemos para evitar inyecciones SQL
    $ress->execute([
        ':name' => $name,
        ':age' => $age,
        ':matricula' => $matricula
    ]);

    $query = "SELECT * FROM students";
    $result = $conn->query($query);
    $data = [];
    foreach($result as $student)
        $data[] = $student;
    //echo json_encode($data); //al usar json encode tambien se puede usar echo

   
    
} catch (PDOException $e) {
    echo "Error de conexion: " . $e->getMessage();
}
?>