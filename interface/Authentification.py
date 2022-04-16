from modules.user.utilisateur import Utilisateur
from setup.window import Window
from tkinter import *
from tkinter import messagebox
from modules.user.ListeUtilisateurs import ListeUtilisateurs

FONT = "Arial"

def login_test():
	listUser = ListeUtilisateurs(ListUsers=[Utilisateur("admin","admin","admin@admin.com")])
	login = login_entry.get()
	mdp = password_entry.get()
	if listUser.authentifier(login, mdp):
		win.destroy()
		from interface.Accueil import Accueil
	else:
		messagebox.showwarning(message="Login ou Mot de pass incorrect", title="Location Voiture")
		return 0

def authentication():
	global win
	global login_entry
	global password_entry

	win = Window(500, 500, "Athentification")
	win.maxsize(width=500, height=500)
	win.config(padx=50, pady=50)
	win.grab_set()

	# logo
	logo = Canvas(width=403, height=136, highlightthickness=0)
	logo_image = PhotoImage(file="./logo.png")
	logo.create_image(202, 68 , image=logo_image)
	logo.grid(column=1, row=0)

	#labels
	labelAuth = Label(text="Authentication", font=(FONT, 24))
	labelAuth.grid(column=1, row=1, pady=20)

	login_label = Label(text="Login", font=(FONT, 15))
	login_label.grid(column=1, row=2)

	password_label = Label(text="Mot de passe", font=(FONT, 15),)
	password_label.grid(column=1, row=4)

	# entries
	login_entry = Entry(border=0, width=21, highlightthickness=2, highlightcolor="red", cursor="text")
	login_entry.grid(column=1, row=3, ipady=3, pady=8)
	login_entry.focus()
	# ----
	password_entry = Entry(border=0, show="*",width=21, highlightthickness=2, highlightcolor="red", cursor="text")
	password_entry.grid(column=1, row=5 ,ipady=2, pady=2)

	# buttons
	connect_btn = Button(text="Se Connecter", highlightthickness=0, border=0, bg='red', width=16, command=login_test)
	connect_btn.grid(column=1, row=6 , ipady=3, pady=20)

	win.mainloop()
