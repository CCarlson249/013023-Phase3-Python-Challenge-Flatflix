import importlib

class Viewer:
    _usernames = set()
    all = []
    
    def __init__(self, username):
        if not isinstance(username, str):
            raise Exception("Username must be a string.")
        if not (6 <= len(username) <= 16):
            raise Exception("Username must be between 6 and 16 characters, inclusive.")
        if username in self._usernames:
            raise Exception("Username must be unique.")
        self._username = username
        self._usernames.add(username)
        self.reviews = []
        self.reviewed_movies = []
        pass

    # username property goes here!
    @property
    def username(self):
        return self._username

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies
    

    def rate_movie(self, movie, rating):
        for review in self.reviews:
            if review.movie == movie:
                review.rating = rating
                break
        else:
            from classes.review import Review
            new_review = Review(self, movie, rating)
            self.reviews.append(new_review)
            movie.add_review(new_review, self)
        if movie not in self.reviewed_movies:
            self.reviewed_movies.append(movie)

        