class NaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

class NaryTree(object):
    def __init__(self):
        self.root=  None
        
    def add_node(self, data, parent=None):
        new_node = NaryTreeNode(data)
        if parent is None:
            self.root = new_node
        else:
             for node in self._find_node(parent.name,parent.id, self.root):
                node.children.append(new_node)
                
    
    def _find_node(self, data,id, current_node):
        nodes = []
        if id == None:
            current_node.data.id = None
        if current_node.data.name == data and current_node.data.id == id:
            nodes.append(current_node)
        for child in current_node.children:
             nodes += self._find_node(data,id, child)
        return nodes

    def find_node(self, data,id):
        
        nodes = self._find_node(data,id, self.root)
        if nodes:
             return nodes[0]
        return None

 
        

    def _eliminar_nodos(self, arbol, nodo):
        # Verificar si el nodo es la raíz del árbol
        if arbol == nodo:
            arbol = None
            return

        # Buscar el nodo en los hijos del padre
        padre = None
        for hijo in arbol.children:
            if hijo == nodo:
                padre = arbol
                break

        # Si se encontró el nodo en los hijos del padre
        if padre:
            padre.children.remove(hijo)
        else:
            # Si no se encontró en los hijos directos, buscar recursivamente en los hijos de los hijos
            for hijo in arbol.children:
                self._eliminar_nodo(hijo, nodo)
                
    
    def eliminar_nodo(self, nodo):
        self._eliminar_nodos(self.root, nodo)
    

    
    def _print_node(self, node, altura = 0):
        print((altura*"--")+str(node.data.name)+str(node.children))
        for node_children in node.children:
            self._print_node(node_children,altura + 1) #la altura afuera se mantiene constante
        
    
    def print_node (self):
        self._print_node(self.root)
        
        
class Archivo(object):
    def __init__(self, name,path,isDir,id,father=None):
       self.name = name
       self.path = path
       self.father = father
       self.isDir = isDir
       self.id = id
        
          
       
        
        
        