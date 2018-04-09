from socket import *
import sys

if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} <ip> <port>", file=sys.stderr)
	sys.exit(1)

TAILLE_TAMPON = 256

while True :
	with socket(AF_INET, SOCK_DGRAM) as sock :
		# Remarque : pas besoin de bind car le port local est choisi par le système
		mess = input("Entrez votre commande : ")
		if mess == "quit" :
			print("Arret du dialogue avec le serveur...")
			sys.exit(0)

		# Envoi de la requête au serveur (ip, port) après encodage de str en bytes
		sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
		# Réception de la réponse du serveur et décodage de bytes en str
		reponse, _ = sock.recvfrom(TAILLE_TAMPON)
		print("Réponse = " + reponse.decode())
