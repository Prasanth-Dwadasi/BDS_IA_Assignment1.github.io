## DAMG7245_Spring2022

## Big Data Systems and Int Analytics Assignment 2

## Objective

The aim of this assignment is to get familiar with the models and work with pre-trained models, generating the test data. Validate the model for 2 -3 event ids and create the dataset for Nowcasting and Synrad. 
After the model is built, we designed the functional requirement document on how to deploy and distribute the model to the client.

This repository contains data, lab work ,Design Document and source code of assignment2 which covers:

* Generated test data for Nowcasting and Synrad
* Forecasting the weather for test data generated using Nowcasting
* 

# Design Document Covers

* The main objective of this documenmt is how to provide our model as a service to Government of USA
* Plan for the deployment of Model in GCP and how we distribute the model as a service in different modes
* The services will be provided as a package, WebSite and as an API

Assignent2:
codelab link : https://codelabs-preview.appspot.com/?file_id=16aRMFUkgOyrIq6IpsfH2n9inzhNRKbJBjWQ-SxjbQjQ#6


## Instructor Information:
[Prof. Sri Krishnamurthy](https://www.linkedin.com/in/srikrishnamurthy/)

## Team Information

| NAME              |     NUID        |
|-------------------|-----------------|
| Sudarshan Waydande|   001563532     |
| Divyanshu Bhardwaj|   002181815     |
| Prasanth Dwadasi  |   002115654     |


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── CATALOG.CSV    <- The metadata for all EventID's along with thier data
│   ├── CAT.CSV        <- The subset data of the EventID's we choose
│   └── model_urls.csv <- The url of all the pre-trained models
│
├── docs               <- The Assignment document 
│
├── notebooks          <- Jupyter notebooks of both Nowcast and Synrad
│
├── references         <- Sevir paper published by MIT
│
├── reports            <- Generated analysis as PDF, PNG, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│              
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── Nowcast        <- Code to Nowcast weather
│   │   
│   │
│   ├── Synrad         <- Code to generated SYnthethic data
│
│
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```