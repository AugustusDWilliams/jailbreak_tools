import os
import re

def read_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data

def parse_data(data):
    data = data.strip().split("\n\n")
    tweak_list = list()
    for tweak in data:
        tweak_info = [t.strip() for t in tweak.split("\n")]
        tweak_data = dict()
        name = re.match(r"(?:Visible name: )(.+)", tweak_info[1]).group(1)
        version = re.match(r"(?:Version: )(.+)", tweak_info[2]).group(1)
        tweak_data['Name'] =  name
        tweak_data['Version'] = version
        tweak_data['Repo'] = tweak_info[0]
        tweak_list.append(tweak_data)
    return tweak_list

if __name__ == "__main__":
    filename = "/home/development/Code/Projects/jailbreak_tools/data/tweak_list.csv"
    data = read_file(filename)
    tweak_list = parse_data(data)
    print(tweak_list)
    #print(len(tweak_list))

