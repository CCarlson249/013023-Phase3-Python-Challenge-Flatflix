class Movie:
    all = []
    
    def __init__(self, title):
        """Initialize a Movie instance with a title."""
        if isinstance(title, str) and len(title) > 0:
            self._title = title
            self.reviews = []
            self.reviewers = []
            Movie.all.append(self)
        else:
            raise Exception("Title must be a non-empty string")

    def gettitle(self):
        """Get the movie title."""
        return self._title
    
    def settitle(self, title):
        """Set the movie title."""
        self._title = title

    # title property goes here!
    title = property(gettitle, settitle)

    def add_review(self, review, reviewer):
        self.reviews.append(review)
        self.reviewers.append(reviewer)


    def average_rating(self):
        if len(self.reviews) == 0:
            return None
        return sum(review.rating for review in self.reviews) / len(self.reviews)


    @classmethod
    def highest_rated(cls):
        if len(cls.all) == 0:
            return None
        return max(cls.all, key=lambda movie: movie.average_rating())

    