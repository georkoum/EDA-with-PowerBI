import pandas as pd

#reading the data file
dataset = pd.read_csv("path/to_file")

# check the columns of the dataset
dataset.columns
#check the first 5 samples of the data
dataset.head()

#check for missing values in the dataset
dataset.isnull().sum()

# translate weekdays from german to english
days = {'Montag': 'Monday', 'Dienstag':'Tuesday', 'Mittwoch': 'Wednesday', 'Donnerstag':'Thursday', 'Freitag': 'Friday', 'Samstag': 'Saturday', 'Sonntag': 'Sunday'}
for x in days:
    dataset['orderdate_weekday_En'] = dataset["orderdate_weekday"].map(lambda x: days[x])
    dataset['shipdate_weekday_En'] = dataset["shipdate_weekday"].map(lambda x: days[x])
    
# drop columns with german weekdays
dataset.drop('orderdate_weekday', axis=1, inplace=True)
dataset.drop('shipdate_weekday', axis=1, inplace=True)

# create attribute season
dataset['season'] = dataset["orderdate_month"].map(lambda x: 'winter' if x in [12,1,2] else x)
dataset['season'] = dataset["season"].map(lambda x: 'spring' if x in [3,4,5] else x)
dataset['season'] = dataset["season"].map(lambda x: 'summer' if x in [6,7,8] else x)
dataset['season'] = dataset["season"].map(lambda x: 'autumn' if x in [9,10,11] else x)

# create columns with full format of order and ship dates 
for col in ['orderdate_day', 'orderdate_month', 'orderdate_year', 'shipdate_day', 'shipdate_month', 'shipdate_year']:
    dataset[col] = dataset[col].apply(str)

dataset['order_date'] = dataset['orderdate_day'] + '/' + dataset['orderdate_month'] + '/' + dataset['orderdate_year']
dataset['ship_date'] = dataset['shipdate_day'] + '/' + dataset['shipdate_month'] + '/' + dataset['shipdate_year']

# check for changes
dataset.head(1).T

# save new dataset
dataset.to_excel("path/to_export", index=False)
