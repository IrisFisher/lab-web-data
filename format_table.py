"""Compare f-string alignment and number formats; repr makes spaces visible."""

name = 'Alice'
print(repr(f'{name:<10}'))
print(repr(f'{name:>10}'))
print(repr(f'{name:^10}'))
print(repr(f'{name:*^10}'))

pi = 3.14159265
print(repr(f'{pi:.2f}'))
print(repr(f'{pi:.4f}'))
print(repr(f'{pi:8.2f}'))
print(repr(f'{pi:08.2f}'))
print(repr(f'{7.73:05.2f}'))
