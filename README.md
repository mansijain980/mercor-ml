# mercor-ml
Mercor ML Engineer Vetting Project

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. Your solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.

## Steps to be followed to deploy docker image on Gogle Cloud Run

### Libraries(if you are using editor like Vscode )

~~~
pip install pandas
pip install numpy
pip install TfidfVectorizer
pip install cosine_similarity
pip install transformers

~~~

## To containerize the application using Docker and deploy it on Google Cloud Functions or Google Cloud Run, you can follow these steps:

### Build the Docker image:
Open a terminal or command prompt and navigate to the project directory. Run the following command to build the Docker image:

~~~
docker build -t myapp .
~~~
Note: Replace myapp with a suitable name for your Docker image.

### Test the Docker image:
You can test the Docker image locally by running the following command:

~~~
docker run -p 8080:8080 myapp
~~~
This will start the container and map the container's port 8080 to your local machine's port 8080. You can send a test request to http://localhost:8080/ to verify if the application is working correctly.

## Upload the Docker image to a container registry:
You need to upload the Docker image to a container registry in order to deploy it on Google Cloud Functions or Google Cloud Run. Here's an example of how to upload the Docker image to Google Container Registry (GCR):



