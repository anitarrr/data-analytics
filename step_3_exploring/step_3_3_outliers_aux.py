import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning) 

# load dataset into notebook
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

df = pd.read_csv (
    "airline_2m.csv",
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

COLUMN = 'DepDelayMinutes'
Q80    = df[COLUMN].quantile (0.8)
Q85    = df[COLUMN].quantile (0.85)
Q90    = df[COLUMN].quantile (0.9)
Q95    = df[COLUMN].quantile (0.95)
Q97    = df[COLUMN].quantile (0.97)
Q98    = df[COLUMN].quantile (0.98)
Q99    = df[COLUMN].quantile (0.99)

print (f"Percentile 80 is {Q80}")
print (f"Percentile 85 is {Q85}")
print (f"Percentile 90 is {Q90}")
print (f"Percentile 95 is {Q95}")
print (f"Percentile 97 is {Q97}")
print (f"Percentile 98 is {Q98}")
print (f"Percentile 99 is {Q99}")
