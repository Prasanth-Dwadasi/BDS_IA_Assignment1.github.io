## DAMG7245_Spring2022

## Big Data Systems and Int Analytics Assignment 4 Part 2

## Objective

The aim of this assignment is get the location as input from user, search fot the nearest available locations in our cached database and if it is not found in cache we get the data by running the images thorugh the model. The cache stores the popular 50 locations nowcast data by running batch processing on airflow every hour. The frontend which was provided through stereamlit has been made secure for the authorized user only with the help of JWT.

This repository contains data, lab work ,Design Document and source code of assignment4 part 2 which covers:

* The authorization of user using JWT
* Batch processing of 50 popular locations every hour using airflow and cached them
* Updated code which pipelines the user request through cache or through model if user wants latest data

Assignent4  Part2 :
codelab link : https://codelabs-preview.appspot.com/?file_id=1KH-V6PSW73jn9yeL-NzLM0T7C2pbLdTwGoSIT64zLmc#0


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
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
