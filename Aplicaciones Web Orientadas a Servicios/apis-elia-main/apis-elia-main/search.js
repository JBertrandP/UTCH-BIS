
async function searchPets() {
    const breed = document.getElementById('breed-search').value;
    if (!breed) {
      alert("Por favor, ingrese una raza para buscar.");
      return;
    }

    try {
    
      const apiUrl1 = `https://api.example.com/search?breed=${breed}&key=live_fenUjkuCcBWH5FwznxBanhYZgFYJyLWwstH46nwGQapwBGtoZOdMj1L9OPMRCKqs`;
      
   
      const apiUrl2 = `https://api.example.com/search?breed=${breed}&key=live_PtYd0yX90wRRrPAZllcpSsnrID5IHJ6ZIhKcLYkArGiP9giKrP7fCzllWgDjp06o`;

 
      const response1 = await fetch(apiUrl1);
      const data1 = await response1.json();
      console.log("Resultados con la primera API:", data1);
      
    
      const response2 = await fetch(apiUrl2);
      const data2 = await response2.json();
      console.log("Resultados con la segunda API:", data2);

      
      alert(`Resultados encontrados: ${data1.length + data2.length}`);
    } catch (error) {
      console.error("Error al buscar razas de mascotas:", error);
      alert("Hubo un error al buscar las razas de mascotas.");
    }
}
