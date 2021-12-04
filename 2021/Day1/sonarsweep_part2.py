import sys

with open('sample_sonarsweep.txt', 'r') as file:
    depths = file.readlines()

windows = []

for i in range(len(depths) - 2):
    sum = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
    windows.append(sum)

measurement_changes = []

for i in range(len(windows)):
    if i == 0:
        measurement_changes.append('NA')
    elif windows[i] > windows[i-1]:
        measurement_changes.append('increased')
    else:
        measurement_changes.append('decreased')

increaments = measurement_changes.count('increased')

print(len(measurement_changes))
print(increaments)