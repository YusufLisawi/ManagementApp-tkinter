from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from modules.user.utilisateur import Utilisateur
from modules.user.ListeUtilisateurs import ListeUtilisateurs

FONT = "Arial"
listUser = ListeUtilisateurs(ListUsers=[Utilisateur("admin","admin","admin@admin.com")])
class GuserAdd:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.master.geometry('260x300+300+305')
		self.master.title("Gestion Utilisateur - Ajouter")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=260, height=320)

		# add user widgets
		self.login_label = Label(self.frame, text="Login", font=(FONT, 15))
		self.login_label.grid(column=0, columnspan=2, row=0)

		self.email_label = Label(self.frame, text="Email", font=(FONT, 15))
		self.email_label.grid(column=0,columnspan=2, row=2)

		self.password_label = Label(self.frame, text="Mot de passe", font=(FONT, 15),)
		self.password_label.grid(column=0,columnspan=2, row=4)

		# entries
		self.login_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.login_entry.grid(column=0,columnspan=2, row=1, ipady=3, pady=8)
		self.login_entry.focus()

		self.email_entry = Entry(self.frame, border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.email_entry.grid(column=0,columnspan=2, row=3, ipady=3, pady=8)
		# ----
		self.password_entry = Entry(self.frame, border=0, show="*",width=21, highlightthickness=2, highlightcolor="red", cursor="text")
		self.password_entry.grid(column=0,columnspan=2, row=5 ,ipady=2, pady=15)

		self.ajouter_btn = Button(self.frame,text="Ajouter", highlightthickness=0, border=0, width=16, font=(FONT, 16), command=self.adduser)
		self.ajouter_btn.grid(column=1, row=6 , ipadx=4, ipady=5, pady=10)
		# ----
		self.frame.grid(column=0, row=0)

	def adduser(self):
		login = self.login_entry.get()
		email = self.email_entry.get()
		password = self.password_entry.get()
		if login == '' or email == '' or password == '':
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")
		else:
			exist = 0
			for acc in listUser.ListeUtilisateur:
				if login == acc.getLogin() and email == acc.getEmail():
					exist = 1
					break
			if exist == 0: 
				listUser.Ajouter(Utilisateur(login, password, email))
				messagebox.showinfo(message=f"Utilisateur a ete bien ajouter!", title=f"Location voiture")

			else:
				messagebox.showwarning(message="Utilisateur exist deja!", title="Location Voiture")

class GuserShow:		
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.grid(column=0, row=0)
		self.master.geometry('460x400+200+205')
		self.master.title("Gestion Utilisateur - Afficher")
		self.master.config(padx=30,pady=30)
		self.master.minsize(width=460, height=350)

		self.show()
		
		self.refresh_btn = Button(self.frame, text="Refresher", highlightthickness=0, border=0, width=13, font=(FONT, 12), command=self.show)
		self.refresh_btn.grid(column=0, columnspan=2, row=1 , ipadx=2, ipady=3, pady=10)
		
		#labels
		self.login= Label(self.frame, text = "Login")
		self.login.grid(row=3,column=0)

		self.email = Label(self.frame, text="Email")
		self.email.grid(row=3,column=1)

		#Entry boxes
		self.login_entry= Entry(self.frame)
		self.login_entry.grid(row= 4, column=0)

		self.email_entry = Entry(self.frame)
		self.email_entry.grid(row=4,column=1)

		#Buttons
		self.select_button = Button(self.frame,text="Sélectionné", command=self.select_user)
		self.select_button.grid(row = 2, column = 0, columnspan=2, pady = 10)

		self.edit_button = Button(self.frame,text="Modifier",command=self.update_user)
		self.edit_button.grid(row = 5, column = 0,columnspan=2, pady = 10)

		self.delete_button = Button(self.frame,text="Supprimer",command=self.delete_user)
		self.delete_button.grid(row = 6, column = 0, columnspan=2, pady = 10)

	def show(self):
		self.table = Treeview(self.frame, columns=(1,2), show="headings", height="5")
		self.table.grid(column=0, columnspan=2, row=0)
		self.table.heading(1, text="Login")
		self.table.heading(2, text="Email")

		# fetching and displaying info
		rows = []
		try:
			for user in listUser.ListeUtilisateur:
				# print('-- New data --\n', user)
				rows.append(tuple((user.getLogin(), user.getEmail())))
			r = 1
			if len(rows) > 0: 
				for i in rows:
					try:
						self.table.insert(parent='',index='end',iid=r,text='', values=i)
					except:
						r+=1
					r+=1
		except:
			pass


	def select_user(self):
		global LOGIN
		#clear entry boxes
		self.login_entry.delete(0,END)
		self.email_entry.delete(0,END)
		
		selected = self.table.focus()
		values = self.table.item(selected,'values')
		LOGIN = values[0]
		#output to entry boxes
		try:
			self.login_entry.insert(0,values[0])
			self.email_entry.insert(0,values[1])
		except:
			messagebox.showwarning(message="Selecter un utilisateur!", title="Location Voiture")
			

	def update_user(self):
		if self.login_entry.get() != '' and self.email_entry.get() != '':
			#save and update the data
			for acc in listUser.ListeUtilisateur:
				if acc.getLogin() == LOGIN:
					listUser.ModifierUserInfo(acc, self.login_entry.get(), self.email_entry.get())
					break
			self.show()
		
			#clear entry boxes
			self.login_entry.delete(0,END)
			self.email_entry.delete(0,END)
		else:
			messagebox.showwarning(message="Remplir tous les champs!", title="Location Voiture")


	def delete_user(self):
		listUser.Supprimer(self.login_entry.get())
		self.show()
		
		#clear entry boxes
		self.login_entry.delete(0,END)
		self.email_entry.delete(0,END)

