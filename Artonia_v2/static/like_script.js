document.addEventListener('DOMContentLoaded', function () {
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const modelType = this.dataset.modelType;
            const pk = this.dataset.pk;
            const likeIcon = this.querySelector('.like-icon');
            const likeCount = this.querySelector('.like-count');

            fetch(`/toggle-like/${modelType}/${pk}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.is_liked) {
                        likeIcon.textContent = '❤️';
                    } else {
                        likeIcon.textContent = '🤍';
                    }
                    likeCount.textContent = data.total_likes;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});
