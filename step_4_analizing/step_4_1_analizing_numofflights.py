""" 4 - part 1: Analyzing and visualizing trends

 - Number of flights per company, comparing on-time flights vs departure delay > 15 minutes.
 - Number of flights per company, comparing on-time flights vs arrival delay > 15 minutes

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import pandas as pd
import seaborn.objects as so
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "airline_2m.csv"

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

print ("Step 4.1: Visualizing trends")

# From https://stackoverflow.com/questions/18748171/
df['DepDel15'] = df['DepDel15'].astype(bool)
df['ArrDel15'] = df['ArrDel15'].astype(bool)

# Counting number of flights from Carriers with Departure Delay > 15 vs On-Time
p = (
    so.Plot (df, x="IATA_CODE_Reporting_Airline", color="DepDel15")
    .add(so.Bars(), so.Count(), so.Dodge())
    .label(x=" IATA Code reporting Airline")
    .label(y="Number of flights")
)

p.show()

# Counting number of flights from Carriers with Arrival Delay > 15 vs On-Time
p = (
    so.Plot (df, x="IATA_CODE_Reporting_Airline", color="ArrDel15")
    .add(so.Bars(), so.Count(), so.Dodge())
    .label(x=" IATA Code reporting Airline")
    .label(y="Number of flights")
)

p.show()
