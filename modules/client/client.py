class Client:
	def __init__(self, Cin, NumPermis, tele):
		self.__Cin  = Cin
		self.__NumPermis  = NumPermis
		self.__tele  = tele

	def getCin(self): return self.__Cin
	def getNumPermis(self): return self.__NumPermis
	def getTele(self): return self.__tele

	def setCin(self, n): self.__Cin = n
	def setNumPermis(self, n): self.__NumPermis = n
	def setTele(self, n): self.__tele = n

	def ModifierInfo(self, cin, nump, tele):
		self.setCin(cin)
		self.setNumPermis(nump)
		self.setTele(tele)

	def __str__(self) -> str:
		return f"Cin : {self.__Cin} - NumPermis : {self.__NumPermis} - Tele : {self.__tele}"