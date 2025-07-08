from geometry import shapes
from geometry.utils import area_stats

square = shapes.Square(4.0)
print(f'Area: {square.area()}')

circle = shapes.Square(3)
print(f'Area: {circle.area()}')

print(area_stats([square, circle]))