
build:
		docker build -t goshad/webapp-nginx:v${NEW_VERSION} .
push:
	docker login -u goshad -p "${DOCKER_TOKEN}" 
	docker push goshad/webapp-nginx:v${NEW_VERSION}

build-and-push: build push

