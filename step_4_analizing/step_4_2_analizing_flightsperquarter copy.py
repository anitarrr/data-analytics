""" 4 - part 2: Analyzing and visualizing trends

 - Number of flights grouped by quarter
 - Number of flights grouped by month
 - Number of flights grouped by season

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import calendar
import seaborn.objects as so
import pandas as pd

DATA_PATH = "airline_2m.csv"

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

##### Number of flights per quarter
quarter_df = df.groupby(['Month', "Quarter"]).agg(num_of_flights=("Month", 'count'))
p = (so.Plot (quarter_df, x="Quarter", y="num_of_flights")
     .add(so.Bar(), so.Agg("sum"), so.Dodge())
    .label(x = "Quarter")
    .label(y = "Number of flights")
)
p.show()

for i in range(1, 5):
    print (f"Number of flights during Q{i}: {len(df[df["Quarter"]==i])}")

##### Number of flights per months
p = (so.Plot (quarter_df, x="Month", y="num_of_flights")
     .add(so.Bar(), so.Agg("sum"), so.Dodge())
     .label(x = "Month")
     .label(y = "Number of flights")
     
)    
p.show()

for i in range(1, 13):
    print (f"Number of flights during {calendar.month_name[i]}: {len(df[df["Month"]==i])}")

##### Number of flights per season. I create a new colum to make it easier.
""" Return the appropriate season string depending on the quarter """
def winterorsummer(quarter):
    if quarter in (2,3):
        return 'Summer'

    return 'Winter'

df['MYQUARTER'] = df["Quarter"].apply(winterorsummer)
print (f"Number of flights during the summer season: {len(df[df['MYQUARTER']=='Summer'])}")
print (f"Number of flights during the winter season: {len(df[df['MYQUARTER']=='Winter'])}")
p = (so.Plot (df, x="MYQUARTER").add(so.Bar(), so.Hist(discrete=True))
    .label(x=" Quarter")
    .label(y="Number of flights")
)
p.show()
