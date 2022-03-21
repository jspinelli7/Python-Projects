# As a user I'd like to be able to...
# Add new movies to my collection, so that i can keep track of all my movies
# List all of the movies in my collection, so that I can see what movies I already have
# Find a movie by using the movie title, so I can locate a specific movie easily when the collection grows

movies = [
    {'title': 'Avatar', 'director': 'James Cameron', 'year': 2009},
    {'title': 'The Wolf of Wall Street', 'director': 'Martin Scorsese', 'year': 2013},
]

menu_prompt = "\nEnter 'a' to add a movie, 'l' to see your movie list, 'f' to find a movie by title, or 'q' to exit: "


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    # This works too movies.append(dict(title=title, director=director, year=year))
    movies.append({
        'title': title,
        'director': director,
        'year': year,
    })


def list_movie():
    for movie in movies:
        print_movie(movie)


def search_movie():
    user_title = input("Enter the title of the movie you would like to search for: ")
    user_title = user_title.lower()

    for movie in movies:
        if movie["title"].lower() == user_title:
            print_movie(movie)
    # found_movie = list(filter(lambda movies: movies['title'].lower() == user_title, movies))
    # if found_movie:
    #    print(found_movie)
    # else:
    #    print("The movie you searched for is not in the list.")

def print_movie(movie):
    print(f"{movie['title']} was directed by {movie['director']} in {movie['year']}.")

# first clas functions:
user_options = {
    "a": add_movie,
    "l": list_movie,
    "f": search_movie,
}

def menu():
    selection = input(menu_prompt)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again')

        selection = input(menu_prompt)


menu()