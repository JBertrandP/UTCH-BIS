// Este bloque de código se ejecuta cuando el documento HTML está completamente cargado
$(document).ready(function() {
    // Inicializa la tabla de canciones utilizando el plugin DataTables
    var table = $('#songsTable').DataTable({
        // Configura el origen de los datos que se cargarán en la tabla
        ajax: {
            url: 'api/canciones.php', // URL del endpoint que devuelve los datos
            dataSrc: '' // Indica que la respuesta debe ser un array plano
        },
        // Define las columnas que se mostrarán en la tabla
        columns: [
            { data: 'id' }, // Muestra el ID de la canción
            { data: 'titulo' }, // Muestra el título de la canción
            { data: 'artista' }, // Muestra el nombre del artista
            { data: 'genero' }, // Muestra el género de la canción
            {
                data: 'archivo', // Muestra el archivo relacionado con la canción
                render: function(data) {
                    // Lógica para mostrar un reproductor de audio o video según el tipo de archivo
                    if (data.endsWith('.mp3')) {
                        return `<audio controls><source src="${data}" type="audio/mp3">Tu navegador no soporta el elemento de audio.</audio>`;
                    } else if (data.endsWith('.mp4')) {
                        return `<video controls width="250"><source src="${data}" type="video/mp4">Tu navegador no soporta el elemento de video.</video>`;
                    } else {
                        return `<p>Formato no soportado</p>`; // Si no es mp3 ni mp4, muestra un mensaje de error
                    }
                }
            },
            {
                data: null, // No se extrae directamente un campo de la respuesta
                render: function(data) {
                    // Renderiza botones de editar y eliminar para cada canción
                    return `
                        <button class="btn btn-warning btn-sm btnEdit" data-id="${data.id}">Editar</button>
                        <button class="btn btn-danger btn-sm btnDelete" data-id="${data.id}">Eliminar</button>
                    `;
                }
            }
        ]
    });

    // Evento para agregar una nueva canción
    $('#addSongForm').on('submit', function(e) {
        e.preventDefault(); // Previene el comportamiento predeterminado del formulario

        var fileInput = $('#archivo')[0].files[0]; // Obtiene el archivo seleccionado por el usuario
        if (fileInput) {
            var fileExtension = fileInput.name.split('.').pop().toLowerCase(); // Extrae la extensión del archivo
            // Verifica que el archivo sea de tipo mp3 o mp4
            if (!['mp3', 'mp4'].includes(fileExtension)) {
                alert("Solo se permiten archivos MP3 y MP4."); // Muestra alerta si el archivo tiene una extensión incorrecta
                return;
            }
        } else {
            alert("Debe seleccionar un archivo."); // Muestra alerta si no se selecciona ningún archivo
            return;
        }

        var formData = new FormData(this); // Crea un objeto FormData con los datos del formulario

        $.ajax({
            url: 'api/canciones.php', // URL del endpoint donde se enviarán los datos
            type: 'POST', // Método HTTP POST
            data: formData, // Los datos del formulario (incluyendo el archivo)
            processData: false, // No procesar los datos (para archivos)
            contentType: false, // No establecer el tipo de contenido (esto se maneja automáticamente cuando se suben archivos)
            success: function(response) {
                console.log(response); // Muestra la respuesta del servidor en consola
                $('#addSongModal').modal('hide'); // Cierra el modal de agregar canción
                table.ajax.reload(); // Recarga la tabla con los datos actualizados
                $('#addSongForm')[0].reset(); // Resetea el formulario
            },
            error: function(xhr, status, error) {
                console.error("Error al agregar la canción:", error); // Muestra errores si los hay
            }
        });
    });

    // Evento para cargar los datos de una canción para editarla
    $('#songsTable').on('click', '.btnEdit', function () {
        var id = $(this).data('id'); // Obtiene el ID de la canción seleccionada
        
        // Busca la canción con el ID correspondiente en los datos de la tabla
        var songData = table.row($(this).closest('tr')).data();
        
        if (songData) {
            // Rellena el formulario de actualización con los datos de la canción
            $('#updateSongId').val(songData.id);
            $('#updateTitulo').val(songData.titulo);
            $('#updateArtista').val(songData.artista);
            $('#updateGenero').val(songData.genero);
            $('#updateSongModal').modal('show'); // Muestra el modal de actualización
        } else {
            console.error('No se pudo obtener los datos de la canción');
        }
    });

    // Evento para actualizar una canción existente
    $('#updateSongForm').on('submit', function (e) {
        e.preventDefault(); // Previene el comportamiento predeterminado del formulario
        
        // Crea un objeto FormData para enviar datos incluyendo posibles archivos
        var formData = new FormData();
        
        // Agrega los campos al FormData
        formData.append('id', $('#updateSongId').val());
        formData.append('titulo', $('#updateTitulo').val());
        formData.append('artista', $('#updateArtista').val());
        formData.append('genero', $('#updateGenero').val());
        
        // Verifica si se seleccionó un nuevo archivo
        var fileInput = $('#updateArchivo')[0];
        if (fileInput.files.length > 0) {
            var file = fileInput.files[0];
            var fileExtension = file.name.split('.').pop().toLowerCase();
            
            // Verifica que el archivo sea de tipo mp3 o mp4
            if (!['mp3', 'mp4'].includes(fileExtension)) {
                alert("Solo se permiten archivos MP3 y MP4.");
                return;
            }
            
            formData.append('archivo', file);
        }
        
        // Convierte FormData a un objeto URL codificado para PUT
        var formDataString = '';
        for (var pair of formData.entries()) {
            // No incluimos el archivo en esta cadena
            if (pair[0] !== 'archivo') {
                formDataString += pair[0] + '=' + encodeURIComponent(pair[1]) + '&';
            }
        }
        formDataString = formDataString.slice(0, -1); // Elimina el último '&'
        
        $.ajax({
            url: 'api/canciones.php', // URL del endpoint para actualizar la canción
            type: 'PUT', // Método HTTP PUT
            data: formDataString, // Envía los datos como un string codificado en URL
            contentType: 'application/x-www-form-urlencoded', // Especifica el tipo de contenido correcto
            success: function (response) {
                console.log(response); // Muestra la respuesta del servidor en consola
                
                // Si se seleccionó un nuevo archivo, lo enviamos en una solicitud separada
                if (fileInput.files.length > 0) {
                    var id = $('#updateSongId').val();
                    var fileFormData = new FormData();
                    fileFormData.append('id', id);
                    fileFormData.append('archivo', fileInput.files[0]);
                    
                    $.ajax({
                        url: 'api/update_file.php', // URL del endpoint para actualizar el archivo
                        type: 'POST',
                        data: fileFormData,
                        processData: false,
                        contentType: false,
                        success: function(fileResponse) {
                            console.log('Archivo actualizado:', fileResponse);
                            $('#updateSongModal').modal('hide'); // Cierra el modal de actualización
                            table.ajax.reload(); // Recarga la tabla con los datos actualizados
                        },
                        error: function(xhr, status, fileError) {
                            console.error('Error al actualizar el archivo:', fileError);
                        }
                    });
                } else {
                    $('#updateSongModal').modal('hide'); // Cierra el modal de actualización
                    table.ajax.reload(); // Recarga la tabla con los datos actualizados
                }
            },
            error: function (xhr, status, error) {
                console.error('Error al actualizar la canción:', error); // Muestra errores si los hay
                console.log(xhr.responseText); // Muestra la respuesta completa para depuración
            },
        });
    });

    // Evento para eliminar una canción
    $('#songsTable').on('click', '.btnDelete', function() {
        var id = $(this).data('id'); // Obtiene el ID de la canción seleccionada
        $('#deleteSongId').val(id); // Rellena el campo del ID de la canción a eliminar
        $('#deleteSongModal').modal('show'); // Muestra el modal de confirmación de eliminación
    });

    // Confirmación para eliminar una canción
    $('#confirmDelete').on('click', function() {
        var id = $('#deleteSongId').val(); // Obtiene el ID de la canción a eliminar
        $.ajax({
            url: 'api/canciones.php?id=' + id, // URL del endpoint para eliminar la canción
            type: 'DELETE', // Método HTTP DELETE
            success: function(response) {
                console.log(response); // Muestra la respuesta del servidor en consola
                $('#deleteSongModal').modal('hide'); // Cierra el modal de eliminación
                table.ajax.reload(); // Recarga la tabla con los datos actualizados
            },
            error: function(xhr, status, error) {
                console.error("Error al eliminar la canción:", error); // Muestra errores si los hay
            }
        });
    });
});
