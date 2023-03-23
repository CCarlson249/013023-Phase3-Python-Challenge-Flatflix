from classes.movie import Movie
from classes.viewer import Viewer

class Review:
    
    def __init__(self, viewer, movie, rating):
        if not isinstance(movie, Movie):
            raise Exception("movie must be an instance of Movie class")
        
        if not isinstance(viewer, Viewer):
            raise Exception("viewer must be an instance of Viewer class")
        
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise Exception("rating must be an integer between 1 and 5, inclusive")
        
        self.movie = movie
        self.viewer = viewer
        self.rating = rating
        
        viewer.reviews.append(self)
        viewer.reviewed_movies.append(movie)
        movie.reviews.append(self)
        movie.reviewers.append(viewer)

    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or value < 1 or value > 5:
            raise Exception("rating must be an integer between 1 and 5, inclusive")
        self._rating = value

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, value):
        if not isinstance(value, Viewer):
            raise Exception("viewer must be an instance of Viewer class")
        self._viewer = value

    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, value):
        if not isinstance(value, Movie):
            raise Exception("movie must be an instance of Movie class")
        self._movie = value