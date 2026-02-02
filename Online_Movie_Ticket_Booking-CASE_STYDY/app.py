from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []
bookings = []

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
       if movie["id"] == movie_id:
          return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    # check duplicate movie id
    for movie in movies:
        if movie["id"] == data["id"]:
            return jsonify({"error": "Movie with this ID already exists"}), 400
    movies.append(data)
    return jsonify(data), 201


@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data=request.json
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json
    if data.get("tickets") <= 0:
        return jsonify({"error": "Invalid ticket count"}), 400
    bookings.append(data)
    return jsonify({"message": "Booking successful"}), 201

if __name__ == "__main__":
    app.run(debug=True)