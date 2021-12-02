measurement_file = open('inputs.txt')
measurements = measurement_file.readlines()
count = 0
for i in range(1, len(measurements)):
    if int(measurements[i]) > int(measurements[i-1]):
        count += 1
print(count)
