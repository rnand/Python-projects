import csv
import os

INPUT_DIR=raw_input("Enter the location of csv:")
filename=raw_input("Enter the filename:")
for filename in os.listdir(INPUT_DIR):
   with open(os.path.join(INPUT_DIR,filename),'rb') as infile:  #generate proper path to the file and open it
      reader = csv.reader(infile, dialect='excel-tab') #csvs exported from microsoft excel
      for row in reader:
          print row
