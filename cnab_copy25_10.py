import os
import os.path
import shutil
from pathlib import Path
import datetime

data=datetime.datetime.now()
datahoje=(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
#print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
#print(data)
#print(datahoje)
#print(data.strftime("%d/%m/%y"))
print(data.strftime("%d/%m/%y"))

#ler todos os arquivos do diretorio
#Origem
#caminho = "C://TESTE1/Santander/Enviadosoutbox"

#Diretorio de Producao
caminho = "//SRV19270/AFTData/INBOX/GE204963"
#caminho = "\\SRV19270\AFTData\INBOX\GE204963"

#Caminho QAS210
#caminho = "C://Santander/enviar_arquivo/"

#Linha 18
#Destino
#caminho_destino = "C://TESTE1/Santander/Movidos/"
#caminho_destino = "C://TESTE1/Santander/Movidos/"
caminho_destino = "C://Santander/retorno_arquivo/"

lista_arquivos = os.listdir(caminho)
#print(lista_arquivos)
#linha 25
qtd_arquivos = 1
dir = caminho
for path in os.listdir(dir):
    nomearquivo = os.listdir(dir)
    if os.path.isfile(os.path.join(dir, path)):
      
        
#        print("Quantidade de arquivos dentro do diretóio = ",qtd_arquivos)
#        print("o nome do arquivo é = ", path)
        with open((os.path.join(dir, path)), 'r') as arquivo:
            texto = arquivo.readlines()
#            print(texto)
        # verificar se existe a palavra "salario dentro do arquivo                     
        for frase in texto:
#linha 40            
#            if "YL-PAGAMENTO SALARIOS" and (data.strftime("%d/%m/%y")) in frase:
			
		    If "FERNANDA" and (data.strftime("%d/%m/%y")) in frase:
#            if "YL-PAGAMENTO SALARIOS" in frase:
              #concatenar o diretorio com o nome do arquivo 
                df=os.path.join(caminho, path)
#                print(df,  "nome e diretorio do arquivo na pasta")
                
#                Path(os.path.join(dir, path).touch()
#               shutil.copy((os.path.join(dir, path), 'C:\TESTE1\\Santander\\Copiados\\cnab_new23.txt')
#                Path(r"C:\TESTE1\\Santander\\Enviadosoutbox\\SAL_M4NM_08_300922P_REL.txt").touch()
                Path(df).touch()
                shutil.copy(df, caminho_destino)
#Linha 53
#                shutil.copy(r"C:\TESTE1\\Santander\\Enviadosoutbox\\SAL_M4NM_08_300922P_REL.txt", 'C:\TESTE1\\Santander\\Copiados\\cnab_new.txt')
#        print(frase)
#                print("Path é = ", path)
#        print(caminho_destino) 
        #else:
#                print('Não consta a palavra salario')
    qtd_arquivos += 1
       
