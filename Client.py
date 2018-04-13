from socket import *
import sys

if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} <ip> <port>", file=sys.stderr)
	sys.exit(1)
	
TAILLE_TAMPON = 256
cmd =""

with socket() as client:
	#Appel de sa mÃÂ©thode connect()
	try:
		client.connect((sys.argv[1], int(sys.argv[2])))
	except (error):
		print ("Connexion au server impossible \nFin du programme")
		sys.exit(1)
	#Check le pseudo du client
	
	#client.send(str(sys.argv[1]).encode())
	

	while cmd != "quit":
		cmd = input("Entrez une commande (help pour la liste, quit pour quitter) : ")
		#if cmd != "quit":
		client.send(cmd.encode())
		messageFromServer = client.recv(TAILLE_TAMPON).decode()
		print(messageFromServer);
		
	print('Deconnexion.')
