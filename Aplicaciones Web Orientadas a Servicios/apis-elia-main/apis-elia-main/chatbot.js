// chatbot.js

async function getChatbotResponse() {
    const message = document.getElementById('chat-input').value;
    if (!message) {
      alert("Por favor, escribe una pregunta.");
      return;
    }
  
    // Aquí se hace una simulación de respuesta del chatbot
    alert(`Consultando al chatbot: ${message}`);
  
    // Integrar OpenAI o cualquier chatbot real
    /*
    const response = await fetch(config.openAiApiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        prompt: message,
        max_tokens: 100
      })
    });
  
    const data = await response.json();
    alert(data.choices[0].text);
    */
  }
  