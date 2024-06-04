document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');
    const phoneList = document.getElementById('phone-list');


    filterForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(filterForm);
        const params = new URLSearchParams(formData).toString();
        fetch(`/filter_phones/?${params}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            // Clear current phone list
            phoneList.innerHTML = '';

            // Add filtered phones to the list
            data.phones.forEach(phone => {
                const phoneItem = document.createElement('li');
                phoneItem.classList.add('phone-item');

                const phoneImage = document.createElement('img');
                phoneImage.classList.add('phone-image');
                phoneImage.src = phone.image_url;
                phoneImage.alt = 'phone';

                const phoneTitle = document.createElement('h2');
                phoneTitle.classList.add('phone-title');
                phoneTitle.textContent = phone.title;

                const phoneDescription = document.createElement('p');
                phoneDescription.classList.add('phone-description');
                phoneDescription.textContent = phone.description;

                const phonePrice = document.createElement('p');
                phonePrice.classList.add('phone-price');
                phonePrice.textContent = `${phone.price}$`;

                const phoneStock = document.createElement('p');
                phoneStock.classList.add('phone-stock');
                phoneStock.textContent = phone.in_stock ? 'В наличии' : 'Нет в наличии';

                const phoneDetailLink = document.createElement('a');
                phoneDetailLink.classList.add('phone-detail-link');
                phoneDetailLink.href = `/phone_detail/${phone.id}`;
                phoneDetailLink.textContent = 'Подробнее';

                phoneItem.appendChild(phoneImage);
                phoneItem.appendChild(phoneTitle);
                phoneItem.appendChild(phoneDescription);
                phoneItem.appendChild(phonePrice);
                phoneItem.appendChild(phoneStock);
                phoneItem.appendChild(phoneDetailLink);

                phoneList.appendChild(phoneItem);
            });
        })
        .catch(error => console.error('Error:', error));
    });
});
