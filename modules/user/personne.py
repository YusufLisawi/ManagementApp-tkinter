class Personne:
	def __init__(self, Cin, Nom, prénom):
		self.__Cin = Cin
		self.__Nom = Nom
		self.__prénom = prénom

	def getCin(self): return self.__Cin
	def getNom(self): return self.__Nom
	def getPrénom(self): return self.__prénom

	def setCin(self, n): self.__Cin = n
	def setNom(self, n): self.__Nom = n
	def setPrénom(self, n): self.__prénom = n

	def __str__(self) -> str:
		return f"Cin : {self.__Cin} - Nom : {self.__Nom} - Prénom : {self.__prénom}"