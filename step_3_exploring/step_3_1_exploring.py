""" 3.1 - part 1: Describe some variables

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
from os import path
import pandas as pd

# Verifying the file was extracted properly
DATA_PATH = "airline_2m.csv"
path.exists (DATA_PATH)

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

print ("Step 3.1: using the function pandas.DataFrame.describe ()")

columns = [
    "Distance",
    "Year",
    "Quarter",
    "Month",
    "DayofMonth",
    "DayOfWeek",
    "DepDelayMinutes",
    "AirTime"
]

for current_column in columns:
    print (df[current_column].describe (include='all'))
