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

      url = articles[article_name]
      self.getArticle(url, article_name) # use the key as the filename
      counter += 1

      os.system('clear || cls')

    print("Done!")

  def getArticle(self, url: str, output_filename: str):
    page_source = self.scrapper.scrape(url)
    processed_text = self.analyzer.process(page_source)

    self.transformer.convert_to_pdf(processed_text, output_filename)