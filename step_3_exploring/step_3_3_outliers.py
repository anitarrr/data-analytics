""" 3.3: Detecting outliers for some variables

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import pandas as pd
import numpy as np

DATA_PATH = "airline_2m.csv"
ZSCORE_THRESHOLD = 3

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

print ("Step 3.3.1: Calculating thresholds for variables")

columns = [
    "Distance",
    "DepDelayMinutes",
    "AirTime"
]

# Get min and max thresholds for some variables
for current_column in columns:
    mean          = np.mean (df[current_column])
    std           = np.std (df[current_column])
    # df.quantile calculates percentile defined as parameter
    Q1            = df[current_column].quantile (0.25)
    Q3            = df[current_column].quantile (0.75)
    IQR           = Q3 - Q1
    limit         = 1.5 * IQR
    min_threshold = Q1 - limit
    max_threshold = Q3 + limit

    print (f"\nMethod                       Q1       Q3       IQR      Limit   Min       Max")
    print (f"[{current_column} using IQR: {Q1 : .3f} {Q3 : .3f} {IQR : .3f} {limit : .3f} {min_threshold : .3f} {max_threshold : .3f}")

    df[f"zscore_{current_column}"] = (df[current_column] - mean ) / std
    z_3 = (ZSCORE_THRESHOLD * std)+ (mean)
    z_minus3 = (mean) - (ZSCORE_THRESHOLD * std)
    print (f"\nMethod                           mean      std      z_3    z_minus3")
    print (f"[{current_column} using Z-Score:         {mean : .3f}, {std : .3f}, {z_3 : .3f}, {z_minus3 : .3f}")
