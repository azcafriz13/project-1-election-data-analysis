# Project 1:  US Presidential Election:  Exploratory Data Analysis
## Presented by:  Krishan Fotedar and Cristina Frisby
### In Partial Fulfillment of The Requirements of AI Bootcamp

## About the Project
This project reviews actual historical US presidential election results and demographic
poll data to identify trends and patterns in the voting activities of Americans over
the past several decades.  The data exploration intends to provide insights into the
predicted results of the 2024 US presidential election and what patterns if any indicate
influence in cyclic election results.

## Why Study US Presidential Elections?
Areas of interest in anticipating the future President of the United States (POTUS) include
but not limited to the following:
    1. Financial Impact
    2. Personal Interests
    3. Global Impacts

Stock markets and business directions are often influenced by the general trend in politics,
as well as anticipation of stability or disruption in financial markets.  Many citizens have 
person interests beyond finances in political directions, such as civil rights and protections.
World markets and governments also watch US politics with great interest, expecting different
responses in foreign policies with the swing of US elections.

## About the Code
The code for this project is broken down into four primary groups:

**1. General Historic Voting Records**
This section of code uploads historical presidential results for many elections.
The results are this analyzed to trend voting tendencies towards major parties over time.
This can be an indication of the trend of the next election.

The approach we took with this was to pull general election results by site and party from 1976 to 2020. We did some data cleaning by aggregating 3rd party candidates into the "Other" category.
We then used the Prophet time series forecast to predict the election results by state for 2024. We ran the model again to see how the model predicted the 2020 election results.
The model is predicting a Democratic Win in 2024 with 51% of the vote and 272 electoral votes. The model correctly predicted a Democratic win in 2020 with 51% of the vote. It did miss on 4 states: Arizona, Iowa, Georgia and Ohio.

- The code for this is in the git repository in the following files:
<strong>'1976 to 2020 by state.py'</strong> and <strong>'1976 to 2020 by state 2020 prediciction.py'</strong>
- The data can be found in <strong>'data_files'</strong> folder in the <strong>'1976-2020-president.csv'</strong>. file
- The scripts will print the results into <strong>'state_results'</strong> directory

**2. Historically Accurate Predictors**
This section of the code analyzes how success voting districts are at the micro level
in predicting the next POTUS.  The code sorts district results from high to low based upon
how many times the district's selection for POTUS matched the final electoral college results. 

In this case, we identified 44 "bellweather" counties that have correctly predicted the outcome of each presidential election since 1980 save one.
From there we ran a prophet model for each county to see what it will predict in 2024. The model is showing 38 counties will go Democratic and 6 will go Republican.
We ran a prediction of the 2020 election and all but 2 counties went Democratic.

- The code for this is in the git repository in the following files:
<strong>'bellweather.py'</strong> and <strong>'bellweather 2020.py'</strong>

- The data can be found in <strong>'data_files'</strong> folder in the <strong>'Sheet1.xlsx'</strong> file. The data was pulled from Wikipedia https://en.wikipedia.org/wiki/List_of_election_bellwether_counties_in_the_United_States

- The scripts will  print the results into <strong>'bellweather_results'</strong> folder

**3. Exit Poll Demographics**

The code for this is in the git repository in the following files:
- Demographic_Dataframe_Collection.ipynb

After running this file, the user must select the .csv data file:
- Aggregate-Data-Demographic.csv
from the "data files" folder.

Because the individual votes of citizens is generally protected, most demographic data that
may lead towards particular parties has to be obtained through polling data, not election results. 
Two major demographic areas were analyzed for trended results in the presidential elections. 
These demographic groups included men and women voters, and then racial and ethnic groups. 
The demographic data used was collected by Pew Research Center through exit polls and can be
viewed at this link:  
https://www.pewresearch.org/politics/2024/04/09/changing-partisan-coalitions-in-a-politically-divided-nation/

Multiple sets of files from Pew Research Center were aggregated into one .csv file
for use in the code.  The first analysis compared the previous historical results
with the Pew numbers for strictly Democrat and Republican voters to evaluate the point
spread between the actual voting results and the Pew results.  Once this comparison was
determined to be accurate (within 2% points in most cases), the demographc data was
then separated and trended.  The trends were prepared using the prophet functions.
The trend results were then evaluated to identify any outstanding patterns worth noting.
The results include the trend result for Democrat women as "declining" more than any
other men or women's voting groups (Republican Men, Republican Women, and Democrat Men).
Another anomoly was what appeared to be the "disappearing vote" of Black voters.

