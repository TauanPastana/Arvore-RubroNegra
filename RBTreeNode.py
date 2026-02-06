# RBTreeNode.py
BLACK = True
RED = False

class RBTreeNode:
    # construtor do nó
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = RED

    # representação do nó como string
    def __str__(self):
        cor = "BLACK" if self.color == BLACK else "RED"
        return f"{self.key}\t{cor}"

    # retorna o avô do nó
    def avo(self):
        return self.parent.parent if self.parent is not None else None

    # retorna o tio do nó
    def tio(self):
        avo = self.avo()
        if avo is None:
            return None

        # se o pai for filho esquerdo, tio é o filho direito e vice-versa
        if avo.left is self.parent:
            return avo.right
        if avo.right is self.parent:
            return avo.left
        return None

    def paiVermelho(self):
        # corrigido: era "self.parentcolor" no seu código
        return self.parent is not None and self.parent.color == RED

    # método para saber se é folha
    def Isfolha(self) -> bool:
        return self.left is None and self.right is None

    # método responsável por recolorir o nó
    def recolorir(self):
        self.color = BLACK if self.color == RED else RED

    # helper: troca 'self' por 'novo' na ligação com o pai (ou vira raiz)
    def _substituirNoPai(self, tree, novo):
        if self.parent is None:
            tree.root = novo
        else:
            if self.parent.left is self:
                self.parent.left = novo
            else:
                self.parent.right = novo

        if novo is not None:
            novo.parent = self.parent

    def rotacaoEsquerda(self, tree):
        pivô = self.right
        if pivô is None:
            return self

        # 1) subárvore do meio sobe para a direita do self
        self.right = pivô.left
        if pivô.left is not None:
            pivô.left.parent = self

        # 2) pivô ocupa o lugar do self (no pai ou na raiz)
        self._substituirNoPai(tree, pivô)

        # 3) self desce para a esquerda do pivô
        pivô.left = self
        self.parent = pivô

        return pivô

    def rotacaoDireita(self, tree):
        pivô = self.left
        if pivô is None:
            return self

        # 1) subárvore do meio sobe para a esquerda do self
        self.left = pivô.right
        if pivô.right is not None:
            pivô.right.parent = self

        # 2) pivô ocupa o lugar do self (no pai ou na raiz)
        self._substituirNoPai(tree, pivô)

        # 3) self desce para a direita do pivô
        pivô.right = self
        self.parent = pivô

        return pivô
