from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '921e9393001d0fbc6f69d55dd9c100b5'  # Replace with your TMDb API key

# Search route to handle form submission and fetch data
@app.route("/search", methods=["POST"])
def search():
    # Get the movie query from the form
    movie_query = request.form["movie"]
    # Make the API request to TMDb
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_query}')
    data = response.json()  # Parse the response JSON
    movies = data.get('results', [])  # Extract movie results

    # Return the template with the movies data
    return render_template("index.html", movies=movies)

# Home route to display the form
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", movies=[])

if __name__ == "__main__":
    app.run(debug=True)
