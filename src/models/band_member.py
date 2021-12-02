

class BandMember:
    __name: str
    __instrument: str

    def __init__(self, name: str, instrument: str) -> None:
        self.__name = name
        self.__instrument = instrument

    @property
    def name(self) -> str:
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name

    @property
    def instrument(self) -> str:
        return self.__instrument

    def __repr__(self):
        return f'\nName: {self.__name}\n' \
               f'Instrument: {self.__instrument}\n'





