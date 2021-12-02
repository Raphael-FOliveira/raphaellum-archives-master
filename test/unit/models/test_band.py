from unittest import TestCase

from src.models.band import Band
from src.models.band_genre import BandGenre


class TestBand(TestCase):
    # GIVEN genre
    # WHEN genre is valid
    # THEN returns expected genre
    def test_genre_WHEN_genre_is_rock_THEN_returns_rock_band_genre(self):
        # ARRANGE 
        band_genre = BandGenre.ROCK
        band = Band(name='Fake band', genre=band_genre, members=[])

        # ACT
        result_band_genre = band.genre

        # ASSERT
        expected_band_genre = BandGenre.ROCK
        self.assertEqual(expected_band_genre, result_band_genre)

    def test_name_WHEN_name_is_fake_band_THEN_returns_fake_band(self):
        # ARRANGE 
        band_name = 'Fake band'
        band = Band(name=band_name, genre=BandGenre.ROCK, members=[])

        # ACT
        result_band_name = band.name

        # ASSERT
        expected_band_name = 'Fake band'
        self.assertEqual(expected_band_name, result_band_name)

    def test_members_WHEN_members_is_empty_list_THEN_returns_empty_list(self):
        # ARRANGE
        band_members = []
        band = Band(name='Fake band', genre=BandGenre.ROCK, members=band_members)

        # ACT
        result_band_members = band_members

        # ASSERT
        expected_band_members = []
        self.assertEqual(expected_band_members, result_band_members)

