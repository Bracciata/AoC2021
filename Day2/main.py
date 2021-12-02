directions_file = open('input.txt')
directions = directions_file.readlines()
horizontal, vertical = 0, 0
for direction in directions:
    if direction.startswith('up'):
        vertical -= int(direction.split(' ')[1])
    elif direction.startswith('forward'):
        horizontal += int(direction.split(' ')[1])
    else:
        vertical += int(direction.split(' ')[1])
print(f'Horizontal: {horizontal}\nVertical:{vertical}')
print(f'Product: {horizontal*vertical}')
