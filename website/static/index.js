// This code is for handling flash messages (error or success) for flask 

// Add event listener to the parent element to handle clicks on dismiss buttons
document.addEventListener('DOMContentLoaded', function () {
    let flashMsg = document.querySelector('.flash-messages');

    let msgSpan = document.querySelector('.msg-span');

    // Function to hide the flash message after a delay
    function hideFlashMessage(msgElem) {
        setTimeout(function () {
            msgElem.style.display = 'none';
        }, 3000); // Adjust the time delay as needed (in milliseconds)
    }

    // flashMsg.addEventListener('click', function (evt) {
    //     let msgElem = evt.target.parentElement;
    //     msgElem.style.display = 'none';
    // });

    // Hide flash messages automatically after a delay
    let flashMessages = document.querySelectorAll('.flash-messages li');
    flashMessages.forEach(function (msgElem) {
        hideFlashMessage(msgElem);
    });

    // Hide the span with the message 'You are logged in'
    function hideUserMsg() {
        setTimeout(() => {
            msgSpan.style.display = 'none';
        }, 5000);
    }

    hideUserMsg();
});



