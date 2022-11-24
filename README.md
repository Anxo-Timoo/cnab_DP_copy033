# cnab_DP_copy033

Estes script foi criado por José Marins para realizar a cópia de arquivos do Departamento Pessoal da BRQ para a VAN( CISA ) do santander.
O script foi escrito em python

JIRA:SISAP-279

TÍTULO:Criação de programa para envio de pgtos DP Automático
Descrição

Bom dia, Marcelo.

Por favor, solicitamos criar um programa/aplicação no SAP para que o DP faça a transmissão dos arquivos de pagamento de forma automática.

1 - Salvar o arquivo TXT em uma pasta da rede que só eles terão acesso;

2 - JOB pegue a pasta e transmita para o Banco Santander;

3 - JOB pegue o retorno do banco e salve em outra pasta para conferência e validação.

Se precisar de qualquer informação adicional, só chamar! 

Aguardamos e agradecemos.

![image](https://user-images.githubusercontent.com/114781613/203681159-13c7f6e8-9455-416b-8056-d0ec6472c38c.png)
1) Pegar um arquivo teste de cnab e inserir no diretório: “  I:\usr\sap\INTERFACE\FDTA\CNAB_FOLHA_DP  “
2) o arquivo será movido por um script executavel "Santander_outbound_Folha.bat", o qual roda de 5 em 5 minutos.
   Nessa etapa o arquivo é enviado para o banco Santander para ser processado.

   Caminho de entrada da VAn do Santander:  C:\Santander\AFTData\OUTBOX\GE204963
   ![image](https://user-images.githubusercontent.com/114781613/203681385-3f7c6707-db52-40fa-b35b-d4bf57110590.png)
4) apos ser processado pelo banco o arquivo será entregue na pasta abaixo:
Obs: Este processo pode levar em torno de 15 minutos apos o envio do arquivo.
5) o arquivo apos processado pelo banco e já constando na pasta "INBOX" será processado pelo programa CNAB.py e será direcionado para a pasta do cliente.
Aqui no caso do teste em QAS210:   "C:\Santander\retorno_arquivo"
