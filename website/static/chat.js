// document.addEventListener('DOMContentLoaded', function () {
//     const sendBtn = document.querySelector('#btn-1');
//     sendBtn.addEventListener('click', function () {
//         const messageInput = document.querySelector('#user_input').value;
//         fetch('/send_message', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'  // Set content type to JSON
//             },
//             body: JSON.stringify({ user_input: messageInput }) // Corrected
//         })
//             .then(response => {
//                 if (response.ok) {
//                     // Clear input field after sending message
//                     document.querySelector('#user_input').value = '';
//                     // Optionally, you can fetch and display updated messages
//                     fetchMessages(); // Fetch messages when the page loads
//                 } else {
//                     console.error('Error sending message:', response.statusText);
//                 }
//             })
//             .catch(error => {
//                 console.error('Error sending message:', error);
//             });
//     });

//     // Function to fetch all messages and display them
//     function fetchMessages() {
//         fetch('/all_messages')
//             .then(response => response.json())
//             .then(messages => {
//                 const messagesLog = document.querySelector('#messages-log');
//                 messagesLog.innerHTML = ''; // Clear previous messages
//                 messages.forEach(message => {
//                     messagesLog.innerHTML += `
//                         <p><strong>${message.user}</strong></p>`;
//                     messagesLog.innerHTML += `<p>${message.message}</p>`
//                 });
//             })
//             .catch(error => {
//                 console.error('Error fetching messages', error);
//             });
//     }
//     // Poll for new message every 3 seconds
//     setInterval(fetchMessages, 3000);
// });

document.addEventListener('DOMContentLoaded', function () {
    const messageInput = document.querySelector('#user_input');
    const messageLog = document.querySelector('#messages-log');
    const sendBtn = document.querySelector('#btn-1');

    sendBtn.addEventListener('click', newMessageHandler);
    messageInput.addEventListener('keypress', (evt) => {
        if (evt.key === 'Enter') {
            newMessageHandler();
        }
    });

    // function to send a new message
    function newMessageHandler() {
        if (messageInput.value === '') {
            alert('Please enter a message!');
            return;
        }

        fetch('/send_message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: messageInput.value })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.message == 'OK') {
                    messageInput.value = '';
                } else {
                    alert('Error: Message could not be send')
                }
            })
            .catch(error => {
                console.error('Problem with fetch operation', error)
                alert('Error: Failed to send message. Please try again later.')
            });
    }


    // Scroll to the bottom of the chat log area
    messageLog.scrollTop = messageLog.scrollHeight;
});


// document.addEventListener('DOMContentLoaded', function () {
//     const messageInput = document.querySelector('#user_input');
//     const messageLog = document.querySelector('#messages-log');

//     document.querySelector('#btn-1').addEventListener('click', sendMessageHandler);
//     messageInput.addEventListener('keypress', (evt) => {
//         if (evt.key === 'Enter') sendMessageHandler();

//     });

//     function sendMessageHandler() {
//         if (messageInput.value === '') {
//             alert('Please enter a message!')
//             return;
//         }

//         fetch('/send_message', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ text: messageInput.value })
//         })
//             .then(response => response.json())
//             .then(response => {
//                 if (response.message == 'OK') {
//                     messageInput.value = '';
//                     getMessages();
//                 } else {
//                     alert(response.message);
//                 }
//             });
//     }

//     function getMessages() {
//         fetch('/all_messages')
//             .then(response => response.json())
//             .then(processNewMessages)
//     }
//     getMessages();

//     // Loop through each message to create a giant HTML string, then display it to the UI
//     function processNewMessages(all_messages) {
//         let new_text = '';
//         all_messages.forEach(message => {
//             new_text += `
//                <div class="message ${message.user === currUser ? "user_message" : "other_message"}">
//                     <div class="message_header">
//                         <div class="message_sender">${message.user}</div>
//                         <div class="message_datetime">${message.time}</div>
//                     </div>
//                     <div class="message_text">${message.text}</div>
//                 </div>
//             `;
//         });
//         messageLog.innerHTML = new_text;

//         // Scroll to the bottom of the chat log area
//         messageLog.scrollTop = messageLog.scrollHeight;

//         setTimeout(getMessages, 4000);
//     }

// });