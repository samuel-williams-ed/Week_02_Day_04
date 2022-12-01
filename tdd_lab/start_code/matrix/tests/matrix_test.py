import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    # Tests
    def setUp(self):
        self.test_matrix_string = "9 8 7\n5 3 2\n6 6 7"
        self.test_matrix_object = Matrix(self.test_matrix_string)
    # def test_extract_row_from_one_number_matrix(self):
    #     # matrix = Matrix("1")
    #     # self.assertEqual(matrix.row(1), [1])
    #     test_matrix = ("9 8 7\n5 3 2\n6 6 7")
    #     print(test_matrix[6])

    def test_matrix_object_has_string(self):
        self.assertEqual(self.test_matrix_string, self.test_matrix_object.matrix_string)

    def test_rows(self):
        self.assertEqual(["9 8 7", "5 3 2", "6 6 7"], self.test_matrix_object.return_matrix_by_row())

    def test_columns(self):
        self.assertEqual(["9 5 6", "8 3 6", "7 2 7"], self.test_matrix_object.return_matrix_by_column())






























    # Test can extract a given row

    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20

    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column

    # Test can extract column from a one number matrix

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800



