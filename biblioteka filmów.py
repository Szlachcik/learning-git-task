class movie:
    def __init__(self, title, year, type, number_of_plays):
        self.title = title
        self.year = year
        self.type = type
        self.number_of_plays = number_of_plays

movie_1 = movie(title="Forest Gump", year="1994", type="Drama / Comedy", number_of_plays=8)
movie_2 = movie(title="Fight Club", year="1999", type="Thriller / Psychological", number_of_plays=5)
movie_3 = movie(title="The Grand Budapest Hotel", year="2014", type="Drama / Comedy", number_of_plays=4)
movie_4 = movie(title="Snatch", year="2000", type="crime comedy", number_of_plays=3)
movie_5 = movie(title="Avengers: Infinity War", year="2018", type="Action / Sci-Fi", number_of_plays=7)


class series:
    def __init__(self, title, year, type, E, S, number_of_plays):
        self.title = title
        self.year = year
        self.type = type
        self.E = E
        self.S = S
        self.number_of_plays = number_of_plays

series_1 = series(title="Game of Thrones", year="2016", type="Drama / Fantasy / Adventure", S="S06", E="E09", number_of_plays=5)
series_2 = series(title="House M.D.", year="2009", type="Drama / Comedy", S="S04", E="E16", number_of_plays=3)
series_3 = series(title="House of Cards", year="2014", type="Drama / Political", S="S02", E="E13", number_of_plays=1)
series_4 = series(title="True Detective", year="2014", type="Drama / Crime", S="S01", E="E05", number_of_plays=3)
series_5 = series(title="How I Met Your Mother", year="2010", type="Comedy", S="S05", E="E08", number_of_plays=2)


print("Biblioteka filmów:\n")

print(f"1. {movie_1.title}")
print(f"2. {movie_2.title}")
print(f"3. {movie_3.title}")
print(f"4. {movie_4.title}")
print(f"5. {movie_5.title}")
print(f"6. {series_1.title}")
print(f"7. {series_2.title}")
print(f"8. {series_3.title}")
print(f"9. {series_4.title}")
print(f"10. {series_5.title}\n")

while True:
    def biblioteka():
        x = int(input('Wybierz numer filmmu: '))
        y = 1
        if x == 1:
            print(f"Tytuł: {movie_1.title} ({movie_1.year})\nGatunek filmu: {movie_1.type}\nLiczba odtworzeń: {movie_1.number_of_plays + y}")
        elif x == 2:
            print(f"Tytuł: {movie_2.title} ({movie_2.year})\nGatunek filmu: {movie_2.type}\nLiczba odtworzeń: {movie_2.number_of_plays + y}")
        elif x == 3:
            print(f"Tytuł: {movie_3.title} ({movie_3.year})\nGatunek filmu: {movie_3.type}\nLiczba odtworzeń: {movie_3.number_of_plays + y}")
        elif x == 4:
            print(f"Tytuł: {movie_4.title} ({movie_4.year})\nGatunek filmu: {movie_4.type}\nLiczba odtworzeń: {movie_4.number_of_plays + y}")
        elif x == 5:
            print(f"Tytuł: {movie_5.title} ({movie_5.year})\nGatunek filmu: {movie_5.type}\nLiczba odtworzeń: {movie_5.number_of_plays + y}")
        elif x == 6:
            print(f"Tytuł: {series_1.title} {series_1.S}{series_1.E} ({series_1.year})\nGatunek filmu: {series_1.type}\nLiczba odtworzeń: {series_1.number_of_plays + y}")
        elif x == 7:
            print(f"Tytuł: {series_2.title} {series_2.S}{series_2.E} ({series_2.year})\nGatunek filmu: {series_2.type}\nLiczba odtworzeń: {series_2.number_of_plays + y}")
        elif x == 8:
            print(f"Tytuł: {series_3.title} {series_3.S}{series_3.E} ({series_3.year})\nGatunek filmu: {series_3.type}\nLiczba odtworzeń: {series_3.number_of_plays + y}")
        elif x == 9:
            print(f"Tytuł: {series_4.title} {series_4.S}{series_4.E} ({series_4.year})\nGatunek filmu: {series_4.type}\nLiczba odtworzeń: {series_4.number_of_plays + y}")
        elif x == 10:
            print(f"Tytuł: {series_5.title}, {series_5.S}{series_5.E} ({series_5.year})\nGatunek filmu: {series_5.type}\nLiczba odtworzeń: {series_5.number_of_plays + y}")

    biblioteka()