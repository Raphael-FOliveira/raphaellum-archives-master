

class BandMember:
    __name: str
    __instrument: str

    def __init__(self, name: str, instrument: str) -> None:
        self.__name = name
        self.__instrument = instrument

    @property
    def name(self) -> str:
        return self.__name

    @property
    def instrument(self) -> str:
        return self.__instrument

    # TODO: Create personalized method to represent the bandmember in containers.
    def __repr__(self):
        return f'\nName: {self.__name}\n' \
               f'Instrument: {self.__instrument}\n'
