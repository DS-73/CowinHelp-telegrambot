import sys
import re
import csv
import pandas as pd
import numpy as np
from cowin_api import CoWinAPI
from csv import reader


def get_states(state_id, state_name):
    cowin = CoWinAPI()
    districts = cowin.get_districts(state_id)['districts']
    
    field_names= ['district_id', 'district_name']
    # Path
    path = ".\\Districts\\"
    # CSV Name along with path

    csv_name = path + state_id + "_" + state_name + "Districts.csv"
    response_text = path + state_id + "_" + state_name + "Districtsresponse.txt"
    
    with open(csv_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(districts)


    df = pd.read_csv(csv_name)
    new_df = df.dropna()
    df.to_csv(csv_name, index=False)
    text = df.to_string(index=False)
    
    fhand = open(response_text, "w")
    fhand.writelines(text)
    fhand.close()

def main():
    # Path
    path = ".\\States\\"
    # CSV Name along with path
    csv_name = path + 'States.csv'
    
    with open(csv_name, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            if len(row) > 0:
                if len(row[0]) <=2:
                    print(row)
                    state_id = row[0]
                    state_name = row[1]
                    get_states(state_id, state_name)


if __name__ == "__main__":
    
    main()
