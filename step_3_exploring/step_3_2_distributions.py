""" 3.2: Create histograms for some variables

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import seaborn as sns
import matplotlib.pyplot as plt
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

print ("Step 3.2: graphically calculating the distribution of data for some variables (columns)")

columns = [
    "Distance",
    "AirTime",
    "DayOfWeek",
    "DayofMonth",
    "Month",
    "Quarter",
    "Year",
    "DepDelayMinutes"
]

# Create a histogram with density curve overlaid (enabling KDE, which means
# kernel density estimates (KDEs)). It also calculates automatically the
# number of columns (= bins) that suits bets for the histogram.
for current_column in columns:
    sns.displot (data = df[current_column], bins = "auto")
    plt.show ()