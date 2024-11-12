# DIO - Bootcamp Microsoft Certification Challenge #1 - AI 102

## Análise de Documentos Anti-fraude com AzureAI

### Analisador de Cartão de Crédito com AzureAI

<br/>
Na raiz do projeto, crie um arquivo ".env" com o seguinte conteúdo:

```
ENDPOINT = "https://<YOUR_AZURE_SERVICE>.cognitiveservices.azure.com/"
SUBSCRIPTION_KEY = "<YOUR_KEY>"
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=<YOUR_ACCOUNT_NAME>;AccountKey=<YOUR_ACCOUNT_KEY>;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "<YOUR_CONTAINER_NAME>"
```

<br/>
Na pasta /src, rode o comando abaixo para instalar as dependências:

```
pip install -r requirements.txt
```
<br/>
Ainda na pasta /src, rode o comando abaixo para iniciar a aplicação:

```
streamlit run ./app.py
```
