with open('input.txt', 'r') as file:
    segments = file.read().split('\n')

segments_dic = {}
for i in segments:
    key, value = i.split('|')
    segments_dic[key.strip()] = value.strip()

list_digts = []
for e in segments_dic.values():
    list_digts.append(e.split())

count = 0
for list in list_digts:
    for i in range(4):
        if len(list[i]) in (2, 3, 4, 7):
            count += 1

print(count)