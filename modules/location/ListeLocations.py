from modules.voiture.voiture import VoitureCitadinne, VoitureVip
from modules.location.location import Location

class ListeLocations:
	def __init__(self, ListLocations = []):
		self.ListLocations = ListLocations
	
	def AjouterLocation(self, Location):
		self.ListLocations.append(Location)

	def SupprimerLocation(self, Location):
		self.ListLocations.remove(Location)
	
	def FilterLocationDate(self, date):
		location_date = []
		for location in self.ListLocations:
			if (location.getdate_location == date):
				location_date.append(location)
		return (location_date)
	
	def AfficherListeLocation(self):
		return self.ListLocations

	def AfficherListeLocationCitadine(self):
		location_citadine = []
		for location in self.ListLocations:
			if (isinstance(location, VoitureCitadinne)):
				location_citadine.append(location)
		return (location_citadine)

	def AfficherListeLocationVip(self):
		location_Vip = []
		for location in self.ListLocations:
			if (isinstance(location, VoitureVip)):
				location_Vip.append(location)
		return (location_Vip)

	def AfficherLocationMarque(self, marque):
		location_marque = []
		for location in self.ListLocations:
			if (location.getVoiture().getMarque() == marque):
				location_marque.append(location)
		return (location_marque)

	def AfficherLocationImma(self, immatricule):
		location_Imma = []
		for location in self.ListLocations:
			if (location.getVoiture().getImmatricule() == immatricule):
				location_Imma.append(location)
		return (location_Imma)

	def AfficherLocationClient(self, Cin):
		location_cin = []
		for location in self.ListLocations:
			if (location.getClient().getCin() == Cin):
				location_cin.append(location)
		return (location_cin)
	

	

