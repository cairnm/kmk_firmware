import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
# from kmk.quickpin.pro_micro.nice_nano import pinout as pins
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[11],
        pins[10],
        pins[9],
        pins[8],
        pins[7],
    )
    row_pins = (
        pins[19],
        pins[18],
        pins[17],
        pins[16],
        pins[15],
        pins[14],
        pins[13],
        pins[12],
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

