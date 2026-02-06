from RBTreeNode import RBTreeNode

BLACK = True
RED   = False

class RBTree:

    def __init__(self):
        self.root = None


    def __str__(self):
        # Mostra a estrutura (mais útil para depurar)
        return self.pretty()

    # Mantém a sua impressão "em ordem" (in-order), só renomeei
    def inorder(self, node=None):
        if node is None:
            node = self.root
        return self._inorder(node)

    def _inorder(self, node):
        if node is None:
            return ''
        result = ''
        if node.left is not None:
            result += self._inorder(node.left)
        result += node.__str__() + '\n'
        if node.right is not None:
            result += self._inorder(node.right)
        return result

    # NOVO: imprime a árvore com estrutura
    def pretty(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return '<árvore vazia>\n'
        return self._pretty(node, prefix='', is_left=None)

    def _pretty(self, node, prefix='', is_left=None):
        if node is None:
            return ''

        # Conector do nó atual
        if is_left is None:
            connector = ''          # raiz
        else:
            connector = '├── ' if is_left else '└── '

        # Rótulo do nó (valor + cor)
        color = 'B' if node.color else 'R'  # no seu código: BLACK=True, RED=False [file:2]
        line = f"{prefix}{connector}{node.key}({color})\n"

        # Prefixo para os filhos (mantém as barras verticais alinhadas)
        child_prefix = prefix
        if is_left is None:
            child_prefix += ''
        else:
            child_prefix += '│   ' if is_left else '    '

        # Para ficar mais “natural” ao ler de cima pra baixo:
        # imprime primeiro o filho esquerdo (se existir) e depois o direito
        left_part = self._pretty(node.left,  child_prefix, True)  if node.left  is not None else ''
        right_part = self._pretty(node.right, child_prefix, False) if node.right is not None else ''
        return line + left_part + right_part
        
        
    def insert(self, key, node:RBTreeNode):
        
            
        # se a arvore não estiver vazia #
        if node is not None:
            # se for folha #
            if node.Isfolha():
                
                # cria um novo nó #
                newNode = RBTreeNode( key, parent=node)

                # define se é filho direito ou esquerdo #
                if key > node.key:
                    node.right = newNode
                elif key < node.key:
                    node.left = newNode
                
                self.corrigir(newNode)
                return True

            # se tiver filho direito #

            if key > node.key:
                if node.right == None:
                    newNode = RBTreeNode(key, node)
                    node.right = newNode
                    self.corrigir(newNode)  
                    return True
                else:
                    return self.insert(key, node.right)
            if key < node.key:
                if node.left == None:
                    newNode = RBTreeNode(key, node)
                    node.left = newNode
                    self.corrigir(newNode)  
                    return True
                else:
                    return self.insert(key, node.left)
         
            
            
                
            

        # se a arvore estiver vazia #
        else:
                # cria um novo nó #
                self.criarNo(key)
                return True
        
    
    def criarNo(self, key, parent=None):
        newNode = RBTreeNode(key, parent)
        self.root = newNode
        self.corrigir(newNode)
        
        return True
    

    def nodesisRED(self, node):
        return node.parent.color == RED 

    def corrigir(self, node):


        
            
        
        # caso 1 #
        if node.parent is None:
            node.color = BLACK
        
        # caso 2 #
        else:
            avo = node.avo()
            tio = node.tio()
            pai = node.parent

            if pai.color == BLACK:
                return True

            if tio != None and tio.color == RED:
                pai.color = BLACK
                avo.color = RED
                tio.color = BLACK

                self.corrigir(avo)
            
            # caso 3 #
            else:

                # subcaso 1 (LL): pai é filho esquerdo do avô e node é filho esquerdo do pai
                    if avo.left == pai and node == pai.left:
                        if avo.color == BLACK and pai.color == RED:
                            pai.recolorir()
                            avo.recolorir()

                            novoTopo = avo.rotacaoDireita(self)
                            return True
                           

                    # subcaso 2 (RR): pai é filho direito do avô e node é filho direito do pai
                    elif avo.right == pai and node == pai.right:
                        if avo.color == BLACK and pai.color == RED:
                            pai.recolorir()
                            avo.recolorir()

                            novoTopo = avo.rotacaoEsquerda(self)
                            return True
                            

                    # subcaso 3 (RL): pai é filho direito do avô e node é filho esquerdo do pai
                    elif avo.right == pai and node == pai.left:
                        if avo.color == BLACK and pai.color == RED:
                            # 1) rotaciona à direita no pai
                            pai.rotacaoDireita(self)

                            # 2) rotaciona à esquerda no avô (retorna o novo topo)
                            novoTopo = avo.rotacaoEsquerda(self)

                            # 3) recoloração correta pós-rotação dupla
                            novoTopo.color = BLACK
                            if novoTopo.left is not None:
                                novoTopo.left.color = RED
                            if novoTopo.right is not None:
                                novoTopo.right.color = RED

                            return True

                    # subcaso 4 (LR): pai é filho esquerdo do avô e node é filho direito do pai
                    elif avo.left == pai and node == pai.right:
                        if avo.color == BLACK and pai.color == RED:
                            # 1) rotaciona à esquerda no pai
                            pai.rotacaoEsquerda(self)

                            # 2) rotaciona à direita no avô
                            novoTopo = avo.rotacaoDireita(self)

                            # 3) recoloração correta pós-rotação dupla
                            novoTopo.color = BLACK
                            if novoTopo.left is not None:
                                novoTopo.left.color = RED
                            if novoTopo.right is not None:
                                novoTopo.right.color = RED

                            return True

                    # self.corrigir(pai)
