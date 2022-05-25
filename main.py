import gspread, serial, time
import pandas as pd
import numpy as np

# Communication channel with Arduino
serport = serial.Serial(port ="/dev/cu.usbserial-1440" , baudrate=9600, timeout=0.050 )

# Authenticate API (everyone needs to do this on their computer separately, read the readme file)
gc = gspread.oauth()
values = [1,2,3,4,5]

def getResponses():
    # Access and store spreadsheet
    responses = gc.open_by_url('https://docs.google.com/spreadsheets/d/1yb-2lQKs9lE3skyBJqqGjc3sKnAk1rqf9-JGVEyjbpI/edit?resourcekey&pli=1#gid=955346109').sheet1
    df = pd.DataFrame(responses.get_all_records())
    print(df)

    ones = len(df.loc[df['How well do you understand the content that is currently being taught?'] == 1])
    twos = len(df.loc[df['How well do you understand the content that is currently being taught?'] == 2])
    threes = len(df.loc[df['How well do you understand the content that is currently being taught?'] == 3])
    fours = len(df.loc[df['How well do you understand the content that is currently being taught?'] == 4])
    fives = len(df.loc[df['How well do you understand the content that is currently being taught?'] == 5])
    aggregate = [ones, twos, threes, fours, fives]
    
    print(aggregate) 

    numresp = sum(aggregate)
    multiplied = list(np.multiply(aggregate, values))
    average = 0
    if numresp > 0:
        average = sum(multiplied)/numresp
    print(average)
    x = str(round(average))

    time.sleep(2)
     # write to serial port
    serport.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = serport.readline()
    print(data)

    responses.batch_clear(["A3:C4000"]) # clear responses

def run():
    while True:
        getResponses()
        time.sleep(15) # every 10 minutes

run()