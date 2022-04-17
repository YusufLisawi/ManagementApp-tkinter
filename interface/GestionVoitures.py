from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from modules.voiture.voiture import *

FONT = "Arial"
listvoiture = [VoitureVip("6969", "toyota", "test", "2019", "6 CV", type="SUV"), VoitureCitadinne("3402", "toyota", "test", "2019", "6 CV", gamme="A")]
class GvoitureAdd:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('450x100+400+305')
		self.master.title("Gestion Voitures - Ajouter")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=445, height=100)


		self.vip_btn = Button(self.frame,text="Vip", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.vip)
		self.vip_btn.grid(column=0, row=0 , ipadx=4, ipady=5, pady=10, padx=5)
		
		self.Citadinne_btn = Button(self.frame,text="Citadinne", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.citadinne)
		self.Citadinne_btn.grid(column=1, row=0 , ipadx=4, ipady=5, pady=10, padx=5)

		# add voiture widgets
		self.Imma_label = Label(self.frame, text="Immatriculation", font=(FONT, 15))
		self.marque_label = Label(self.frame, text="Marque", font=(FONT, 15))
		self.carburant_label = Label(self.frame, text="Carburant", font=(FONT, 15))
		self.modele_label = Label(self.frame, text="Modele", font=(FONT, 15))		
		self.puissance_label = Label(self.frame, text="Puissance Fiscale", font=(FONT, 15))
		self.type_label = Label(self.frame, text="Type", font=(FONT, 15))
		self.gamme_label = Label(self.frame, text="Gamme", font=(FONT, 15))

		# entries
		self.Imma_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.marque_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.carburant_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.model_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.puissance_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.gamme_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.type_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		

		self.ajouter_btn = Button(self.frame,text="Ajouter", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.addvoiture)		
		# ----

	def vip(self):
		# CLEARING INPUT FIELDS
		self.Imma_entry.delete(0, END)
		self.marque_entry.delete(0, END)
		self.carburant_entry.delete(0, END)
		self.model_entry.delete(0, END)
		self.puissance_entry.delete(0, END)

		self.master.minsize(width=445, height=400)
		self.Imma_label.grid(column=0, row=1)
		self.marque_label.grid(column=1, row=1)
		self.carburant_label.grid(column=0, row=3)
		self.modele_label.grid(column=1, row=3)
		self.puissance_label.grid(column=0, row=5)
		self.Imma_entry.grid(column=0, row=2, ipady=3, pady=8)
		self.Imma_entry.focus()
		self.marque_entry.grid(column=1, row=2, ipady=3, pady=8)
		self.carburant_entry.grid(column=0, row=4 ,ipady=2, pady=15)
		self.model_entry.grid(column=1, row=4, ipady=3, pady=8)
		self.puissance_entry.grid(column=0, row=6 ,ipady=2, pady=15)
		try:
			self.gamme_label.grid_remove()
			self.gamme_entry.grid_remove()
		except:
			pass
		self.gamme_entry.delete(0, END)
		self.type_label.grid(column=1, row=5)
		self.type_entry.grid(column=1, row=6 ,ipady=2, pady=15)

		self.ajouter_btn.grid(column=0, columnspan=2, row=7 , ipadx=4, ipady=5, pady=10)

	def citadinne(self):
		# CLEARING INPUT FIELDS
		self.Imma_entry.delete(0, END)
		self.marque_entry.delete(0, END)
		self.carburant_entry.delete(0, END)
		self.model_entry.delete(0, END)
		self.puissance_entry.delete(0, END)

		self.master.minsize(width=445, height=400)
		self.Imma_label.grid(column=0, row=1)
		self.marque_label.grid(column=1, row=1)
		self.carburant_label.grid(column=0, row=3)
		self.modele_label.grid(column=1, row=3)
		self.puissance_label.grid(column=0, row=5)
		self.Imma_entry.grid(column=0, row=2, ipady=3, pady=8)
		self.Imma_entry.focus()
		self.marque_entry.grid(column=1, row=2, ipady=3, pady=8)
		self.carburant_entry.grid(column=0, row=4 ,ipady=2, pady=15)
		self.model_entry.grid(column=1, row=4, ipady=3, pady=8)
		self.puissance_entry.grid(column=0, row=6 ,ipady=2, pady=15)
		try:
			self.type_label.grid_remove()
			self.type_entry.grid_remove()
		except:
			pass
		self.type_entry.delete(0, END)
		self.gamme_label.grid(column=1, row=5)
		self.gamme_entry.grid(column=1, row=6 ,ipady=2, pady=15)

		self.ajouter_btn.grid(column=0, columnspan=2, row=7 , ipadx=4, ipady=5, pady=10)

	def addvoiture(self):
		Imma = self.Imma_entry.get()
		marque = self.marque_entry.get()
		carburant = self.carburant_entry.get()
		model = self.model_entry.get()
		puissance = self.puissance_entry.get()
		gamme = self.gamme_entry.get()
		type = self.type_entry.get()
		if Imma == '' or marque == '' or carburant == '' or model == '' or puissance == '' or (type == '' and gamme == ''):
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")
		else:
			exist = 0
			for voiture in listvoiture:
				if Imma == voiture.getImmatricule():
					exist = 1
					break
			if exist == 0:
				if type != '' and gamme == '':
					if type in ["4*4", "SUV", "minibus", "limousine"]:
						listvoiture.append(VoitureVip(Imma, marque, carburant, model, puissance, type))
						messagebox.showwarning(message=f"Voiture a ete bien ajouter!", title=f"Location voiture")
					else:
						messagebox.showwarning(message="Le Type est invalide", title="Location Voiture")

				elif type == '' and gamme != '':
					if gamme in ["A", "B", "C"]:
						listvoiture.append(VoitureCitadinne(Imma, marque, carburant, model, puissance, gamme))
						messagebox.showwarning(message=f"Voiture a ete bien ajouter!", title=f"Location voiture")
					else:
						messagebox.showwarning(message="Le Gamme est invalide", title="Location Voiture")
				
			else:
				messagebox.showwarning(message="Voitures exist deja!", title="Location Voiture")

		# for v in listvoiture:
		# 	print(v)

class GvoitureShow:		
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('1250x430+300+205')
		self.master.title("Gestion Voitures - Afficher")
		self.master.config(padx=30, pady=30)
		self.master.minsize(width=1230, height=430)

		self.show()

		self.refresh_btn = Button(self.frame, text="Refresher", highlightthickness=0, border=0, width=13, font=(FONT, 12), command=self.show)
		self.refresh_btn.grid(column=0, columnspan=6, row=3 , ipadx=2, ipady=3, pady=10)
		
		# labels
		self.Imma_label = Label(self.frame, text="Immatriculation", font=(FONT, 15))
		self.marque_label = Label(self.frame, text="Marque", font=(FONT, 15))
		self.carburant_label = Label(self.frame, text="Carburant", font=(FONT, 15))
		self.modele_label = Label(self.frame, text="Modele", font=(FONT, 15))		
		self.puissance_label = Label(self.frame, text="Puissance Fiscale", font=(FONT, 15))
		self.gaty_label = Label(self.frame, text="Gamme/type", font=(FONT, 15))

		# entries
		self.Imma_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.marque_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.carburant_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.model_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.puissance_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		self.gaty_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")		
		# grid
		# labels
		self.Imma_label.grid(column=0, row=5)
		self.marque_label.grid(column=1, row=5)
		self.carburant_label.grid(column=2, row=5)
		self.modele_label.grid(column=3, row=5)
		self.puissance_label.grid(column=4, row=5)
		self.gaty_label.grid(column=5, row=5)
		# entries
		self.Imma_entry.grid(column=0, row=6, ipady=3, pady=8)
		self.Imma_entry.focus()
		self.marque_entry.grid(column=1, row=6, ipady=3, pady=8)
		self.carburant_entry.grid(column=2, row=6 ,ipady=2, pady=15)
		self.model_entry.grid(column=3, row=6, ipady=3, pady=8)
		self.puissance_entry.grid(column=4, row=6 ,ipady=2, pady=15)
		self.gaty_entry.grid(column=5, row=6 ,ipady=2, pady=15)

		#Buttons/ actions
		self.select_button = Button(self.frame,text="Sélectionné", command=self.select_voiture)
		self.select_button.grid(row = 4, column = 0, columnspan=6, pady = 10)

		self.edit_button = Button(self.frame,text="Modifier",command=self.update_voiture)
		self.edit_button.grid(row = 7, column = 0,columnspan=6, pady = 10)

		self.delete_button = Button(self.frame,text="Supprimer",command=self.delete_voiture)
		self.delete_button.grid(row = 8, column = 0, columnspan=6, pady = 10)

	def show(self):
		self.table = Treeview(self.frame, columns=(1,2,3,4,5,6), show="headings", height="5")
		self.table.grid(column=0, columnspan=6, row=2)
		self.table.heading(1, text="Immatriculation")
		self.table.heading(2, text="Marque")
		self.table.heading(3, text="Carburant")
		self.table.heading(4, text="Modèle")
		self.table.heading(5, text="Puissance fiscale")
		self.table.heading(6, text="Gamme/Type")

		# fetching and displaying info
		rows = []
		try:
			for voiture in listvoiture:
				# print('-- New data --\n', voiture)
				if isinstance(voiture, VoitureVip):
					rows.append(tuple((voiture.getImmatricule(), voiture.getMarque(), voiture.getCarburant(), voiture.getModele(), voiture.getPuissancefis(), f"{voiture.getType()} (Type )")))
				elif isinstance(voiture, VoitureCitadinne):
					rows.append(tuple((voiture.getImmatricule(), voiture.getMarque(), voiture.getCarburant(), voiture.getModele(), voiture.getPuissancefis(), f"{voiture.getGamme()} (Gamme)")))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass
		
	def select_voiture(self):
		global IMMA
		# CLEARING INPUT FIELDS
		self.clearBoxes()
		
		selected = self.table.focus()
		values = self.table.item(selected,'values')
		IMMA = values[0]
		#output to entry boxes
		try:
			self.Imma_entry.insert(0,values[0])
			self.marque_entry.insert(0,values[1])
			self.carburant_entry.insert(0, values[2])
			self.model_entry.insert(0, values[3])
			self.puissance_entry.insert(0, values[4])
			self.gaty_entry.insert(0,values[5][:-8])
		except:
			messagebox.showwarning(message="Selecter un Voitures!", title="Location Voiture")
			

	def update_voiture(self):
		if self.Imma_entry.get() != '' and self.marque_entry.get() != '' and self.carburant_entry.get() != '' and self.model_entry.get() != '' and self.puissance_entry.get() != '' and self.gaty_entry.get() != '':
			#save and update the data
			for voiture in listvoiture:
				if voiture.getImmatricule() == IMMA:
					if isinstance(voiture, VoitureVip):
						if self.gaty_entry.get() in ["4*4", "SUV", "minibus", "limousine"]:
							voiture.ModifierInfo(self.Imma_entry.get(), self.marque_entry.get(), self.carburant_entry.get(), self.model_entry.get(), self.puissance_entry.get(), self.gaty_entry.get())
							self.clearBoxes()
							break
						else:
							messagebox.showwarning(message="Le type est invalide", title="Location Voiture")

					elif isinstance(voiture, VoitureCitadinne):
						if self.gaty_entry.get().upper() in ['A', 'B', 'C']:
							voiture.ModifierInfo(self.Imma_entry.get(), self.marque_entry.get(), self.carburant_entry.get(), self.model_entry.get(), self.puissance_entry.get(), self.gaty_entry.get().upper())
							self.clearBoxes()
							break
						else:
							messagebox.showwarning(message="Le Gamme est invalide", title="Location Voiture")
			self.show()
		
		else:
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")


	def delete_voiture(self):
		for voiture in listvoiture:
			if voiture.getImmatricule() == self.Imma_entry.get():
				listvoiture.remove(voiture)
				break
		self.show()
		self.clearBoxes()

	def clearBoxes(self):
		#clear entry boxes
		self.Imma_entry.delete(0, END)
		self.marque_entry.delete(0, END)
		self.carburant_entry.delete(0, END)
		self.model_entry.delete(0, END)
		self.puissance_entry.delete(0, END)
		self.gaty_entry.delete(0,END)
