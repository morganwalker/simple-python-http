![Travis](https://travis-ci.org/morganwalker/simple-python-http.svg?branch=master)

[Docker Hub](https://hub.docker.com/r/jmorganwalker/simple-python-http/)

### Firing it up locally!

* docker-machine create -d virtualbox default #create the docker machine
* docker-machine ls #lists the docker machine (not the IP address listed in the URL)
* docker-machine env default #lists the env vars
* eval $(docker-machine env default)  #copy these contents into ~/.bash_profile
* source ~/.bash_profile #adds the env vars so you don't need to restart your terminal (may need to add to ~/.bashrc)
* env | grep DOCKER #confirm the env vars are set
* docker build --build-arg PORT=8001 -t flask . #if you want to change the exposed port
* docker run -e PORT=8001 -e WORKERS=5 -p 8001:8001 --name flask1 -d flask #if you want to change the workers and bind port
* docker exec -i -t flask1 /bin/sh #connect to running container
* Navigate to app at http://192.168.99.100:8001/

## Multi-stage build prerequisites

Docker client and server/machine versions need to be 17.06+

* docker version #determine client and machine versions
* docker-machine upgrade default #upgrade the docker machine
* Check for updates via the Docker for Mac menu item


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

 * [x] Create a working docker image that runs the flask app using Gunicorn
 * [x] Docker image should take in environment variables to configure port and number of workers.
 * [x] Setup a Travis CI environment
 * [x] Tests should run inside the docker container in the CI environment.
 * [x] Travis CI should continously deliver a new image on commits to `master`.
 * [x] Create a new README.md which contains build status and link to docker hub

### Bonus Points

 * [x] Use a small base image(like alpine)
 * [ ] Produce a smaller image with multistage builds
 * [ ] Provide the yaml for creating a Kubernetes Deployment -- **plan on looking into this**
 * [ ] Provide a proof of concept for continous deployment to kubernetes -- **plan on attempting this**
 * [x] Create python tooling for developers to live reload the application -- **can reload gunicorn with** ```docker exec -i -t flask1 /bin/sh -c '/bin/sh /deploy/app/restart_gunicorn.sh'```
   * I understand that I didn't create python tooling for this so I tried to think outside of the box.  My first approach was to start gunicorn with `--reload`, which will restart the workers when code changes, and start the container with `docker run -p 8000:8000 -v $DEV_ROOT/simple-python-http:/deploy/app --name flask1 -d flask`, which will mount the local filesystem to the app's directory.  That way a dev could make changes locally and the app within the container would restart the workers.  However, there are known issues with the host file changes not actually making it into the container when using Virtualbox and Docker for Mac.  So, I went with an inelegant solution of restarting gunicorn from the command line.
