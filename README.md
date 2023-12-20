# cnn-color-classifier
# **Shopping products colour based classification**
![Color Classifier](https://m.media-amazon.com/images/I/71Kn4h8cjhL.__AC_SX300_SY300_QL70_ML2_.jpg)


## Problem description
Color classification one of most desired tasks nowdays in the AI era, which is benifical in differents domains ex: e-commerece, intelligent transportation systems ..
colors which are exist for this dataset include the basic 12 colors:
 `['black', 'blue', 'brown', 'green', 'grey', 'orange', 'pink', 'purple','red', 'silver', 'white', 'yellow']`.
## **Model Training and Hyperparameters Tuning**
---
### 1.Dataset
The dataset is from Kaggle [check here](https://www.kaggle.com/datasets/imoore/6000-store-items-images-classified-by-color)
- composed of 6239 images
- 12 colour categories
- all images for clothing and accessories products
### 2. Used Models
The base models used in this project belongs to the pre-trained Deep learning models that are made available alongside pre-trained weights.

I've selected `EfficientNetB1`, `ResNet50` from keras applications benchmark as I see they look good at balancing between the achieved accuracy and running time espiecially if the used hardware computation power is limited.

### 3.Hyperparameters Tuning
    During the training phase I went through all the following set of parameters one by one independtly seeking for better performance
    - Learning rate
    - Dense layer size
    - Dropout value
### 3.Training data augmentation ( transformation)
    During the training phase I applied bunch of image data transformation to generate different variations for the model to help in genenralization the data features.
    - Image zoom
    - Image rotation
    - Image Shear
## **Conversion notebook to executable python script**
---
using jupyter nbconvert
## **Project Setup**
---

### Step 1: Cloning git repo
```bash
git clone https://github.com/AbdelrahmanElmasry/cnn-color-classifier.git
cd cnn-color-classifier
```

### Step 2: Install Dependencies

1. Ensure you have Python 3.8 installed on your system.

2. Create a virtual environment and install project dependencies using Pipenv:
    > to avoid any dependency conflict with your base environment

   ```bash
   pipenv install
   ```
- Packages
    - flask = "*"
    - pillow = "*"
    - waitress = "*"
    - tflite-runtime = "*"
    - requests = "*"

    This command will create a virtual environment and install the required packages from the Pipfile.
### Step 2: Activate the Virtual Environment

1. Once the dependencies are installed, activate the virtual environment with this command:

   ```bash
   pipenv shell
   ```

    You will see the command prompt left side prefix change to indicate that the environment is active.

    Now, your virtual environment is set up and activated. You can run your Flask application using Waitress with the following command:

    ```bash
    waitress-serve --listen=0.0.0.0:8000 predict:app
    ```
    or simply for dev usage only:

    ```bash
    python predict.py
    ```

## **Loading the model**
Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
Files with dependencies
Pipenv and Pipenv.lock if you use Pipenv
or equivalents: conda environment file, requirements.txt or pyproject.toml
Dockerfile for running the service

## **Containerization**
---

This project has been containerized for easy deployment using Docker. To build and run the container, follow these steps:
### Step 1: Building the Container

1. Make sure you have Docker installed on your system.

2. Navigate to the directory containing your Dockerfile.

3. Use the following command to build the container. Replace `<container-name>` with your preferred container name (e.g., "ml-app"):

   ```bash
   docker build -t <container-Name> .
   ```

    This command instructs Docker to build an image using the Dockerfile in the current directory.

### Step 2: Running the Container

1. Once the container is built, you can run it using the following command:

    ```bash
    docker run -it --rm -p 8080:8080 <container-name>
    ```

   - -it enables an interactive terminal.
   - --rm removes the container when it exits.
   - -p 8080:8080 maps port 9696 on your host to port 9696 within the container.
   - `<container-name>` is the name you provided when container image built.

### Step 3: Publishing the image to ECR service
1. you will need AWSCLI to be installed
    ```bash
    pip install awscli
    ```
2. Configure the AWSCLI from command line
    ```bash
    aws configure
    ```
3. Create new repo
    ```bash
    aws ecr create-repository --repository-name <repo-name>
     ```
4. Tag the built image with ECR identifier
    ```bash
    docker tag clothing-model:latest ${REMOTE_URI}
    ```
5. Finally, Push the image to the registry
    ```bash
    docker push ${REMOTE_URI}
    ```

Deployment
URL to the service you deployed or
Video or image of how you interact with the deployed service

## **Cloud Deployment**
---
I used Lambda serverless service from AWS Cloud, where I'll focus only on the application level development and AWS will take care about the rest of details
- ### URL to the service
 HTTPS post method  [https://e6yc5urqh1.execute-api.eu-central-1.amazonaws.com/test/predict](https://e6yc5urqh1.execute-api.eu-central-1.amazonaws.com/test/predict)

