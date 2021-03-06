import socket
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

fig = plot.figure(figsize=(30,6))
s = socket.socket()
csv = open("temp_and_hum.csv","w")
csv.write("id,temp,humid\n")
s.bind(('0.0.0.0',6666))
s.listen(0)
reqid = 0;
while True:
    client, addrii = s.accept()

    while True:
        data = client.recv(32)

        if data == b'\r\n' or data == b'\n' or data.decode('UTF-8')[:1] == '1':
            data = None
        elif len(data) == 0:
            break
        elif data.decode('UTF-8')[:2] == "30":
            break
        else:
            print(str(reqid)+","+str(data.decode('UTF-8'))[2:])
            csv.write(str(reqid)+","+str(data.decode('UTF-8'))[2:])
            reqid = reqid+1
csv.close()
s.close()
df = pd.read_csv('temp_and_hum.csv')
plt.scatter(df[id], df[humid],c=df[temp], s=500)
plt.blue()
plt.show
