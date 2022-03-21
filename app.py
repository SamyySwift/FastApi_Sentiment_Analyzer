from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
import uvicorn
from typing import Optional
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = FastAPI()


class SentimentalText(BaseModel):
    text: Optional[str] = 'text'
 

@app.post("/prediction") 
def prediction(message: SentimentalText):

    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message.text)
   

    label = None
    score = None

    if sentiment_dict['compound'] >= 0.05 :
        label = "Positive"
        score = round(sentiment_dict["compound"], 2)
 
    elif sentiment_dict['compound'] <= - 0.05 :
        label = "Negative"
        score = round(sentiment_dict["compound"], 2)
 
    else :
       label = "Neutral"
       score = round(sentiment_dict["compound"], 2)
    
    return f"The sentiment of the text is {label} with a Score of: {score}"


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")