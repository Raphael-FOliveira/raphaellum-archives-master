from unittest import TestCase
from src.actions.delete_band import delete_band
from src.models.band import Band, BandGenreEnum, BandMember


class TestDeleteBand(TestCase):
    def test_delete_band(self):
        # ARRANGE
        test_band_name: str = 'Test Band'
        test_band: Band = Band(test_band_name, BandGenreEnum.ARROCHA, [BandMember('Test Member', 'Test Instrument')])
        test_bands_list: list[Band] = [test_band]

        # ACT
        delete_band('Test Band', test_bands_list)

        # ASSERT
        self.assertNotIn(test_band, test_bands_list)
