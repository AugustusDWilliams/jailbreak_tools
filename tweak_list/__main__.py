import os
import re
import csv
from logger import LOGGER as logger


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
        tweak_name = re.match(r"(?:Visible name: )(.+)", tweak_info[1]).group(1)
        version = re.match(r"(?:Version: )(.+)", tweak_info[2]).group(1)
        tweak_data['Tweak'] = tweak_name
        tweak_data['Version'] = version
        tweak_data['Repo'] = tweak_info[0]
        tweak_list.append(tweak_data)
    return tweak_list

def write_data(filename, data):
    header = ["Tweak", "Version", "Repo"]
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for tweak in data:
            writer.writerow(tweak)
    logger.debug("Tweak List Generated")


if __name__ == "__main__":
    filename = "/home/development/Code/Projects/jailbreak_tools/data/tweak_list.csv"
    output_filename = "/home/development/Code/Projects/jailbreak_tools/data/parsed_tweak_list.csv"
    data = read_file(filename)
    tweak_list = parse_data(data)
    write_data(output_filename, tweak_list)
    #print(tweak_list)
    #print(len(tweak_list))
