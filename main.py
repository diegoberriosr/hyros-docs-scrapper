from scrapper import Scrapper
from transformer import Transformer
from analyzer import Analyzer

scrapper = Scrapper()
analyzer = Analyzer()

article = scrapper.scrape('https://docs.hyros.com/tracking-hubspot-sales/')
processed_article = analyzer.process(article)

Transformer.convert_to_pdf(processed_article, 'hubspot')