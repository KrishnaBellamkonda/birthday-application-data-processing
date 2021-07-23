# birthday-application-data-processing
*This repository contains the preprocessing steps and scripts involved in the creation of Birthday Quizzer Electron application.* 

### Aim 
Development of a script that can convert a raw csv file into a reusable data source for Date Quizzer application. 

### Usage 
1) Take CSV files containing Name and birthday information and place them in the dataset folder
2) Verify that the CSV file has two columns as the first two columns (the column names must match exactly - case sensitive)
   * Name
   * Birthdate
3) Run the python script
```
python preprocessing.py
```

### Methodology 
* Obtain data from source 
* Preprocess the data 
* Convert them into suitable json files 
* Save the json files
* Aggregate these steps in the `preprocessing.py` script

### Technology 
* Python 

### Packages 
* os 
* numpy
* pandas
* json

