from openai import AzureOpenAI
from app.config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT_NAME


class AzureOpenAIClient:
  def __init__(self):
    self.client = AzureOpenAI(
      api_key=AZURE_OPENAI_API_KEY,
      azure_endpoint=AZURE_OPENAI_ENDPOINT,
      api_version=AZURE_OPENAI_API_VERSION
    )
    self.development_name = AZURE_OPENAI_DEPLOYMENT_NAME


  def generate_message_with_conversation(self, messages) -> str:
    response = self.client.chat.completions.create(
      model=self.development_name,
      messages=messages
    )
    return response.choices[0].message.content or ''