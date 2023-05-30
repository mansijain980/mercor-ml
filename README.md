## Mercor-ML
Mercor ML Engineer Vetting Project

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. Your solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.

### Steps to be followed to deploy docker image on Gogle Cloud Run

### Libraries(if you are using editor like Vscode )

~~~
pip install pandas
pip install numpy
pip install TfidfVectorizer
pip install cosine_similarity
pip install transformers

~~~

# To containerize the application using Docker and deploy it on Google Cloud Functions or Google Cloud Run, you can follow these steps:

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

# Upload the Docker image to a container registry:
You need to upload the Docker image to a container registry in order to deploy it on Google Cloud Functions or Google Cloud Run. Here's an example of how to upload the Docker image to Google Container Registry (GCR):

a) Tag the Docker image with the GCR location:

~~~
docker tag myapp gcr.io/[PROJECT_ID]/myapp
~~~

Replace [PROJECT_ID] with your Google Cloud project ID.

b. Authenticate Docker with GCR:

~~~
docker login -u _json_key -p "$(cat key.json)" https://gcr.io
~~~

Replace key.json with the path to your Google Cloud service account key file. This step authenticates Docker with GCR using the service account credentials.

c. Push the Docker image to GCR:

~~~
docker push gcr.io/[PROJECT_ID]/myapp
~~~

# Deploy on Google Cloud Run:
To deploy the container on Google Cloud Run, follow these steps:

i. Open the Cloud Run page in the Google Cloud Console.

ii. Click "Create Service" to create a new service.

iii. Provide a service name and choose your preferred region.

iv. Under "Container image", select "Custom".

v. Enter the container image URL in the "Container image URL" field (e.g., gcr.io/[PROJECT_ID]/myapp).

vi. Set the "Memory allocated" and "Maximum requests per container" according to your requirements.

vii. Click "Create" to deploy the service.

Test the deployed function:
After the deployment is successful, you can test the function by sending a JSON payload with the input text to the provided endpoint URL. The function will return a JSON response with the ranked list of similar item URLs.
Make sure to replace [PROJECT_ID] and the endpoint URL with your actual project ID and function/service endpoint URL.

# That's it! You have containerized the application using Docker and deployed it on Google Cloud Functions or Google Cloud Run, enabling it to accept JSON payloads and return JSON responses with the ranked list of similar item URLs.




