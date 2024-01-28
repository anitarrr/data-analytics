""" 3.1 - part 2: Get the shape of some variables

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import pandas as pd

DATA_PATH = "airline_2m.csv"

df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

columns = [
    "AirTime",
    "DepDelayMinutes",
    "DestAirportID",
    "Distance",
    "IATA_CODE_Reporting_Airline",
    "OriginAirportID",
]

for current_column in columns:
    unique_values = len (pd.unique (df[current_column]))
    print (f"There are {unique_values : 5} unique values for {current_column}")
