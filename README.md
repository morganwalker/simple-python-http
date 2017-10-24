![Travis](https://travis-ci.org/morganwalker/simple-python-http.svg?branch=master)

[Docker Hub](https://hub.docker.com/r/jmorganwalker/simple-python-http/)

### Firing it up locally!

1. `docker-machine create -d virtualbox default` #create the docker machine
2. `docker-machine ls` #lists the docker machine (not the IP address listed in the URL)
3. `docker-machine env default` #lists the env vars
4. `eval $(docker-machine env default)`  #copy these contents into ~/.bash_profile
5. `source ~/.bash_profile` #adds the env vars so you don't need to restart your terminal (may need to add to ~/.bashrc)
6. `env | grep DOCKER` #confirm the env vars are set
7. `docker build --build-arg PORT=8001 -t flask .` #if you want to change the exposed port
8. `docker run -e PORT=8001 -e WORKERS=5 -p 8001:8001 --name flask1 -d flask` #if you want to change the workers and bind port
9. `docker exec -i -t flask1 /bin/sh` #connect to running container
10. Navigate to app at http://192.168.99.100:8001/
***

### Overview

In this test project we have a simple flask app that we would like you to wrap in a container, and test in that same container
automating tests and builds to docker hub to your repo in TravisCI.

To host the flask app we ask that you use Gunicorn inside the container.
***

### General Overview

 1. [x] Fork the this repository.
 2. [x] Create a dockerfile for the repository
 3. [ ] Setup tests on Travis CI which run in that -- **test.py is running but I'd like to add another one**
 4. [x] Travis CI should produce a image and push that to Docker Hub(just a free public repo).
 5. [x] Submit link to your github repository, include the docker hub link in your repository.
***

### Requirements

 * [x] Create a working docker image that runs the flask app using Gunicorn
 * [x] Docker image should take in environment variables to configure port and number of workers.
 * [x] Setup a Travis CI environment
 * [x] Tests should run inside the docker container in the CI environment.
 * [x] Travis CI should continously deliver a new image on commits to `master`.
 * [x] Create a new README.md which contains build status and link to docker hub
***

### Bonus Points

 * [x] Use a small base image(like alpine)
 * [ ] Produce a smaller image with multistage builds -- **WIP**
   * Prerequisites - Docker client and server/machine versions need to be 17.06+
     * `docker version` #determine client and machine versions
     * `docker-machine upgrade default` #upgrade the docker machine
     * Check for updates via the Docker for Mac menu item
     * I've grasped how to accomplish this using `FROM as base` and `FROM base` to make the final container smaller, but am still working through how to chop them up.
 * [x] Provide the yaml for creating a Kubernetes Deployment -- **deployment and service successfully fires up; still working on networking**
    1. `brew install kubectl`
    2. `kubectl version` #to verify version
    3. `kubectl cluster-info` #verify cluster is running
    4. `brew install bash-completion` #enable bash completion (follow caveat steps)
    5. `curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.22.3/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/` #install Minikube
    6. `minikube --vm-driver=virtualbox start` #fire up single-node Kubernetes cluster with Virtualbox drivers.  You can verify by viewing the VM in Virtualbox app
    7. `eval $(minikube docker-env)` #work with the docker daemon
    8. `docker ps` #view Minikube-related containers
    9. `minikube dashboard` #access your dashboard
    10. `kubectl create -f ./flask_deployment.yaml` #fire up Flask deployment and service
    11. `kubectl get deployments` #verify deployment creation
    12. `kubectl describe services flask-service` #verify service creation
    13. `kubectl get pods` #list pods running in deployment
    14. `kubectl exec <pod_name> -- printenv` #get more details on pod
    15. `docker ps` #show both Flask containers running
    16. `kubectl proxy` #create a connection between our host (the online terminal) and the Kubernetes cluster
    17. Clean up with `kubectl delete services flask-service` and `kubectl delete deployment flask-deployment`
 * [ ] Provide a proof of concept for continous deployment to kubernetes -- **WIP**
 * [x] Create python tooling for developers to live reload the application -- **can reload gunicorn with** ```docker exec -i -t flask1 /bin/sh -c '/bin/sh /deploy/app/restart_gunicorn.sh'```
   * I understand that I didn't create python tooling for this so I tried to think outside of the box.  My first approach was to start gunicorn with `--reload`, which will restart the workers when code changes, and start the container with `docker run -p 8000:8000 -v $DEV_ROOT/simple-python-http:/deploy/app --name flask1 -d flask`, which will mount the local filesystem to the app's directory.  That way a dev could make changes locally and the app within the container would restart the workers.  However, there are known issues with the host file changes not actually making it into the container when using Virtualbox and Docker for Mac.  So, I went with an inelegant solution of restarting gunicorn from the command line.
