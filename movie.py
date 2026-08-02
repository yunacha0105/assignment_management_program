class Movie:
    def __init__(self, title, actor, genre, year):
        self.title = title
        self.actor = actor
        self.genre = genre
        self.year = year

    def __str__(self):
        return f'{self.title}, {self.actor} 출연, {self.genre}, {self.year}'