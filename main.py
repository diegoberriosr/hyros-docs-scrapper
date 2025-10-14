from scrapping_assistant import ScrappingAssistant
from articles import ARTICLE_LIST

def main():
  ScrappingAssistant().getArticles(ARTICLE_LIST)


if __name__ == "__main__":
  main()