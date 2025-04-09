// app.js

// Función para manejar la búsqueda de razas de mascotas
async function searchPets() {
    const breed = document.getElementById('breed-search').value;
    if (!breed) {
      alert("Por favor, ingrese una raza para buscar.");
      return;
    }
  
    // Lógica para llamar a las APIs de razas y mostrar los resultados
    // Puedes agregar el código para buscar razas en las APIs correspondientes aquí
    alert(`Buscando la raza de mascota: ${breed}`);
  }
  