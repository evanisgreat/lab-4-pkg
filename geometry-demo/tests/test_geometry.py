import pytest
from geometry.shapes import Square, Circle
from geometry.utils import area_stats

def test_square_area_zero_and_positive():
# Arrange: choose side lengths
# Act: compute areas
# Assert: use pytest.approx to compare with expected
    s1 = Square(0)
    assert s1.area() == pytest.approx(0.0)

    s2 = Square(4)
    assert s2.area() == pytest.approx(16.0)

    s3 = Square(1.2)
    assert s3.area() == pytest.approx(1.44)


def test_stats_keys_and_values():
# Arrange: create several shapes
# Act: call area_stats
# Assert: stats is dict, has correct keys, and values are numbers
    shapes = [Square(3), Circle(2), Square(6)]
    assert type(area_stats(shapes)) == dict
    assert len(area_stats(shapes)) == 5

def test_stats_raises_without_shapes():
# Assert that calling area_stats() raises ValueError
    with pytest.raises(ValueError):
            area_stats(None)