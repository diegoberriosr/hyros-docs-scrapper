from scrapper import Scrapper
from analyzer import Analyzer
from transformer import Transformer

import os


class ScrappingAssistant():
  scrapper: Scrapper
  analyzer: Analyzer
  transformer: Transformer


  def __init__(self):
    self.scrapper = Scrapper()
    self.analyzer = Analyzer()
    self.transformer = Transformer()


  def getArticles(self, articles: dict):
    counter = 0

    for article_name in articles:
      progress = counter / len(articles) * 100
      print(f"Processing articles... ({progress}%)")
      print(f"Current article: {article_name}")

      article = articles[article_name]
      self.getArticle(article, article_name) # use the key as the filename
      counter += 1

      os.system('clear || cls')

    print("Done!")

  def getArticle(self, article, output_filename: str):
    url = article['url']
    is_flow = article['is_flow']

    page_source = self.scrapper.scrape(url)
    processed_text = self.analyzer.process(page_source, is_flow)

    self.transformer.convert_to_pdf(processed_text, output_filename)