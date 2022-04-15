## DAMG7245_Spring2022

## Big Data Systems and Int Analytics Assignment 5

## Objective

The aim of this assignment is Log the usage of the application and restrict the user to ‘n' number of requests (in our case n=10). Visualize the Logged Data. Added a new functionality which uses NLP models from Huggingface to summrize and get Named entities from the Episode and Event Narratives. Deployed the containers on AWS lambda for a serverless functionality.

This repository contains data, lab work ,Design Document and source code of assignment5 which covers:

* Logging of User data onto Bigquery and restrict users to 'n' number of requests
* Summarize and extract named entities from the Event and Episode narratives using Hugging face models
* Deploy the container on AWS Lambda for scaling of requests

Assignent5 :
codelab link : https://codelabs-preview.appspot.com/?file_id=1H0FiY7oTCZwJBtE_0qAensEWmy6RTufJKVdkyQ8cnBs#0


## Instructor Information:
[Prof. Sri Krishnamurthy](https://www.linkedin.com/in/srikrishnamurthy/)

## Team Information

| NAME              |     NUID        |    Contribution   |
|-------------------|-----------------|-------------------|
| Sudarshan Waydande|   001563532     |     33.3          |
| Divyanshu Bhardwaj|   002181815     |     33.3          |
| Prasanth Dwadasi  |   002115654     |     33.3          |


## Note 
“WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK”


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   └── mse.h5 		   <- The url of all the pre-trained models
│
├── docs               <- The Assignment document
│
├── references         <- Sevir paper published by MIT
│
├── results            <- Generated gif using the pretrained model
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│              
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
│
├── src                <- Source code containing frontend and backend code
│    └── airflow       <- Added airflow code which creates cache every hour
│    └── Lamda         <- DEployed containerized code for Summary and NER on Narratives
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
