import cv2
import csv

class Deteccao:   #classe de desenhar nas imagens
    def __init__(self,id,xmin,ymin,xmax,ymax):              
        self.id = id
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def desenhar(self,imagem): #metodo para desenhar o retangulo
        cv2.rectangle(imagem,(self.xmin,self.ymin),(self.xmax,self.ymax)) 



class ImagemAnotada: