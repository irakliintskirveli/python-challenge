import os
import csv

# Files to load (Remember to change these)
file_to_load = "election_data_2.csv"

#open the csv file
with open(file_to_load) as election:
	reader=csv.reader(election)

	#skipp headers, 1st row
	#Set empty list variable
	next(reader)
	totalvotes = [ ]

	#loop through the row to count vote ID

	for row in reader:
		totalvotes.append(row[0])

		
		print("Election Results")
		print("-----------------------------------")
		print("Total Votes:", len(totalvotes))
    
