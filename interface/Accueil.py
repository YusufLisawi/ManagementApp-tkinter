from tkinter import ttk
from setup.window import Window
from tkinter import *
from tkinter import messagebox
from interface.GestionUtilisateur import GuserAdd, GuserShow
from interface.GestionClients import GclientAdd, GclientShow
from interface.GestionVoitures import GvoitureAdd, GvoitureShow

FONT = "Arial"	
class Accueil:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		# logo
		self.logo = Canvas(self.frame, width=403, height=136, highlightthickness=0)
		self.logo_image = PhotoImage(file="./logo.png")
		self.logo.create_image(202, 68 , image=self.logo_image)
		self.logo.grid(column=1, row=0)
		#labels
		self.label = Label(self.frame,text="Bienvenu!", font=(FONT, 24))
		self.label.grid(column=1, row=1, pady=20)

		#  button options
		self.gUser_button = Button(self.frame,text="Gestion Utilisateur", highlightthickness=0, border=0, width=16, font=(FONT, 20), command=self.selectU)
		self.gUser_button.grid(column=0, row=2 , ipadx=4, ipady=8, pady=20)

		self.gClient_button = Button(self.frame,text="Gestion Client", highlightthickness=0, border=0, width=16, font=(FONT, 20), command=self.selectC)
		self.gClient_button.grid(column=1, row=2 , ipadx=4, ipady=8, pady=20)

		self.gVoiture_button = Button(self.frame,text="Gestion Voiture", highlightthickness=0, border=0, width=16, font=(FONT, 20), command=self.selectV)
		self.gVoiture_button.grid(column=2, row=2 , ipadx=4, ipady=8, pady=20)

		self.gLocation_button = Button(self.frame,text="Gestion Location", highlightthickness=0, border=0, width=16, font=(FONT, 20), command=self.selectL)
		self.gLocation_button.grid(column=1, row=3 , ipadx=4, ipady=8, pady=20)

		# menus
		self.comboGuser = ["Afficher Utilisateur", "Ajouter Utilisateur"]
		self.comboGclient = ["Afficher Client", "Ajouter Client"]
		self.comboGvoiture = ["Afficher Voiture", "Ajouter Voiture"]
		self.comboGlocation = ["Afficher Location", "Ajouter Location"]

		self.combo = ttk.Combobox(self.frame, values = [], state="readonly")

		self.demarrer_button = Button(self.frame, text="Démarrer", highlightthickness=0, border=0, width=12, font=(FONT, 20), command = self.launch)

		self.frame.grid(column=0, row=0)

	def selectU(self):
		self.option = "Gestion Utilisateur"
		self.combo = ttk.Combobox(self.frame, values = self.comboGuser, state="readonly")
		self.combo.set(self.option)
		self.combo.grid(column=1, row=4, pady=10)
		self.demarrer_button.grid(column=1, row=5 , ipadx=4, ipady=8, pady=20)

	def selectC(self):
		self.option = "Gestion Client"
		self.combo = ttk.Combobox(self.frame, values = self.comboGclient, state="readonly")
		self.combo.set(self.option)
		self.combo.grid(column=1, row=4, pady=10)
		self.demarrer_button.grid(column=1, row=5 , ipadx=4, ipady=8, pady=20)

	def selectV(self):
		self.option = "Gestion Voiture"
		self.combo = ttk.Combobox(self.frame, values = self.comboGvoiture, state="readonly")
		self.combo.set(self.option)
		self.combo.grid(column=1, row=4, pady=10)
		self.demarrer_button.grid(column=1, row=5 , ipadx=4, ipady=8, pady=20)

	def selectL(self):
		self.option = "Gestion Location"
		self.combo = ttk.Combobox(self.frame, values = self.comboGlocation, state="readonly")
		self.combo.set(self.option)
		self.combo.grid(column=1, row=4, pady=10)
		self.demarrer_button.grid(column=1, row=5 , ipadx=4, ipady=8, pady=20)


	def launch(self):
		choice = self.combo.get()
		self.newWindow = Toplevel(self.master)
		# user
		if choice == self.comboGuser[0]:
			self.app = GuserShow(self.newWindow)
		elif choice == self.comboGuser[1]:
			self.app = GuserAdd(self.newWindow)
		# client
		elif choice == self.comboGclient[1]:
			self.app = GclientAdd(self.newWindow)
		elif choice == self.comboGclient[0]:
			self.app = GclientShow(self.newWindow)
		# client
		elif choice == self.comboGvoiture[1]:
			self.app = GvoitureAdd(self.newWindow)
		elif choice == self.comboGvoiture[0]:
			self.app = GvoitureShow(self.newWindow)



def main(): 
	root = Window(900, 450, "Accueil")
	style = ttk.Style()
	style.theme_use('clam')
	root.maxsize(width=980, height=580)
	root.config(padx=50, pady=50)
	app = Accueil(root)
	root.mainloop()

main()