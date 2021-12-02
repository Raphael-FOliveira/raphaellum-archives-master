from src.models.band import Band


def delete_band(name, bands_list):
    for band in bands_list:
        if band.name == name:
            bands_list.remove(band)
