import os
import tkinter as tk
import shutil
from NaryTree import NaryTree
from NaryTree import Archivo
from tkinter import ttk, filedialog, messagebox, simpledialog

class DirectoryExplorer:

    def __init__(self, master):
        self.master = master
        self.master.title("Explorador de Directorios")
        self.tree = NaryTree()
        self.current_path = os.getcwd()

        self.path_var = tk.StringVar()
        self.path_var.set(self.current_path)
        
        self.path_copy = None
        self.is_copiar = False
        self.ruta_origen = None

        self.treeview = ttk.Treeview(self.master)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        self.populate_treeview()
        self.tree2 = self.tree

        self.treeview.bind('<<TreeviewOpen>>', self.on_open)
        self.treeview.bind('<Double-Button-1>', self.on_select)

        button_frame = tk.Frame(self.master)
        button_frame.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.place(relx=1, y=0, anchor="ne") 

        self.entry.bind("<KeyRelease>", lambda event: self.find_archive())

        up_button = tk.Button(button_frame, text="Subir", command=self.go_up)
        up_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Agregar", command=self.agregar)
        rename_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Crear Archivo", command=self.agregar_archivo)
        rename_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Renombrar", command=self.rename)
        rename_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Copiar", command=self.copiar)
        rename_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Cortar", command=self.cortar)
        rename_button.pack(side=tk.LEFT)
        
        rename_button = tk.Button(button_frame, text="Pegar", command=self.pegar)
        rename_button.pack(side=tk.LEFT)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete)
        delete_button.pack(side=tk.LEFT)

        quit_button = tk.Button(button_frame, text="Salir", command=self.quit)
        quit_button.pack(side=tk.RIGHT)

    def populate_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        self.add_directory("", self.current_path)

    def add_directory(self, parent, path, obj = None):
        name = os.path.basename(path)
        item = self.treeview.insert(parent, "end", text=name, open=False)
        archivo = Archivo(name,path,os.path.isdir(path),item,obj)
        self.tree.add_node(archivo, obj)
        
        if os.path.isdir(path):
            for item_name in os.listdir(path):
                item_path = os.path.join(path, item_name)
                
                self.add_directory(item, item_path,archivo)

    def on_open(self, event):
        item = self.treeview.focus()
        path = self.get_item_path(item)
        if os.path.isdir(path):
            pass
            # self.treeview.delete(*self.treeview.get_children(item))
            # self.add_directory(item, path)
        else:
            print("aqui estoy perros")
            os.startfile(path)
        

    def on_select(self, event):
        item = self.treeview.focus()
        path = self.get_item_path(item)
        print("aqui estoy perros otra vez")
        if os.path.isdir(path):
            pass
            # self.treeview.delete(*self.treeview.get_children(item))
            # self.add_directory(item, path)
        else:
            print("aqui estoy perros")
            os.startfile(path)
        
        

    def get_item_path(self, item):
        path = ""
        
        text = self.treeview.item(item, "text")

        return self.tree.find_node(text,item).data.path
    
    
    def agregar(self): #Carpetas 
        item = self.treeview.focus()
        path = self.get_item_path(item)
        new_name = simpledialog.askstring("Crear Carpeta", f"Ingrese el nombre")
        if new_name:
            ruta_completa = os.path.join(path, new_name)
            try:
                os.makedirs(ruta_completa)
                self.populate_treeview()
            except OSError as error:
                messagebox.showerror("Error", f"No se pudo crear la carpeta")
                
    def agregar_archivo(self): #Archivos
        item = self.treeview.focus()
        path = self.get_item_path(item)
        new_name = simpledialog.askstring("Crear Archivo", "Ingrese el nombre")
        if new_name:
            ruta_completa = os.path.join(path, new_name)
            try:
                archivo = open(ruta_completa, "w")
                archivo.close()
                self.populate_treeview()
            except OSError as error:
                messagebox.showerror("Error", f"No se pudo crear el Archivo")
           
        

    def go_up(self):
        carpeta = filedialog.askdirectory()
        self.tree.vaciar_arbol()
        # Imprime la ruta del documento seleccionado
        self.treeview.delete(*self.treeview.get_children())
        self.add_directory("", carpeta)

    
    #tampoco funciona
    def rename(self):
        item = self.treeview.focus()
        path = self.get_item_path(item)
        

        if path:
            new_name = simpledialog.askstring("Renombrar", f"Ingrese el nuevo nombre para '{os.path.basename(path)}'")
           
            if new_name:

                new_path = os.path.join(os.path.dirname(path), new_name)
                
                try:
                    os.rename(path, new_path)
                    self.populate_treeview()

                except OSError as error:
                   
                    messagebox.showerror("Error", f"No se pudo renombrar '{os.path.basename(path)}'")

    #no funciona
    def delete(self):
        item = self.treeview.focus()
        path = self.get_item_path(item)
        if path:
            confirm = messagebox.askyesno("Eliminar", f"¿Estás seguro de que deseas eliminar '{os.path.basename(path)}'?")
            if confirm:
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)  # Elimina el directorio y su contenido
                        
                    else:
                        os.remove(path)  # Elimina el archivo
                        node = self.tree.find_node(os.path.basename(path), item)
                        self.populate_treeview()
                        self.tree.print_node()
                except OSError:
                    messagebox.showerror("Error", f"No se pudo eliminar '{os.path.basename(path)}'")

        
    def quit(self):
        self.master.quit()
        
        
        
    def copiar(self): #Archivos
        item = self.treeview.focus()
        path = self.get_item_path(item)
        self.path_copy = path
        self.is_copiar = True
    
    def cortar(self): #Archivos
        item = self.treeview.focus()
        path = self.get_item_path(item)
        self.is_copiar = False
        self.ruta_origen = path
        
    
    def pegar(self): #Archivos
        item = self.treeview.focus()
        path = self.get_item_path(item)
        if self.is_copiar:
            if os.path.isdir(path):
                try:
                    archivo_destino = os.path.join(path, os.path.basename(self.path_copy))
                    if not os.path.exists(archivo_destino):
                        shutil.copy(self.path_copy, path)
                        
                    else:
                        base_ruta = ""
                        if "." in os.path.basename(self.path_copy):
                            partes = os.path.basename(self.path_copy).split(".")
                            base_ruta = partes[0] + "_copy." + partes[1] 
                        else:
                            base_ruta = os.path.basename(self.path_copy) + "_copy"
                            
                        new_path = os.path.join(path, base_ruta)  
                        print(new_path)  
                        shutil.copy(self.path_copy, new_path)
                    self.populate_treeview()
        

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"No se pudo copiar '{os.path.basename(self.path_copy)}'")
        else:
            try:
                if os.path.dirname(self.ruta_origen) != path:
                    shutil.move(self.ruta_origen, path)
                    self.populate_treeview()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cortar '{os.path.basename(self.path_copy)}'")
            
           
    def find_archive(self):
        valor = self.entry.get()
        self.tree.print_node()
        print("origin",self.tree.find_node(valor, None))
        obj = self.tree.find_node(valor, None)
        self.tree2.print_node()
        if obj is not None:
            self.treeview.delete(*self.treeview.get_children())
            self.add_directory("",obj.data.path)
            self.tree = self.tree2

if __name__ == "__main__":
    root = tk.Tk()
    DirectoryExplorer(root)
    root.mainloop()