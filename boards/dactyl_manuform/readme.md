# Dactyl ManuForm

The [Dactyl ManuForm](https://github.com/tshort/dactyl-keyboard) is a handwired, split bodied, tented, curved keywell keyboard.  
Adapted from the [Dactyl](https://github.com/adereth/dactyl-keyboard) keyboard combining the thumb cluster from the [ManuForm](https://geekhack.org/index.php?topic=46015.0) keyboard (2013-07).  
Information for building a Dactyl Manuform found in first link.

![WiredDm](https://i.imgur.com/7y0Vbyd.jpg)
*Two wired Dactyl ManuForm 4x6 variants*

![WirelessDm](https://i.imgur.com/FpkRuCH.jpeg)
*Wireless Dactyl ManuForm 5x6 variant*

## Variants

Dactyl ManuForm's are built in variations that cater for different row and column counts, and thumb clusters.  
Variants are denoted as `RowCount`*x*`ColumnCount` and share the common configuration of:
- The finger key-well bottom row has 2 keys; 1 each in ring and middle columns.
    - Exception to this rule is the 7 column variants that have two additional keys in this row.
- The thumb cluster has 6 keys, arranged in 2 columns by 3 rows.

### Row
| Count | Description |
| --- | --- |
| 4 | Three rows, typically for alphabet and some punctuation characters, with 2 key (finger keywell) bottom row |
| 5 | Like *4 rows* with number row above |
| 6 | Like *5 rows* with function row above |

### Column
| Count | Description |
| --- | --- |
| 5 | A column for each finger with additiona index finger column |  
| 6 | Like *5 columns* with additional pinky finger column |
| 7 | Like *6 columns* with either an additional index finger column (`5x7`) or additional pinky column (`6x7`) |

## Microcontroller Support

If microcontrollers are not 0xCB Helios:  
Please amend `helios` in the following line of desired variant's `kb.py` file to supported microcontroller listed in `kmk/quickpin/pro_micro`:

```python
from kmk.quickpin.pro_micro.helios import pinout as pins
```
For example, nice!nano controller(s): 
```python
from kmk.quickpin.pro_micro.nice_nano import pinout as pins
```

## KMK Specifics

Extentions enabled by default:  
- [Layers](/docs/en/layers.md): As many as you want/need
- [Split](/docs/en/split_keyboards.md): Configured to 1-wire UART to match legacy configuration. Please see documentation for enabling 2-wire UART or, for capable controllers, Bluetooth.
