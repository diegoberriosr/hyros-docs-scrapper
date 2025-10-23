from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from prompts import SETUP_FLOW_PROMPT, FAQ_PROMPT, ARTICLE_TEMPLATE

class Analyzer():
  chat_model: BaseChatModel

  def __init__(self):
    self.chat_model = init_chat_model('gpt-4o', model_provider='openai')

  def process(self, article: str, is_setup_article: bool = False) -> str:
    messages = [
      SystemMessage(SETUP_FLOW_PROMPT if is_setup_article else FAQ_PROMPT),
      HumanMessage(ARTICLE_TEMPLATE.format(article=article))]

    return self.chat_model.invoke(messages).content

