from typing import List
from src.models.band import Band, BandGenreEnum, BandMember


def add_new_band(
        name: str,
        genre: BandGenreEnum,
        members: List[BandMember],
        bands_list: List[Band]
) -> Band:
    new_band = Band(name, genre, members)
    bands_list.append(new_band)
    return new_band
