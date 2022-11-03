from db.conn_mongodb import mydb

Locations = mydb["Location"]
Voiture = mydb["Voiture"]

def FiltrerLocationDate(date):
	return (Locations.find({"date" : date}))

def AfficherListeLocation():
	return (Locations.find())

def AfficherListeLocationCitadine():
	VoitureCitadinne = Voiture.find({"voiture": "citadinne"}, {"imma" : 1, "_id": 0})
	allLocations = []
	for l in Locations.find():
		for v in VoitureCitadinne:
			if l["Voiture"] == v:
				allLocations.append(l)
	return (allLocations)

def AfficherListeLocationVip():
	VoitureCitadinne = Voiture.find({"voiture": "vip"}, {"imma" : 1, "_id": 0})
	allLocations = []
	for l in Locations.find():
		for v in VoitureCitadinne:
			if l["Voiture"] == v["imma"]:
				allLocations.append(l)
	return (allLocations)

def AfficherLocationMarque(marque):
	voitures = Voiture.find({"marque" : marque}, {"imma" : 1, "marque" : 1, "_id": 0})
	allLocations = []
	for l in Locations.find():
		for v in voitures:
			if l["Voiture"] == v["imma"]:
				allLocations.append(l)
	return (allLocations)

def AfficherLocationImma(immatricule):
	return (Locations.find({"Voiture" : immatricule}))

def AfficherLocationClient(Cin):
	clients = mydb["Client"].find({"cin" : Cin}, {"cin" : 1,"_id": 0})
	allLocations = []
	for l in Locations.find():
		for c in clients:
			if l["Client"] == c["cin"]:
				allLocations.append(l)
	return (allLocations)
