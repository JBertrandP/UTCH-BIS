Sonic Skyline
Este proyecto es una plataforma de recomendación de viajes que permite a los usuarios seleccionar un destino y recibir recomendaciones personalizadas basadas en diferentes filtros de búsqueda. Los usuarios pueden elegir el destino, el interés, el presupuesto, el clima y la época del año para obtener sugerencias de destinos y ver imágenes, intereses y recomendaciones relacionadas. Además, se incluye un mapa interactivo para visualizar la ubicación del destino seleccionado.

Requisitos del Proyecto
Antes de comenzar, asegúrate de tener los siguientes elementos instalados en tu sistema:

Un servidor web como Apache o Nginx (para ejecutar el proyecto en local).
PHP para manejar el backend (backend.php).
Conexión a Internet para cargar los recursos externos, como las hojas de estilo y las bibliotecas de Leaflet.
Estructura de Archivos
El proyecto contiene los siguientes archivos y carpetas:

/travel-recommendation
│
├── index.html            # Página principal con el formulario y los resultados
├── styles.css            # Hoja de estilos para el diseño de la página
├── script.js             # Archivo JavaScript para la lógica interactiva
├── logo.png              # Logo de la aplicación
├── fondo.png             # Imagen de fondo basada en las Islas de Mykonos
├── backend.php           # Script PHP para manejar las solicitudes y generar recomendaciones
└── README.md             # Documentación del proyecto

Manual de Usuario
1. Acceso a la Plataforma
Al ingresar a la página web, verás un formulario con varias opciones que puedes personalizar para obtener las recomendaciones de viaje adecuadas. Estas opciones incluyen:

Destino: Selecciona tu destino favorito entre los siguientes: París, Hong Kong, Tokio, Cancún y Ámsterdam.

Interés: Elige qué tipo de actividades o lugares te interesan más (por ejemplo, cultura, gastronomía, playas, etc.).

Presupuesto: Define el presupuesto para tu viaje (Bajo, Medio o Alto).

Clima: Elige el tipo de clima que prefieres (Cálido, Frío o Templado).

Época del Año: Selecciona la temporada que más te convenga (Primavera, Verano, Otoño o Invierno).

2. Búsqueda de Destinos
Una vez que hayas completado todos los filtros de búsqueda, presiona el botón "Buscar Destino" para enviar la solicitud.

El sistema procesará la información y te mostrará las siguientes recomendaciones:

Intereses: Una lista de actividades o intereses disponibles en el destino seleccionado.

Imágenes: Una galería de fotos relacionadas con el destino.

Recomendaciones de Viaje: Una lista de actividades, lugares y consejos personalizados para tu viaje.

Mapa: Un mapa interactivo de la ubicación del destino.

3. Visualización de Resultados
Intereses: Aparecerá una lista con los intereses que puedes disfrutar en el destino elegido.

Imágenes: Se mostrará una galería con fotos de lugares e actividades en el destino.

Recomendaciones: Te aparecerán sugerencias adicionales como actividades, lugares turísticos y consejos personalizados.

Mapa: El mapa interactivo mostrará la ubicación del destino seleccionado. Puedes hacer zoom y ver el área con más detalle.

4. Interactividad
El mapa permite ver la ubicación exacta del destino. Puedes interactuar con él, hacer zoom y explorar la zona.

Instrucciones para Desarrolladores
Si deseas ejecutar o modificar este proyecto en tu propio entorno, sigue estos pasos:

Instala un servidor web (Apache o Nginx).
Configura PHP en tu servidor para que puedas ejecutar el archivo backend.php.
Coloca todos los archivos en el directorio raíz de tu servidor web.
Abre index.html en tu navegador.