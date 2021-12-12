import sys

with open('sample_sonarsweep.txt', 'r') as file:
    depths = file.readlines()

measurement_changes = []

for i in range(len(depths)):
    if i == 0:
        measurement_changes.append('NA')
    elif int(depths[i]) > int(depths[i-1]):
        measurement_changes.append('increased')
    else:
        measurement_changes.append('decreased')

increaments = measurement_changes.count('increased')

print(len(measurement_changes))
print(increaments)