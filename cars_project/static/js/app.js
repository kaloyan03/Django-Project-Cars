// function solve() {
//     let rentButtonElement = document.querySelector('.rent-button');
//     console.log('You clicked it !!!');
// }
//

let rentButton = document.querySelector('.rent-btn');
rentButton.addEventListener('click', (e) => {
    e.preventDefault();
    let notificationBox = document.querySelector('.notification-box');

    notificationBox.style.display = 'block';


    setTimeout(function() {
        notificationBox.style.display = 'none';
    }, 3000)
})