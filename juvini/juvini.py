#!/usr/bin/env python
# coding: utf-8

# In[29]:


from itertools import combinations_with_replacement
from itertools import product
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[49]:


def juvini_profile(df,**kwargs):
    '''
    This code takes the entire dataframe and based on the datatype of columns , it will plot all relations
    args 
    1) df
    2) size_figure=(13,4) , can specify the size of the plot
    3) cap=5 , this parameter allows you to limit the number of categorical columns that are part of output
    4) hue_col , can provide a column name for hue , this will plot all graphs based on this column
    '''
    kwargs['xcap']=kwargs['cap'] if 'cap' in kwargs else 5
    kwargs['ycap']=kwargs['cap'] if 'cap' in kwargs else 5
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    #cat_cols=df.select_dtypes(['category','object','bool','datetime','datetimetz'])
    if hue_col==None:
        num_cols=list(df.select_dtypes(['number']).columns)
        cat_cols=[x for x in df.columns if x not in num_cols]
    else:
        num_cols=[x for x in list(df.select_dtypes(['number']).columns) if not x==hue_col]
        cat_cols=[x for x in df.columns if x not in num_cols and not x==hue_col ]
    print("Numerical columns:",num_cols)
    print("Categorical columns:",cat_cols)
    #intra num cols
    if hue_col==None:
        for xcol,ycol in list(combinations_with_replacement(num_cols,2)):
            print("Analysis of numeric",xcol,"and numeric",ycol)
            xy_auto_plot(df[[xcol,ycol]],**kwargs)
        ##intra cat cols
        for xcol,ycol in list(product(cat_cols,cat_cols)):
            print("Analysis of categorical",xcol,"and categorical",ycol)
            xy_auto_plot(df[[xcol,ycol]],**kwargs)

        ##inter num cat cols
        for xcol,ycol in [(x,y) for x in num_cols for y in cat_cols]:
            print("Analysis of categorical",xcol,"and numerical",ycol)
            xy_auto_plot(df[[xcol,ycol]],**kwargs)
    else:
        for xcol,ycol in list(combinations_with_replacement(num_cols,2)):
            print("Analysis of numeric",xcol,"and numeric",ycol)
            xy_auto_plot(df[[xcol,ycol,hue_col]],**kwargs)
        ##intra cat cols
        for xcol,ycol in list(product(cat_cols,cat_cols)):
            print("Analysis of categorical",xcol,"and categorical",ycol)
            xy_auto_plot(df[[xcol,ycol,hue_col]],**kwargs)

        ##inter num cat cols
        for xcol,ycol in [(x,y) for x in cat_cols for y in num_cols]:
            print("Analysis of categorical",xcol,"and numerical",ycol)
            xy_auto_plot(df[[xcol,ycol,hue_col]],**kwargs)
    return(True)

# In[1]:


def find_type(df,colname):
    if colname in df.select_dtypes(['category','object','bool']):
        xtype='cat'
    elif colname in df.select_dtypes(['number']):
        xtype='num'
    elif colname in df.select_dtypes(['datetime','datetimetz']):
        xtype='cat' ##consider date as category
    elif colname in df.columns:
        print('unhandled X datatype, categorizing it as category')
        xtype='cat'
    else:
        #print("No column found for",colname)
        raise ValueError("No column found for",colname)
    return(xtype)


# In[66]:


##x_cols=list of all independent columns , if not provided , then all columns by default will be selected
##target=the column against which we need to plot graph
##special_vals = if there is any specific variable in y_col against which we need the graph ,rest all will be taken as others , 
##for NULL values give it as'nan'
def xy_auto_plot(df,**kwargs):
    '''
    a utility function that will decide the graph based on the columns provided
    By default code will consider the first and the second column for X and Y.
    If parameter hue_col is provided , then the specified column will be used for hue
    args:
    Docstring for plotting categorical vs numerical
    This method expects a dataframe as input with first column as categorical column and second column as numeric.
    Additionally you can provide a third categorical column that can act like a hue.
    NAN in x_axis is converted as string 'nan' and treated as a value to give insight on NAN.
    But nan in y_axis or hue_col is ignored.
    It will output boxplot for second column for each value in first column. It will also give sum of second columns 
    for each value in X column. Because only apart from sum , rest all datas on mean , median , min , max are found in 
    boxplot itself
    extra arguments
    x_specialvalue , the code will consider only this single value for X column and keep rest as 'others'. Useful to plot a certain value stats
    y_specialvalue , same as x_specialvalue for y axis
    xcap=5 , will cap the maximum categories with top 5 based on its count , default 5
    others=True/False - this will add aditional column called others where rest all the values apart from top chosen will go.
    x_name='xvalue' , the name that you want in x axis for the first column , 
            sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
    y_name='yvalue' , same as x_name , but for Y axis
    size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4
                 tight layout
    hue_col='hue_colname' , if you require an additional layer to add hue to the plot
    '''
    x_specialvalue=kwargs['x_specialvalue'] if 'x_specialvalue' in kwargs else None
    y_specialvalue=kwargs['y_specialvalue'] if 'y_specialvalue' in kwargs else None

    #xcap=kwargs['xcap'] if 'xcap' in kwargs else 5
    #ycap=kwargs['ycap'] if 'ycap' in kwargs else 5 
    #others=kwargs['others'] if 'others' in kwargs else False
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    y_name = kwargs['y_name'] if 'y_name' in kwargs else df.columns[1]
    #size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    #scols=kwargs['scols'] if 'scols' in kwargs else 3 ##used in get_rows_cols
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    if x_name==y_name:
        xtype=find_type(df,x_name)
        if not hue_col==None:
            sing_cols=[x_name,hue_col]
            if hue_col==x_name:
                raise ValueError("Hue column cannot be part of other columns , please remove hue column from the input df cols to the function")
            else:
                df.columns=[x_name,x_name+'_2',hue_col]
        else:
            sing_cols=[x_name]
            df.columns=[x_name,x_name+'_2']
        if xtype=='cat':
            #print(sing_cols)
            #print(df[sing_cols])
            single_cat(df[sing_cols],**kwargs)
        else:
            single_num(df[sing_cols],**kwargs)
        return True
            
    #print(df.columns)   
    df.rename(columns = {df.columns[0]:x_name}, inplace=True)
    df.rename(columns = {df.columns[1]:y_name}, inplace=True)
    #print(x_name,y_name,df.columns)
    if not x_specialvalue == None:
        df[x_name]=df[x_name].astype(str).apply(lambda x:x if x==str(x_specialvalue) else 'others')
        #print(df[x_name])
    if not y_specialvalue == None:
        df[y_name]=df[y_name].astype(str).apply(lambda x:x if x==str(y_specialvalue) else 'others')
    xtype=find_type(df,x_name)
    ytype=find_type(df,y_name)
    if xtype=='cat' and ytype=='cat':
        cat_cat(df,**kwargs)
    elif xtype=='cat' and ytype=='num':
        cat_num(df,**kwargs)
    elif xtype=='num' and ytype=='cat':
        num_cat(df,**kwargs)
    elif xtype=='num' and ytype=='num':
        num_num(df,**kwargs)
    return True


# In[ ]:


def single_cat(df,**kwargs):
    xcap=kwargs['xcap'] if 'xcap' in kwargs else 20
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    df[x_name]=df[x_name].astype('str')
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    #print(df[x_name])
    top_val=list(df[x_name].value_counts().iloc[:xcap].index)
    #xvalue,orderx=top_vals(xfilter,cap=xcap,**kwargs)
    #top_order=xvalue.value_counts().iloc[:cap].index
    #print(df.info())
    #df.iloc[:,0] = x
    plt.figure(figsize=size_figure,tight_layout=True)
    sns.countplot(data=df,x=x_name,order=top_val,hue=hue_col)
    if not hue_col==None:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #sns.countplot(xvalue,order=orderx)
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.title('total count of '+x_name)
    plt.show()
    return True


# In[ ]:


def single_num(df,**kwargs):
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    fig,axes=plt.subplots(1,2,figsize=size_figure,tight_layout=True)
    plt.subplot(1,2,1)
    sns.boxplot(data=df,y=x_name,x=hue_col)
    #if not hue_col==None:
    #    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.title('box plot for '+x_name)
    plt.subplot(1,2,2)
    sns.distplot(df[x_name])
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('dist plot for '+x_name)
    plt.xticks(rotation=90)
    plt.show()
    return True

# In[2]:


def top_vals(co,**kwargs):
    '''
    select categories based on count rather than plotting whole graph
    by default it is taken as 5. meaning the count of 5 topmost categories will be used for plotting
    args : first argument is pandas series
    others=True/False - this will add aditional value called others where rest all the values apart from top chosen will go.
    cap=10 to change the topmost 5 to any other number , pass cap=<number> for eg top_vals(df[col1],cap=10)
    '''
    cap=kwargs['cap'] if 'cap' in kwargs else 5
    others=kwargs['others'] if 'others' in kwargs else False
    co=co.astype('str')
    top_val=list(co.value_counts().iloc[:cap].index)
    #co2=co.apply(lambda x:x if x in top_val else 'Restall')
    if others:
        #print('here we go')
        co2=co.apply(lambda x:x if x in top_val else 'Restall')
        top_val.append('Restall') 
    else:
        co2=co[co.apply(lambda x:True if x in top_val else False)]
        #print(co2)
    #top_val = [str(x) for x in top_val]
    top_val.sort(reverse=False)
    return (co2,top_val)


# In[3]:


###plot for X1 for values given in y1 , special vals will come from y1
###only top values of X1 will be plotted
def get_rows_cols(x,**kwargs):
    '''
    a simple function to return the plot grid required to fit
    args:
        x : total number of graphs needed , for eg to plot each value in categorical column , unique values count will be x
        scols=<number> : parameter to control how many graphs in a row , by default it is 3
    '''
    scols=kwargs['scols'] if 'scols' in kwargs else 3
    if x>scols:
        #scols=3 ##capping max columns for subplot as 3
        if (x)%scols == 0:
            srows=(x)//scols
        else:
            srows=(x)//scols+1
    else:
        srows=1
    return (scols,srows)


# In[ ]:


def cat_num(df,**kwargs):
    '''Docstring for plotting categorical vs numerical
    This method expects a dataframe as input with first column as categorical column and second column as numeric.
    Additionally you can provide a third categorical column that can act like a hue.
    NAN in x_axis is converted as string 'nan' and treated as a value to give insight on NAN.
    But nan in y_axis or hue_col is ignored.
    It will output boxplot for second column for each value in first column. It will also give sum of second columns 
    for each value in X column. Because only apart from sum , rest all datas on mean , median , min , max are found in 
    boxplot itself
    extra arguments
    xcap=5 , will cap the maximum categories with top 5 based on its count , default 5
    others=True/False - this will add aditional column called others where rest all the values apart from top chosen will go.
    x_name='xvalue' , the name that you want in x axis for the first column , 
            sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
    y_name='yvalue' , same as x_name , but for Y axis
    size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4
                 tight layout
    hue_col='hue_colname' , if you require an additional layer to add hue to the plot
    '''
    xcap=kwargs['xcap'] if 'xcap' in kwargs else 5  
    others=kwargs['others'] if 'others' in kwargs else False
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    y_name = kwargs['y_name'] if 'y_name' in kwargs else df.columns[1]
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    
    df.rename(columns = {df.columns[0]:x_name}, inplace=True)
    df.rename(columns = {df.columns[1]:y_name}, inplace=True)
    df[x_name]=df[[x_name]].astype('str').fillna('nan')
    #vals=df.loc[:,'x1'].unique()
    df[x_name],orderv=top_vals(df[x_name],cap=xcap,**kwargs)
    fig,axes=plt.subplots(1,2,figsize=size_figure,tight_layout=True)
    plt.subplot(1,2,1)
    sns.boxplot(data=df,x=x_name,y=y_name,order=orderv,hue=hue_col)
    if not hue_col==None:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.title('box plot for '+x_name+' against '+y_name)
    plt.subplot(1,2,2)
    sns.barplot(x=x_name, y=y_name, data=df, estimator=sum ,order=orderv, hue=hue_col) ##mean , median , min , max etc are taken care by boxplot
    plt.title('bar plot for '+x_name+' against '+y_name)
    plt.xticks(rotation=90)
    plt.show()
    return True
    
def num_cat(df,**kwargs):
    '''Docstring for plotting numerical vs categorical
    This method expects a dataframe as input with first column as numerical column and second column as categorical.
    Additionally you can provide a third categorical column that can act like a hue.
    NAN in y_axis is converted as string 'nan' and treated as a value to give insight on NAN.
    But nan in x_axis or hue_col is ignored.
    It will output boxplot for first column for each value in second column. It will also give sum of first columns 
    for each value in Y column. Because only apart from sum , rest all datas on mean , median , min , max are found in 
    boxplot itself
    extra arguments
    ycap=5 , will cap the maximum categories with top 5 based on its count , default 5
    others=True/False - this will add aditional column called others where rest all the values apart from top chosen will go.
    x_name='xvalue' , the name that you want in x axis for the first column , 
            sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
    y_name='yvalue' , same as x_name , but for Y axis
    size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4
                 tight layout
    hue_col='hue_colname' , if you require an additional layer to add hue to the plot
    '''
    xcap=kwargs['ycap'] if 'ycap' in kwargs else 5   ###important switching x and y
    others=kwargs['others'] if 'others' in kwargs else False 
    x_name = kwargs['y_name'] if 'y_name' in kwargs else df.columns[1] ###important switching x and y
    y_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0] ###important switching x and y
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    
    df.rename(columns = {df.columns[1]:x_name}, inplace=True) ###important switching x and y
    df.rename(columns = {df.columns[0]:y_name}, inplace=True) ###important switching x and y
    df[x_name]=df[[x_name]].astype('str').fillna('nan')
    #vals=df.loc[:,'x1'].unique()
    df[x_name],orderv=top_vals(df[x_name],cap=xcap,**kwargs)
    fig,axes=plt.subplots(1,2,figsize=size_figure,tight_layout=True)
    plt.subplot(1,2,1)
    sns.boxplot(data=df,x=x_name,y=y_name,order=orderv,hue=hue_col)
    if not hue_col==None:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.title('box plot for '+x_name+' against '+y_name)
    plt.subplot(1,2,2)
    sns.barplot(x=x_name, y=y_name, data=df, estimator=sum ,order=orderv, hue=hue_col) ##mean , median , min , max etc are taken care by boxplot
    plt.title('bar plot for '+x_name+' against '+y_name)
    plt.xticks(rotation=90)
    plt.show()
    return True

# In[4]:


def cat_cat(df,**kwargs):
    '''Docstring for plotting categorical vs categorical
    This method expects a dataframe as input with first column and second column as categorical column.
    Additionally you can provide a third categorical column that can act like a hue.
    NAN in x_axis and y_axis is converted as string 'nan' and treated as a value to give insight on NAN.
    It will output countplot for second column for each value in second column.Note here , x column axis will remain same here. It is just that the 
    output for each graph will be for each value in y. A final output will also be given.
    extra arguments
    xcap=5 , will cap the maximum categories with top 4 based on its count for x axis 1st column , default 5
    ycap=5 , will cap the maximum categories with top 4 based on its count for y axis 2nd column , default 5
    x_name='xvalue' , the name that you want in x axis for the first column , 
            sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
    y_name='yvalue' , same as x_name , but for Y axis
    size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4
                 tight layout
    hue_col='hue_colname' , if you require an additional layer to add hue to the plot
    scols=<number> : parameter to control how many graphs in a row , by default it is 3
    '''
    xcap=kwargs['xcap'] if 'xcap' in kwargs else 5
    ycap=kwargs['ycap'] if 'ycap' in kwargs else 5 
    others=kwargs['others'] if 'others' in kwargs else False
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    y_name = kwargs['y_name'] if 'y_name' in kwargs else df.columns[1]
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    scols=kwargs['scols'] if 'scols' in kwargs else 3 ##used in get_rows_cols
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    df.rename(columns = {df.columns[0]:x_name}, inplace=True)
    df.rename(columns = {df.columns[1]:y_name}, inplace=True)
    #df[x_name]=df[[x_name]].astype('str').fillna('nan')
    df[y_name]=df[[y_name]].astype('str').fillna('nan')
    #df[x_name],orderx=top_vals(df[x_name],cap=xcap)
    df[y_name],ordery=top_vals(df[y_name],cap=ycap,**kwargs)
    #vals=df.loc[:,y_name].unique()
    scols,srows=get_rows_cols(len(ordery)+1,**kwargs)
    size_figure=(size_figure[0],srows*size_figure[1])
    fig,axes=plt.subplots(srows,scols,figsize=size_figure,tight_layout=True)
    for ctr,value in enumerate(ordery):
            #value=str(value) ##not needed as NULL is already handled with nan replacement for topval
            plt.subplot(srows,scols,ctr+1)
            ###capping the values with top 5 counts of X for the value specified in Y
            ##else the graph would look pretty bad
            #xvalue=df.loc[df['y1'].astype(str)==value,'x1']
            xfilter=df.loc[df[y_name].astype(str)==value,x_name]
            #top_order=xvalue.value_counts().iloc[:cap].index
            #print(xfilter)
            #fi=xfilter
            xvalue,orderx=top_vals(xfilter,cap=xcap,**kwargs)
            #print(xvalue,orderx)
            sns.countplot(xvalue,order=orderx,label=value)
            #ab=xvalue
            #od=orderx
            #lb=value
            plt.xlabel(x_name)
            plt.xticks(rotation=90)
            #plt.ylabel(value)
            plt.title('COUNTPLOT '+x_name+' for '+y_name+' : '+value)
            #plt.show()
    plt.subplot(srows,scols,len(ordery)+1)
    xfilter=df.loc[:,x_name]
    xvalue,orderx=top_vals(xfilter,cap=xcap,**kwargs)
    #top_order=xvalue.value_counts().iloc[:cap].index
    #print(df.info())
    #sns.countplot(data=df,x=x_name,order=orderx,hue=y_name)
    sns.countplot(xvalue,order=orderx)
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.title('total count of '+x_name)
    plt.show()
    #return (fi)
    return True

# In[81]:


def num_num(df,**kwargs):
    ####x is always df.iloc[0] , y is df.iloc[1]
    '''Docstring for plotting numerical vs numerical
    This method expects a dataframe as input with first column and second column as numerical column.
    Additionally you can provide a third categorical column that can act like a hue.
    NAN in x_axis and y_axis is ignored here
    It will output scatterplot
    x_name='xvalue' , the name that you want in x axis for the first column , 
            sometimes the column name are different from the name you want to see in the graph.By default the first column name is taken
    y_name='yvalue' , same as x_name , but for Y axis
    size_figure=(13,4) , for playing around with the size. depending on size of the screen you may want to  change it. default is 13,4
                 tight layout
    hue_col='hue_colname' , if you require an additional layer to add hue to the plot
    '''
    x_name = kwargs['x_name'] if 'x_name' in kwargs else df.columns[0]
    y_name = kwargs['y_name'] if 'y_name' in kwargs else df.columns[1]
    size_figure = kwargs['size_figure'] if 'size_figure' in kwargs else (13,4)
    hue_col = kwargs['hue_col'] if 'hue_col' in kwargs else None
    df.rename(columns = {df.columns[0]:x_name}, inplace=True)
    df.rename(columns = {df.columns[1]:y_name}, inplace=True)
    #print(kwargs)
    plt.figure(figsize=size_figure,tight_layout=True)
    sns.scatterplot(data=df,x=x_name,y=y_name,hue=hue_col)
    if not hue_col==None:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xticks(rotation=90)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    title_str='scatter plot for :'+x_name+' vs '+y_name
    plt.title(title_str)
    plt.show()
    return True