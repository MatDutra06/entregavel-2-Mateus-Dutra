import csv
import cv2
with open("dados/anotacoes.csv",encoding = "utf-8",newline ="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=",")
     # lista de dicionários



imagem = cv2.imread('imagens/cena_01_parque.jpg')
if imagem is None:
    print('Erro ao carregar imagem')
else:
    cv2.imshow('Minha janela do open cv',imagem)

    tecla = cv2.waitKey(0) & 0xFF
    if tecla == ord("q"):
        cv2.destroyAllWindows

    