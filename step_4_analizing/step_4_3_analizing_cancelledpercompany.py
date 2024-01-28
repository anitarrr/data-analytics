""" 4 - part 3: Analyzing and visualizing trends

 - Number of cancelled flights grouped by company

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import calendar
import seaborn.objects as so

import seaborn as sns
import numpy as np

import pandas as pd

DATA_PATH = "airline_2m.csv"

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

##### Number of cancelled flights per company
df['Cancelled'] = df['Cancelled'].astype(bool)

p = (
    so.Plot (df, x="IATA_CODE_Reporting_Airline", color="Cancelled")
    .add(so.Bars(), so.Count(), so.Dodge())
    .label(x="IATA Code reporting Airline")
    .label(y="Number of flights")
)

p.show()

##### Process the dataframe to get the values for each carrier
df['Cancelled'] = df['Cancelled'].astype(int)
df = df.drop(df[df["Cancelled"] == 0].index)
unique_values_array = pd.unique (df["IATA_CODE_Reporting_Airline"])
df = df.groupby("IATA_CODE_Reporting_Airline")["FlightDate"].count()

# Highly discouraged!
for index, row in df.items():
    print (f"The carrier {index} has cancelled {row : >4} flights")
