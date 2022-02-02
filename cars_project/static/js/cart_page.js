let checkoutButton = document.querySelector('.send-email-button');

checkoutButton.addEventListener('click', (e) => {
    e.preventDefault();

    let notificationBox = document.querySelector('.notification-box');

    notificationBox.style.display = 'block';


    setTimeout(function () {
        notificationBox.style.display = 'none';
    }, 3000)
})