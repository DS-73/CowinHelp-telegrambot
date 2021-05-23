import sys, os
import re
import csv
import pandas as pd
import numpy as np
from cowin_api import CoWinAPI
from csv import reader


def get_keyboard_layout(file_name):
    # Path
    path = ".\\Districts\\" 
    district_csv = path + file_name
    df = pd.read_csv(district_csv)
    
    rows = df.shape[0]
    
    
    path = ".\\Keyboard\\"
    f_name = path + file_name[: -13] + ".txt"
    fhand = open(f_name, "a")

    counter = 0
    with open(district_csv, 'r') as read_obj:
        csv_reader = reader(read_obj)
        print(f'-------{f_name} : {rows}--------')
        string = f'[\n[\n'
        fhand.write(string)

        for row in csv_reader:
            if len(row) == 2 and row[1] != 'district_name':
                if counter % 2 == 0 and counter != 0:
                    string = f'],\n[\n'
                    fhand.write(string)
                    start, end = True, False

                string = f"InlineKeyboardButton('{row[1]}', callback_data='{row[1]}-{row[0]}'),\n"
                fhand.write(string)
                counter += 1

    string = f']\n'
    fhand.write(string)
    if counter % 2 == 1:
        fhand.write(string)

    fhand.close()


def main():
    files = os.listdir('.\\Districts\\')
    for file_name in files:
        if file_name.endswith(".csv"):
            get_keyboard_layout(file_name)
            
if __name__ == "__main__":
    main()
