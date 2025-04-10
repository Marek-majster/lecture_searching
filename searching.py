import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    soubor = file_name
    with open(soubor, "r") as objekt:
        data = json.load(objekt)
        sequential_data = data[field]
    return sequential_data

def linear_search(sequence,number):
    index = 0
    kanal = {}
    pozice = []
    for i in sequence:
        index +=1
        if i == number:
            pozice.append(index)
    kanal["index"] = pozice
    kanal["pocet"] = sequence.count(number)
    return kanal

def pattern_search(sequence,vzor):
    kanal = {}
    pozice = []
    delka = len(vzor)
    for i in range(len(sequence) - delka + 1):
        if sequence[i:i + delka] == vzor:
            pozice.append(i)
    kanal["index"] = pozice
    return kanal


def main(file_name,field,number,vzor):
    a = read_data(file_name,field)
 #   b = linear_search(a,number)
    c = pattern_search(a,vzor)
    return print(f"{c}")



if __name__ == '__main__':
    main("sequential.json","dna_sequence", 0, "ATA")