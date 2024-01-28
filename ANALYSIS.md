# Analysing the Airline Reporting Carrier On-Time Performance Dataset
## How to proceed
The main goal for this project is to analyse a dataset, and to discover trends from the dataset we will follow these steps:

1. Download and extract the dataset: 
   * [Download the 2 million row sample dataset](https://developer.ibm.com/data/airline/).
   * Extract the contents of the downloaded file.

2. Load the dataset:
   * In this case, I will use Python, specifically the latest stable one, which is [version 3.12.1](https://www.python.org/downloads/release/python-3121/), to load the dataset into a [Pandas DataFrame data structure](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html), and then start exploring it.

3. Explore the dataset:
   * I will start understanding the structure of the dataset by examining the available 109 columns and their descriptions. This step will help me identify the data points that can be used for trend analysis.
   * I will also examine the distribution of the data by using plots to uncover any patterns that may indicate a trend. Patterns are recurring structures or sequences found in data. Using Pandas to work with the data first and then using MatPlotLib and Seaborn to plot such data later, I will be able to vizualize and finally analyze the data. 

4. Analyze the dataset and visualize the trends:
   * I will examine data throughout time to identify temporal trends. I will perform further analysis on data comparing multiple variables in a single plot.
   * I will create visualizations to represent the identified trends effectively by using line charts, bar graphs, heatmaps, or any other relevant visualization methods to present the trends in an understandable and insightful manner.

5. Interpret and communicate the results:
   * Finally, I will share my thoughts on trends I have discovered. I will look for patterns, seasonality, correlations, or any other significant findings within the dataset.
   * The purpose of this document is to share a useful insight of my personal analysis using the sample dataset for this exercise.

## Exploring the dataset
### How to approach the dataset for the first time
First of all, I have found some limitations in working with 2M rows of data, mainly with first approaches to data, and getting to know how is the dataset built.
Therefore, I decided to work with a 100 row random sample that I saved in a temporary .csv file. This way of working has, mainly, speeded up the process of learning, manipulating and most of all plotting data. After making sure I was getting a correct insight on the 100 sample, then I have just changed over to the initial 2M row .csv file to have a full analysis of the data set, and also, accurate plotting including all data.

### Basic information of the main variables
I have used the [Python script step_3_1_exploring.py](step_3_exploring/step_3_1_exploring.py) to get some basic information about the distribution of some important variables (columns) and the data type they store.

For now, I want to remark the information for the following variables (columns): `Distance`, `Year`, `Quarter`, `Month`, `DayofMonth`, `DayOfWeek`, `DepDelayMinutes` and `AirTime`:

```
| Variable | Distance     | Year         | 
| count    | 2.000000e+06 | 2.000000e+06 |
| mean     | 7.334963e+02 | 2.004314e+03 |
| std      | 5.684968e+02 | 9.228930e+00 |
| min      | 1.100000e+01 | 1.987000e+03 |
| 25%      | 3.250000e+02 | 1.997000e+03 |
| 50%      | 5.800000e+02 | 2.005000e+03 |
| 75%      | 9.670000e+02 | 2.012000e+03 |
| max      | 5.095000e+03 | 2.020000e+03 |
| dtype    | float64      | float64      |

|Quarter      | Month        | DayofMonth  |
|2.000000e+06 | 2.000000e+06 | 2.000000e+06|
|2.501267e+00 | 6.500761e+00 | 1.572202e+01|
|1.118022e+00 | 3.443460e+00 | 8.778412e+00|
|1.000000e+00 | 1.000000e+00 | 1.000000e+00|
|1.000000e+00 | 3.000000e+00 | 8.000000e+00|
|3.000000e+00 | 7.000000e+00 | 1.600000e+01|
|3.000000e+00 | 9.000000e+00 | 2.300000e+01|
|4.000000e+00 | 1.200000e+01 | 3.100000e+01|
|float64      | float64      | float64     |

|DayOfWeek     | DepDelayMinutes | AirTime       |
| 2.000000e+06 | 1.963932e+06    | 1.580651e+06  |
| 3.937445e+00 | 1.049667e+01    | 1.059533e+02  |
| 1.990369e+00 | 3.196467e+01    | 6.859287e+01  |
| 1.000000e+00 | 0.000000e+00    | -7.030000e+02 |
| 2.000000e+00 | 0.000000e+00    | 5.600000e+01  |
| 4.000000e+00 | 0.000000e+00    | 8.700000e+01  |
| 6.000000e+00 | 7.000000e+00    | 1.350000e+02  |
| 7.000000e+00 | 1.878000e+03    | 9.650000e+02  |
| float64      | float64         | float64       |
```

To know the whole period that this dataset comprehends, we can see above that min value is 1987 and max is 2020. TO be more accurate and have a better understanding on the time frame, I have used csvtool to check that it starts on October 1987 and finishes on March 2020.

Also checking above, I can see that the distribution for the variable `Distance` (which is the 55th column), for example, has the expected 2 million rows, its mean value is 733 miles, and its values are in the range [11, 5095].

Additionally, it is interesting to know how many unique values are in some variables. To get that information, I have prepared the script [Python script step_3_1_exploring_unique_values.py](step_3_exploring/step_3_1_exploring_unique_values.py). This is the output of this file:

```
There are   669 unique values for AirTime
There are   876 unique values for DepDelayMinutes
There are   409 unique values for DestAirportID
There are  1906 unique values for Distance
There are    35 unique values for IATA_CODE_Reporting_Airline
There are   407 unique values for OriginAirportID
```

### Distribution of data
I have prepared some plots to have a visual insight on how the main variables are distributed; they are located in the [folder step_3_exploring/plots/](step_3_exploring/plots/), and follow this naming convention: `3_2-Histogram-<variable>-Frequency-tiny.png`. They have been generated by running the [Python script step_3_2_distributions.py](step_3_exploring/step_3_2_distributions.py).

They shown an even distribution of data for the time-related variables `Year`, `Quarter`, `Month`, `DayofMonth` (except for the 31st) and `DayOfWeek` (except on Saturdays!).

The variable `Distance` confirms that the dataset contains data from domestic flights, as most of the distance values are under 1000 miles (1609.344 Km). The variable `AirTime` shows that most of the flights lasts less than three hours, too.

Lastly, the variable `DepDelayMinutes` shows that most of the delays are under an hour. On the previous section we noticed that the quartiles 25 and 50 are exactly zero, and the quartile 75 is just 7 minutes... By using the [IQR method](https://en.wikipedia.org/wiki/Interquartile_range) on this variable, we get that the meaningful values are in the range `[Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]`, which translates to [-10.5, 17.5] in this case:

```
Q1  = Quantile (25) = 0
Q3  = Quantile (75) = 7
IQR = Q3 - Q1 = 7
```

Using the script [step_3_3_outliers_aux.py](step_3_exploring/step_3_3_outliers_aux.py) we get the following output:
```
Percentile 80 is 11 minutes
Percentile 85 is 17 minutes
Percentile 90 is 29 minutes
Percentile 95 is 57 minutes
Percentile 97 is 82 minutes
Percentile 98 is 104 minutes
Percentile 99 is 144 minutes
```
The higher percentiles for this variable confirms that most of the delays are under 60 minutes.

### Detecting and acting on the outliers
#### Definition
Outliers are data points that deviate from the rest of the data, hence are significantly different from the norm.

They can be a major problem in statistics and data analysis areas, because outliers can distort the average and influence the correlations between data points and lead to incorrect predictions. However, they can also provide valuable insights as well as opportunities for innovation.

I have taken the decision on acting on outliers since the plot given by AirTime variale throughout the whole sample. That histogram has showed negative AirTime values for flights, making not much sense for those flights to have such value. Therefore, using two different methods (references can be seen at the end of this document), I have made an approach to delete outliers from this dataset.

#### Discovering outliers with visualization tools
I have tried a visual approach to this matter by creating a plot for the main variables (see previous section); however, we might leverage on some well-known statistical techniques to uncover them by using more robust approach.

#### Discovering outliers with mathematical functions: IQR score
Just as I did on the previous section for the variable `DepDelayMinutes`, the [interquartile range measure](https://en.wikipedia.org/wiki/Interquartile_range), also known as the IQR score, can uncover the outliers of a variable.

For the variable `Distance`, the IQR is 642; therefore, the IQR score lies within the range [-638, 1930]. There are no negative distances in this variable, so the real result for this range is [0, 1930].

For the variable `DepDelayMinutes`, the real range is [-10.5, 17.5], as calculated above.

For the variable `AirTime`, the IQR is 79; therefore, the IQR score lies within the range [-62.5, 253.5]. This variable has been the responsible I started looking into outliers, since I have been able to spot some negative values for AirTime. This makes not much sense, since `AirTime` should be a positive value, else zero if the flight never departed.
You can see some of this negative values spotted in the plot [3_2-Histogram-AirTime-Frequency-NEGATIVE.png](step_3_exploring/plots/3_2-Histogram-AirTime-Frequency-NEGATIVE.png) after some zoome in is done in the histogram.

All of these values have been compared to the output of the [Python script step_3_3_outliers.py](step_3_exploring/step_3_3_outliers.py), and they match the expected values.

#### Discovering outliers with mathematical functions: Z-Score
To determine which values are outliers in the variables `Distance` and `DepDelayMinutes`, we can start by using the [standard score measure](https://en.wikipedia.org/wiki/Z-score), also known as *Z-Score*. The idea behind Z-score is to describe any data point by finding their relationship with the standard deviation and mean of the group of data points.

In this case, this measure certainly improves the IQR score, because it sets improved thresholds (they have been rounded to 2 decimals) for outliers for the previous variables:
* Distance: the real result for this range is [0, 2438.99]. This is slightly below percentile 98.
* DepDelayMinutes: the real result for this range is [-85.397, 106.39]. This is slightly above percentile 98.
* AirTime: the real result for this range is [0, 311.73]. This is slightly above percentile 98.

This is the output that the Python script has returned
```
Step 3.3.1: Calculating thresholds for variables
Method                       Q1      Q3       IQR      Limit    Min      Max
[Distance using IQR:        325.000  967.000  642.000  963.000 -638.000  1930.000

Method                       mean      std      z_3       z_minus3
[Distance using Z-Score:     733.496,  568.497, 2438.986, -971.994

Method                       Q1     Q3     IQR    Limit    Min     Max
[DepDelayMinutes using IQR:  0.000  7.000  7.000  10.500  -10.500  17.500

Method                           mean     std      z_3    z_minus3
[DepDelayMinutes using Z-Score:  10.497,  31.965,  106.391, -85.397

Method                       Q1       Q3       IQR      Limit   Min       Max
[AirTime using IQR:          56.000  135.000  79.000  118.500 -62.500  253.500

Method                       mean      std      z_3      z_minus3
[AirTime using Z-Score:      105.953,  68.593,  311.732, -99.825
```

#### Acting on the outliers
For the sake of simplicity, I have decided to work with data under percentile 98 for the above three variables, thus removing the outliers from the dataframe. There are [other methods for outlier detection](https://en.wikipedia.org/wiki/Outlier), but they are out of this task's scope.

I have created three improved histograms to visualize the new data in histograms. They are stored in the [folder step_3_exploring/plots/](step_3_exploring/plots/), and follow this naming convention: `3_4-Histogram-<variable>-Frequency-NO_OUTLIERS.png`. They have been generated by running the simplified [Python script step_3_4_removing_outliers.py](step_3_exploring/step_3_4_removing_outliers.py).

## Analyzing the dataset and visualizing the trends
Working with a dataset full of flights information means that it might be interesting to analyze trends related to flight delays, cancellations, airline performance, or specific routes.

The goal is to extract meaningful insights from data by identifying patterns, trends, and relationships. This process can aid in predictive modeling and anomaly identification. Plots are located in the [folder step_4_analizing/plots/](step_4_analizing/plots/).

I have used the following assumptions in this step:
* A flight is marked as having arrived with delay if the value of the variable `ArrDelay15` is strictly greater than 15 (expresed in minutes).
* Similarly, a flight is marked as having departed with delay if the value of the variable `DepDelay15` is strictly greater than 15 (expresed in minutes).
* To simplify the required calculations, the flights from April to September (that is, Q2 and Q3) are marked as part of the summer season.
* Similarly, the flights from October to March (that is, Q4 and Q1) are marked as part of the winter season.

I have created different plots to visualize some trends:
* A plot to compare the number of flights which are marked as delayed in the arrival planned time versus those who are not, for every carrier in the data set. I have also created a similar one, but for the departure delays. They have been generated by running the simplified [Python script step_4_1_analizing_numofflights.py](step_4_analizing/step_4_1_analizing_numofflights.py).
* Three different plots to compare the number of flights per quarter, month and season (see results below), for every flight in the data set. They have been generated by running the [Python script step_4_2_analizing_flightsperquarter.py](step_4_analizing/step_4_2_analizing_flightsperquarter.py).

   ```
      * Number of flights during Q1: 500486
      * Number of flights during Q2: 495982
      * Number of flights during Q3: 504044
      * Number of flights during Q4: 499488
      * Number of flights during January: 169561
      * Number of flights during February: 155629
      * Number of flights during March: 175296
      * Number of flights during April: 163016
      * Number of flights during May: 166763
      * Number of flights during June: 166203
      * Number of flights during July: 171679
      * Number of flights during August: 171990
      * Number of flights during September: 160375
      * Number of flights during October: 170617
      * Number of flights during November: 161952
      * Number of flights during December: 166919
      * Number of flights during the summer season: 1000026
      * Number of flights during the winter season: 999974
   ```

* A plot that helps us visualize the total amount of cancel flights in the dataset. They have been generated by running the [Python script step_4_3_analizing_cancelledpercompany.py](step_4_analizing\step_4_3_analizing_cancelledpercompany.py). A quick analysis of data via csvtool, has showed that the total amount of cancelled flights is just of 36462 among 2M rows of data. That represents just the 0.018% of the data. Moreover, there are 16243 flights without a Cancellation Code value, and that represents almost half of the cancelled flights: 44.5%. Therefore, I have decided not to study further on the Cancellation Code column, due to the small amount of data available in the whole dataset. I have assumed there is not enough data to have any good conclusion on cancelled flights and the motived for such cancellation.   

   ```
   The carrier 9E has cancelled  512 flights
   The carrier AA has cancelled 4401 flights
   The carrier AL has cancelled   53 flights
   The carrier AQ has cancelled   31 flights
   The carrier AS has cancelled  733 flights
   The carrier B6 has cancelled  605 flights
   The carrier CO has cancelled 1233 flights
   The carrier DH has cancelled  221 flights
   The carrier DL has cancelled 3561 flights
   The carrier EA has cancelled  307 flights
   The carrier EV has cancelled 2016 flights
   The carrier F9 has cancelled  145 flights
   The carrier FL has cancelled  251 flights
   The carrier G4 has cancelled   46 flights
   The carrier HA has cancelled   38 flights
   The carrier HP has cancelled  581 flights
   The carrier ML has cancelled   18 flights
   The carrier MQ has cancelled 3028 flights
   The carrier NK has cancelled  184 flights
   The carrier NW has cancelled 2280 flights
   The carrier OH has cancelled  811 flights
   The carrier OO has cancelled 2156 flights
   The carrier PA has cancelled   32 flights
   The carrier PI has cancelled  105 flights
   The carrier PS has cancelled    8 flights
   The carrier RU has cancelled  278 flights
   The carrier TW has cancelled  705 flights
   The carrier TZ has cancelled   24 flights
   The carrier UA has cancelled 3670 flights
   The carrier US has cancelled 3412 flights
   The carrier VX has cancelled   33 flights
   The carrier WN has cancelled 3535 flights
   The carrier XE has cancelled  536 flights
   The carrier YV has cancelled  694 flights
   The carrier YX has cancelled  219 flights
   ```

* A plot to visualize the relevant delays (above fifteen minutes) per each carrier, and a similar one but showing the delayed one versus the non-delayed ones. They have been generated by running the [Python script step_4_4_analyzing_delays.py](step_4_analizing\step_4_4_analyzing_delays.py). There are some companies with lots of delayed flights, which might mean structural issues, flying to locations with seasonal bad weather or some other reasons which require further analysis.
   * Take a look at the sidecar file [step_4_4_analyzing_delays.txt](step_4_analizing\step_4_4_analyzing_delays.txt) to see the list of the number of flights delayed and non-delayed for each carrier.
   * Using the same script I have also generated a list with percentage of delayed flights at arrival vs the total number of lights, for each company.
  
      ```
      Company 9E: the quocient is 15.69%
      Company AA: the quocient is 18.22%
      Company AL: the quocient is 21.67%
      Company AQ: the quocient is 9.73%
      Company AS: the quocient is 17.92%
      Company B6: the quocient is 20.90%
      Company CO: the quocient is 18.66%
      Company DH: the quocient is 19.73%
      Company DL: the quocient is 17.49%
      Company EA: the quocient is 17.27%
      Company EV: the quocient is 20.38%
      Company F9: the quocient is 20.16%
      Company FL: the quocient is 18.10%
      Company G4: the quocient is 18.82%
      Company HA: the quocient is 7.98%
      Company HP: the quocient is 18.81%
      Company ML: the quocient is 17.78%
      Company MQ: the quocient is 20.08%
      Company NK: the quocient is 18.10%
      Company NW: the quocient is 17.99%
      Company OH: the quocient is 19.81%
      Company OO: the quocient is 15.93%
      Company PA: the quocient is 19.78%
      Company PI: the quocient is 25.14%
      Company PS: the quocient is 24.41%
      Company RU: the quocient is 19.85%
      Company TW: the quocient is 19.07%
      Company TZ: the quocient is 18.04%
      Company UA: the quocient is 19.28%
      Company US: the quocient is 18.52%
      Company VX: the quocient is 18.72%
      Company WN: the quocient is 16.92%
      Company XE: the quocient is 19.62%
      Company YV: the quocient is 17.46%
      Company YX: the quocient is 16.30%
      ```

# Interpreting and communicating the results
For the sake of simplicity, I have prepared a presentation with the interesting plots and some insights on them in a [separate presentation](step_5_insights.pdf).

# Next steps
This test was designed to be completed in a few days, so there is plenty of room for improvement:

* Cancellation code: correlate the cancellation code with the number of total cancellation flights, per carrier, for example. Also could be analised per season, quarter, etc...
* Diversions: explore, analize and visualize the diversions variables, how do they work, what do they mean and how can be studied in a profitable way for smart insights and trends.
* Exploring manual plots using the [seaborn library](https://seaborn.pydata.org/tutorial/introduction.html) for precise plots with text; or percentage over the bars when comparing [facet variables](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html) (for example, delays vs no delayed flights).
* Parametrize the previous plots and data for a single year or time period on demand.

# Limitations
* [The seaborn.objects interface](https://seaborn.pydata.org/tutorial/objects_interface) does not allow to show numbers on top of bars when using count plots, which would make plots more visual and appealing.
* The learning curve for the `pandas` library from Python, and how to prepare dataframes to be visualized in an appropriate plot.

# References
* [Cómo identificar y tratar outliers con Python](https://medium.com/@martacasdelg/c%C3%B3mo-identificar-y-tratar-outliers-con-python-bf7dd530fc3)
* [Ways to Detect and Remove the Outliers](https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba)
* [Official Seaborn documentation on "Visualizing distributions of data"](http://seaborn.pydata.org/tutorial/distributions.html)
* [Official Pandas documentation](https://pandas.pydata.org/docs/reference/index.html)
* [Official IATA webpage to search Airline Codes](https://www.iata.org/en/publications/directories/code-search?airline.search=OH)
* [Combining Data in Pandas With merge, join, and concat](https://realpython.com/pandas-merge-join-and-concat/)