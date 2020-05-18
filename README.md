<p align="center">
  <a href="url"><img src="https://github.com/btphan95/greenr/blob/master/logo.png?raw=true" align="middle" height="300" width="300" ></a>
</p>

# greenr 🍃

A web app to let users upload an image to classify it as a dandelion or grass.

[<img src="https://img.shields.io/badge/live-demo-brightgreen?style=for-the-badge&logo=appveyor?">](http://34.68.160.231)

Click the badge above to run the demo.


greenr is powered by a deep learning model created in FastAI. If you are interested in learning how I  created an image dataset from Google Images and trained a dandelions and grass classifier in FastAI, check out this Github repo that links to a Kaggle kernel outlining my process. FastAI is a deep learning library built on top of PyTorch that makes it extremely to get started with deep learning.

To deploy greenr onto the web, I utilized [Flask](https://flask.palletsprojects.com/en/1.1.x/) as the back-end to serve the model as an endpoint, [Flask-CORS](https://flask-cors.readthedocs.io/) to enable Cross Origin Resource Sharing (CORS), [Docker](https://www.docker.com/) to containerize the server, and [Heroku](https://www.heroku.com/)[(https://greenr.herokuapp.com/)](https://greenr.herokuapp.com/) and [Google Cloud Platform](http://cloud.google.com/)[(http://34.68.160.231)](http://34.68.160.231) (for redundancy) to host the container and serve the app.

