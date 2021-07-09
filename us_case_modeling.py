import pandas as pd 
import numpy as np 
import matplotlib.pyplot

#path for US-County Case/Death data saved from us_case_formating.py file (possibly change to env variable in future)
rawUSCountyCaseDataPath = "data/usCountyCasesDeathsRaw.csv"

#load data into dataframe for easy manipulation 
rawUsCountyData = pd.read_csv(rawUSCountyCaseDataPath)
print(rawUsCountyData["state"].unique())

for state in rawUsCountyData["state"].unique():

    #find all counties in specific state 
    stateDFData = rawUsCountyData[rawUsCountyData["state"] == state]
    fipsCodesState = stateDFData["fips"].unique()
    print(fipsCodesState)

    #drop nan values 
    rawUsCountyData.dropna()

    #define plot and give title 
    CasesPlot = matplotlib.pyplot 
    CasesPlot.title("Cases Over Time In " + state)

    for fipsCode in fipsCodesState:
        if str(fipsCode) != "nan": #ingnore the "none" county fips id... For some reason I could only get this to work with conversion to str.
            
            fipsCodeDFData = rawUsCountyData[rawUsCountyData["fips"] == fipsCode]
            countyName = fipsCodeDFData["county"].tolist()
            
            CasesPlot.plot(fipsCodeDFData["date"], fipsCodeDFData["cases"], label=countyName[0])

    CasesPlot.legend()
    CasesPlot.show()