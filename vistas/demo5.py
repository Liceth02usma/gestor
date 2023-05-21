import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class DirectoryExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title("Explorador de Directorios")

        self.current_path = os.getcwd()

        self.path_var = tk.StringVar()
        self.path_var.set(self.current_path)

        self.path_label = tk.Label(self.master, textvariable=self.path_var)
        self.path_label.pack()

        self.listbox = tk.Listbox(self.master)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.populate_listbox()

        self.listbox.bind('<Double-Button-1>', self.on_select)

        button_frame = tk.Frame(self.master)
        button_frame.pack()

        up_button = tk.Button(button_frame, text="Subir", command=self.go_up)
        up_button.pack(side=tk.LEFT)

        open_button = tk.Button(button_frame, text="Abrir", command=self.open)
        open_button.pack(side=tk.LEFT)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete)
        delete_button.pack(side=tk.LEFT)

        rename_button = tk.Button(button_frame, text="Renombrar", command=self.rename)
        rename_button.pack(side=tk.LEFT)

        quit_button = tk.Button(button_frame, text="Salir", command=self.quit)
        quit_button.pack(side=tk.RIGHT)

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in os.listdir(self.current_path):
            self.listbox.insert(tk.END, item)

    def on_select(self, event):
        selection = self.listbox.get(self.listbox.curselection())
        path = os.path.join(self.current_path, selection)
        if os.path.isdir(path):
            self.current_path = path
            self.path_var.set(self.current_path)
            self.populate_listbox()

    def go_up(self):
        parent = os.path.dirname(self.current_path)
        if parent != self.current_path:
            self.current_path = parent
            self.path_var.set(self.current_path)
            self.populate_listbox()

    def open(self):
        selection = self.listbox.get(self.listbox.curselection())
        path = os.path.join(self.current_path, selection)
        if os.path.isdir(path):
            self.current_path = path
            self.path_var.set(self.current_path)
            self.populate_listbox()
        else:
            os.startfile(path)

    def rename(self):
        selection = self.listbox.get(self.listbox.curselection())
        path = os.path.join(self.current_path, selection)
        print(path)
        if os.path.isdir(path):
            new_name = simpledialog.askstring("Renombrar Carpeta", f"Ingrese el nuevo nombre para '{selection}'")
            
            if new_name:
                new_path = os.path.join(self.current_path, new_name)
                try:

                    os.rename(path, new_path)

                    self.populate_listbox()
                except OSError:
                    messagebox.showerror("Error", f"No se pudo renombrar la carpeta '{selection}'")
        else:
            new_name = simpledialog.askstring("Renombrar Archivo", f"Ingrese el nuevo nombre para '{selection}'")
            if new_name:
                new_path = os.path.join(self.current_path, new_name)
                try:
                    print("Hola",path)
                    print("Nueva ruta",new_path)
                    os.rename(path, new_path)
                    self.populate_listbox()
                except OSError:
                    messagebox.showerror("Error", f"No se pudo renombrar el archivo '{selection}'")

    def delete(self):
        selection = self.listbox.get(self.listbox.curselection())
        path = os.path.join(self.current_path, selection)
        print(path)
        if os.path.isdir(path):
            confirm = messagebox.askyesno("Eliminar Carpeta", f"¿Estás seguro de que quieres eliminar la carpeta '{selection}'?")
            if confirm:
                try:
                    os.rmdir(path)
                    self.populate_listbox()
                except OSError:
                    messagebox.showerror("Error", f"No se pudo eliminar la carpeta '{selection}'")
        else:
            confirm = messagebox.askyesno("Eliminar Archivo", f"¿Estás seguro de que quieres eliminar el archivo '{selection}'?")
            if confirm:
                try:
                    os.remove(path)
                    self.populate_listbox()
                except OSError:
                    messagebox.showerror("Error", f"No se pudo eliminar el archivo '{selection}'")

    def quit(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    DirectoryExplorer(root)
    root.mainloop()