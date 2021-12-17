counts = {}
def count_bits_by_pos(lines):
    for line in lines:
        for i in range(len(line)):
            if i in counts:
                if line[i] in counts[i]:
                    counts[i][line[i]]+=1
                else:
                    counts[i][line[i]]=1
            else:
                counts[i]={line[i]:1}

def get_gamma_rate():
    bits = ''
    for i in range(13):
        bits += max(counts[i], key=counts[i].get)
    return int(bits,2)
def get_epsilon_rate():
    bits = ''
    for i in range(13):
        bits += min(counts[i], key=counts[i].get)
    return int(bits,2)
input_file = open('input.txt', 'r')
lines = input_file.readlines()

count_bits_by_pos(lines)
gamma = get_gamma_rate()
epsilon =  get_epsilon_rate()
print(gamma*epsilon)