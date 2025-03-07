# Simple List Comprehension

temps = [221, 234, 340, 230]

new_temps = [t / 10 for t in temps]

print (new_temps)

# List Comprehesion with If Conditional

temps = [221, 234, 340, -9999, 230]

new_temps = [t/10 for t in temps if t != -9999]

print(new_temps)

# List comprehension with if-else conditional

temps = [221, 234, 340, -9999, 230]

new_temps = [t/10 if t != -9999 else 0 for t in temps]

print(new_temps)