import os
import sys
import unittest
from decimal import Decimal


if __name__ == "__main__":
    # Allow import if ran directly
    TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
    REPO_DIR = os.path.dirname(TESTS_DIR)
    sys.path.insert(0, REPO_DIR)

from gcodefollower import (
    changed_cmd,
    get_cmd_meta,
)


class Testing(unittest.TestCase):
    def test_changed_cmd(self):
        old = "G0 F9000 X27.781 Y32.781 Z{z:.3f}\n".format(z=.2)
        expected = "G0 F9000 X27.781 Y32.781 Z{z}".format(z=.4)
        # ^ removed \n
        new = changed_cmd(old, 'Z', Decimal(.4))
        self.assertEqual(new, expected)
        new = changed_cmd(old, 'Z', .4)
        self.assertEqual(new, expected)

    def test_get_cmd_meta(self):
        self.assertEqual(
            get_cmd_meta(" G1 X110 E45 F500.0"),
            [['G', '1'], ['X', '110'], ['E', '45'], ['F', '500.0']]
        )

    def test_get_cmd_meta_klipper(self):
        self.assertEqual(
            get_cmd_meta("BED_MESH_PROFILE  LOAD=magnetic-enomaker-PEI-smooth_side-60C"),
            [['BED_MESH_PROFILE'], ['LOAD=', 'magnetic-enomaker-PEI-smooth_side-60C']]
            # ^ '=' is kept as a flag to denote it is not G-code
        )



if __name__ == '__main__':
    unittest.main()
