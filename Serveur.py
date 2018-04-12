#Dico de Robot
#les pseudos sont associés à un Robot
#si


from socket import *
import sys
import Robot

#DEFINITION DES METHODES

def CONNECT(port, nom) :
  sock.connect(nom, port)
  for cle in dico_robot:
  	if cle == nom:

  dico_robot["nom"]=
  #Fonction connect
  #Verifier si le nom du robot est libre ou pas
  #retourne la map
def INIT():
def	PAUSE():
def	PLAY():
def	SETPSEUDO(nom):
def TRANSFER(nom):
def	LASTUPDATE():
  #retourne la date de la derniere update
def	GETMAP():
  #retourne la position du dernier robot
def	QUIT():
  #déconnecte user
def GETATPOS(abscisse, ordonee):
def	MOVETO(abscisse, ordonee):

def	APPSTATUS():
def HELP():
	return "Connect, Init, pause, play,	setpseudo, transfer, lastupdate, getmap, quit, getatpos,moveto, appstatus";
########################################################################

if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
	sys.exit(1)

#logging.basicConfig(filename = './serveurDate.log', level = logging.INFO)

TAILLE_TAMPON = 256

sock = socket(AF_INET, SOCK_STREAM)

with open("SpaceX.log", "w") as log: #Creation ou ecrasement du fichier log
	log.write(SpaceXlog() + "Serveur started\n")

# Liaison de la socket a toutes les IP possibles de la machine
sock.bind(('', int(sys.argv[1])))

log = open("SpaceX.log", "a") # ouverture du fichier log

print("Serveur en attente sur le port " + sys.argv[1], file=sys.stderr)
log.write(SpaceXlog() + "Listen on :" + sys.argv[1] + "\n")
while True:
	try:
		log = open("SpaceX.log", "a") # ouverture du fichier log

		# Recuperation de la requete du client
		requete = sock.recvfrom(TAILLE_TAMPON)
		# Extraction du message et de l'adresse sur le client
		(mess, adr_client) = requete
		ip_client, port_client = adr_client
		print(f"Requete provenant de {ip_client} par {port_client}. Longueur = {len(mess)}", file=sys.stderr)
		commande=mess.decode().upper()

		# Operations
		if commande == "CONNECT":
			CONNECT()
		elif commande == "INIT":
			INIT()
		elif commande == "PAUSE":
			PAUSE()
		elif commande == "SETPSEUDO":
			SETPSEUDO()
		elif commande == "TRANSFER":
			TRANSFER()
		elif commande == "LASTUPDATE":
			LASTUPDATE()
	    elif commande == "GETMAP":
		    GETMAP()
	    elif commande == "QUIT":
		    QUIT()
	    elif commande == "GETATPOS":
		    GETATPOS()
	    elif commande == "APPSTATUS":
		    APPSTATUS()
	    elif commande == "MOVETO":
		    MOVETO()
		else :
			commande = "Commande introuvable"


		# Construction de la reponse

		log.write(SpaceXlog() + "Received " + cmd + " from " + ip_client+"\n")
		print(cmd)

		# Envoi de la reponse au client
		sock.sendto(reponse.encode(), adr_client)
	except KeyboardInterrupt: break
sock.close()
log.write(SpaceXlog() + "Server stopped...")
log.close()
print("Arret du serveur", file=sys.stderr)
sys.exit(0)
