import socket,select,sys,nmap

host="0.0.0.0"
port=7777


sfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sfd.bind((host,port))
print ("Hello ,I'm SERVER\nput in '88' to leave me!")
sfd.listen(10)
print ("Now start listen......")

clientlist=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]#10  -1
currentplace=0


while 1:
	carefd=[0,sfd.fileno()]
	for membe in clientlist:
		if membe!=-1:
			#membe.fileno()
			carefd.append(membe.fileno())			
	infds,outfds,errfds=select.select(carefd,[],[],999)
	if len(infds)!=0:
		for membe in infds:
			if membe==sfd.fileno():
				newclientsock,newclientaddr=sfd.accept()
				clientlist[currentplace]=newclientsock
				currentplace+=1
			elif membe==0:
				#print ("55\n")
				tosend=sys.stdin.readline()
				if tosend=="88\n":
					sfd.close()
					sys.exit()
				for allclient in clientlist:
					if allclient!=-1:
						allclient.send(tosend)
				print(("Send To Client Succeed!->"),(tosend),)
			else :
				for allclient in clientlist:
					if allclient!=-1:
						if membe==allclient.fileno():
							torecv=allclient.recv(100)
							if torecv=="":
								print ("!!!!!!a client drop!!!!!!")
								clientlist.remove(allclient)
								currentplace-=1
							else:
								print ("receive->",(torecv),)
	else:
		print("999 second passed!nothing happened!")	
