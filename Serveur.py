from socket import *
from datetime import *
from calendar import *
import sys, threading, os, os.path, re


#DEFINITION DES METHODES
#DICTIONNAIRE DES ROBOTS
dico_robot = {}

#DEFINITION DES METHODES

def CONNECT(port, nom) :
  sock.connect(nom, port)
  for cle in dico_robot:
  	if cle == nom:
		if dico_robot[nom].get_state() == "DISCONNECTED":
			return "\n101 : Connection succeed" 
		return "\n201 : Robot name taken"
	
	
  
  #Fonction connect
  #Verifier si le nom du robot est libre ou pas
  #retourne la map
def INIT(x, y):
	
	
def	PAUSE():
	
def	PLAY():
	
def	SETPSEUDO(nom):
	
def TRANSFER(nom):
	
def	LASTUPDATE():
	
  #retourne la date de la derniere update
def	GETMAP():
	rmap = []
	for r in dico_robot:
		rmap += r.get_position
		
  #retourne la position du dernier robot

  #dÃ©connecte user
def GETATPOS(abscisse, ordonee):
	
def	MOVETO(abscisse, ordonee):

def	APPSTATUS():
	
def HELP():
	return "Connect, Init, pause, play,	setpseudo, transfer, lastupdate, getmap, quit, getatpos, moveto, appstatus";
	
	
def rep(client, adr):
	cmd = ""
	while cmd != "QUIT":
		print(f"RequÃªte provenant de {adr[0]}.",
					file=sys.stderr)			
					
			# Construction de la rÃ©ponse
		cmd = client.recv(TAILLE_TAMPON).decode().upper()
			
		if cmd == "CONNECT":
		 	CONNECT()
		elif cmd == "INIT":
			INIT()
		elif cmd == "PAUSE":
			PAUSE()
		elif cmd == "SETPSEUDO":
			SETPSEUDO()
		elif cmd == "TRANSFER":
			TRANSFER()
		elif cmd == "LASTUPDATE":
			LASTUPDATE()
	    elif cmd == "GETMAP":
		    GETMAP()
	    elif cmd == "QUIT":
		    QUIT()
	    elif cmd == "GETATPOS":
		    GETATPOS()
	    elif cmd == "APPSTATUS":
		    APPSTATUS()
	    elif cmd == "MOVETO":
		    MOVETO()		
		elif cmd != "QUIT" :
			reponse = "200 : Erreur : commande erronÃ©e : " + cmd
			
			
		log.write(datelog() + "Received " + cmd + " from " +adr[0]+"\n")
		print(cmd)
		client.send(reponse.encode())	
	
########
	
	
if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
	sys.exit(1)

#logging.basicConfig(filename = './serveurDate.log', level = logging.INFO)

TAILLE_TAMPON = 256
today = datetime.now()

sock_server = socket()
sock_server.bind(("", int(sys.argv[1])))
sock_server.listen(10)

with open("serveurDate.log", "w") as log: #Creation ou ecrasement du fichier log
	log.write( datelog() + "Serveur started\n")
	

log = open("serveurDate.log", "a") # ouverture du fichier log

print("Serveur en attente sur le port " + sys.argv[1], file=sys.stderr)
log.write( datelog() + "Listen on :" + sys.argv[1] + "\n")
while True:
	try:
		log = open("serveurDate.log", "a") # ouverture du fichier log
		sock_client, adr_client = sock_server.accept()
		print("Connexion de ".format(adr_client))
		threading.Thread(target=rep, args=(sock_client, adr_client,)) \
				 .start()
				 
		
	except KeyboardInterrupt: break
	



sock_server.close()
log.write(datelog() + "Server stopped...")
log.close()
print("ArrÃªt du serveur", file=sys.stderr)
sys.exit(0)
