![Travis](https://travis-ci.org/morganwalker/simple-python-http.svg?branch=master)

### Firing it up locally!

* docker-machine create -d virtualbox default
* docker-machine ls #lists the VM
* docker-machine env default #lists the env vars
* eval $(docker-machine env default)  #copy these contents into ~/.bash_profile
* source ~/.bash_profile #adds the env vars so you don't need to restart your terminal (may need to add to ~/.bashrc)
* env | grep DOCKER #confirm the env vars are set
* docker build --build-arg PORT=8001 -t flask . #if you want to change the exposed port
* docker run -e PORT=8001 -e WORKERS=5 -p 8001:8001 -t flask #if you want to change the workers and bind port


### Overview

In this test project we have a simple flask app that we would like you to wrap in a container, and test in that same container
automating tests and builds to docker hub to your repo in TravisCI.

To host the flask app we ask that you use Gunicorn inside the container.

### General Overview

 1. [x] Fork the this repository.
 2. [x] Create a dockerfile for the repository
 3. [ ] Setup tests on Travis CI which run in that -- **test.py is running but I'd like to add another one**
 4. [x] Travis CI should produce a image and push that to Docker Hub(just a free public repo).
 5. [x] Submit link to your github repository, include the docker hub link in your repository.

### Requirements

 * [ ] Create a working docker image that runs the flask app using Gunicorn -- **everything fires up properly but I'm not able to hit the site on http://0.0.0.0:8000**
 * [x] Docker image should take in environment variables to configure port and number of workers.
 * [x] Setup a Travis CI environment
 * [x] Tests should run inside the docker container in the CI environment.
 * [x] Travis CI should continously deliver a new image on commits to `master`.
 * [x] Create a new README.md which contains build status and link to docker hub

### Bonus Points

 * [ ] Use a small base image(like alpine) -- **plan on doing this**
 * [ ] Produce a smaller image with multistage builds
 * [ ] Provide the yaml for creating a Kubernetes Deployment -- **plan on looking into this**
 * [ ] Provide a proof of concept for continous deployment to kubernetes -- **plan on attempting this**
 * [ ] Create python tooling for developers to live reload the application
