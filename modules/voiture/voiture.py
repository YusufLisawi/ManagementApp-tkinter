from abc import ABC, abstractmethod

class Voiture(ABC):
	def __init__(self, immatricule, marque, carburant, modele, puissance_fiscale):
		self._immatricule = immatricule
		self._marque = marque
		self._carburant = carburant
		self._modele = modele
		self._puissance_fiscale = puissance_fiscale

	def getImmatricule(self): return self._immatricule
	def getMarque(self): return self._marque
	def getCarburant(self): return self._carburant
	def getModele(self): return self._modele
	def getPuissancefis(self): return self._puissance_fiscale
	
	def setImmatricule(self, n): self._immatricule = n
	def setMarque(self, n): self._marque = n
	def setCarburant(self, n): self._carburant = n
	def setModele(self, n): self._modele = n
	def setPuissancefis(self, n): self._puissance_fiscale = n

	# @abstractmethod
	# def Ajouter(self):
	# 	pass

	# @abstractmethod
	# def SupprimerIm(self, immatriculation):
	# 	pass

	def ModifierInfo(self, imma, marque, carburant, modele, puissace):
		self.setImmatricule(imma)
		self.setMarque(marque)
		self.setCarburant(carburant)
		self.setModele(modele)
		self.setPuissancefis(puissace)

	def __str__(self) -> str:
		return f"Immatriculation : {self._immatricule} - Marque : {self._marque} - Carburant : {self._carburant} - Modele : {self._modele} - Puissance fiscale : {self._puissance_fiscale}"
	
class VoitureVip(Voiture):
	def __init__(self, immatricule, marque, carburant, modele, puissance_fiscale, type = "SUV"):
		super().__init__(immatricule, marque, carburant, modele, puissance_fiscale)
		self.__type = type

	def getType(self): return self.__type
	def setType(self, n):
		if (n in ["4*4", "SUV", "minibus", "limousine"]):
			self.__type = n
			return 1
		else:
			return 0
		
	def ModifierInfo(self, imma, marque, carburant, modele, puissace, type):
		self.setType(type)
		return super().ModifierInfo(imma, marque, carburant, modele, puissace)

	def __str__(self) -> str:
		return super().__str__() + f" - Type : {self.__type}"

class VoitureCitadinne(Voiture):
	def __init__(self, immatricule, marque, carburant, modele, puissance_fiscale, gamme = "A"):
		super().__init__(immatricule, marque, carburant, modele, puissance_fiscale)
		self.__gamme = gamme

	def getGamme(self): return self.__gamme
	def setGamme(self, n):
		if (n in ['A', 'B', 'C']):
			self.__gamme = n
		else:
			return "Invalide Gamme"

	def ModifierInfo(self, imma, marque, carburant, modele, puissace, gamme):
		self.setGamme(gamme)
		return super().ModifierInfo(imma, marque, carburant, modele, puissace)

	def __str__(self) -> str:
		return super().__str__() + f" - Gamme : {self.__gamme}"