import csv

for filename in os.listdir(INPUT_DIR):
   with open(os.path.join(INPUT_DIR,filename), dialect='excel-tab') as infile:
      reader = csv.reader(infile)
      for row in reader:
          print row
