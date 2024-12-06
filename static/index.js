

document.addEventListener('DOMContentLoaded', function() {
    const reviewButtons = document.querySelectorAll('.review-btn'); // Select all buttons

    reviewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const movieId = button.getAttribute('data-movie-id'); // Get the movie ID
            showReviewForm(movieId); // Show the review form for this movie
        });
    });
});

function showReviewForm(movieId) {
    console.log("Movie ID: ", movieId); // Check if the movie ID is being passed
    const form = document.getElementById('reviewForm_' + movieId);
    if (form) {
        form.style.display = 'block';  // Show the review form
    }

    console.log("Movie ID: ", movieId);
    }
