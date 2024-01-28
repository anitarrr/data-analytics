""" 4 - part 3: Analyzing and visualizing trends

 - Number of flights vs cancelled flights grouped by carrier

This simple script assumes that the dataset is already downloaded and
extracted into the current working directory.
"""

# Remove the Pyarrow deprecation warning related to Pandas 3.0, additional info
# in https://github.com/pandas-dev/pandas/issues/54466
import warnings
warnings.filterwarnings ("ignore", category = DeprecationWarning)
import pandas as pd
import seaborn.objects as so
import json

DATA_PATH = "airline_2m.csv"

# Read data from the dataset and make sure to force some columns with mixed
# types fo be read as strings.
df = pd.read_csv (
    DATA_PATH,
    encoding = "ISO-8859-1",
    dtype    = {'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

df["FlightDate"] = pd.to_datetime(df["FlightDate"])

##### A: Obtenemos el numero total de vuelos con ArrDelayMinutes > 15 agrupado por carrier
df1 = df

# 1. Borramos los vuelos que no tienen informado los campos ArrDel* --> 100 - 2 = 98 filas
df1 = df1.dropna(
    how="any",
    subset=["ArrDelay", "ArrDelayMinutes", "ArrDel15", "ArrivalDelayGroups"]
)

# 2. Borramos los vuelos con retraso outlier -------------------------> 98 - 2 = 96 filas
df1 = df1[df1["ArrDelayMinutes"] < df1["ArrDelayMinutes"].quantile (0.98)]

# 3. Borramos los vuelos que no tienen retraso ArrDel15 = 0 ----------> 96 - 76 = 20 filas
# (en realidad hay 22 vuelos con retraso)
df1['ArrDel15'] = df1['ArrDel15'].astype(int)
df1 = df1[df1["ArrDel15"] == 1]

# Plot: mumero de vuelos con retraso > 15 minutos desglosado por carrier
df1 = df1.groupby(["IATA_CODE_Reporting_Airline"]).agg(arrival_delay_greater_than_15_min=("ArrDel15", 'count'))
df1 = df1.reset_index()
print (df1)
so.Plot (df1, x="IATA_CODE_Reporting_Airline", y="arrival_delay_greater_than_15_min").add(so.Bar()).show()

##### B: Obtenemos el numero total de vuelos con ArrDelayMinutes > 15 agrupado por carrier
#####    comparando con el total
# 1. Borramos los vuelos que no tienen informado los campos ArrDel* --> 41078 filas menos
#    Nos quedan 1958922 filas
df2 = df.dropna(
    how="any",
    subset=["ArrDelay", "ArrDelayMinutes", "ArrDel15", "ArrivalDelayGroups"]
)

# 2. Borramos los vuelos con retraso outlier -------------------------> 39775 filas menos
#    Nos quedan 1919147 filas
df2 = df2[df2["ArrDelayMinutes"] < df2["ArrDelayMinutes"].quantile (0.98)]

# 3. Borramos los vuelos que no tienen retraso ArrDel15 = 0 ----------> 1570987 filas menos
#    Nos quedan 348160 filas
df2['ArrDel15'] = df2['ArrDel15'].astype(int)
df2a = df2[df2["ArrDel15"] == 1]

# 4. df ahora sólo tiene 2 columnas: "IATA_CODE_Reporting_Airline" y "arrival_delay_greater_than_15_min"
df2a = df2a.groupby(["IATA_CODE_Reporting_Airline"]).agg(number_of_flights=("ArrDel15", 'count'))
df2a = df2a.reset_index()

# 5. Añadimos una nueva columna indicando delay = 1
df2a['delay'] = 1

# 6. Usando el dataframe previo df2, borramos los vuelos que no tienen retraso ArrDel15 = 1
df2b = df2[df2["ArrDel15"] == 0]

# 7. df ahora sólo tiene 2 columnas: "IATA_CODE_Reporting_Airline" y "arrival_delay_less_than_15_min"
df2b = df2b.groupby(["IATA_CODE_Reporting_Airline"]).agg(number_of_flights=("ArrDel15", 'count'))
df2b = df2b.reset_index()

# 8. Añadimos una nueva columna indicando delay = 0
df2b['delay'] = 0

# 9. Concatenamos ambos dataframes
df2c = pd.concat([df2a, df2b], ignore_index=True)

# 10. Get statistics from the dataframe using a Python dictionary of dictionaries
stats = dict()

for row in df2c.itertuples():
    # Data visualization method #1: storing data in a dictionary
    # If the inner dictionary does not exist, create it first!
    if (row.IATA_CODE_Reporting_Airline not in stats.keys()):
        stats[row.IATA_CODE_Reporting_Airline] = dict()

    if (row.delay):
        stats[row.IATA_CODE_Reporting_Airline]["NumOfFlights_WITH_delay"] = row.number_of_flights
    else:
        stats[row.IATA_CODE_Reporting_Airline]["NumOfFlights_WITHOUT_delay"] = row.number_of_flights

    print (json.dumps(stats, sort_keys=True, indent=2))

    # Data visualization method #2: sending data to standard output
    if (row.delay): text = 'greater  '
    else:           text = 'less than'

    print (f"The carrier {row.IATA_CODE_Reporting_Airline} has {row.number_of_flights : >5} flights with arrival delay {text} than 15 minutes")

# 11. Bars plot
p = (
    so.Plot(df2c, x="IATA_CODE_Reporting_Airline", y="number_of_flights")
    .add(so.Bars(), so.Dodge())
)

p.show()

# 12. Get quocients
for carrier in stats:
    # We can generate a quocient if both values do exist!
    try:
        nof_with_delay = stats[carrier]["NumOfFlights_WITH_delay"]
        nof_no_delay   = stats[carrier]["NumOfFlights_WITHOUT_delay"]
        nof            = nof_with_delay + nof_no_delay
        quocient=(nof_with_delay / nof)
        print(f"Company {carrier}: the quocient is {quocient:.2%}")
    except KeyError:
        print(f"Company {carrier}: it has NO delayed flights registered")
