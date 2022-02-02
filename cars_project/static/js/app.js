// function solve() {
//     let rentButtonElement = document.querySelector('.rent-button');
//     console.log('You clicked it !!!');
// }
//

let rentButton = document.querySelector('.rent-btn');
rentButton.addEventListener('click', (e) => {
    let notificationBox = document.querySelector('.notification-box');

    notificationBox.style.display = 'block';


    setTimeout(function () {
        notificationBox.style.display = 'none';
    }, 3000)
})


let checkoutButton = document.querySelector('.send-email-button');

checkoutButton.addEventListener('click', () => {
    e.preventDefault();

    let notificationBox = document.querySelector('.notification-box');

    notificationBox.style.display = 'block';


    setTimeout(function () {
        notificationBox.style.display = 'none';
    }, 3000)
})