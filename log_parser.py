import csv

logfile = "./pycryptobot.log"

with open(logfile, encoding="ISO-8859-1") as log, open('logfile.csv', 'w') as output: 
    writer = csv.writer(output)
    writer.writerow(['timestamp', 'A', 'B', 'C', 'D'])
    txt = log.read()
    tokens = [(x.split(" ")[0].strip(),
             x.split(",")[1].strip(),
             x.split(",")[2].strip()) 
        for x in txt.split("\n")]

    # i = 0
    # for line in log:
    #     writer.writerow([i] + line.rstrip().split('|'))
    #     i += 1
    #     if i == 10000:
    #         break
    