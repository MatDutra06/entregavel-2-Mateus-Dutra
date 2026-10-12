import cv2
from arquivos import ler_anotacoes


def main():
    imagens = ler_anotacoes("dados/anotacoes.csv")

    test = cv2.imread() 