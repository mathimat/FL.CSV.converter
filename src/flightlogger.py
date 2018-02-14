import os
import csv
import datetime
from codecs import EncodedFile

from Tkinter import Tk
from tkFileDialog import askopenfilename

print("Select file..")

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print("Executing..")


with EncodedFile(open(filename, 'rb'),'utf-8','iso8859-1') as input,EncodedFile(open('importThis.csv', 'wb'),'utf-8','iso8859-1') as output:
    #import file
    reader = csv.reader(input, delimiter=',', quotechar='"')
    writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')

    reader.next()
    Header=["date","departure_airport","departure_time","arrival_airport","arrival_time","aircraft_type","aircraft_registration","pic_name","total_time","night","single_engine_vfr","single_engine_ifr","multi_engine_vfr","multi_engine_ifr","pic","co_pilot","multi_pilot","instructor","dual","simulator","ldgs_day","ldgs_night","remarks"]
    #8-18
    writer.writerow(Header)
    for row in reader:
        rad=8
        #row 8-18 is time in seconds in FL need to be HH:MM
        while rad<20:
            tid = ''
            if(row[rad] != ''):
                tid = str(datetime.timedelta(seconds=int(row[int(rad)])))
                tid = str(tid)
                tid = ''.join(tid.split())
                tid = tid[:-3]
            row[rad] = tid
            rad+=1
        row[0] = datetime.datetime.strptime(row[0],'%d.%m.%Y')
        row[0] = datetime.date.strftime(row[0], '%d/%m/%Y')
        #03.10.2017 -> 03/10/2017
        
        writer.writerow(row)
        
        
        
print("Done!")
