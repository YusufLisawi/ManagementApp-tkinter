from db.conn_mongodb import mydb
from db.createInstances import getListVoiture
from db.createInstances import getListClient

clients = getListClient(mydb["Client"].find())
voitures = getListVoiture(mydb["Voiture"].find())