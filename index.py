from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# TMDb API key (replace with your own key)
API_KEY = '921e9393001d0fbc6f69d55dd9c100b5'

# Store reviews in a dictionary (this can be replaced with a database)
movie_reviews = {}

class ReviewForm(FlaskForm):
    review = TextAreaField('Write your review:')
    submit = SubmitField('Submit')

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        movie_query = request.form["movie"]
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_query}"
        response = requests.get(url)
        movies = response.json().get('results', [])
        return render_template("index.html", movies=movies)
    return render_template("index.html")

@app.route("/movie/<int:movie_id>", methods=["GET", "POST"])
def view_movie(movie_id):
    # Fetch movie details from TMDb
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}')
    movie = response.json()

    # Get the reviews for the movie
    reviews = movie_reviews.get(str(movie_id), [])

    # Process review form submission
    form = ReviewForm()
    if form.validate_on_submit():
        review = form.review.data
        # Save the review (in-memory storage for now)
        if str(movie_id) not in movie_reviews:
            movie_reviews[str(movie_id)] = []
        movie_reviews[str(movie_id)].append(review)
        return redirect(url_for('view_movie', movie_id=movie_id))

    return render_template("moviedetail.html", movie=movie, reviews=reviews, form=form)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
