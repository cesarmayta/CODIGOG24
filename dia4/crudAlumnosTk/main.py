from tkinter import *
from libalumnos import Alumno

app = Tk()


if __name__ == '__main__':
    app_alumno = Alumno(app)
    app.mainloop()