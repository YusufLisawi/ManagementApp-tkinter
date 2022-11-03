from db.conn_mongodb import mydb
from modules.user.utilisateur import Utilisateur

usersCollection = mydb['Users']
class ListeUtilisateurs:
	def __init__(self, ListUsers = []):
		self.ListeUtilisateur = ListUsers
	
	def authentifier(login, mdp):
		# Mongodb find
		user = mydb["Users"].find_one({"login" : login, "passw" : mdp})
		if (user != None):
			print(user["login"])
			return True
		return False

	def Ajouter(self, login, password, email):
		self.ListeUtilisateur.append(Utilisateur(login, password, email))
		# Mongodb insert
		usersCollection.insert_one({"login":login, "email": email, "passw" : password})

	def Supprimer(self, login):
		for acc in self.ListeUtilisateur:
			if acc.getLogin() == login:
				self.ListeUtilisateur.remove(acc)
				break
		# Mongodb delete
		usersCollection.delete_one({"login":login})
		

	def ModifierUserInfo(self, user, login, email):
		for acc in self.ListeUtilisateur:
			if acc == user:
				acc.setLogin(login)
				acc.setEmail(email)
				break
		