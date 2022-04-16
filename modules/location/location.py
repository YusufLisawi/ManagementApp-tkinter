from datetime import *
class Location:
	auto = 0
	def __init__(self, date_location:date , durée_location , prix_location , Client , Voiture):
		self.__date_location = date_location
		self.__durée_location = durée_location
		self.__prix_location = prix_location
		self.__Client = Client
		self.__Voiture = Voiture
		self.__idLocation = Location.auto
		auto += 1

	def getdate_location(self): return self.__date_location
	def getdurée_location(self): return self.__durée_location
	def getprix_location(self): return self.__prix_location
	def getClient(self): return self.__Client
	def getVoiture(self): return self.__Voiture
	def getidLocation(self): return self.__idLocation

	def setdate_location(self, n): self.__date_location = n
	def setdurée_location(self, n): self.__durée_location = n
	def setprix_location(self, n): self.__prix_location = n
	def setClient(self, n): self.__Client = n
	def setVoiture(self, n): self.__Voiture = n
	def setidLocation(self, n): self.__idLocation = n

	def __str__(self) -> str:
		return f"idLocation : {self.__idLocation} , date de location : {self.__date_location}, durée de location : {self.__durée_location}, prix de location : {self.__prix_location}, Client : {self.getClient} ,Voiture : {self.getVoiture}"
	


		