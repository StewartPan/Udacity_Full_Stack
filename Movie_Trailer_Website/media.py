import webbrowser


class Movie():
    # Constructor for the Movie Class
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # open trailer youtube url to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
