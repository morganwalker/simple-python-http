## Overview

In this test project we have a simple flask app that we would like you to wrap in a container, and test in that same container
automating tests and builds to docker hub to your repo in TravisCI.

To host the flask app we ask that you use Gunicorn inside the container.

### General Overview

 1. Fork the this repository.
 2. Create a dockerfile for the repository
 3. Setup tests on Travis CI which run in that
 4. Travis CI should produce a image and push that to Docker Hub(just a free public repo).
 5. Submit link to your github repository, include the docker hub link in your repository.

### Requirements

 * Create a working docker image that runs the flask app using Gunicorn.
 * Docker image should take in environment variables to configure port and number of workers.
 * Setup a Travis CI environment
 * Tests should run inside the docker container in the CI environment.
 * Travis CI should continously deliver a new image on commits to `master`.
 * Create a new README.md which contains build status and link to docker hub

### Bonus Points

 * Use a small base image(like alpine)
 * Produce a smaller image with multistage builds
 * Provide the yaml for creating a Kubernetes Deployment
 * Provide a proof of concept for continous deployment to kubernetes
 * Create python tooling for developers to live reload the application
