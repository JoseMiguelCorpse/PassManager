from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database


db = Database("Database/Password.db")
root=Tk()
root.title("Passculebra")
#root.resizable(0,0)
root.geometry("1920x1080+0+0")
root.config(bg="lightblue")
root.state("zoomed")
root.resizable(0,0)
root.iconbitmap("Candado.ico")


mititulo=StringVar()
miUsuario=StringVar()
miEmail=StringVar()
miCategoria=StringVar()
miPassword=StringVar()
miUrl=StringVar()

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    mititulo.set(row[1])
    miUsuario.set(row[2])
    miEmail.set(row[3])
    miCategoria.set(row[4])
    miPassword.set(row[5])
    miUrl.set(row[6])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_pass():
    if tituloEntry.get() == "" or userEntry.get() == "" or emailEntry.get() == "" or categoriaCombo.get() == "" or passEntry.get() == "" or urlEntry.get() == "":
        messagebox.showerror("Error en la entrada", "Complete todos los detalles")
        return
    db.insert(tituloEntry.get(),userEntry.get(), emailEntry.get() , categoriaCombo.get() ,passEntry.get(), urlEntry.get())
    messagebox.showinfo("Éxito", "Registro insertado")
    clearAll()
    dispalyAll()

def update_pass():
    if tituloEntry.get() == "" or userEntry.get() == "" or emailEntry.get() == "" or categoriaCombo.get() == "" or passEntry.get() == "" or urlEntry.get() == "":
        messagebox.showerror("Error en la entrada", "Complete todos los detalles")
        return
    db.update(row[0],tituloEntry.get(), userEntry.get(), emailEntry.get(), categoriaCombo.get(), passEntry.get(), urlEntry.get())
    messagebox.showinfo("Éxito", "Registro insertado")
    clearAll()
    dispalyAll()


def delete_pass():
    db.remove(row[2])
    clearAll()
    dispalyAll()

def show():
    passEntry.config(show="")
def hide():
    passEntry.config(show="*")

def salirAPP():
	resultado = messagebox.askquestion("Salir", 
	"¿Está seguro que desea salir?")

	if resultado == "yes":
	    root.destroy()

def clearAll():
    mititulo.set("")
    miUsuario.set("")
    miEmail.set("")
    miCategoria.set("")
    miPassword.set("")
    miUrl.set("")

def about_popup():
   about= Toplevel(root, pady=50)
   about.resizable(0,0)
   about.title("Acerca de...")
   nombreApp = Label(about, text= "Passculebra", font=("Helvetica",20))
   nombreApp.grid(padx=10,)
   licenciaApp = Label(about, text= "Sin Licencia", font=("Helvetica",10))
   licenciaApp.grid(padx=10)
   copyApp = Label(about, text= "@copyright 2022", font=("Helvetica",14))
   copyApp.grid(padx=10)


#------------------------#
# Configuración del Menu #
#------------------------#

#Creamos el menu y lo configuramos
barraMenu = Menu(root)
root.config(menu=barraMenu)

#Se añaden los nombres de los submenus y comandos
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Añadir", command=add_pass)
archivoMenu.add_command(label="Actualizar", command=update_pass)
archivoMenu.add_command(label="Borrar", command=delete_pass)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAPP )

herramientasMenu = Menu(barraMenu, tearoff=0)
herramientasMenu.add_command(label="Limpiar Campos", command=clearAll)

ayudaMenu = Menu(barraMenu, tearoff=0)
#ayudaMenu.add_command(label="Ayuda")
#ayudaMenu.add_separator()
ayudaMenu.add_command(label="Acerca de...", command=about_popup)

#Se declaran los nombres de los campos en la barra de menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#---------------------------------------#
#      Contenido de la izquierda        #
#---------------------------------------#

contenido = Frame(root)
contenido.pack(side=TOP)
contenido.config(bg="lightblue")

#------------------------------#
#      Entrada de datos        #
#------------------------------#

cabecera = Label(contenido, text="Gestión de Contraseñas", font=("Calibri", 18, "bold"),bg="lightblue")
cabecera.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

tituloLabel = Label(contenido, text="Titulo",font=("Calibri", 16),bg="lightblue")
tituloLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

tituloEntry = Entry(contenido,font=("Calibri", 16),textvariable=mititulo)
tituloEntry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

tituloLabel = Label(contenido, text="Usuario",font=("Calibri", 16),bg="lightblue")
tituloLabel.grid(row=1, column=2, padx=10, pady=10, sticky="w")

userEntry = Entry(contenido,font=("Calibri", 16),textvariable=miUsuario)
userEntry.grid(row=1, column=3, padx=10, pady=10, sticky="w")

emailLabel = Label(contenido, text="Email",font=("Calibri", 16),bg="lightblue")
emailLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")

emailEntry = Entry(contenido,font=("Calibri", 16),textvariable=miEmail)
emailEntry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

categoriaLabel = Label(contenido, text="Categoría",font=("Calibri", 16),bg="lightblue")
categoriaLabel.grid(row=2, column=2, padx=10, pady=10, sticky="w")

categoriaCombo = ttk.Combobox(contenido, font=("Calibri", 16), state="readonly",textvariable=miCategoria)
categoriaCombo['values'] = ("Trabajo","Personal","Banco","Redes Sociales","Stream","Videojuegos","Email","Internet")
categoriaCombo.grid(row=2, column=3, padx=10, sticky="w")

passLabel = Label(contenido, text="Password",font=("Calibri", 16),bg="lightblue")
passLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

passEntry = Entry(contenido,font=("Calibri", 16), show='*',textvariable=miPassword)
passEntry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

urlLabel = Label(contenido, text="Url",font=("Calibri", 16),bg="lightblue")
urlLabel.grid(row=3, column=2, padx=10, pady=10, sticky="w")

urlEntry = Entry(contenido,font=("Calibri", 16),textvariable=miUrl)
urlEntry.grid(row=3, column=3, padx=10, pady=10, sticky="w")

mostrarContraseña = Label(contenido, text='Mostrar Contraseña',bg="lightblue")
mostrarContraseña.grid(row=4, column=1, sticky="ne", padx=30)
mostrarContraseña.bind("<ButtonPress>", lambda event:show())
mostrarContraseña.bind("<ButtonRelease>", lambda event:hide())


#--------------------------#
#      Botones CRUD        #
#--------------------------#
frameBoton = Frame(contenido)
frameBoton.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
frameBoton.config(bg="lightblue")

addButton = Button(frameBoton, text="Añadir",font=("Calibri", 16, "bold"), width=15, bg="green", fg="white", command=add_pass).grid(row=0, column=0, pady=15, padx=10)
UpdateButton = Button(frameBoton, text="Actualizar",font=("Calibri", 16, "bold"), width=15, bg="blue", fg="white", command=update_pass).grid(row=0, column=1, pady=15, padx=10)
borrarButton = Button(frameBoton, text="Borrar",font=("Calibri", 16, "bold"), width=15, bg="red", fg="white", command=delete_pass).grid(row=0, column=2, pady=15, padx=10)
clearButton = Button(frameBoton, text="Limpiar Campos",font=("Calibri", 16, "bold"), width=15, bg="orange", fg="white", command=clearAll).grid(row=0, column=3, pady=15, padx=10)
todosButton = Button(frameBoton, text="Mostrar Todos",font=("Calibri", 16, "bold"), width=15, bg="black", fg="white", command=dispalyAll).grid(row=1, column=1, columnspan=2, padx=10)

#---------------------------------#
#      Contenido de abajo         #
#---------------------------------#

contenido2 = Frame(root, bg="#ecf0f1")
contenido2.place(x=0, y=400, width=1918, height=530)
estilo = ttk.Style()
#crear scrollbar
tree_scroll=Scrollbar(contenido2)
tree_scroll.pack(side=RIGHT, fill=Y)
estilo.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
estilo.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(contenido2, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview", yscrollcommand=tree_scroll.set)
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="Titulo")
tv.column("2", width=5)
tv.heading("3", text="Usuario")
tv.column("3", width=5)
tv.heading("4", text="Email")
tv.column("4", width=5)
tv.heading("5", text="Categoría")
tv.column("5", width=5)
tv.heading("6", text="Password")
tv.column("6", width=5)
tv.heading("7", text="Url")
tv.column("7", width=5)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

tree_scroll.configure(command=tv.yview)

dispalyAll
root.mainloop()
