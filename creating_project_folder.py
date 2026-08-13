#-----------------------------------------------------------------------------------
#This script creates GIS folder and its subfolders with a standard naming convention
#-----------------------------------------------------------------------------------

import os


#------------------------------------------------------------------------
#PROJECT INFORMATION - change these values
#------------------------------------------------------------------------

base_folder = r"C:\Users\61415\OneDrive\Documents\Personal Project\Learning Plans\GIS_Automation_Projects"
project_year = "2026"
project_name = "Smart_Road_Management_System_test"
area_name = "Marsden_Park"
author = "PA"



project_folder_name = (project_year+"_"+project_name+"_"+area_name+"_"+author) #CREATE FULL PROJECT FOLDER NAME

project_folder=os.path.join(base_folder,project_folder_name) #CREATE THE COMPLETE PROJECT FOLDER PATH

subfolders=["01_Input_Data","02_ArcGIS_Project","03_Scripts","04_Working_Data","05_Outputs","06_Documentation","07_Maps", "08_FieldMaps","09_WebGIS"] #CREATING NAMES FOR THE SUBFOLDERS INSIDE THE PROJECT

os.makedirs(project_folder,exist_ok=True) #CREATE THE MAIN PROJECT FOLDER
print("Project folder created")
print(project_folder)


for folder_name in subfolders:
    folder_path = os.path.join(project_folder, folder_name) #CREATE PATH FOR SUBFOLDERS
    os.makedirs(folder_path,exist_ok=True) #CREATE SUBFOLDERS
print("Folder created successfully")





