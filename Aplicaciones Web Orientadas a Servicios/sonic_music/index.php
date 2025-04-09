<?php
error_reporting(E_ALL); // Reporta todos los errores de PHP, lo que ayuda a detectar cualquier problema en el código (habilita la visualización de errores detallados)
ini_set('display_errors', 1); // Muestra los errores en pantalla para facilitar la depuración durante el desarrollo
include_once 'config/database.php'; // Incluye el archivo de configuración de la base de datos, donde se configuran las credenciales y la conexión
?>
<!DOCTYPE html>
<html lang="es"> <!-- Declara el idioma de la página como español -->
<head>
    <meta charset="UTF-8"> <!-- Especifica el conjunto de caracteres que se utilizarán en la página (UTF-8) -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Asegura que la página sea responsiva en dispositivos móviles -->
    <title>Gestión de Canciones de Sonic</title> <!-- Título de la página que se mostrará en la pestaña del navegador -->
    <!-- Enlaces a hojas de estilo externas para usar Bootstrap y DataTables -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"> 
    <link href="https://cdn.datatables.net/1.12.1/css/jquery.dataTables.min.css" rel="stylesheet"> 
    <link rel="stylesheet" href="assets/css/style.css"> <!-- Enlace a la hoja de estilo personalizada para la página -->
</head>
<body>
<div class="container mt-5"> <!-- Contenedor con margen superior de 5 unidades -->
<div class="text-center">
    <img src="assets/img/sonic.gif" alt="Sonic animado" width="450
    ">
</div>
    <h1 class="text-center">Gestión de Canciones de Sonic</h1> <!-- Título principal centrado en la página -->
    <button class="btn btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addSongModal">Agregar Canción</button> <!-- Botón para abrir el modal de agregar canción -->
    <table id="songsTable" class="table table-striped"> <!-- Tabla para mostrar las canciones con estilo de filas alternadas -->
        <thead>
            <tr>
                <th>ID</th> <!-- Encabezado de la columna que muestra el ID de cada canción -->
                <th>Título</th> <!-- Encabezado de la columna que muestra el título de cada canción -->
                <th>Artista</th> <!-- Encabezado de la columna que muestra el nombre del artista -->
                <th>Género</th> <!-- Encabezado de la columna que muestra el género musical de la canción -->
                <th>Reproducir</th> <!-- Encabezado de la columna para un botón o acción de reproducción -->
                <th>Acciones</th> <!-- Encabezado de la columna para acciones como editar o eliminar -->
            </tr>
        </thead>
        <tbody>
            <!-- Los datos de las canciones se cargarán aquí dinámicamente mediante JavaScript -->
        </tbody>
    </table>
</div>

<!-- Modal para Agregar Canción -->
<div class="modal fade" id="addSongModal" tabindex="-1" aria-labelledby="addSongModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="addSongModalLabel">Agregar Canción</h5> <!-- Título del modal -->
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> <!-- Botón para cerrar el modal -->
            </div>
            <div class="modal-body">
                <form id="addSongForm" enctype="multipart/form-data"> <!-- Formulario para agregar una nueva canción -->
                    <div class="mb-3">
                        <label for="titulo" class="form-label">Título</label> <!-- Etiqueta para el campo de título -->
                        <input type="text" class="form-control" id="titulo" name="titulo" required> <!-- Campo para ingresar el título de la canción -->
                    </div>
                    <div class="mb-3">
                        <label for="artista" class="form-label">Artista</label> <!-- Etiqueta para el campo de artista -->
                        <input type="text" class="form-control" id="artista" name="artista" required> <!-- Campo para ingresar el nombre del artista -->
                    </div>
                    <div class="mb-3">
                        <label for="genero" class="form-label">Género</label> <!-- Etiqueta para el campo de género -->
                        <input type="text" class="form-control" id="genero" name="genero" required> <!-- Campo para ingresar el género musical -->
                    </div>
                    <div class="mb-3">
                        <label for="archivo" class="form-label">Archivo de la Canción (mp3 o mp4)</label> <!-- Etiqueta para el campo de archivo de la canción -->
                        <input type="file" class="form-control" id="archivo" name="archivo" accept=".mp3,.mp4" required> <!-- Campo para subir el archivo de la canción -->
                    </div>
                    <button type="submit" class="btn btn-primary">Guardar</button> <!-- Botón para enviar el formulario y guardar la nueva canción -->
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Modal para Actualizar Canción -->
<div class="modal fade" id="updateSongModal" tabindex="-1" aria-labelledby="updateSongModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="updateSongModalLabel">Actualizar Canción</h5> <!-- Título del modal de actualización -->
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> <!-- Botón para cerrar el modal -->
            </div>
            <div class="modal-body">
                <form id="updateSongForm">
                    <input type="hidden" id="updateSongId" name="id"> <!-- Campo oculto para almacenar el ID de la canción a actualizar -->
                    <div class="mb-3">
                        <label for="updateTitulo" class="form-label">Título</label> <!-- Etiqueta para el campo de título -->
                        <input type="text" class="form-control" id="updateTitulo" name="titulo" required> <!-- Campo para actualizar el título de la canción -->
                    </div>
                    <div class="mb-3">
                        <label for="updateArtista" class="form-label">Artista</label> <!-- Etiqueta para el campo de artista -->
                        <input type="text" class="form-control" id="updateArtista" name="artista" required> <!-- Campo para actualizar el nombre del artista -->
                    </div>
                    <div class="mb-3">
                        <label for="updateGenero" class="form-label">Género</label> <!-- Etiqueta para el campo de género -->
                        <input type="text" class="form-control" id="updateGenero" name="genero" required> <!-- Campo para actualizar el género musical -->
                    </div>
                    <div class="mb-3">
                        <label for="updateArchivo" class="form-label">Archivo de la Canción (mp3 o mp4)</label> <!-- Etiqueta para el campo de archivo de la canción -->
                        <input type="file" class="form-control" id="updateArchivo" name="archivo" accept=".mp3,.mp4"> <!-- Campo para actualizar el archivo de la canción -->
                        <small class="text-muted">Deja este campo vacío si no deseas cambiar el archivo.</small> <!-- Mensaje informativo para el usuario -->
                    </div>
                    <button type="submit" class="btn btn-primary">Actualizar</button> <!-- Botón para enviar el formulario de actualización -->
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Modal para Eliminar Canción -->
<div class="modal fade" id="deleteSongModal" tabindex="-1" aria-labelledby="deleteSongModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="deleteSongModalLabel">Eliminar Canción</h5> <!-- Título del modal para eliminar canción -->
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> <!-- Botón para cerrar el modal -->
            </div>
            <div class="modal-body">
                <p>¿Estás seguro de que deseas eliminar esta canción?</p> <!-- Mensaje de confirmación antes de eliminar la canción -->
                <input type="hidden" id="deleteSongId"> <!-- Campo oculto para almacenar el ID de la canción a eliminar -->
                <button type="button" id="confirmDelete" class="btn btn-danger">Eliminar</button> <!-- Botón para confirmar la eliminación -->
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button> <!-- Botón para cancelar la eliminación -->
            </div>
        </div>
    </div>
</div>

<!-- Scripts necesarios para el funcionamiento de la página -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> <!-- Enlace a la librería jQuery -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script> <!-- Enlace al archivo JS de Bootstrap -->
<script src="https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js"></script> <!-- Enlace a la librería JS de DataTables -->
<script src="assets/js/script.js"></script> <!-- Enlace a la hoja de estilo y funcionalidad personalizada -->
</body>
</html>
