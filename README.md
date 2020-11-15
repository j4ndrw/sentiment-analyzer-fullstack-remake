# Sentiment analysis 
## Check out the web app [here](http://ec2-18-130-255-217.eu-west-2.compute.amazonaws.com/)!

This project is a full stack remake of the first project I have ever pushed to my GitHub account. That project involved sentiment analysis and it was the very first ML project I have ever done.

At the time of building that project I was still very new to NLP, so my approach to it was very poor, as all I did was converting words into embeddings and passing them to a class DNN, which wasn't a good idea since I used to get 70% accuracy, and that was based only on training. I had no idea that you can split your data and validate it, so you can imagine the network was *very* bad.

Since I find myself to be a bit more advanced in Deep Learning and Full Stack Development, I thought it would be nice to remake that project, following good programming principles and State of the Art techniques in Deep Learning, such as an LSTM network, which I have implemented.

I used Vue.js for the frontend, as I wanted to get a bit more into it since I saw a lot of people saying really good things about it, and I loved it. This is my first Vue app.

For the backend I used Flask. I simply love it, it's lightweight, it's fast and doesn't take long to create a REST API with it.

For DL, I used PyTorch, which I also love.

I managed to develop an MVP for this project in around 11 hours, and after that it was just improving the features and deploying the app. I deployed to app to an EC2 instance on AWS using a Docker image which I pushed on AWS' Elastic Container Registry. The web server I used was NGINX, as I am quite used to it.

At the moment I don't have a domain and probably it wouldn't be worth it acquiring one since this app is on a free tier instance (which will be there for a year I think, not too sure though, this is the first time I ever used AWS, I am mostly used to Azure).

Thank you for checking this app out.

Here are some links to the datasets I used to train my model:
- [**IMDB Dataset of 50K Movie Reviews**](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- [**Twitter and Reddit Sentimental analysis Dataset**](https://www.kaggle.com/cosmos98/twitter-and-reddit-sentimental-analysis-dataset)