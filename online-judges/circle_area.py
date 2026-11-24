# Circle Area - The Huxley #271 (beecrowd 1002)
# Reads a radius in cm and shows the circle area in m².

radius = float(input('Enter any radius (cm): '))
pi = 3.14159
area = pi * pow(radius, 2)
area_m2 = area / (100 * 100)
print(f'Area: {area_m2:.4f} m²')
