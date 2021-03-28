#!python3.8

import unittest

def flight_movies(flight_length, movie_lengths):

    """return true if two movies sum up to a flight length duration"""

    lengths = {}  # lengths to the movies


    for length in movie_lengths:
       

        second_movie = flight_length - length
        if second_movie in lengths:
            return True

        lengths[length] = True

    return False


class TestFlightMovies(unittest.TestCase):

    def setUp(self):
        self.movies = list(range(100, 120))

    def test_1no_matches(self):
        self.assertFalse(flight_movies(256, self.movies))

    def test_one_match(self):
        self.movies[5] = 256 - self.movies[10]
        self.assertTrue(flight_movies(256, self.movies))

    def test_other_match(self):
        self.movies[10] = 256 - self.movies[5]
        self.assertTrue(flight_movies(256, self.movies))
      

    def test_one_match_but_same_movie(self):
        self.movies[5] = 128
        self.assertFalse(flight_movies(256, self.movies))

    def test_two_matches(self):
        self.movies[5] = 128
        self.movies[15] = 128
        self.assertTrue(flight_movies(256, self.movies))

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlightMovies)
    unittest.TextTestRunner(verbosity=2).run(suite)


