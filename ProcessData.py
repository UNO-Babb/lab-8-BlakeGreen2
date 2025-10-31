#ProcessData.py
#Name: Blake Green
#Date: 10/31/25
#Assignment: Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    line = line.strip()
    if line == "":
      continue

    parts = line.split()
    first = parts[0]
    last = parts[1]
    studentID = parts[3]
    year = parts[5]
    major = " ".join(parts[6:])

    # Build UserID: first initial + last name + last 3 digits of student ID
    userID = first[0].lower() + last.lower()
    if len(last) < 5:
      userID += "x"
    userID += studentID[-3:]

    # Convert year to abbreviation
    if year.lower() == "freshman":
      yearAbbr = "FR"
    elif year.lower() == "sophomore":
      yearAbbr = "SO"
    elif year.lower() == "junior":
      yearAbbr = "JR"
    elif year.lower() == "senior":
      yearAbbr = "SR"
    else:
      yearAbbr = year

    # Major-Year format
    majorYear = major[:3].upper() + "-" + yearAbbr

    # Write to CSV
    outFile.write(last + "," + first + "," + userID + "," + majorYear + "\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
