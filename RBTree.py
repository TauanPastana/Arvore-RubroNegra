from RBTreeNode import RBTreeNode

BLACK = True
RED   = False

class RBTree:

    def __init__(self):
        self.root = None


    def __str__(self):
        return self.printTree(self.root)

    def printTree(self, node):
        if node is None:
            return ''
        
        result = ''
        if node.left is not None:
            result += self.printTree(node.left)

        result += node.__str__() + '\n'

        if node.right is not None:
            result += self.printTree(node.right)
        
        return result
        
        
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
                
                # self.corrigir(newNode)
                return True

            # se tiver filho direito #

            if key > node.key:
                if node.right == None:
                    newNode = RBTreeNode(key, node)
                    node.right = newNode
                    return True
                else:
                    return self.insert(key, node.right)
            if key < node.key:
                if node.left == None:
                    newNode = RBTreeNode(key, node)
                    node.left = newNode
                    return True
                else:
                    return self.insert(key, node.left)
            # if node.right != None:
                
            #     # compara o valor das chaves #
            #     if key > node.key:
            #         return self.insert( key, node.right)
                

            # # se tiver filho esquerdo #
            # if node.left != None:
                
            #     # compara o valor das chaves #
            #     if key < node.key:
            #         return self.insert( key, node.left)
            
            
                
            

        # se a arvore estiver vazia #
        else:
                # cria um novo nó #
                self.criarNo(key)
                # self.corrigir(newNode)
                return True
        
    
    def criarNo(self, key, parent=None):
        newNode = RBTreeNode(key, parent)
        self.root = newNode
        return True
        

    def corrigir(self, node):
        # caso 1 #
        if node.parent is None:
            node.color = BLACK
        
        # caso 2 #
        else:
            avo = node.avo()
            tio = node.tio()
            pai = node.parent

            if tio != None and tio.color == RED:
                pai.color = BLACK
                avo.color = RED
                tio.color = BLACK

                self.corrigir(avo)
            
            # caso 3 #
            else:

                # subcaso 1 #
                
                # Caso o nó inserido seja filho esquerdo e o pai do nó também seja filho esquerdo
                
                if avo is not None:
                    if avo.left == pai and node == pai.left:
                        
                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # faz-se uma rotação a direita
                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoDireita()
                                else:
                                    avo.parent.right = pai.rotacaoDireita()
                            else:
                                self.root = pai.rotacaoEsquerda()
                            

                    # subcaso 2 #

                    # Caso o nó inserido seja filho direito e o pai do nó também seja filho direito
                    elif avo.right == pai and node == pai.right:
                        
                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # faz-se uma rotação a esquerda
                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoEsquerda()
                                else:
                                    avo.parent.right = pai.rotacaoEsquerda()
                            else:
                                self.root = pai.rotacaoEsquerda()

                    # subcaso 3 #

                    # Caso o nó inserido seja filho esquedro e o pai seja filho direito   
                    elif avo.right == pai and node == pai.left:

                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            # pai.recolorir()
                            # avo.recolorir()

                            # realiza-se uma rotação simples a direita
                            avo.right = node.rotacaoDireita()

                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoEsquerda()
                                else:
                                    avo.parent.right = pai.rotacaoEsquerda()
                            else:
                                self.root = pai.rotacaoEsquerda()

                    # subcaso 4 #

                    # Caso o nó inserido seja filho esquedro e o pai seja filho direito   
                    elif avo.left == pai and node == pai.right:

                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            # pai.recolorir()
                            # avo.recolorir()

                            # realiza-se uma rotação simples a esqueda
                            avo.left = node.rotacaoEsquerda()

                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoDireita()
                                else:
                                    avo.parent.right = pai.rotacaoDireita()
                            else:
                                self.root = pai.rotacaoDireita()
                self.corrigir(pai)