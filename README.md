<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Chatbot Interativo com PDFs</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f9;
      margin: 0;
      padding: 0;
    }
    .chat-container {
      width: 100%;
      max-width: 800px;
      margin: 50px auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      overflow: hidden;
    }
    .chat-header {
      background: #0078D7;
      color: #fff;
      padding: 15px;
      text-align: center;
      font-size: 18px;
    }
    .chat-box {
      height: 400px;
      overflow-y: auto;
      padding: 20px;
      border-bottom: 1px solid #ddd;
    }
    .message {
      margin: 10px 0;
      padding: 10px;
      border-radius: 5px;
      max-width: 70%;
    }
    .user-message {
      background: #0078D7;
      color: #fff;
      margin-left: auto;
    }
    .bot-message {
      background: #eaeaea;
      color: #333;
      margin-right: auto;
    }
    .chat-input {
      display: flex;
      padding: 10px;
    }
    .chat-input input {
      flex: 1;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
    .chat-input button {
      margin-left: 10px;
      padding: 10px 20px;
      background: #0078D7;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .chat-input button:hover {
      background: #005a9e;
    }
  </style>
</head>
<body>
  <div class="chat-container">
    <div class="chat-header">🤖 Chatbot Interativo com PDFs</div>
    <div class="chat-box" id="chat-box"></div>
    <div class="chat-input">
      <input type="text" id="user-input" placeholder="Digite sua pergunta...">
      <button onclick="sendMessage()">Enviar</button>
    </div>
  </div>

  <script>
    function sendMessage() {
      const input = document.getElementById("user-input");
      const message = input.value.trim();
      if (message === "") return;

      const chatBox = document.getElementById("chat-box");

      // Exibe mensagem do usuário
      const userMsg = document.createElement("div");
      userMsg.className = "message user-message";
      userMsg.textContent = message;
      chatBox.appendChild(userMsg);

      // Simula resposta do bot (aqui você conecta com backend/IA)
      const botMsg = document.createElement("div");
      botMsg.className = "message bot-message";
      botMsg.textContent = "🔎 Buscando resposta nos PDFs...";
      chatBox.appendChild(botMsg);

      // Aqui você faria uma chamada ao backend (API/Azure Function)
      // Exemplo fictício:
      setTimeout(() => {
        botMsg.textContent = "Resposta baseada no conteúdo dos PDFs: " + message;
      }, 1000);

      input.value = "";
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  </script>
</body>
</html>
