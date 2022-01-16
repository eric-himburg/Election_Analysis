# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load=os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options=[]
candidate_votes={}

# Winning candidate and winning count tracker
winning_candidate=""
winning_count = 0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    #Skip the header row
    headers=next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name=row[2]

        #Add unique candidate names to a list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # initialize each candidate's vote count to zero
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1


# Determine the percentage of votes for each candidate
for candidate_name in candidate_votes:
    #Retrieve vote count of each candidate
    votes=candidate_votes[candidate_name]
    #Calculate the percentage of votes
    vote_percentage=float(votes)/float(total_votes)*100
    
    #Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and set the winning_candidate equal to the candidate's name
        winning_candidate=candidate_name

# print out the winning candidate, vote count and percentage to the terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner:  {winning_candidate}\n"
    f"Winning Vote Count:  {winning_count:,}\n"
    f"Winning Percentage:  {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



    


