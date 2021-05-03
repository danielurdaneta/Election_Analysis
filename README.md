# Election_Analysis

## Overview of Election Audit

We started this project with a  cvs dataset of over 310,000 rows each of that represented a vote casted in this elections. We made a Audit of this dataset and extracted this important information for the Colorado Board of Elections:

- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote
- Largest County Turnout
- Total number of votes count for each county
- Each County's and percentage of the total votes 

We did this by programming a code with python.

## Election-Audit Results

The results obtanied due to the Audit are the following: 

- How many votes were cast in this congressional election?

      369,711 votes were cast in this election.
 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

      County Votes:
      
      Jefferson: 10.5% (38,855)
      Denver: 82.8% (306,055)
      Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes?

      Largest County Turnout: Denver
  
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

      Charles Casper Stockham: 23.0% (85,213)
      Diana DeGette: 73.8% (272,892)
      Raymon Anthony Doane: 3.1% (11,606)
  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes
      
      Winner: Diana DeGette
      Winning Vote Count: 272,892
      Winning Percentage: 73.8%

## Election-Audit Summary

One recommendation for future elections is to change the python code in such a way that we can extract from the dataset how many votes each candidate won from each County, this may be done by creating a list of dictionaries that holds the County as keys, and each Candidate votes as values :

  ```
  Candidates_County = [{County1:Candidate1_votes}, {County1:Candidate2_votes}....]
  ```
  
With a script made based on this idea we can draw important conclusions that can lead to further investigation, such as why a particular candidate won in a specific county. 
 
Another recommendation is to modify the script so it prints the extracted information in a program like excel where we can use formats and another data visualization techniques so it can better understand by all kind of users. 
