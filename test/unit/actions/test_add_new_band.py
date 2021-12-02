from unittest import TestCase
from src.actions.add_new_band import add_new_band
from src.models.band import Band, BandGenre, BandMember


class TestAddNewBand(TestCase):
    def test_add_new_band(self):
        # ARRANGE
        test_band_name: str = 'Test Name'
        test_band_genre: BandGenre = BandGenre.ROCK
        test_band_members: list[BandMember] = [BandMember('Test Member', 'Test Instrument')]
        test_bands_list: list[Band] = []

        # ACT
        new_test_band = add_new_band(test_band_name, test_band_genre, test_band_members, test_bands_list)

        # ASSERT
        self.assertIn(new_test_band, test_bands_list)
