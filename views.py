from flask import Flask, render_template

from newsapi import NewsApiClient


app=Flask(__name__)
@app.route('/')
def test():
    
    newapi = NewsApiClient(api_key="45778e35f22c47dfadc524155cee34d6")
    newswordhippos = newapi.get_news_wordhippos(sources="bbc-news")
    
    articles = newswordhippos['articles']
    
    
    tit= []
    description= []
    image= []
    content= []
    url= []
    publishedAt= []
    
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        
        tit.append(myarticles['title'])
        description.append(myarticles['description'])
        image.append(myarticles['urlToImage'])
        content.append(myarticles['content'])
        url.append(myarticles['url'])
        publishedAt.append(myarticles['publishedAt'])
        
        my_list = zip(tit,description,image,content)
        
        return render_template('index.html', context=my_list)
        
        if __name__ == '__main__':
         app.run(debug=True)
        
    
    
        
        
    
    

