from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import get_value_from_api
def analyze_sentiment(text):
    endpoint = get_value_from_api('text_analytics_endpoint')
    key = get_value_from_api('text_analytics_key')
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

    response = client.analyze_sentiment(documents=[text])

    sentiment = response[0].sentiment
    confidence_scores = response[0].confidence_scores

    print('Sentiment:', sentiment)
    print('Positive score:', confidence_scores.positive)
    print('Negative score:', confidence_scores.negative)
    print('Neutral score:', confidence_scores.neutral)
