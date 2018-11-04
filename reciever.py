import socket
import numpy as np
import pandas as pd

s = socket.socket()
df = pd.DataFrame
csv = open("temp_and_hum.csv","w")
csv.write("id, temp, humid\n")
s.bind(('0.0.0.0',7777))
s.listen(0)

while True:
    client, addrii = s.accept()

    while True:
        data = client.recv(32)

        if data == b'\r\n':
            data = None
        elif len(data) == 0:
            break
        else:
            print(str(data.decode('UTF-8')))
            csv.write(str(data.decode('UTF-8')))
