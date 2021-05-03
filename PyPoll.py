
import os
import csv

#Assign a variable for the file to save

File_to_save = os.path.join("Analysis", "Election_Analysis")

#Assign a variable for the file to load and path

File_to_load = "Resources/election_results.csv"

with open(File_to_load) as election_data:
  
#Read and analyze cvs file
    File_reader = csv.reader(election_data)

#Skip headers in cvs file
    headers = next(File_reader)

    






    










# The data we need to retrieve.
# 1. Total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

 
