import urllib.request
from numpy.lib.function_base import average
import pandas as pd

#url for nytimes COVID US-County case & death data
CSV_URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

#path for where to save US-County COVID data 
filePath = "data/usCountyCasesDeathsRaw.csv"

#Download data and save to file 
urllib.request.urlretrieve(CSV_URL, filePath)

#import data into dataframe for formatting 
rawUsCountyData = pd.read_csv(filePath)

# print(rawUsCountyData)
# print(rawUsCountyData['state'].unique())
# print(len(rawUsCountyData["fips"].unique()))
# print(rawUsCountyData["date"].unique())

#remove all nan values from data as they cause errors and aren't entirely that helpful...
rawUsCountyData.dropna(inplace=True)

#calculate death rate and put into column
rawUsCountyData["death_rate"] = rawUsCountyData["deaths"]/rawUsCountyData["cases"]
print("average death rate: " + str(average(list(rawUsCountyData["death_rate"]))))



print(rawUsCountyData)
