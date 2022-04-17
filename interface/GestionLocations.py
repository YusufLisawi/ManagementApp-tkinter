from datetime import datetime
import string
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkcalendar import DateEntry
from modules.location.location import Location
from modules.location.ListeLocations import ListeLocations, Location
from interface.GestionClients import listclients
from interface.GestionVoitures import listvoiture

FONT = "Arial"
listlocation = ListeLocations(ListLocations=[])
class GlocationAdd:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('475x330+400+305')
		self.master.title("Gestion locations - Ajouter")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=465, height=330)

		# add location widgets
		self.idLocation_label = Label(self.frame, text="Id Location", font=(FONT, 15))
		self.Client_label = Label(self.frame, text="Client Cin", font=(FONT, 15))
		self.Voiture_label = Label(self.frame, text="Voiture Immatricule", font=(FONT, 15))
		self.date_location_label = Label(self.frame, text="Date location", font=(FONT, 15))
		self.durée_location_label = Label(self.frame, text="Durée location (Jours)", font=(FONT, 15))
		self.prix_location_label = Label(self.frame, text="Prix location (Dhs)", font=(FONT, 15))

		self.idLocation_label.grid(column=0, row=1, pady=5)
		self.Client_label.grid(column=1, row=1, pady=5)
		self.Voiture_label.grid(column=0, row=3, pady=5)
		self.date_location_label.grid(column=1, row=3, pady=5)
		self.durée_location_label.grid(column=0, row=5, pady=5)
		self.prix_location_label.grid(column=1, row=5, pady=5)

		# entries
		self.idLoc = StringVar()
		self.idLoc.set(Location.auto)
		self.idLocation_entry = Entry(self.frame, border=1, width=21, highlightthickness=2, highlightcolor="red", cursor="text", textvariable=self.idLoc, state=DISABLED)
		self.Client_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.Voiture_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.date_location_entry = DateEntry(self.frame, width=21, selectmode='day', borderwidth=2)
		self.durée_location_entry = Spinbox(self.frame,from_=0, to=325, border=0, width=19, highlightthickness=2, highlightcolor="red",)
		self.prix_location_entry = Spinbox(self.frame, border=0,from_=0, to=999999999, width=19, highlightthickness=2, highlightcolor="red",)

		self.idLocation_entry.grid(column=0, row=2, pady=4, ipady=8)
		self.Client_entry.grid(column=1, row=2, pady=4, ipady=8)
		self.Voiture_entry.grid(column=0, row=4, pady=4, ipady=8)
		self.date_location_entry.grid(column=1, row=4, pady=4, ipady=8)
		self.durée_location_entry.grid(column=0, row=6, pady=4, ipady=8)
		self.prix_location_entry.grid(column=1, row=6, pady=4, ipady=8)


		self.ajouter_btn = Button(self.frame,text="Ajouter", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.addlocation)		
		self.ajouter_btn.grid(column=0, columnspan=2, row=7 , ipadx=4, ipady=5, pady=10)
		# ----

	def addlocation(self):
		# get the new selected date 
		def getDateEntry(*args):
			global date_location
			date_location = self.date_location_entry.get_date()

		Client = self.Client_entry.get()
		Voiture = self.Voiture_entry.get()
		date_location = self.date_location_entry.get_date()
		durée_location = self.durée_location_entry.get()
		prix_location = self.prix_location_entry.get()

		self.date_location_entry.bind("<<DateEntrySelected>>", getDateEntry)

		if Client == '' or Voiture == '' or date_location == '' or durée_location == '0' or prix_location == '0':
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")
		else:
			exist = 0
			for lct in listlocation.ListLocations:
				if Client == lct.getClient().getCin() and Voiture == lct.getVoiture().getImmatricule():
					exist = 1
					break
			if exist == 0: 
				# searching for a client with the same Cin given
				foundc = 0
				foundv = 0
				for clt in listclients:
					if Client == clt.getCin():
						foundc = 1
						break
				# searching for a 'Voiture' with the same Imma given
				for vtr in listvoiture:
					if Voiture == vtr.getImmatricule():
						foundv = 1
						break
				if foundc and foundv:
					location = Location(date_location, durée_location, prix_location, clt, vtr) 
					listlocation.AjouterLocation(location)
					# show the incremented id
					self.idLoc.set(Location.auto)
					self.idLocation_entry = Entry(self.frame, border=1, width=21, highlightthickness=2, highlightcolor="red", cursor="text", textvariable=self.idLoc, state=DISABLED)
					self.idLocation_entry.grid(column=0, row=2, pady=4, ipady=8)
					self.clearBoxes()
					messagebox.showwarning(message="Location a bien ajouter!", title=f"Location ID : {self.idLoc}")
					# print(location)
				else:
					messagebox.showwarning(message="Client ou Voiture n'exist pas!", title="Location Voiture")
			else:
				messagebox.showwarning(message="Location exist deja!", title="Location Voiture")
				# self.clearBoxes()

	def clearBoxes(self):
		self.Client_entry.delete(0, END)
		self.Voiture_entry.delete(0, END)
		# self.date_location_entry.get_date()
		self.durée_location_entry.delete(0, END)
		self.prix_location_entry.delete(0, END)
		


# class GlocationShow:		
# 	def __init__(self, master):
# 		self.master = master
# 		self.frame = Frame(self.master)
# 		self.frame.grid(column=0, row=0)
# 		self.master.geometry('1250x430+300+205')
# 		self.master.title("Gestion locations - Afficher")
# 		self.master.config(padx=30, pady=30)
# 		self.master.minsize(width=1230, height=430)

# 		self.show()

# 		self.refresh_btn = Button(self.frame, text="Refresher", highlightthickness=0, border=0, width=13, font=(FONT, 12), command=self.show)
# 		self.refresh_btn.grid(column=0, columnspan=6, row=3 , ipadx=2, ipady=3, pady=10)
		
# 		# labels
# 		self.Imma_label = Label(self.frame, text="Immatriculation", font=(FONT, 15))
# 		self.marque_label = Label(self.frame, text="Marque", font=(FONT, 15))
# 		self.carburant_label = Label(self.frame, text="Carburant", font=(FONT, 15))
# 		self.modele_label = Label(self.frame, text="Modele", font=(FONT, 15))		
# 		self.puissance_label = Label(self.frame, text="Puissance Fiscale", font=(FONT, 15))
# 		self.gaty_label = Label(self.frame, text="Gamme/type", font=(FONT, 15))

# 		# entries
# 		self.Imma_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
# 		self.marque_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
# 		self.carburant_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
# 		self.model_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
# 		self.puissance_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
# 		self.gaty_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
# 		# grid
# 		# labels
# 		self.Imma_label.grid(column=0, row=5)
# 		self.marque_label.grid(column=1, row=5)
# 		self.carburant_label.grid(column=2, row=5)
# 		self.modele_label.grid(column=3, row=5)
# 		self.puissance_label.grid(column=4, row=5)
# 		self.gaty_label.grid(column=5, row=5)
# 		# entries
# 		self.Imma_entry.grid(column=0, row=6, ipady=3, pady=8)
# 		self.Imma_entry.focus()
# 		self.marque_entry.grid(column=1, row=6, ipady=3, pady=8)
# 		self.carburant_entry.grid(column=2, row=6 ,ipady=2, pady=15)
# 		self.model_entry.grid(column=3, row=6, ipady=3, pady=8)
# 		self.puissance_entry.grid(column=4, row=6 ,ipady=2, pady=15)
# 		self.gaty_entry.grid(column=5, row=6 ,ipady=2, pady=15)

# 		#Buttons/ actions
# 		self.select_button = Button(self.frame,text="Sélectionné", command=self.select_location)
# 		self.select_button.grid(row = 4, column = 0, columnspan=6, pady = 10)

# 		self.edit_button = Button(self.frame,text="Modifier",command=self.update_location)
# 		self.edit_button.grid(row = 7, column = 0,columnspan=6, pady = 10)

# 		self.delete_button = Button(self.frame,text="Supprimer",command=self.delete_location)
# 		self.delete_button.grid(row = 8, column = 0, columnspan=6, pady = 10)

# 	def show(self):
# 		self.table = Treeview(self.frame, columns=(1,2,3,4,5,6), show="headings", height="5")
# 		self.table.grid(column=0, columnspan=6, row=2)
# 		self.table.heading(1, text="Immatriculation")
# 		self.table.heading(2, text="Marque")
# 		self.table.heading(3, text="Carburant")
# 		self.table.heading(4, text="Modèle")
# 		self.table.heading(5, text="Puissance fiscale")
# 		self.table.heading(6, text="Gamme/Type")

# 		# fetching and displaying info
# 		rows = []
# 		try:
# 			for location in listlocation:
# 				# print('-- New data --\n', location)
# 				if isinstance(location, locationVip):
# 					rows.append(tuple((location.getImmatricule(), location.getMarque(), location.getCarburant(), location.getModele(), location.getPuissancefis(), f"{location.getType()} (Type )")))
# 				elif isinstance(location, locationCitadinne):
# 					rows.append(tuple((location.getImmatricule(), location.getMarque(), location.getCarburant(), location.getModele(), location.getPuissancefis(), f"{location.getGamme()} (Gamme)")))
# 			r = 1
# 			for i in rows:
# 				try:
# 					self.table.insert(parent='',index='end',iid=r,text='', values=i)
# 				except:
# 					r+=1
# 				r+=1
# 		except:
# 			pass
		
# 	def select_location(self):
# 		global IMMA
# 		# CLEARING INPUT FIELDS
# 		self.clearBoxes()
		
# 		selected = self.table.focus()
# 		values = self.table.item(selected,'values')
# 		IMMA = values[0]
# 		#output to entry boxes
# 		try:
# 			self.Imma_entry.insert(0,values[0])
# 			self.marque_entry.insert(0,values[1])
# 			self.carburant_entry.insert(0, values[2])
# 			self.model_entry.insert(0, values[3])
# 			self.puissance_entry.insert(0, values[4])
# 			self.gaty_entry.insert(0,values[5][:-8])
# 		except:
# 			messagebox.showwarning(message="Selecter un locations!", title="Location location")

# 	def update_location(self):
# 		if self.Imma_entry.get() != '' and self.marque_entry.get() != '' and self.carburant_entry.get() != '' and self.model_entry.get() != '' and self.puissance_entry.get() != '' and self.gaty_entry.get() != '':
# 			#save and update the data
# 			for location in listlocation:
# 				if location.getImmatricule() == IMMA:
# 					if isinstance(location, locationVip):
# 						if self.gaty_entry.get() in ["4*4", "SUV", "minibus", "limousine"]:
# 							location.ModifierInfo(self.Imma_entry.get(), self.marque_entry.get(), self.carburant_entry.get(), self.model_entry.get(), self.puissance_entry.get(), self.gaty_entry.get())
# 							self.clearBoxes()
# 							break
# 						else:
# 							messagebox.showwarning(message="Le type est invalide", title="Location location")

# 					elif isinstance(location, locationCitadinne):
# 						if self.gaty_entry.get().upper() in ['A', 'B', 'C']:
# 							location.ModifierInfo(self.Imma_entry.get(), self.marque_entry.get(), self.carburant_entry.get(), self.model_entry.get(), self.puissance_entry.get(), self.gaty_entry.get().upper())
# 							self.clearBoxes()
# 							break
# 						else:
# 							messagebox.showwarning(message="Le Gamme est invalide", title="Location location")
# 			self.show()
		
# 		else:
# 			messagebox.showwarning(message="Remplir tous les champs!", title="Location location")

# 	def delete_location(self):
# 		for location in listlocation:
# 			if location.getImmatricule() == self.Imma_entry.get():
# 				listlocation.remove(location)
# 				break
# 		self.show()
# 		self.clearBoxes()

# 	def clearBoxes(self):
# 		#clear entry boxes
# 		self.Imma_entry.delete(0, END)
# 		self.marque_entry.delete(0, END)
# 		self.carburant_entry.delete(0, END)
# 		self.model_entry.delete(0, END)
# 		self.puissance_entry.delete(0, END)
# 		self.gaty_entry.delete(0,END)
