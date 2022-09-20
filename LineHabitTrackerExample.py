# LineHabitTrackerExample.py, line chart example

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Create dictionary to assign values to yes no
booleanDictionary = {'Yes': 1, 'No': 0}

# Read in HabitTracker CSV, then reasign to broken out dataframes
df = pd.read_csv('travel/HabitTracker.csv')
dfCoding =  df.get(['Date','Coding'])
dfCreativity =  df.get(['Date','Creativity'])
dfFasting =  df.get(['Date','Fasting'])
dfFitness =  df.get(['Date','Fitness'])
dfGardening =  df.get(['Date','Gardening'])
dfGratitude =  df.get(['Date','Gratitude'])
dfMeditation =  df.get(['Date','Meditation'])
dfReading =  df.get(['Date','Reading'])
dfStudy =  df.get(['Date','Study'])
dfYoga =  df.get(['Date','Yoga'])
dfZettel =  df.get(['Date','Zettel'])

# Add new columns
dfCoding['Count'] = df['Coding'].map(booleanDictionary)
dfCoding['Month'] = pd.DatetimeIndex(df['Date']).month
dfCreativity['Count'] = df['Creativity'].map(booleanDictionary)
dfCreativity['Month'] = pd.DatetimeIndex(df['Date']).month
dfFasting['Count'] = df['Fasting'].map(booleanDictionary)
dfFasting['Month'] = pd.DatetimeIndex(df['Date']).month
dfFitness['Count'] = df['Fitness'].map(booleanDictionary)
dfFitness['Month'] = pd.DatetimeIndex(df['Date']).month
dfGardening['Count'] = df['Gardening'].map(booleanDictionary)
dfGardening['Month'] = pd.DatetimeIndex(df['Date']).month
dfGratitude['Count'] = df['Gratitude'].map(booleanDictionary)
dfGratitude['Month'] = pd.DatetimeIndex(df['Date']).month
dfMeditation['Count'] = df['Meditation'].map(booleanDictionary)
dfMeditation['Month'] = pd.DatetimeIndex(df['Date']).month
dfReading['Count'] = df['Reading'].map(booleanDictionary)
dfReading['Month'] = pd.DatetimeIndex(df['Date']).month
dfStudy['Count'] = df['Study'].map(booleanDictionary)
dfStudy['Month'] = pd.DatetimeIndex(df['Date']).month
dfYoga['Count'] = df['Yoga'].map(booleanDictionary)
dfYoga['Month'] = pd.DatetimeIndex(df['Date']).month
dfZettel['Count'] = df['Zettel'].map(booleanDictionary)
dfZettel['Month'] = pd.DatetimeIndex(df['Date']).month

# Create a series from the aggregation
dfCodSeries = pd.Series(data=dfCoding.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Coding").rename_axis("month", axis=0)    
dfCreSeries = pd.Series(data=dfCreativity.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Creativity").rename_axis("month", axis=0)
dfFasSeries = pd.Series(data=dfFasting.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Fasting").rename_axis("month", axis=0)
dfFitSeries = pd.Series(data=dfFitness.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Fasting").rename_axis("month", axis=0)  
dfGarSeries = pd.Series(data=dfGardening.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Fasting").rename_axis("month", axis=0)                                                    
dfGraSeries = pd.Series(data=dfGratitude.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Gratitude").rename_axis("month", axis=0)
dfMedSeries = pd.Series(data=dfMeditation.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Meditation").rename_axis("month", axis=0)                        
dfReaSeries = pd.Series(data=dfReading.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Reading").rename_axis("month", axis=0)  
dfStuSeries = pd.Series(data=dfStudy.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Reading").rename_axis("month", axis=0)   
dfYogSeries = pd.Series(data=dfYoga.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Reading").rename_axis("month", axis=0)                                                                          
dfZetSeries = pd.Series(data=dfZettel.groupby("Month")["Count"].sum(),
                        index=[1,2,3,4,5,6,7,8,9,10,11,12],
                        name="Zettel").rename_axis("month", axis=0)  

# Local collection to plot in the graph
xCod = dfCodSeries.index
yCod = dfCodSeries.values
xCre = dfCreSeries.index
yCre = dfCreSeries.values
xFas = dfFasSeries.index
yFas = dfFasSeries.values
xFit = dfFitSeries.index
yFit = dfFitSeries.values
xGar = dfGarSeries.index
yGar = dfGarSeries.values
xGra = dfGraSeries.index
yGra = dfGraSeries.values
xMed = dfMedSeries.index
yMed = dfMedSeries.values
xRea = dfReaSeries.index
yRea = dfReaSeries.values
xStu = dfStuSeries.index
yStu = dfStuSeries.values
xYog = dfYogSeries.index
yYog = dfYogSeries.values
xZet = dfZetSeries.index
yZet = dfZetSeries.values


# Draw the lines
trace1 = go.Scatter(x=xCod,y=yCod,mode='lines+markers',name='Coding')
trace2 = go.Scatter(x=xCre,y=yCre,mode='lines+markers',name='Creativity')
trace3 = go.Scatter(x=xFas,y=yFas,mode='lines+markers',name='Fasting')
trace4 = go.Scatter(x=xFit,y=yFit,mode='lines+markers',name='Fitness')
trace5 = go.Scatter(x=xGar,y=yGar,mode='lines+markers',name='Gardening')
trace4 = go.Scatter(x=xGra,y=yGra,mode='lines+markers',name='Gratitude')
trace5 = go.Scatter(x=xMed,y=yMed,mode='lines+markers',name='Meditation')
trace6 = go.Scatter(x=xRea,y=yRea,mode='lines+markers',name='Reading')
trace7 = go.Scatter(x=xStu,y=yStu,mode='lines+markers',name='Study')
trace8 = go.Scatter(x=xYog,y=yYog,mode='lines+markers',name='Yoga')
trace9 = go.Scatter(x=xZet,y=yZet,mode='lines+markers',name='Zettel')



# Assign values to the Data Object, and since this is a list, you plot multiple lines
data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9]

# Assign values to the Layout Object
layout = go.Layout(title='Habit Tracker')

# Create Figure object to display data with layout
fig = go.Figure(data=data,layout=layout)

# Create graph with Figure object
pyo.plot(fig,filename='HabitTrackerChart.html')