from geometry import pi

def square(figure_type, **kwargs):
    if figure_type == 'rhombus':
        return kwargs['d1'] * kwargs['d2'] / 2
    if figure_type == 'square':
        return kwargs['a'] ** 2
    if figure_type == 'trapezoid':
        return 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
    if figure_type == 'circle':
        return pi * kwargs['r'] ** 2
    return 'invalid data'


print(square(figure_type='rhombus', d1=10, d2=8))
print(square(figure_type='square', a=5))
print(square(figure_type='trapezoid', a=12, b=3, h=6))
print(square(figure_type='circle', r=18))
print(square(figure_type='unknown', a=1, b=2, c=3))