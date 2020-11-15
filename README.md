# Budget Tracker Backend

## Install
You need pipenv install for this project. To install all the dependencies run 
`pipenv install`

## Building Docker Image
This project is Dockerized. To build a new image run
`docker build -t <tag> .`

## Running Docker Image
The docker image exposes port 5000. To run the image
`docker run -p 5000:5000 <image>` 
You can pass in the -d flag to run the container in the background 
