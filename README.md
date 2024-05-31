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

**2. Historically Accurate Predictors**
This section of the code analyzes how success voting districts are at the micro level
in predicting the next POTUS.  The code sorts district results from high to low based upon
how many times the district's selection for POTUS matched the final electoral college results.

**3. Exit Poll Demographics**
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

