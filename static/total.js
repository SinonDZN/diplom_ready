var button = document.querySelector('.catrbtn');
button.addEventListener('click', caclCartPrice);

function caclCartPrice() {
    const cartItems = document.querySelectorAll('.idk');
    const priceTotal = document.querySelectorAll('.total');

    let totalPrice = 0;

    cartItems.forEach(function (item) {

        const amountEL = item.querySelector('[data-counter]');
        const priceEL = item.querySelector('.price');
        const currentPrice = parseInt(amountEL.innerText) * parseInt(priceEL.innerText);
        totalPrice += currentPrice;
        localStorage.setItem('total', totalPrice)


    });
    priceTotal.innerText = totalPrice;
    var frame = document.querySelector('.total-rub');
    frame.innerHTML = 'Итого: ' + totalPrice + ' ₽';


    const rubb = document.querySelector('[rub]');
    const empty = document.querySelector('.emptys');
    const shine = document.querySelector('.shine-button')
    if (totalPrice === 0) {

        shine.classList.add('d-none')
        rubb.classList.add('d-none')
        empty.classList.remove('d-none')

        localStorage.clear()

    } else {
        shine.classList.remove('d-none')
        rubb.classList.remove('d-none')
        empty.classList.add('d-none')
    }


}


