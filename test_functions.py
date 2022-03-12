"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import builtins
import mock
from functions import start, by_year, by_title, more_info, random_movie, choose_movie

def test_start():
    assert callable(start)

def test_by_year():
    years_list = ['2016', '2017', '2018']
    dictionary = {'Avengers': ('2018', 'link1'), 'Coco': ('2017', 'link2')}

    assert callable(by_year)
    assert type(by_year('2017', years_list, dictionary)) == list
    assert by_year('2017', years_list, dictionary) == ['Coco']
    assert type(by_year('2000', years_list, dictionary)) == str
    assert by_year('2000', years_list,
                           dictionary) == 'This year is not on our list'

def test_by_title():
    dictionary = {'Avengers': ('2018', 'link1'), 'Coco': ('2017', 'link2')}

    with mock.patch.object(builtins, 'input', lambda _: 'avengers'):
        assert callable(by_title)
        assert by_title(dictionary) == 'Avengers'
        assert type(by_title(dictionary)) == str
        assert len(by_title(dictionary)) == 8

    with mock.patch.object(builtins, 'input', lambda _: 'Parasite'):
        assert callable(by_title)
        assert by_title(dictionary) == 'This movie is not in our list'
        assert type(by_title(dictionary)) == str
        assert len(by_title(dictionary)) == 29

def test_more_info():
    assert callable(more_info)

def test_random_movie():

    movies_list = ['Bolt', 'Coco']

    assert callable(random_movie)
    assert type(random_movie(movies_list)) == str
    assert len(random_movie(movies_list)) == 4
    assert random_movie(movies_list) in movies_list

def test_choose_movie():

    assert callable(choose_movie)
    assert type(choose_movie('yes')) == str
    assert choose_movie('yes') == 'Enjoy the movie!'
    assert choose_movie('No') == 'Rerun the function to choose another movie!'
    assert choose_movie('hmm') == "Please answer 'Yes or 'No'"
