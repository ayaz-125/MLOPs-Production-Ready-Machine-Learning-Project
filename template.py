# ********************************STEP-1*************************

#  This file is used for making the project sturucture
#  It is used to create the project structure and to make the project ready for development.

import os  # for importing the operating system
from pathlib import Path # we use this for the path

project_name = "us_visa" # This is the name of the project

# Various file and folder
list_of_file =[
    f"{project_name}/__init__.py", #Here __init__ is the constructor file
    f"{project_name}/components/__init__.py",   
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configurations/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
    

]

for filepath in list_of_file:
    filepath = Path(filepath)
    # print("These are ",filepath) --- This  will help to print the filepath means the upper files
    filedir,filename = os.path.split(filepath)
    # print(f"The name of the dir is {filedir} and the name of the file is {filename}") ---This will help to seperate the filedir and filename from the filepath

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        print("created successfully")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath))):
        with open(filepath,"w") as f:
            pass
    
    else:
        print(f"file is already present at :{filepath}")