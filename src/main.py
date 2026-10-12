import cv2
from arquivos import ler_anotacoes #importa a funcao dos arquivos.py



def teclas():
    while True:
        print("Para fechar as janelas,basta pressionar a tecla q e para avançar basta apertar espaço.")
        tecla = cv2.waitKey(0) & 0xFF
        if tecla == ord("q"):
            cv2.destroyAllWindows()
            return True
        if tecla == ord(" "):
            break


def tratamento_erros(nome,arg,anotacao):


    if arg is None:
        print(f"Erro ao carregar imagem {nome}")
        raise SystemExit(1)

    altura , largura = arg.shape[:2]

    for teste in anotacao.lista:

        if teste.xmin >= teste.xmax or teste.xmax >= largura or teste.xmin <0:
            print("Erro: Valores invalidos")
            raise SystemExit(1)
        if teste.ymin >= teste.ymax or teste.ymax >= altura or teste.ymin < 0:
            print("Erro: Valores invalidos")
            raise SystemExit(1)


def main():

    imagens = ler_anotacoes("dados/anotacoes.csv")

    print(f"Ha {len(imagens)} imagens para serem analisadas")

    for nome in sorted(imagens):  #iterando cada nome de chave de imagem
        arg = cv2.imread(f"imagens/{nome}") #le a imagem
        
        tratamento_erros(nome,arg,imagens[nome]) #chama funcao para tratar erros

        print(f"Nesta imagem {nome},existem {len(imagens[nome])} caixinhas")

        arg2 = imagens[nome].gerar_imagem(arg) # desenha a nova imagem

        cv2.putText(arg2,text = "ID 1= vermelho , ID 0 = azul",org=(250,30),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0,255,0),thickness = 2)

        cv2.imwrite(f"resultados/{nome}",arg2)

        if not cv2.imwrite(f"resultados/{nome}",arg2):

            print("Erro: Nao foi possivel salvar imagem")
         
        cv2.imshow(nome, arg2) #mostra imagens alteradas

        if teclas():
            break
        else: continue
       
        
if __name__ == "__main__": #checa se a execucao e na main
    main()    