import csv
#Abertura das tabelas
with (open("dados/anotacoes.csv",encoding = "utf-8",newline="") as arquivo1,            #tabela de dados sobre retangulos nas imagens
     open("dados/mapeamento_imagens.csv",encoding = "utf-8",newline="") as arquivo2)    :   #tabela de dados sobre tamanhos das imagens
   
    leitor1 = csv.DictReader(arquivo1,delimiter = ',')  # leitura dos dados
    leitor2 = csv.DictReader(arquivo2,delimiter = ',')  




    
   