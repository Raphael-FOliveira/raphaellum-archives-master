from unittest import TestCase
from src.actions.search_band_by_name import search_band_by_name
from src.models.band import BandGenre, Band, BandMember


class TestSearch(TestCase):
    def test_search_band_by_name(self):
        # ARRANGE
        searched_name = 'fake'
        band1 = Band('Example', BandGenre.PAGODE, [BandMember('Any Member', 'Any instrument')] )
        band2 = Band('Fake Band', BandGenre.PAGODE, [BandMember('Any Member', 'Any instrument')])
        searched_bands_list = [band1, band2]

        # ACT
        search_result_list = [name for name in search_band_by_name(searched_name, searched_bands_list)]

        # ASSERT
        self.assertIn(band2, search_result_list)
        self.assertNotIn(band1, search_result_list)
