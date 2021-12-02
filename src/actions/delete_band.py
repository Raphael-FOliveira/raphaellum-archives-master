from typing import List
from src.models.band import Band


def delete_band(name: str, bands_list: List[Band]) -> None:
    for band in bands_list:
        if band.name == name:
            bands_list.remove(band)
