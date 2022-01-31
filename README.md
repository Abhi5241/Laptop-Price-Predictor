# Laptop_Price_Predictor
* Designed a web app that predicts the price of the laptop given the configurations.
* Developed Linear, Lasso, and Random Forest Regressors using GridsearchCV to get the best model.
* Deployed the Machine Learning model using streamlit library in Heroku.

# Feature Engineering
We go through all the features one by one and keep adding new features. I have made the following changes and created new variables: RAM - Made columns for Ram Capacity in GB and the DDR version
Processor - Made columns for Name of the Processor, Type of the Processor, Generation
Operating System - Parsed the Operating System from this column and made a new column
Storage - Made new columns for the type of Disk Drive and the capacity of the Disk Drive
Display - Made new columns for the size of the laptop(in inches) and touchscreen
Description - Made new columns for the company and graphic card

# Data Preprocessing
There are a few columns which are categorical here but they actually contain numerical values.So we need to convert few categorical columns to numerical columns. These are DDR_Version,Generation,Storage_GB,Price
* Heroku Deployed Link: https://price-predictor-ap.herokuapp.com

![alt text](https://github.com/Aryanvj00/Laptop_Price_Predictor/blob/main/Image/Image(1).png)
![alt text](https://github.com/Aryanvj00/Laptop_Price_Predictor/blob/main/Image/Image(2).png)
