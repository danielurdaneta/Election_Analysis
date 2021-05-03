
#Import modules to use in the analysis
import os
import csv

#Assign a variable for the file to save
File_to_save = os.path.join("Analysis", "Election_Analysis")

#Assign a variable for the file to load and path
File_to_load = "Resources/election_results.csv"

#Create a variable to calculate total votes
Total_votes = 0

#Create a list for the candidate options
Candidate_options = []
#Declare the empty dictionary
Candidate_votes = {}
#Winning candidate and winning count tracker:
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the file to analyze
with open(File_to_load) as election_data:
  
    #Read and analyze cvs file
    File_reader = csv.reader(election_data)

    #Skip headers in cvs file
    headers = next(File_reader)

    #Total votes skiping header
    for row in File_reader:
        Total_votes+= 1
        candidate_name = row[2]

        #If the candidte does not match any candidate in the list...  
        if candidate_name not in Candidate_options:
            #Add candidate to the list
            Candidate_options.append(candidate_name)
            #Start tracking votes for each candidate
            Candidate_votes[candidate_name] = 0
        Candidate_votes[candidate_name] += 1

with open(File_to_save,"w") as txt_file:
    
    election_results = (
        f"\n Election Results\n"
        f"------------------------\n"
        f"Total votes: {Total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in Candidate_options:  
        votes = Candidate_votes[candidate_name]
    
        vote_percentage = float(votes)/float(Total_votes)*100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    




# The data we need to retrieve.
# 1. Total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

 
