import csv
import os

INPUT_DIR=raw_input("Enter the location of csv:")
filename=raw_input("Enter the filename:")
for filename in os.listdir(INPUT_DIR):
   with open(os.path.join(INPUT_DIR,filename)) as infile:
      reader = csv.reader(infile)
      for row in reader:
          print row
