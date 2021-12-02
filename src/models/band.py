from src.models.band_genre_enum import BandGenreEnum
from src.models.band_member import BandMember


class Band:
    __name: str
    __genre: BandGenreEnum
    __members: list[BandMember]

    def __init__(self, name: str, genre: BandGenreEnum, members: list[BandMember]) -> None:
        self.__name = name
        self.__genre = genre
        self.__members = members

    @property
    def genre(self) -> BandGenreEnum:
        return self.__genre

    @property
    def name(self) -> str:
        return self.__name

    @property
    def members(self) -> list[BandMember]:
        return self.__members


    def add_member(self, members: BandMember):
        self.__members.append(members)

    # TODO: Create personalized method to represent the band in containers.
    def __repr__(self):
        return f'Name: {self.__name}\n' \
               f'Genre: {self.__genre}\n' \
               f'Members: {self.__members}\n'
