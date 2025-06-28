from openai import AzureOpenAI
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT_NAME


client = AzureOpenAI(
  azure_ad_token=AZURE_OPENAI_API_KEY,
  azure_endpoint=AZURE_OPENAI_ENDPOINT,
  api_version=AZURE_OPENAI_API_VERSION
)

development_name = AZURE_OPENAI_DEPLOYMENT_NAME


def generate_text_with_conversation(messages) -> str | None:
  response = client.chat.completions.create(
    model=development_name,
    messages=messages
  )
  return response.choices[0].message.content