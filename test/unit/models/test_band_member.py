from unittest import TestCase

from src.models.band_member import BandMember


class TestBandMember(TestCase):

    def test_name_when_name_is_fake_member_then_returns_fake_member(self):
        # ARRANGE
        member_name = 'Fake Member'
        band_member = BandMember(name=member_name, instrument='No Instrument')

        # ACT
        result_member_name = band_member.name

        # ASSERT
        expected_member_name = 'Fake Member'
        self.assertEqual(expected_member_name, result_member_name)

    def test_instrument_when_instrument_is_oboe_then_returns_oboe(self):
        # ARRANGE
        member_instrument = 'Oboé'
        band_member = BandMember(name='Fake Member', instrument=member_instrument)

        # ACT
        result_member_instrument = member_instrument

        # ASSERT
        expected_member_instrument = 'Oboé'
        self.assertEqual(expected_member_instrument, result_member_instrument)
        