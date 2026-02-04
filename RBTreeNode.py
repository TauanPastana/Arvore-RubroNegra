

BLACK = True
RED   = False

class RBTreeNode:

    # construtor do nó #
    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.color = RED
        
        self.key = key

    # representação do nó como uma string #
    def __str__(self):
        if self.color == BLACK:
            return str(self.key) + '\tBLACK'
        else:
            return str(self.key) + '\tRED'


    # retorna o avo do nó #
    def avo(self):
        if self.parent != None:
            return self.parent.parent
        return None

    # retorna o tio do nó #
    def tio(self):
        # se o avo existir #
        if self.avo() != None:

            # se o pai for filho esquerdo #
            if self.avo().left == self.parent: # type: ignore
                
                # retorna o filho direito #
                return self.avo().right  # type: ignore

            # se o pai for o filho direito #
            elif self.avo().right == self.parent: #type:ignore

                # retorna o filho esquerdo #
                return self.avo().left
        
        
        return None


    # metodo para saber se é folha
    def Isfolha(self) -> bool:
        return self.left == None and self.right == None

    # método resposável por recolorir o nó #
    def recolorir(self):
        if self.color == RED:
            self.color = BLACK
        else:
            self.color = RED

    def rotacaoDireita(self):
        self.parent.right = self.left
        
        if self.left is not None:
            self.left.parent = self.parent
        
        self.left = self.parent
        self.parent = self.left.parent
        self.left.parent = self
        
        return self

    def rotacaoEsquerda(self):
        self.parent.left = self.right
        
        if self.right is not None:
            self.right.parent = self.parent
        
        self.right = self.parent
        if self.right is not None:
            self.parent = self.right.parent
        else:
            self.parent = None
        self.right.parent = self

        return self