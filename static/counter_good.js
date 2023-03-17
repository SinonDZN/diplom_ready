const btnminus = document.querySelector('[data-action="minus"]');
const btnplus = document.querySelector('[data-action="plus"]');
const count = document.querySelector('[data-counter]');


btnminus.addEventListener('click', function () {

    if (parseInt(count.innerText) > 1) {
        count.innerText = --count.innerText;
    }

});

btnplus.addEventListener('click', function () {
    count.innerText = ++count.innerText;
});


window.addEventListener('click', function (event) {

        if (event.target.dataset.action === 'plus') {
            const wrapper = event.target.closest('.d-grid');
            const divcount = wrapper.querySelector('[data-counter]');
            divcount.innerText = ++divcount.innerText;

        }
        if (event.target.dataset.action === 'minus') {
            const wrapper = event.target.closest('.d-grid');
            const divcount = wrapper.querySelector('[data-counter]');
            if (parseInt(divcount.innerText) > 1) {
                divcount.innerText = --divcount.innerText;
            } else if (event.target.closest('.item') && parseInt(divcount.innerText) === 1) {
                event.target.closest('.idk').remove();
                const ops = document.querySelector('.tbh').outerHTML
                localStorage.setItem('div', ops)



                caclCartPrice();

            }


        }
        if (event.target.hasAttribute('data-action') && event.target.closest('.item')) {
            caclCartPrice();

        }
    }
)
;
