from boilerpipe.extract import Extractor

if __name__ == '__main__':
    URL = 'http://programmingisterrible.com/post/112612689998/san-francisco-for-londoners'
    extractor = Extractor(extractor='ArticleExtractor', url=URL)
    print extractor.getText()
