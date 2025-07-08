# Foobar

Foobar is a Python library for dealing with geometric shapes.

```bash
pip install geometry
```

## Usage

```python
from geometry import shapes
from geometry.utils import area_stats

square = shapes.Square(4.0)
print(f'Area: {square.area()}')

circle = shapes.Square(3)
print(f'Area: {circle.area()}')

print(area_stats([square, circle]))
```

## Contributing

Please update tests as appropriate

Create a pull request

## License

Me