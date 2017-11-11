import os
import csv

# Files to load (Remember to change these)
file_to_load = "budget_data_1.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue:
    reader = csv.reader(revenue)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    rev_change = []

 # in this loop I did sum of column 1 which is revenue in csv file 
 # and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

        totaldate=len(date)
        totalrevenue=sum(revenue)

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. 
    #Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


# 2end file
# Files to load (Remember to change these)
file_to_load_2 = "budget_data_2.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load_2) as revenue:
    reader2 = csv.reader(revenue)

    # use of next to skip first title row in csv file
    next(reader2) 
    revenue2 = []
    date2 = []
    rev_change2 = []

 # in this loop I did sum of column 1 which is revenue in csv file 
 # and counted total months which is column 0 
    for row in reader2:

        revenue2.append(float(row[1]))
        date2.append(row[0])

        totaldate2=len(date2)
        totalrevenue2=sum(revenue2)

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date2))
    print("Total Revenue: $", sum(revenue2))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. 
    #Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue2)):
        rev_change2.append(revenue2[i] - revenue2[i-1])   
        avg_rev_change2 = sum(rev_change2)/len(rev_change2)

        max_rev_change2 = max(rev_change2)

        min_rev_change2 = min(rev_change2)

        max_rev_change_date2 = str(date2[rev_change2.index(max(rev_change2))])
        min_rev_change_date2 = str(date2[rev_change2.index(min(rev_change2))])


    print("Avereage Revenue Change: $", round(avg_rev_change2))
    print("Greatest Increase in Revenue:", max_rev_change_date2,"($", max_rev_change2,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date2,"($", min_rev_change2,")")

    