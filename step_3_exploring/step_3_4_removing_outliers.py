""" 3.4: Removing outliers for some variables

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import pandas as pd

DATA_PATH = "airline_2m.csv"

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

print ("Step 3.4: Removing outliers")

columns = [
    "Distance",
    "DepDelayMinutes",
    "AirTime"
]

for current_column in columns:
    new_df = df[df[current_column] < df[current_column].quantile (0.98)]
    # We are only removing negative values for AirTime.
    # if current_column == "AirTime":
    #     new_df = new_df[new_df[current_column] >= 0]

    # Create a histogram with density curve overlaid (enabling KDE, which means
    # kernel density estimates (KDEs)). It also calculates automatically the
    # number of columns (= bins) that suits best for the histogram.
    sns.displot (data = new_df[current_column], kde = True, bins = "auto")
    plt.show ()
