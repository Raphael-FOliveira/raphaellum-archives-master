from src.models.band_genre import BandGenre
from src.models.band_member import BandMember


class Band:
    __name: str
    __genre: BandGenre
    __members: list[BandMember]

    def __init__(self, name: str, genre: BandGenre, members: list[BandMember]) -> None:
        self.__name = name
        self.__genre = genre
        self.__members = members

    @property
    def genre(self) -> BandGenre:
        return self.__genre

    @property
    def name(self) -> str:
        return self.__name

    @property
    def members(self) -> list[BandMember]:
        return self.__members

    def set_members(self, members: BandMember):
        self.__members.append(members)

    def __repr__(self):
        return f'Name: {self.__name}\n' \
               f'Genre: {self.__genre}\n' \
               f'Members: {self.__members}\n'



