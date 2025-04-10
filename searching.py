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

print(read_data("sequential.json","unordered_numbers"))

def main():
    pass


if __name__ == '__main__':
    main()