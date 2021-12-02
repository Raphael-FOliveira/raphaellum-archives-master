from src.models.band import Band


def list_all_bands(bands_list: list[Band]):
    for band in bands_list:
        print(band.name)
        print("\n")
