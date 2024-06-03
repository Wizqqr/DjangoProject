document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');
    const phoneList = document.getElementById('phone-list');

    filterForm.addEventListener('change', function(event) {
        event.preventDefault();

        const formData = new FormData(filterForm);

        fetch('{% url "phone_filter" %}', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                phoneList.innerHTML = data.html;
            } else {
                console.error('Error filtering phones:', data.errors);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const comments = document.querySelectorAll('.comment-text');

    function fadeInComments() {
        comments.forEach(function(comment, index) {
            const commentPosition = comment.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (commentPosition < windowHeight) {
                comment.style.opacity = 1;
                comment.style.transition = 'opacity 0.5s ease ' + (index * 0.2) + 's';
            }
        });
    }

    function fadeOutComments() {
        comments.forEach(function(comment) {
            comment.style.opacity = 0;
        });
    }

    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            fadeInComments();
        } else {
            fadeOutComments();
        }
    });

    fadeInComments(); // Trigger the animation for comments already in view
});


// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//     anchor.addEventListener('click', function (e) {
//         e.preventDefault();
//
//         document.querySelector(this.getAttribute('href')).scrollIntoView({
//             behavior: 'smooth'
//         });
//     });
// });
//
// function fadeInPhoneListItems() {
//     const phoneItems = document.querySelectorAll('.phone-item');
//     phoneItems.forEach(function(item, index) {
//         const itemPosition = item.getBoundingClientRect().top;
//         const windowHeight = window.innerHeight;
//
//         if (itemPosition < windowHeight) {
//             item.style.opacity = 1;
//             item.style.transition = 'opacity 0.5s ease ' + (index * 0.2) + 's';
//         }
//     });
// }
//
// window.addEventListener('scroll', function() {
//     fadeInPhoneListItems();
// });
//
// fadeInPhoneListItems(); // Trigger the animation for items already in view
//
// function fadeInCommentsSection() {
//     const commentsSection = document.querySelector('.comments-section');
//     const sectionPosition = commentsSection.getBoundingClientRect().top;
//     const windowHeight = window.innerHeight;
//
//     if (sectionPosition < windowHeight) {
//         commentsSection.style.opacity = 1;
//         commentsSection.style.transition = 'opacity 0.5s ease';
//     }
// }
//
// window.addEventListener('scroll', function() {
//     fadeInCommentsSection();
// });
//
// fadeInCommentsSection(); // Trigger the animation for comments section already in view
