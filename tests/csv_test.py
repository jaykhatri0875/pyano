import csv

data_file = open('data/datapoints.csv','w',newline='')
writer = csv.writer(data_file)
writer.writerow(["tip","pip","dip",'ispress'])
writer.writerow([0.12,0.43,0.45,0])
data_file.close()
