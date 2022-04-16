class Utilisateur:
	def __init__(self, Login , mot_passe , email):
		self.__login = Login
		self.__mot_passe = mot_passe
		self.__email = email

	def getLogin(self): return self.__login
	def getMdp(self): return self.__mot_passe
	def getEmail(self): return self.__email

	def setLogin(self, n): self.__login = n
	def setMdp(self, n): self.__mot_passe = n
	def setEmail(self, n): self.__email = n

	def __str__(self) -> str:
		return f"Login : {self.__login} - Mot de pass : {self.__mot_passe} - Email : {self.__email}"