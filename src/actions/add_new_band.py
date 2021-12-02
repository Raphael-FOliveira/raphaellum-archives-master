from src.models.band import Band, BandGenre, BandMember


def add_new_band(
        name: str,
        genre: BandGenre,
        members: list[BandMember],
        bands_list: list[Band]
):
    new_band = Band(name, genre, members)
    bands_list.append(new_band)
    return new_band
