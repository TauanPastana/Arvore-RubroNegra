# RBTree.py
from RBTreeNode import RBTreeNode, BLACK, RED


class RBTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.pretty()

    # ---------------- Impressão ---------------- #

    def inorder(self, node=None):
        if node is None:
            node = self.root
        return self._inorder(node)

    def _inorder(self, node):
        if node is None:
            return ""
        return (
            self._inorder(node.left)
            + str(node) + "\n"
            + self._inorder(node.right)
        )

    def pretty(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return "<árvore vazia>\n"
        return self._pretty(node, prefix="", is_left=None)

    def _pretty(self, node, prefix="", is_left=None):
        if node is None:
            return ""

        if is_left is None:
            connector = ""
        else:
            connector = "├── " if is_left else "└── "

        color = "B" if node.color == BLACK else "R"
        line = f"{prefix}{connector}{node.key}({color})\n"

        child_prefix = prefix
        if is_left is not None:
            child_prefix += "│ " if is_left else "  "

        left_part = self._pretty(node.left, child_prefix, True)
        right_part = self._pretty(node.right, child_prefix, False)
        return line + left_part + right_part

    # ---------------- Busca / mínimo ---------------- #

    def busca(self, key, node=None):
        if node is None:
            node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    def minimo(self, node):
        while node.left:
            node = node.left
        return node

    # ---------------- Inserção ---------------- #

    def insert(self, key, node=None):
        if self.root is None:
            self.root = RBTreeNode(key, color=BLACK)
            return True

        if node is None:
            node = self.root

        # busca posição
        atual = node
        pai = None
        while atual:
            pai = atual
            if key == atual.key:
                return False
            atual = atual.left if key < atual.key else atual.right

        novo = RBTreeNode(key, parent=pai)
        if key < pai.key:
            pai.left = novo
        else:
            pai.right = novo

        self._corrigir_insercao(novo)
        return True

    def _corrigir_insercao(self, node):
        while node.parent and node.parent.color == RED:
            avô = node.avô
            tio = node.tio
            pai = node.parent

            # caso tio vermelho: recolore e sobe
            if tio and tio.color == RED:
                pai.color = BLACK
                tio.color = BLACK
                avô.color = RED
                node = avô
                continue

            # casos 3 (rotações)
            if avô.left is pai:
                if node is pai.right:
                    # LR
                    pai.rotacao_esquerda(self)
                    node = pai
                    pai = node.parent
                # LL
                pai.recolorir()
                avô.recolorir()
                avô.rotacao_direita(self)
            else:
                if node is pai.left:
                    # RL
                    pai.rotacao_direita(self)
                    node = pai
                    pai = node.parent
                # RR
                pai.recolorir()
                avô.recolorir()
                avô.rotacao_esquerda(self)
            break

        self.root.color = BLACK

    # ---------------- Remoção ---------------- #

    def _transplantar(self, u, v):
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent
    # remoção da arvore binária de busca (normaj)
    def removeABB(self, z):
        """Remove z como numa ABB. Retorna (x, pai_x)."""
        if z.left is None:
            x = z.right
            pai_x = z.parent
            self._transplantar(z, z.right)
        elif z.right is None:
            x = z.left
            pai_x = z.parent
            self._transplantar(z, z.left)
        else:
            y = self.minimo(z.right)
            x = y.right
            pai_x = y if y.parent is z else y.parent

            if y.parent is not z:
                self._transplantar(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplantar(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        return x, pai_x

    def _irmão(self, x, pai_x):
        if not pai_x:
            return None
        return pai_x.right if x is pai_x.left else pai_x.left

    @staticmethod
    def _é_preto(node):
        return node is None or node.color == BLACK

    @staticmethod
    def _é_vermelho(node):
        return node is not None and node.color == RED

    def _corrigir_remocao(self, x, pai_x):
        while x is not self.root and self._é_preto(x):
            x_esq = pai_x and x is pai_x.left
            w = pai_x.right if x_esq else pai_x.left

            filho_perto = w.left if x_esq else w.right if w else None
            filho_longe = w.right if x_esq else w.left if w else None

            # caso 1: irmão vermelho
            if self._é_vermelho(w):
                w.color = BLACK
                pai_x.color = RED
                if x_esq:
                    pai_x.rotacao_esquerda(self)
                else:
                    pai_x.rotacao_direita(self)
                w = pai_x.right if x_esq else pai_x.left
                filho_perto = w.left if x_esq else w.right if w else None
                filho_longe = w.right if x_esq else w.left if w else None

            # caso 2: irmão preto e filhos pretos
            if self._é_preto(filho_perto) and self._é_preto(filho_longe):
                if w:
                    w.color = RED
                x = pai_x
                pai_x = x.parent
                continue

            # caso 3: irmão preto, filho perto vermelho, filho longe preto
            if self._é_vermelho(filho_perto) and self._é_preto(filho_longe):
                filho_perto.color = BLACK
                w.color = RED
                if x_esq:
                    w.rotacao_direita(self)
                else:
                    w.rotacao_esquerda(self)
                w = pai_x.right if x_esq else pai_x.left
                filho_perto = w.left if x_esq else w.right if w else None
                filho_longe = w.right if x_esq else w.left if w else None

            # caso 4: irmão preto e filho longe vermelho
            if self._é_vermelho(filho_longe):
                w.color = pai_x.color
                pai_x.color = BLACK
                filho_longe.color = BLACK
                if x_esq:
                    pai_x.rotacao_esquerda(self)
                else:
                    pai_x.rotacao_direita(self)
                x = self.root
                break

        if x:
            x.color = BLACK

    def remover(self, key):
        z = self.busca(key)
        if z is None:
            return False

        if z.color == RED:
            self.removeABB(z)
            return True

        # nó preto: seguir casos de remoção RB
        # decide y, x (como no seu código, mas com menos duplicação)
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.minimo(z.right)

        x, pai_x = self.removeABB(z)
        y_vermelho = (y.color == RED)

        # proc. 1: z tinha dois filhos e y vermelho
        if z.left and z.right and y_vermelho:
            y.color = BLACK
            return True

        self._corrigir_remocao(x, pai_x)
        return True
