from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from modules.client.client import Client

FONT = "Arial"
listclients = [Client("L678946", "test00", "0682860421")]
class GclientAdd:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.master.geometry('260x300+300+305')
		self.master.title("Gestion Client - Ajouter")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=260, height=320)

		# add client widgets
		self.Cin_label = Label(self.frame, text="Cin", font=(FONT, 15))
		self.Cin_label.grid(column=0, columnspan=2, row=0)

		self.NumPermis_label = Label(self.frame, text="Num Permis", font=(FONT, 15))
		self.NumPermis_label.grid(column=0,columnspan=2, row=2)

		self.tele_label = Label(self.frame, text="Tele", font=(FONT, 15),)
		self.tele_label.grid(column=0,columnspan=2, row=4)

		# entries
		self.Cin_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.Cin_entry.grid(column=0,columnspan=2, row=1, ipady=3, pady=8)
		self.Cin_entry.focus()

		self.NumPermis_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.NumPermis_entry.grid(column=0,columnspan=2, row=3, ipady=3, pady=8)
		# ----
		self.Tele_entry = Entry(self.frame, border=0,width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.Tele_entry.grid(column=0,columnspan=2, row=5 ,ipady=2, pady=15)

		self.ajouter_btn = Button(self.frame,text="Ajouter", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.addclient)
		self.ajouter_btn.grid(column=1, row=6 , ipadx=4, ipady=5, pady=10)
		# ----
		self.frame.grid(column=0, row=0)

	def addclient(self):
		Cin = self.Cin_entry.get()
		NumPermis = self.NumPermis_entry.get()
		Tele = self.Tele_entry.get()
		if Cin == '' and NumPermis == '' and Tele == '':
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")
		else:
			exist = 0
			for client in listclients:
				if Cin == client.getCin() or NumPermis == client.getNumPermis() or Tele == client.getTele():
					exist = 1
					break
			if exist == 0:
				listclients.append(Client(Cin, NumPermis, Tele))
				messagebox.showwarning(message=f"Client a ete bien ajouter!", title=f"Location voiture")
			else:
				messagebox.showwarning(message="Client exist deja!", title="Location Voiture")
		pass

class GclientShow:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('660x400+200+205')
		self.master.title("Gestion Client - Afficher")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=660, height=350)

		self.show()
		
		self.refresh_btn = Button(self.frame, text="Refresher", highlightthickness=0, border=0, width=13, font=(FONT, 12), command=self.show)
		self.refresh_btn.grid(column=0, columnspan=3, row=1 , ipadx=2, ipady=3, pady=10)
		
		#labels
		self.Cin = Label(self.frame, text = "Cin")
		self.Cin.grid(row=3,column=0)

		self.NumPermis = Label(self.frame, text="NumPermis")
		self.NumPermis.grid(row=3,column=1)

		self.Tele = Label(self.frame, text="Tele")
		self.Tele.grid(row=3,column=2)

		#Entry boxes
		self.Cin_entry= Entry(self.frame)
		self.Cin_entry.grid(row= 4, column=0)

		self.NumPermis_entry = Entry(self.frame)
		self.NumPermis_entry.grid(row=4,column=1)

		self.Tele_entry = Entry(self.frame)
		self.Tele_entry.grid(row=4,column=2)

		#Buttons
		self.select_button = Button(self.frame,text="Sélectionné", command=self.select_client)
		self.select_button.grid(row = 2, column = 0, columnspan=3, pady = 10)

		self.edit_button = Button(self.frame,text="Modifier",command=self.update_client)
		self.edit_button.grid(row = 5, column = 0,columnspan=3, pady = 10)

		self.edit_button = Button(self.frame,text="Supprimer",command=self.delete_client)
		self.edit_button.grid(row = 6, column = 0, columnspan=3, pady = 10)

	def show(self):
		self.table = Treeview(self.frame, columns=(1, 2, 3), show="headings", height="5")
		self.table.grid(column=0, columnspan=3, row=0)
		self.table.heading(1, text="Cin")
		self.table.heading(2, text="NumPermis")
		self.table.heading(3, text="Tele")

		# fetching and displaying info
		rows = []
		try:
			for client in listclients:
				# print('-- New data --\n', client)
				rows.append(tuple((client.getCin(), client.getNumPermis(), client.getTele())))
			r = 1
			for i in rows:
				try:
					self.table.insert(parent='',index='end',iid=r,text='', values=i)
				except:
					r+=1
				r+=1
		except:
			pass


	def select_client(self):
		global CIN
		#clear entry boxes
		self.Cin_entry.delete(0,END)
		self.NumPermis_entry.delete(0,END)
		self.Tele_entry.delete(0,END)
		
		selected = self.table.focus()
		values = self.table.item(selected,'values')
		CIN = values[0]
		#output to entry boxes
		try:
			self.Cin_entry.insert(0,values[0])
			self.NumPermis_entry.insert(0,values[1])
			self.Tele_entry.insert(0,values[2])
		except:
			messagebox.showwarning(message="Selecter un Client!", title="Location Voiture")
			

	def update_client(self):
		if self.Cin_entry.get() != '' and self.NumPermis_entry.get() != '' and self.Tele_entry.get() != '':
			#save and update the data
			for client in listclients:
				if client.getCin() == CIN:
					client.ModifierInfo(self.Cin_entry.get(), self.NumPermis_entry.get(), self.Tele_entry.get())
					break
			self.show()
			
			#clear entry boxes
			self.Cin_entry.delete(0,END)
			self.NumPermis_entry.delete(0,END)
			self.Tele_entry.delete(0,END)
		else:
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")


	def delete_client(self):
		for client in listclients:
			if client.getCin() == self.Cin_entry.get():
				listclients.remove(client)
				break
		self.show()
		
		#clear entry boxes
		self.Cin_entry.delete(0,END)
		self.NumPermis_entry.delete(0,END)
		self.Tele_entry.delete(0,END)

