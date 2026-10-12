import csv
from modelos import Deteccao, ImagemAnotada

def ler_anotacoes(caminho):

     try:

        with open(caminho,encoding = "utf-8",newline="") as arquivo1:            #tabela de dados sobre retangulos nas imagens
            
            leitor1 = csv.DictReader(arquivo1,delimiter = ',')  # leitura dos dados
        
            imagens = {}

            for linha in leitor1:
                check = True
                nome = linha["imagem"]

                if nome not in imagens:
                    imagens[nome] = ImagemAnotada(nome)
        
                objeto = Deteccao(int(linha["classe_id"]),int(linha["x_min"]),int(linha["y_min"]),int(linha["x_max"]),int(linha["y_max"]))
                imagens[nome].add_deteccao(objeto)

     except FileNotFoundError:
          print("Erro : Arquivo csv invalido")
          raise(SystemExit(1))

     return imagens
