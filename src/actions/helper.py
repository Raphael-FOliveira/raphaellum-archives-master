from src.models.band import Band, BandGenre, BandMember
from src.actions.add_new_band import add_new_band
from src.actions.delete_band import delete_band
from src.actions.search_band_by_name import search_band_by_name
from src.actions.list_all_bands import list_all_bands

testbandlist = [Band("Test", BandGenre.PAGODE, [BandMember("Dundas", "Guitar")])]


add_new_band("Test2", BandGenre.ROCK, [BandMember("Skyadron", "Drums")], testbandlist)
list_all_bands(testbandlist)

