from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config


def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)

        document_client = DocumentIntelligenceClient(
            endpoint=Config.ENDPOINT,
            credential=credential
        )

        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
        )

        result = card_info.result()

        print('result: ',result)
        
        for document in result.documents:
            fields = document.get("fields", {})

            return {
                "card_name": fields.get("CardHolderName", {}).get("content"),
                "card_number": fields.get("CardNumber", {}).get("content"),
                "expiry_date": fields.get("ExpirationDate", {}).get("content"),
                "bank_name": fields.get("IssuingBank", {}).get("content"),
            }

    except Exception as e:
        print(f"Erro ao analisar o cartão de crédito: {e}")
        return None
