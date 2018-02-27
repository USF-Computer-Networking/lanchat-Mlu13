import socket,select,sys

host="127.0.0.1"
port=7777

sfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Hello, I'm CLIENT")
sfd.connect((host,port))
sfd.sendto("hello server!","0.0.0.0")
print("NOW SERVER IS LINKED OK......")

while 1:
	infds,outfds,errfds=select.select([sfd.fileno(),0],[],[],999)
	if len(infds)!=0:
		for membe in infds:
			if membe==sfd.fileno():
				buf=sfd.recv(100)
				if buf=="":
					print("server cut")
					sys.exit()
				else:
					print("receive->"),(buf),
				
					
				
			if membe==0:
				#print ("inin\n")
				tosend=sys.stdin.readline()				
				sfd.send(tosend)
				print("send ok!->"),tosend,
				
		
		
	else:
		print("999 second passed!no things happen!")