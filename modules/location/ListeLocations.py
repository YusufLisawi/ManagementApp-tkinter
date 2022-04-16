from voiture import VoitureCitadinne, VoitureVip

class ListeLocations:
	def __init__(self, ListLocations = []):
		self.ListLocations = ListLocations
	
	def AjouterLocation(self, Location):
		self.ListLocation.append(Location)

	def SupprimerLocation(self, Location):
		self.ListLocation.remove(Location)
	
	def FilterLocationDate(self, date):
		location_date = []
		for location in self.ListLocations:
			if (location.getdate_location == date):
				location_date.append(location)
		return(location_date)
	
	def AfficherListeLocation(self):
		return self.ListLocations

	def AfficherListeLocationCitadine(self):
		location_citadine = []
		for location in self.ListLocations:
			if (isinstance(VoitureCitadinne, location)):
				location_citadine.append(location)
		return(location_citadine)

	def AfficherListeLocationVip(self):
		location_Vip = []
		for location in self.ListLocations:
			if (isinstance(VoitureVip, location)):
				location_Vip.append(location)
		return(location_Vip)

	def AfficherLocationMarque(self, marque):
		location_marque = []
		for location in self.ListLocations:
			if (location.getVoiture().getMarque() == marque):
				location_marque.append(location)
		return(location_marque)

	def AfficherLocationImma(self, immatricule):
		location_Imma = []
		for location in self.ListLocations:
			if (location.getVoiture().getImmatricule() == immatricule):
				location_Imma.append(location)
		return(location_Imma)

	def AfficherLocationClient(self, Cin):
		location_cin = []
		for location in self.ListLocations:
			if (location.getClient().getCin() == Cin):
				location_cin.append(location)
		return(location_cin)
	
	


	

