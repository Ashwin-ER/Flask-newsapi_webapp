from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)



@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="06b5ba6d0f9b4d2085e865292f521aa6")
    topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])



    mylist = zip(news, desc, img)


    return render_template('index.html', context = mylist)



@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="06b5ba6d0f9b4d2085e865292f521aa6")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('bbc.html', context=mylist)



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
#NEWS-SOURCE
'''International Sources:
al-jazeera-english

bbc-news

cnn

reuters

the-hindu

the-times-of-india

the-indian-express

hindustan-times

ndtv

news24

Indian Sources:
the-times-of-india

the-hindu

the-indian-express

hindustan-times

ndtv

india-today

firstpost

livemint

business-standard

news18
'''