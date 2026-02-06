# RBTreeNode.py

BLACK = True
RED = False


class RBTreeNode:
    def __init__(self, key, parent=None, left=None, right=None, color=RED):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def __str__(self):
        cor = "BLACK" if self.color == BLACK else "RED"
        return f"{self.key}\t{cor}"

    # atalhos de navegação
    @property
    def avô(self):
        return self.parent.parent if self.parent else None

    @property
    def tio(self):
        avô = self.avô
        if not avô:
            return None
        return avô.right if avô.left is self.parent else avô.left

    @property
    def é_folha(self) -> bool:
        return self.left is None and self.right is None

    def recolorir(self):
        self.color = BLACK if self.color == RED else RED

    def _substituir_no_pai(self, tree, novo):
        if self.parent is None:
            tree.root = novo
        else:
            if self.parent.left is self:
                self.parent.left = novo
            else:
                self.parent.right = novo
        if novo is not None:
            novo.parent = self.parent

    def rotacao_esquerda(self, tree):
        pivo = self.right
        if pivo is None:
            return self

        self.right = pivo.left
        if pivo.left:
            pivo.left.parent = self

        self._substituir_no_pai(tree, pivo)
        pivo.left = self
        self.parent = pivo
        return pivo

    def rotacao_direita(self, tree):
        pivo = self.left
        if pivo is None:
            return self

        self.left = pivo.right
        if pivo.right:
            pivo.right.parent = self

        self._substituir_no_pai(tree, pivo)
        pivo.right = self
        self.parent = pivo
        return pivo
