from flask import Flask,render_template
import requests
from datetime import datetime


app=Flask(__name__)

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-02-11&'
       'sortBy=popularity&'
       'apiKey=')  # use your own api key

response = requests.get(url)
news_data = response.json()
now = datetime.now()
time_news = now.time().strftime("%H:%M %p")

now = datetime.now()
date = now.strftime("%a,%d %b, %Y")

@app.route('/')
def home_news():
  
  return render_template('index.html',news_data = news_data,date=date,time_news=time_news)


@app.route('/allnews')
def all_news():

 
  return render_template('all_news.html', news_data=news_data,date=date, time_news=time_news)  

@app.route('/allnews2')
def all_news2():

 
  return render_template('all_news2.html', news_data=news_data,date=date, time_news=time_news)  


if __name__=='__main__':
    app.run(debug=True)







