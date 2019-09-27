#Bonus material #1
def print_movie(movie, year):
    print(f'The movie {movie} is from year {year}.')


movie = "The Matrix"
year = 1999

print(print_movie(movie, year))

# Bonus material #2
def movie_info(user_movie, user_movie_year):
    print(f'The movie {user_movie} was released in {user_movie_year}.')

user_movie = input("what is your favorite movie? ")
user_movie_year = input("what year was the movie made? ")

print(movie_info(user_movie,user_movie_year))


#Bonus material #3
movie_list = [
                {"year":1979, "name": "name": Star Wars}
                {"year":1983, "name": "name": Empire Strikes Back}
                {"year":1987, "name": "name": Return of the Jedi}
            ];

movie1 = {"year":1979, "name": "name": Star Wars}
movie2 =
movie3 = 
for movie in movie_list:
    print (movie_info(movie["name"], movie["year"]))
