import webbrowser


# a class specify the movie properites that will show on movie trailer website
class Movie():
    # Moive class constructor.
    # __init__ gets called whenever we try to create object of class
    def __init__(self, movie_title, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    # method to open youtube trailer in popup
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
