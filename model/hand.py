from strenum import StrEnum


class hand(StrEnum):
    HIGH_CARD = 'Todas diferentes'
    PAIR = 'Un par'
    TWO_PAIR = 'Doble par'
    TREE_OF_A_KIND = 'Trio'
    FULL_HOUSE = 'Full'
    FOUR_OF_A_KIND = 'Cuatro del mismo valor'
    FIVE_OF_A_KIND = 'Cinco del mismo valor'

    ERROR = "Error"
