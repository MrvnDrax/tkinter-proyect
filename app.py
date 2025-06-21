import tkinter as tk

root = tk.Tk()
root.title("To-Do's App")
root.geometry("600x400")
root.minsize(300, 300)
root.resizable(True, True)

root.columnconfigure(0, weight=1)

label = tk.Label(root, text="Bienvenido a nuestra app para organizar tus tareas")
label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

tlabel = tk.Label(root, text="Ingresa una nueva tarea")
tlabel.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

tarea = tk.Entry(root)
tarea.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="ew")

tboton = tk.Button(root, text="Ingresar tarea")
tboton.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

frame_tareas = tk.Frame(root)
frame_tareas.grid(row=4, column=0, sticky="nsew", padx=10)

root.rowconfigure(4, weight=1)
frame_tareas.columnconfigure(0, weight=1)

def eliminar(frame):
    frame.destroy()

def ingresar():
    text = tarea.get()
    if text.strip() != "":
        tframe = tk.Frame(frame_tareas)
        tframe.pack(fill=tk.X, pady=2, expand=True)

        check = tk.Checkbutton(tframe, text=text)
        check.pack(side=tk.LEFT, padx=5, anchor="w")

        eboton = tk.Button(tframe, text="Eliminar", command=lambda: eliminar(tframe))
        eboton.pack(side=tk.RIGHT, padx=5)

        tarea.delete(0, tk.END)

tboton.config(command=ingresar)

root.mainloop()
