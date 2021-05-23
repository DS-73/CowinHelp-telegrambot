import sys
import re
import csv
import pandas as pd
import numpy as np
from cowin_api import CoWinAPI

def get_states():
    cowin = CoWinAPI()
    states = cowin.get_states()["states"]
    
    field_names= ['state_id', 'state_name']

    # Path
    path = ".\\States\\"

    # CSV Name along with path
    csv_name = path + 'States.csv'
    with open(csv_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(states)

    # Reading CSV
    df = pd.read_csv(csv_name)
    print(df)

    # File Name
    file_name = path + 'states_list_response.txt'
    sys.stdout = open(file_name, 'w')
    print(df.to_string(index=False))
    sys.stdout.close()


def main():
    get_states()

if __name__ == "__main__":
    main()
