import socket , pickle
import time
import threading 

queu = [] 
queuForUser = [] 
executing = 0


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 6550))
server.listen(5)

client_socket0, address = server.accept()
print ("Conencted to - " + str(address))
client_socket1, address = server.accept()
print ("Conencted to - " + str(address))
client_socket2, address = server.accept()
print ("Conencted to - " + str(address))


def thread_function(client,pc):
    while(1):
        data = client.recv(1024)
        ob = pickle.loads(data)
        if(ob=='demande'):
            print ("Demande recived from - " + str(pc))
            global executing
            if(executing==0 and not queu):
                executing = 1
                print ("Queu is empty start executing - " + str(pc))
                client.send(pickle.dumps(1))
                data = client.recv(1024)
                print ("End of execution \n")
                executing = 0
            else:
                queu.append(client)
                queuForUser.append(pc)
                client.send(pickle.dumps(0))
                print(queuForUser)
        elif(ob=='Done'):
            print ("End of execution \n")
            executing = 0
            queu.remove(queu[0])
            queuForUser.remove(queuForUser[0])
            print(queuForUser)




client0 = threading.Thread(target=thread_function, args=(client_socket0,"pc 1"))
client0.start()
client1 = threading.Thread(target=thread_function, args=(client_socket1,"pc 2"))
client1.start()
client2 = threading.Thread(target=thread_function, args=(client_socket2,"pc 3"))
client2.start()

while(1):
    if(queu):
        if(executing==0):
                executing = 1
                print ("Permession grented to for execution - " + str(queuForUser[0]))
                queu[0].send(pickle.dumps(1))
    time.sleep(1)
