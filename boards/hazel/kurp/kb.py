import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D9,
        board.D8,
        board.D7,
        board.D6,
        board.D5,
    )
    row_pins = (
        board.D29,
        board.D28,
        board.D27,
        board.D26,
        board.D22,
        board.D20,
        board.D23,
        board.D21,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    # flake8: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,    24, 23, 22, 21, 20,
         5,  6,  7,  8,  9,    29, 28, 27, 26, 25,
        10, 11, 12, 13, 14,    34, 33, 32, 31, 30,
        15, 16, 17, 18, 19,    39, 38, 37, 36, 35
    ]

