from unittest import TestCase
from src.actions.search_band_by_name import fetch_band_by_name
from src.models.band import BandGenreEnum, Band, BandMember


class TestSearch(TestCase):
    def test_fetch_band_by_name_WHEN_called_THEN_returns_band_with_matching_name(self):
        # ARRANGE
        searched_name = 'fake'
        band2 = Band('Fake Band', BandGenreEnum.PAGODE, [BandMember('Any Member', 'Any instrument')])
        searched_bands_list = [band2]

        # ACT
        search_result_list = [name for name in fetch_band_by_name(searched_name, searched_bands_list)]

        # ASSERT
        self.assertIn(band2, search_result_list)

    def test_fetch_band_by_name_WHEN_called_THEN_doesnot_return_band_with_different_name(self):
        # ARRANGE
        searched_name = 'fake'
        band1 = Band('Example', BandGenreEnum.PAGODE, [BandMember('Any Member', 'Any instrument')])
        searched_bands_list = [band1]

        # ACT
        search_result_list = [name for name in fetch_band_by_name(searched_name, searched_bands_list)]

        # ASSERT
        self.assertNotIn(band1, search_result_list)
