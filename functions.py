"""A collection of functions for doing my project."""

import random
import requests
from bs4 import BeautifulSoup


def start():
    """Start our project and call other functions in a certain order.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # this code is referenced from the beautiful soup documentation page
    # also referenced from youtube video that I linked in project description
    # webscrape titles, years, and links from the imdb page
    # separate different parts into lists to make it easier and update into dictionary
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, features = "html.parser")
    movies_html = soup.find_all(class_ = 'titleColumn')
    years_html = soup.find_all(class_ = 'secondaryInfo')

    movies_list = []
    years_list = []
    url_list = []
    movies_dict = {}
    for i in range(250):
        movies_list.append(movies_html[i].a.text.title())
        years_list.append(years_html[i].text[1:-1])
        
        # this ends the code that I referenced
        url_list.append(url.replace('/chart/top/',
                                    movies_html[i].a.get('href') + '?ref_=ttpl_pl_tt'))
        movies_dict.update({movies_list[i] : (years_list[i], url_list[i]) })

    # use an if statement to get different prompts for different inputs
    search_by = input('Would you like to search by year or by random? ')
    if search_by.title() == 'Year':
        input_year = input('Choose year: ')
        print(by_year(input_year, years_list, movies_dict))

        # only run the rest of the code if we get our desired movie list
        # otherwise, the code will stop if we don't get the correct input
        if type(by_year(input_year, years_list, movies_dict)) == list:
            movie_title = by_title(movies_dict)
            print(movie_title)

            # make sure we have a valid movie title before continuing to other functions
            if movie_title != 'This movie is not in our list':
                more_info(movie_title, movies_dict)
    elif search_by.title() == 'Random':
        random_title = random_movie(movies_list)
        print(random_title)
        more_info(random_title, movies_dict)
    else:
        print("Please input 'Year' or 'Random'")


def by_year(year, years_list, dictionary):
    """Get a list of movies from a certain year.

    Parameters
    ----------
    year : str
        The year we are interested in searching through for our movies.
    years_list : list of str
        A list of movie years.
    dictionary : dict
        The dictionary of movie titles, years, and links that we are using.

    Returns
    -------
    output : list or str
        A list of movies, or a string saying the year is not listed.
    """

    output_list = []

    # make sure we have a valid year inputted before we continue
    if year in years_list:

        for i in dictionary:

            # this code ensures that if our input matches a movie's year
            # the movie title will be included in our output list
            if year == dictionary[i][0]:
                output_list.append(i)
            else:
                continue

        output = output_list
    else:
        output = 'This year is not on our list'

    return output


def by_title(dictionary):
    """Asks for user to input a movie title.

    Parameters
    ----------
    dictionary : dict
        The dictionary of movie titles, years, and links that we are using.

    Returns
    -------
    output : str
        The title of a movie, or a string saying that the movie is not listed.
    """

    title_input = input('Choose one of these titles! ' )

    # we have to make sure that the title we input
    # is one of the keys in our dictionary
    # use title case to keep all the titles from our input and dictionary consistent
    if title_input.title() in dictionary:
        output = title_input.title()
    else:
        output = 'This movie is not in our list'

    return output


def more_info(movie_title, dictionary):
    """Print the link of a movie for more information.

    Parameters
    ----------
    movie_title : str
        The title of a movie.
    dictionary : dict
        The dictionary of movie titles, years, and links that we are using.

    Returns
    -------
    None
    """

    info_input = input('Would you like more info for this movie? ')

    # depending on our input, it affects whether the link to the movie is printed
    # our input also affects whether we continue to the choose_input() function
    if info_input.title() == 'Yes':
        print(dictionary[movie_title][1])
        choose_input = input('Choose this movie? ')
        print(choose_movie(choose_input))
    elif info_input.title() == 'No':
        choose_input = input('Choose this movie? ')
        print(choose_movie(choose_input))
    else:
        print("Please input 'Yes' or 'No'")


def random_movie(movies_list):
    """Print the name of a random movie.

    Parameters
    ----------
    movies_list : list of str
        A list of movie titles.

    Returns
    -------
    output : str
        The name of a random movie from our list of titles.
    """

    output = random.choice(movies_list)

    return output


def choose_movie(choose_input):
    """Answer whether you want to choose a movie or not.

    Parameters
    ----------
    choose_input : str
        A string that says 'Yes' or 'No' depending on if you want to choose a movie.

    Returns
    -------
    output : str
        A string telling you to enjoy the movie, rerun the function, or answer yes/no.
    """

    # depending on our input, it affects what statement is returned
    if choose_input.title() == 'Yes':
        output = 'Enjoy the movie!'
    elif choose_input.title() == 'No':
        output = 'Rerun the function to choose another movie!'
    else:
        output = "Please answer 'Yes or 'No'"

    return output
