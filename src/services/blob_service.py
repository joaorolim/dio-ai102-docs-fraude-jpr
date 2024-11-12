import os
import streamlit as st
from utils.Config import Config
from azure.storage.blob import BlobServiceClient

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        # st.write(f"Arquivo {file_name} enviado com sucesso para o Azure Blob Storage!")
        return blob_client.url
    except Exception as e:
        st.write(f"Erro ao enviar o arquivo {file_name} para o Azure Blob Storage: {e}")
        return None