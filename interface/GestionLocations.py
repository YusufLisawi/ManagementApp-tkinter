from datetime import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from numpy import column_stack
from tkcalendar import DateEntry
from modules.location.location import Location
from modules.location.ListeLocations import ListeLocations, Location
from interface.GestionClients import listclients
from interface.GestionVoitures import listvoiture

FONT = "Arial"
DATE = date(2023,12,19)
lo = Location(DATE, "3", "299", listclients[0], listvoiture[0])
listlocation = ListeLocations(ListLocations=[lo])
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
					messagebox.showinfo(message=f"Location a ete bien ajouter!", title=f"Location voiture")
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
		


class GlocationShow:		
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('1310x520+300+205')
		self.master.title("Gestion locations - Afficher")
		self.master.config(padx=30, pady=30)
		# self.master.minsize(width=1230, height=430)

		self.show()

		self.refresh_btn = Button(self.frame, text="Refresher", highlightthickness=0, border=0, width=13, font=(FONT, 12), command=self.show)
		self.refresh_btn.grid(column=0, columnspan=6, row=3 , ipadx=2, ipady=3, pady=10)
		
		# labels
		self.idLocation_label = Label(self.frame, text="Id Location", font=(FONT, 15))
		self.Client_label = Label(self.frame, text="Client Cin", font=(FONT, 15))
		self.Voiture_label = Label(self.frame, text="Voiture Immatricule", font=(FONT, 15))
		self.date_location_label= Label(self.frame, text="Date location", font=(FONT, 15))
		self.durée_location_label = Label(self.frame, text="Durée location (Jours)", font=(FONT, 15))
		self.prix_location_label = Label(self.frame, text="Prix location (Dhs)", font=(FONT, 15))

		# entries
		self.idLocation_entry = Entry(self.frame, border=1, state="readonly", width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.Client_entry = Entry(self.frame, border=1,state="readonly", width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.Voiture_entry = Entry(self.frame, border=1, state="readonly",width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.date_location_entry = DateEntry(self.frame, border=0, width=19)
		self.durée_location_entry = Spinbox(self.frame,from_=0, to=325, border=0,width=19, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.prix_location_entry = Spinbox(self.frame,from_=0, to=999999, border=0, width=19, highlightthickness=2, highlightcolor="red", cursor="text")		
		# grid
		# labels
		self.idLocation_label.grid(column=0, row=5)
		self.Client_label.grid(column=1, row=5)
		self.Voiture_label.grid(column=2, row=5)
		self.date_location_label.grid(column=3, row=5)
		self.durée_location_label.grid(column=4, row=5)
		self.prix_location_label.grid(column=5, row=5)
		# entries
		self.idLocation_entry.grid(column=0, row=6, ipady=3, pady=8)
		self.Client_entry.grid(column=1, row=6, ipady=3, pady=8)
		self.Voiture_entry.grid(column=2, row=6 ,ipady=2, pady=8)
		self.date_location_entry.grid(column=3, row=6)
		self.durée_location_entry.grid(column=4, row=6 ,ipady=2, pady=8)
		self.prix_location_entry.grid(column=5, row=6 ,ipady=2, pady=8)

		#Buttons/ actions
		self.select_button = Button(self.frame,text="Sélectionné", command=self.select_location)
		self.select_button.grid(row = 4, column = 0, columnspan=6, pady = 10)

		self.edit_button = Button(self.frame,text="Modifier",command=self.update_location)
		self.edit_button.grid(row = 7, column = 0,columnspan=6, pady = 10)

		self.delete_button = Button(self.frame,text="Supprimer",command=self.delete_location)
		self.delete_button.grid(row = 8, column = 0, columnspan=6, pady = 10)

		# menus
		self.filter_options = {
			'fDate' : "Filtrer Location par Date",
			'fCitadine' : "Afficher Locations Citadine",
			'fVip' : "Afficher Locations Vip",
			'fMarque' : "Afficher Locations par Marque",
			'fImma' : "Afficher Locations par Immatricule",
			'fClient' : "Afficher Locations par Client (Cin)"
		}

		self.combo = ttk.Combobox(self.frame, values = list(self.filter_options.values()), state="readonly", width=25)
		self.combo.grid(column=0, columnspan=6, row=9)
		self.combo.set("Filtrer par ...")
		self.combo.bind('<<ComboboxSelected>>', self.selected) 
		self.filterbtn = Button(self.frame, text="Filtrer", highlightthickness=0, border=0, font=(FONT, 20))


	def selected(self, *args):
		choice = self.combo.get()
		if choice == self.filter_options['fDate']:
			global date_filter
			date_filter = DateEntry(self.frame, border=0, width=19)
			self.filterbtn.config(text="Filtrer", command=self.fDate)
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)
		elif choice == self.filter_options['fCitadine']:
			self.filterbtn.config(text="Filtrer", command=self.fCitadine)
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)
		elif choice == self.filter_options['fVip']:
			self.filterbtn.config(text="Filtrer", command=self.fVip)
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)
		elif choice == self.filter_options['fMarque']:
			global marque_filter
			marque_filter = Entry(self.frame, border=0, width=20, highlightthickness=2, highlightcolor="red", cursor="text")
			self.filterbtn.config(text="Filtrer", command=self.fMarque)
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)
		elif choice == self.filter_options['fImma']:
			global imma_filter
			imma_filter = Entry(self.frame, border=0, width=20, highlightthickness=2, highlightcolor="red", cursor="text")
			self.filterbtn.config(text="Filtrer", command=self.fImma)		
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)
		elif choice == self.filter_options['fClient']:
			global Cin_filter
			Cin_filter = Entry(self.frame, border=0, width=20, highlightthickness=2, highlightcolor="red", cursor="text")
			self.filterbtn.config(text="Filtrer", command=self.fClient)
			self.filterbtn.grid(column=0, columnspan=6, row=11, ipady=5, pady=8, ipadx=8)

	def fDate(self):
		self.tableConstructor()
		date_filter.grid(column=0, columnspan=6, row=10)
		listDate = listlocation.FiltrerLocationDate(date=date_filter.get_date())
		# print(listDate)
		rows = []
		try:
			for lct in listDate:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass

	def fCitadine(self):
		self.tableConstructor()
		listCitadine = listlocation.AfficherListeLocationCitadine()
		# print(listCitadine)
		rows = []
		try:
			for lct in listCitadine:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass

	def fVip(self):
		self.tableConstructor()
		listVip = listlocation.AfficherListeLocationVip()
		# print(listVip)
		rows = []
		try:
			for lct in listVip:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass

	def fMarque(self):
		self.tableConstructor()
		marque_filter.grid(column=0, columnspan=6, row=10)
		listMarque = listlocation.AfficherLocationMarque(marque_filter.get())
		rows = []
		try:
			for lct in listMarque:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass

	def fImma(self):
		self.tableConstructor()
		imma_filter.grid(column=0, columnspan=6, row=10)
		listImma = listlocation.AfficherLocationImma(imma_filter.get())
		rows = []
		try:
			for lct in listImma:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass

	def fClient(self):
		self.tableConstructor()
		Cin_filter.grid(column=0, columnspan=6, row=10)
		listClient = listlocation.AfficherLocationClient(Cin_filter.get())
		rows = []
		try:
			for lct in listClient:
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass
		
	def tableConstructor(self):
		self.table = Treeview(self.frame, columns=(1,2,3,4,5,6), show="headings", height="5")
		self.table.grid(column=0, columnspan=6, row=2)
		self.table.heading(1, text="Location Id")
		self.table.heading(2, text="Client")
		self.table.heading(3, text="Voiture")
		self.table.heading(4, text="Date de location")
		self.table.heading(5, text="Durée de location")
		self.table.heading(6, text="Prix de location")

	def show(self):
		self.tableConstructor()
		# fetching and displaying info
		rows = []
		try:
			for lct in listlocation.ListLocations:
				# print('-- New data --\n', location)
				rows.append(tuple((lct.getidLocation(), lct.getClient().getCin(), lct.getVoiture().getImmatricule(), lct.getdate_location(), f"{lct.getdurée_location()} Jour(s)", f"{lct.getprix_location()} Dhs")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass
		
	def select_location(self):
		global LOCA
		# CLEARING INPUT FIELDS
		self.clearBoxes()
		
		selected = self.table.focus()
		values = self.table.item(selected,'values')
		LOCA = values[0]
		#output to entry boxes
		try:
			idLoc = StringVar()
			idLoc.set(values[0])
			clientLoc = StringVar()
			clientLoc.set(values[1])
			voitureLoc = StringVar()
			voitureLoc.set(values[2])
			self.idLocation_entry.config(textvariable=idLoc)
			self.Client_entry.config(textvariable=clientLoc)
			self.Voiture_entry.config(textvariable=voitureLoc)

			ymd = values[3].split('-')
			self.date_location_entry.grid_remove()
			self.date_location_entry = DateEntry(self.frame, border=0, width=19, year=int(ymd[0]), month=int(ymd[1]), day=int(ymd[2]))
			self.date_location_entry.grid(column=3, row=6)

			self.durée_location_entry.insert(0, values[4][:-8])
			self.prix_location_entry.insert(0, values[5][:-4])
		except:
			messagebox.showwarning(message="Selecter un locations!", title="Location location")
		
		

	def update_location(self):
		Client = self.Client_entry.get()
		Voiture = self.Voiture_entry.get()
		date_location = self.date_location_entry.get_date()
		durée_location = self.durée_location_entry.get()
		prix_location = self.prix_location_entry.get()

		if date_location != '' and durée_location != '' and prix_location != '':
			#save and update the data
			try:
				for lct in listlocation.ListLocations:
					if str(lct.getidLocation()) == str(LOCA):
						lct.setdate_location(date_location)
						lct.setdurée_location(durée_location)
						lct.setprix_location(prix_location)
						print(lct)
						break
				self.clearBoxes()
				self.show()
			except:
				messagebox.showwarning(message="Selecter une location", title="Location location")

		else:
			messagebox.showwarning(message="Remplir tous les champs!", title="Location location")

	def delete_location(self):
		for location in listlocation.ListLocations:
			if str(location.getidLocation()) == str(LOCA):
				listlocation.SupprimerLocation(location)
				break
		self.show()
		self.clearBoxes()

	def clearBoxes(self):
		self.idLocation_entry.delete(0, END)
		self.Client_entry.delete(0, END)
		self.Voiture_entry.delete(0, END)
		# self.date_location_entry.get_date()
		self.durée_location_entry.delete(0, END)
		self.prix_location_entry.delete(0, END)

		idLoc = StringVar()
		idLoc.set('')
		clientLoc = StringVar()
		clientLoc.set('')
		voitureLoc = StringVar()
		voitureLoc.set('')
		self.idLocation_entry.config(textvariable=idLoc)
		self.Client_entry.config(textvariable=clientLoc)
		self.Voiture_entry.config(textvariable=voitureLoc)
