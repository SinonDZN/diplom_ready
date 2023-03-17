const cartWrapper = document.querySelector('.item');

window.addEventListener('click', function (event) {
        if (event.target.hasAttribute('data-cart')) {
            const card = event.target.closest('.item');
            const productInfo = {
                img: card.querySelector('[kek]').getAttribute('src'),
                title: card.querySelector('.name').innerText,
                price: card.querySelector('.price').innerText,
            };

            const itemInCart = cartWrapper.querySelector(`[data-id="${productInfo.price}"]`);
            if (itemInCart) {

                const pls = document.querySelector('[nope]');

                pls.classList.remove('d-none')
                const btncll = document.querySelector('[clsbtn1]');
                btncll.addEventListener('click', function () {

                    pls.classList.add('d-none')
                });

            } else {


                const cartItemHTML = `<div class="idk card mb-3" data-id="${productInfo.price}" id="s" style="width: 595px;margin-left: 19px; max-height:200px; box-shadow: none;">
                <div class=" row g-0">
                    <div class="col-md-3 "style="word-break: break-word; box-shadow: none;">
                        <img src="${productInfo.img}"
                             style="height: 140px; width: 140px; margin-left: 5px; margin-top: 18px"
                             class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="title card-title"style="font-size: 15px; margin-top: 24px">${productInfo.title}</h5>
                            <p class="price card-text" style="font-size: 17px; font-weight: 500">${productInfo.price}</p>  
                            <div class="d-grid gap-3 d-md-block" style="font-weight: 500">
                                 <button class="btn btn-light btn-sm" type="button" data-action="minus"><</button>
                                 <button class="data-counter btn btn-light btn-sm" type="button" data-counter>1</button>
                                 <button class="btn btn-light btn-sm" type="button" data-action="plus">></button>
                            </div>                         
                        </div>
                    </div>
                </div>
            </div>

`;


                const view = document.querySelector('.tbh');
                const shine = document.querySelector('.shine-button')

                if (view.children.length > 0) {

                    cartWrapper.insertAdjacentHTML('beforeend', cartItemHTML);
                    localStorage.setItem('div', (localStorage.getItem('div')) + cartItemHTML);
                    shine.classList.remove('d-none')

                } else {

                    cartWrapper.insertAdjacentHTML('beforeend', cartItemHTML);
                    localStorage.setItem('div', cartItemHTML);
                }


                caclCartPrice();
                const sucs = document.querySelector('[alerta]');

                sucs.classList.remove('d-none')

                const btncl = document.querySelector('[clsbtn2]');
                btncl.addEventListener('click', function () {

                    sucs.classList.add('d-none')
                });


            }
        }
    }
)
;
