let chatButton = document.querySelector(".chat-button")
let chatbox = document.querySelector('.chatbox');

chatButton.addEventListener("click", () => {
    if (chatbox.style.display === 'none' || chatbox.style.display === '') {
        chatbox.style.display = 'flex';
    } else {
        chatbox.style.display = 'none';
    }
});

async function sendMessage() {
    const message = document.getElementById('user-input').value;
    const chatContent = document.getElementById('chat-content');

    if (message.trim() === '') return;

    const userMessage = document.createElement('div');
    userMessage.textContent = message;
    userMessage.classList.add("conversation");
    userMessage.classList.add("user");
    chatContent.appendChild(userMessage);

    const response = await fetch('/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    });

    let data = await response.json();
    data = JSON.stringify(data)
    data = JSON.parse(data)

    botMessage = document.createElement("div")
    botMessage.textContent = data.reply
    botMessage.classList.add("conversation")
    botMessage.classList.add("bot")
    chatContent.appendChild(botMessage)

    document.getElementById('user-input').value = '';
}