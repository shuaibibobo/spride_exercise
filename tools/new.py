import newspaper
cnn_paper = newspaper.build('http://www.sina.com.cn/')
for article in cnn_paper.articles:
    print(article.url)