from modules.client.client import Client
from modules.voiture.voiture import VoitureVip, VoitureCitadinne

def getListClient(client):
	listClient = []
	for clt in client:
		listClient.append(Client(clt['cin'], clt['numpermis'], clt['tele']))
	return (listClient)

def getListVoiture(voiture):
	listVoiture = []
	for vtr in voiture:
		if (vtr["voiture"] == "vip"):
			listVoiture.append(VoitureVip(vtr["imma"], vtr["marque"], vtr["carburant"], vtr["model"], vtr["puissance"], vtr["spec"]))
		if (vtr["voiture"] == "citadinne"):
			listVoiture.append(VoitureCitadinne(vtr["imma"], vtr["marque"], vtr["carburant"], vtr["model"], vtr["puissance"], vtr["spec"]))
	return (listVoiture)