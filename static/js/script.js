function sendMessage() {
    const input = document.getElementById("userInput")
    const message = input.value.trim()
    const chatBox = document.getElementById("chatBox")
    const placeholder = document.getElementById("placeholder")


    if (!message) {
        return;
    }

    if (placeholder) {
        placeholder.remove()
    }

    chatBox.innerHTML += `<div class='message user mb-2'><strong>Tú:</strong> ${message}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = '';

    fetch("/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<div class='message bot mb-2'><strong class='text-danger'>Bot:</strong> ${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight
        })
        .catch(() => {
            chatBox.innerHTML += `<div class='message bot'><strong>Bot:</strong> Error al responder 😓</div>`;
            chatBox.scrollTop = chatBox.scrollHeight
        })
}
document.getElementById("userInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage()
    }
})