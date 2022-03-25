## DAMG7245_Spring2022

## Big Data Systems and Int Analytics Assignment 4

## Objective

The aim of this assignment is get the location as input from user, search fot the nearest available locations in our database and providing the nowcast data of the selected location. Deploy this model fastapi client onto a webserver and provide the user a webinterface using streamlit.

This repository contains data, lab work ,Design Document and source code of assignment4 which covers:

* Distance logic to select top 3 nearest locations
* A webinterface created using streamlit
* 5 functional testcases to test model functionality

Assignent4:
codelab link : https://codelabs-preview.appspot.com/?file_id=1OMGnd1EJ6SMUUO3ImAsbepHS31DDMsP7-4PS8iKmjSE#0


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
│   └── mse.h5 		   <- The url of all the pre-trained models
│
├── docs               <- The Assignment document 
│
├── notebooks          <- Jupyter notebooks demonstarting how to use API
│
├── references         <- Sevir paper published by MIT
│
├── results            <- Generated gif using the pretrained model
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│              
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code containing frontend and backend code
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
