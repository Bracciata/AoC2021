input_file = open('input.txt', 'r')
lines = input_file.readlines()
def count_bits_by_pos(values):
    counts = {}
    for line in values:
        for i in range(len(line)):
            if i in counts:
                if line[i] in counts[i]:
                    counts[i][line[i]]+=1
                else:
                    counts[i][line[i]]=1
            else:
                counts[i]={line[i]:1}
    return counts         
def get_oxygen():
    oxygen_options = lines[:]
    for i in range(13):
        counts = count_bits_by_pos(oxygen_options)
        if counts[i]['0']==counts[i]['1']:
            max_occurring = '1'
        else:
            max_occurring = max(counts[i], key=counts[i].get)
        oxygen_options = list(filter(lambda s: s[i]==max_occurring,oxygen_options))
        if len(oxygen_options)==1:
            break
    return int(oxygen_options[0],2)
def get_co2():

    co2_options = lines[:]
    for i in range(13):
        counts = count_bits_by_pos(co2_options)
        if counts[i]['0']==counts[i]['1']:
            min_occurring = '0'
        else:
            min_occurring = min(counts[i], key=counts[i].get)
        co2_options = list(filter(lambda s: s[i]==min_occurring,co2_options))
        if len(co2_options)==1:
            break
    return int(co2_options[0],2)
oxy = get_oxygen()
co2 = get_co2()
print(oxy)
print(co2)
print(oxy*co2)
