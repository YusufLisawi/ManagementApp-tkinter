class ListeUtilisateurs:
	def __init__(self, ListUsers = []):
		self.ListeUtilisateur = ListUsers
	
	def authentifier(self, login, mdp):
		for acc in self.ListeUtilisateur:
			if acc.getLogin() == login and acc.getMdp() == mdp:
				return True
		return False

	def Ajouter(self, user):
		self.ListeUtilisateur.append(user)

	def Supprimer(self, login):
		for acc in self.ListeUtilisateur:
			if acc.getLogin() == login:
				self.ListeUtilisateur.remove(acc)
				break

	def ModifierUserInfo(self, user, login, email):
		for acc in self.ListeUtilisateur:
			if acc == user:
				acc.setLogin(login)
				acc.setEmail(email)
				break 
		