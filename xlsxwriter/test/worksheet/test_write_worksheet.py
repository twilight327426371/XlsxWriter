###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013, John McNamara, jmcnamara@cpan.org
#

import unittest
from StringIO import StringIO
from ...worksheet import Worksheet


class TestWriteWorksheet(unittest.TestCase):
    """
    Test the Worksheet _write_worksheet() method.

    """

    def setUp(self):
        self.fh = StringIO()
        self.worksheet = Worksheet(self.fh)

    def test_write_worksheet(self):
        """Test the _write_worksheet() method"""

        self.worksheet._write_worksheet()

        exp = """<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">"""
        got = self.fh.getvalue()

        self.assertEqual(got, exp)


if __name__ == '__main__':
    unittest.main()
