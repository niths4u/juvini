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
4. The tool will always treat first column as X axis , second input column as Y axis and if parameter `hue_col` is specified then it will search for this column on rest of the dataframe. 


## Usage
consider the standard IRIS dataset.Here we modified it a bit to add a numeric column rating where values are 0.1.2.3. Even though it is categorical , we have purposely kept it as numerical column to show some use cases that will come in later sections.
It consists of 5 columns
1. sepal_length - numeric
2. sepal_width - numeric
3. petal_length - numeric
4. petal_width - numeric
5. species - categorical 
6. rating - numeric ( in fact it is categorical in real scenario )

 
Sample output
1. sepal_length,sepal_width,petal_length,petal_width,species,rating
0. 5.1,3.5,1.4,0.2,setosa,1
1. 4.9,3.0,1.4,0.2,setosa,1
2. 4.7,3.2,1.3,0.2,setosa,0
3. 4.6,3.1,1.5,0.2,setosa,3
4. 5.0,3.6,1.4,0.2,setosa,0
5. 5.4,3.9,1.7,0.4,setosa,1
6. 4.6,3.4,1.4,0.3,setosa,3
7. 5.0,3.4,1.5,0.2,setosa,0
8. 4.4,2.9,1.4,0.2,setosa,1
9. 4.9,3.1,1.5,0.1,setosa,1
10. 5.4,3.7,1.5,0.2,setosa,0


### NUMERIC vs NUMERIC - to plot graph where two columns are numeric.
#### Method : `num_num(df[[num_col1,num_col2]])`
#### Examples

simple numeric to numeric plotting
```
import pandas as pd
from juvini import num_num
df=pd.read_csv('iris_with_rating.csv')
num_num(df[['sepal_length','sepal_width']])
```
![numeric_numeric](/juvini/images/num_num.png)

wait what if i do want to add a hue parameter to it?
Just make sure to add the additional column `species` to the input dataframe and also add the parameter `hue_col='species'`
```
num_num(df[['sepal_length','sepal_width','species']],hue_col='species')
```
![numeric_numeric](/juvini/images/num_num_hue.png)

#### additional parameters 
1. x_name='xvalue' , the name that you want in x axis for the first column , sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
2. y_name='yvalue' , same as x_name , but for Y axis
3. size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4 with tight layout
4. hue_cols , to plot the hue. See the above example


### CATEGORICAL vs CATEGORICAL - to plot graph where two columns that are categorical.
#### Method : `cat_cat(df[[cat_col1,cat_col2]])`
#### Examples

This will take the top 5 categories for each column and plot it. You can change this value 5 using parameters `xcap` and `ycap` as mentioned below
```
import pandas as pd
from juvini import cat_cat
df=pd.read_csv('iris_with_rating.csv')
cat_cat(df[['species','rating']])
```
![categorical_categorical](/juvini/images/cat_cat.png)

similarly interchanging first and second column will change the axis
`cat_cat(df[['rating','species']])`
![categorical_categorical_xy_changed](/juvini/images/cat_cat_interchange.png)

But wait , did we just use a numerical column to plot a categorical column?
Actually yes , if we know that it is categorical , we do not have to change the datatype and all unnecessary things. the code will take care of converting it to category.

Fine , but what if there are too many categories and i simply need to have a gist of top few categories?
Yes that is also supported , simply provide the parameter `xcap=<value>` , the code will sort the categories based on its count and choose the top n values based on the input.

`cat_cat(df[['species','rating']],xcap=2)`

![categorical_categorical_with_xcap](/juvini/images/cat_cat_xcap.png)

Fine , what if i want to change not the xcap but the ycap?
Yes we can do that as well. Simply change the parameter `ycap=<value>` just like the xcap.

How about the hue?
Yes , that also will work here. provide it like `cat_cat(df[['species','rating','hue_column']],hue_col='hue_column)`

#### additional parameters 
1. x_name='xvalue' , the name that you want in x axis for the first column , sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
2. y_name='yvalue' , same as x_name , but for Y axis
3. size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4 with tight layout
4. xcap=5 , will cap the maximum categories with top 5 based on its count for x axis 1st column , default 5
5. ycap=5 , same as xcap , but will be applicable to y column.
6. hue_cols , to plot the hue. See the above example


## Examples
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.

## Best Practices
1. Create a user and group called `labuser` and assign a specific `uid` and `guid` , say 2100. The number 2100 is important because going further docker containers will also be using same uid and guid to ensure the files persisted are accessible from host and vice versa
2. `groupadd -g 2100 labuser`
3. `useradd -u 2100 -d /home/labuser -ms /bin/bash -g labuser -p “$(openssl passwd -1 labuser123)” labuser` Feel free to change the password from *labuser123* to any password.
