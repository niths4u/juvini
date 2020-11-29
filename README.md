# JUVINI
## A Comprehensive tool for EDA


- **[Introduction](#introduction)** 
- **[Requirement](#requirement)**
- **[Assumption](#assumption)**
- **[Usage](#usage)**
- **[Examples](#examples)**
- **[Best Practices](#best-practices)**

## Introduction

Plotting graphs are one of the most important aspects of EDA. Graphs give intuitive insights based because it is processed by our natural neural networks trained and evolved non stop for years. This tool is designed to allow data science users work on plotting the graphs rather than spending time on codes and analysing different methods of each plotting library. This tool has several levels. Highest level is where the user just have to input the entire data frame and the code will take care of giving all plots based on the data type for all combinations. Just like the way pairplot works for numerical datatypes.


## Requirement

1. User should have some idea on python. This can be run from jupyter as well as python console
2. Should have good understanding of different graph types especially boxplot , scatterplot , barplot , countplot and distplot
3. This is not a must , but if the user has a clear understanding of the datatype associated with each column , then converting to the datatype will make the graph look better. For eg , if a column contains categorical value 1,2,3,4. Then it is better to convert it as object or category so that the tool will be able to guess it. Else it will assume the datatype as numeric and will plot for numeric related graphs


## Usage
### NUMERIC vs NUMERIC - to plot graph where two columns are numeric.
#### Method : num_num(df[[num_col1,num_col2]])
#### Examples
import pandas as pd
from juvini import num_num


## Examples
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.

## Best Practices
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.
