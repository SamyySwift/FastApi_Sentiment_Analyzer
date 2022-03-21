# FastApi_Sentiment_Analyzer
An API built for a sentiment analyzer machine learning model. The api returns the polarity score and the sentiment label of any given text or review.

# RUNNING CODE
1. Build the docker image from the Dockerfile provided using this command replacing the image_name with any name you like.

   **docker build -t <image_name> .**
2. Run the container with the command below replacing container_name with any name you wish to give your container.

   **docker run --name <container_name> -p 8080:8000 <image_name>.**
