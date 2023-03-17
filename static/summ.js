const cart = document.querySelector('[total]');
here = localStorage.getItem('total')

cart.insertAdjacentHTML('beforeend', here + '₽')

