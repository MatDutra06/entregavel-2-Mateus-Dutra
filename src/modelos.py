import cv2

class Deteccao:   #classe de desenhar nas imagens
    def __init__(self,id,xmin,ymin,xmax,ymax):              
        self.id = id
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def desenhar(self,imagem): #metodo para desenhar o retangulo
        if self.id == 1:
            cv2.rectangle(imagem,(self.xmin,self.ymin),(self.xmax,self.ymax),(0,255,0))
        else:
            cv2.rectangle(imagem,(self.xmin,self.ymin),(self.xmax,self.ymax),(255,0,0))  


class ImagemAnotada:
    def __init__(self,nome_imagem):
        self.imagem = nome_imagem
        self.lista = []
        

    def add_deteccao(self,objeto_de_deteccao):
        self.lista.append(objeto_de_deteccao)


    def guardar_imagem(self,imagem):
        copia = imagem.copy()
        for lt in self.lista:
            lt.desenhar(self.lista)
        return copia

    def __len__(self):   #numero de dados de cada imagem
        return len(self.lista)