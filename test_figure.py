from unittest import TestCase
from figure import Triangle, Square, InvalidTriangleError, InvalidSquareError


class TestTriangle(TestCase):
    def test_calc_area(self):
        # Arrange
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0

        # Act
        actual_area = triangle.calc_area()

        # Assert
        self.assertAlmostEqual(actual_area, expected_area)

    def test_calc_area_zero(self):
        with self.assertRaises(InvalidTriangleError):
            # Arrange
            triangle = Triangle(3, 0, 5)
            expected_area = 0

            # Act
            actual_area = triangle.calc_area()

            # Assert
            self.assertAlmostEqual(actual_area, expected_area)

    def test_calc_area_not_triangle(self):
        with self.assertRaises(InvalidTriangleError):
            # Arrange
            triangle = Triangle(3, 4, 7)
            expected_area = 6.0

            # Act
            actual_area = triangle.calc_area()

            # Assert
            self.assertAlmostEqual(actual_area, expected_area)

    def test_calc_perimeter(self):
        # Arrange
        triangle = Triangle(3, 4, 5)
        expected_perimeter = 12

        # Act
        actual_perimeter = triangle.calc_perimetr()

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)

    def test_invalid_triangle_zero_side(self):
        # Test creating a triangle with a zero side length should raise an error
        with self.assertRaises(InvalidTriangleError):
            Triangle(3, 0, 5)

    def test_invalid_triangle_not_a_triangle(self):
        # Test creating a triangle that does not satisfy the triangle inequality should raise an error
        with self.assertRaises(InvalidTriangleError):
            Triangle(3, 4, 7)


class TestSquare(TestCase):
    def test_calc_area(self):
        # Arrange
        square = Square(3)
        expected_area = 9

        # Act
        actual_area = square.calc_area()

        # Assert
        self.assertAlmostEqual(actual_area, expected_area)

    def test_calc_area_not_equal(self):
        # Arrange
        square = Square(3)
        expected_area = 10

        # Act
        actual_area = square.calc_area()

        # Assert
        self.assertNotEqual(actual_area, expected_area)

    def test_calc_area_under_zero(self):
        with self.assertRaises(InvalidSquareError):
            # Arrange
            square = Square(-3)
            expected_area = 9

            # Act
            actual_area = square.calc_area()

            # Assert
            self.assertAlmostEqual(actual_area, expected_area)

    def test_calc_perimetr(self):
        triangle = Square(3)
        expected_perimeter = 12

        # Act
        actual_perimeter = triangle.calc_perimetr()

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)

    def test_calc_perimetr_not_equal(self):
        triangle = Square(3)
        expected_perimeter = 10

        # Act
        actual_perimeter = triangle.calc_perimetr()

        # Assert
        self.assertNotEqual(actual_perimeter, expected_perimeter)

    def test_invalid_square_zero_side(self):
        # Test creating a triangle with a zero side length should raise an error
        with self.assertRaises(InvalidSquareError):
            Square(0)

