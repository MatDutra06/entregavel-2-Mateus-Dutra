import cv2
from arquivos import ler_anotacoes #importa a funcao dos arquivos.py



def teclas():
    while True:
        print("Para fechar as janelas,basta pressionar a tecla q e para avançar basta apertar espaço.")
        tecla = cv2.waitKey(0) & 0xFF
        if tecla == ord("q"):
            cv2.destroyAllWindows
            return True
        if tecla == ord(" "):
            break


def tratamento_erros(nome,argumento,anotacao):
    pass





def main():

    imagens = ler_anotacoes("dados/anotacoes.csv")

    print(f"Ha {len(imagens)} imagens para serem analisadas")

    for nome in sorted(imagens):  #iterando cada nome de chave de imagem
        arg = cv2.imread(f"imagens/{nome}") #le a imagem
        
        print(f"Nesta imagem,existem {len(imagens[nome])} caixinhas")

        if arg is None:
            print(f"Erro ao carregar imagem {nome}")
            raise SystemExit(1)
        
        arg2 = imagens[nome].gerar_imagem(arg) # desenha a nova imagem

        altura , largura = arg.shape[:2]

        for teste in imagens[nome].lista:

            if teste.xmin >= teste.xmax or teste.xmax >= largura or teste.xmin <0:
                print("Erro: Valores invalidos")
                raise SystemError(1)
            if teste.ymin >= teste.ymax or teste.ymax >= altura or teste.ymin < 0:
                print("Erro: Valores invalidos")
                raise SystemError(1)

        cv2.imwrite(f"resultados/{nome}",arg2)

        if not cv2.imwrite(f"resultados/{nome}",arg2):

            print("Erro: Nao foi possivel salvar imagem")
         
        cv2.imshow(nome, arg2) #mostra imagens alteradas

        if teclas():
            break
        else: continue
       
        
if __name__ == "__main__": #checa se a execucao e na main
    main()    