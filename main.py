from flask import Flask , render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# Create a Flask App
app = Flask(__name__)

# Homepage- Route
# Home("/") , /about , /contact , /pricing
@app.route("/")
def index():
    query = request.args.get("query","latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    # print(news_data)
    
    articles = news_data.get("articles",[])
    
    # filtered_articles = [article for article in articles  if "Yahoo" not in article["soutce"]["name"] and "removed" not in article["title"].lower()]
    
    return render_template("index.html",articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)