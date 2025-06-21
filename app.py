import tkinter as tk

root = tk.Tk()
root.title("To-Do's App")
root.geometry("600x400")

label = tk.Label(root, text="Bienvenido a nuestra app para organizar tus tareas")
label.pack()

tlabel = tk.Label(root, text="Ingresa una nueva tarea")
tlabel.pack()

tarea = tk.Entry(root)
tarea.pack()

frame_tareas = tk.Frame(root)
frame_tareas.pack(fill=tk.BOTH, expand=True, pady=10)

def eliminar(frame):
    frame.destroy()

def ingresar():
    text = tarea.get()
    if text.strip() != "":

        tframe = tk.Frame(frame_tareas)
        tframe.pack(fill=tk.X, pady=2)
        
        check = tk.Checkbutton(tframe, text=text)
        check.pack(side=tk.LEFT, padx=5)
        
        eboton = tk.Button(tframe, text="Eliminar", command=lambda: eliminar(tframe))
        eboton.pack(side=tk.RIGHT, padx=5)

        tarea.delete(0, tk.END)

tboton = tk.Button(root, text="Ingresar tarea", command=ingresar)
tboton.pack(pady=5)


root.mainloop()
