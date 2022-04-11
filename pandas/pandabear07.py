#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create dataframes, and output graphs"""

import pandas as pd

def main():

    excel_file = 'movies.xls'

    df = pd.concat(pd.read_excel(excel_file, sheet_name=None, index_col=False, usecols="A:B,D,J"), ignore_index=True)

    df = df.dropna()
    df['Year'] = df['Year'].astype(int)
    df['Gross Earnings'] = df['Gross Earnings'].astype(int)

    df = df.sort_values(by='Gross Earnings', ascending=False)
    print(df.head(25))

if __name__ == "__main__":
    main()

