import socket
import numpy as np
import pandas as pd

s = socket.socket()
df = pd.DataFrame

s.bind(('0.0.0.0',6666))
s.listen(0)

while True:
    client, addrii = s.accept()

    while True:
        data = client.recv(32)

        if len(data) == 0:
            break
        else:
            print(data)
