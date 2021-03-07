import socket , pickle
import time 
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6550))

while(1):
    reponse =input("Demande D'execution press enter:")
    client.send(pickle.dumps("demande"))
    data = client.recv(1024)
    ob = pickle.loads(data)
    if(ob==1):
        print("Start execution")
        time.sleep(10)
        client.send(pickle.dumps("Done"))
    else:
        print('Permission denied Another progaram is in execution\nWaiting for permission !')
        data = client.recv(1024)
        ob = pickle.loads(data)
        if(ob==1):
            print("the server Has grented permission to Start execution")
            time.sleep(10)
            client.send(pickle.dumps("Done"))
