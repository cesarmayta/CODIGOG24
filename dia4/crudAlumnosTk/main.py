from tkinter import *
from tkinter.ttk import Treeview

def insertar():
    pass

app = Tk()
app.title('Crud de alumnos')
app.geometry('600x400')

frame = LabelFrame(app,text='Nuevo Alumno')
frame.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
lb_nombre = Label(frame,text='Nombre : ')
lb_nombre.grid(row=1,column=0)
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)

lb_email = Label(frame,text='Email : ')
lb_email.grid(row=2,column=0)
txt_email = Entry(frame)
txt_email.grid(row=2,column=1)

lb_celular = Label(frame,text='Celular : ')
lb_celular.grid(row=3,column=0)
txt_celular = Entry(frame)
txt_celular.grid(row=3,column=1)

btn_insertar = Button(frame,text='Insertar Nuevo Alumno',command=insertar)
btn_insertar.grid(row=4,column=1,columnspan=2)


if __name__ == '__main__':
    app.mainloop()