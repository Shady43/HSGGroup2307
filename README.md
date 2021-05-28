# Covid-19 Data Analysis

## Introduction
The motivation behind our project is to facilitate the processing of data about the Covid-19 pandemic. For this purpose we wanted to develop a program that provides a selection of countries and possible information from which the user can create his own data set. In addition, there is the possibility to make a comparison with the development in Switzerland.

## How does it work
The program obtains a dataset from an Excel, which is then divided into its components by country, date and the specific information. The user's selection is queried by loops, which then pulls the desired information from the already cleaned & sorted dataset. For comparison with Switzerland, the user inputs are drawn into a separate function for calculation. For further possible use of the requested data, we integrated a background function, that inserts the data provided in python in a separate Excel file, the user can use for research, visualisations or more comprehensive analysis. 

For a detailed explanation of the functions and how the code works look into the following file:[Manual and further information](docs/Manual and further information)

## Manual
The program was programmed with Python 3 and can be executed with any Python software. For the script is only the library datetime necessary, which is imported at the beginning of the program. Make sure that the Covid-19-file is saved in the same folder so that there are no complications with the data processing. 

For a detailed explanation of the functions and how the code works look into the following file:

## Credits
The Covid-19 data was derived from https://github.com/owid/covid-19-data/blob/master/public/data/README.md

## Creators
This Programm was created by Project Group 2307, which consists of Andrin, MZanella and DonPablo. We recommend the coding to everyone, as it can be fun, enlightening and helpful for any task!
