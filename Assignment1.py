import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def co2(co2_df):
    '''Function create a stacked line plot which displays top 5 countries
    and their CO2 emissions for 4 years. The argument is a dataframe which is
    used to read a csv file which contains the data for CO2 emission.'''
    #setting the font sizes
    font1 = {'fontsize' : 18} 
    font2 = {'fontsize' : 15}
    #Setting the size of the sheet
    plt.rcParams['figure.figsize'] = (10, 8)
    #Displays the exact values on the y axis instead of exponential forms
    plt.ticklabel_format(style = 'plain')
    #Plotting the line graphs
    plt.plot(co2_df['Country Name'], co2_df['1990 [YR1990]'], label = '1990',
             marker = 'o')
    plt.plot(co2_df['Country Name'], co2_df['2000 [YR2000]'], label = '2000',
             marker = 'o')
    plt.plot(co2_df['Country Name'], co2_df['2010 [YR2010]'], label = '2010', 
             marker = 'o')
    plt.plot(co2_df['Country Name'], co2_df['2019 [YR2019]'], label ='2019', 
             marker = 'o')
    #Displays the legends and shows the spacing between them.
    plt.legend(labelspacing = 1.2)
    #Displays the title and the labels for x axis and y axis.
    plt.title('CO2 EMISSIONS FOR TOP5 COUNTRIES', **font1, fontweight = 'bold')
    plt.xlabel('COUNTRIES', **font1)
    plt.ylabel('CO2 EMISSION in KT', **font1)
    plt.xticks(**font2)
    plt.yticks(**font2)
    plt.grid(zorder = 0)
    #Setting the xlim so the lines start from the 0 of x axis.
    plt.xlim(['India', 'Japan'])
    plt.show()
    return


def methane(methane_df):
    '''Function create a grouped bar chart which displays top 5 countries 
    and their methane emissions for 4 years. The argument is a dataframe which
    is used to read a csv file which contains the data for methane emission.'''
    #setting the font sizes
    font1 = {'fontsize' : 18}
    font2 = {'fontsize' : 15}
    #Setting the size of the sheet.
    plt.rcParams['figure.figsize'] = (10, 6)
    width = 0.2
    #Displays the exact values on the y axis instead of exponential forms.
    plt.ticklabel_format(style = 'plain')
    countries = methane_df['Country Name']
    values = np.arange(len(countries))
    #plotting the grouped bar plots
    plt.bar(values, methane_df['1990 [YR1990]'], width,  label = '1990')
    plt.bar(values+width, methane_df['2000 [YR2000]'],
    width, label = '2000')
    plt.bar(values+width+width, methane_df['2010 [YR2010]'],
    width, label = '2010')
    plt.bar(values+width+width+width, methane_df['2019 [YR2019]'],
    width, label = '2019')
    plt.xticks(values+0.1,countries)
    plt.legend()    
    #Displays the title, labels for x axis and y axis.
    plt.title('METHANE EMISSIONS FOR TOP 5 COUNTRIES', **font1,
              fontweight = 'bold')
    plt.xlabel('COUNTRIES', **font1)
    plt.ylabel('METHANE EMISSION in KT', **font1)
    plt.xticks(**font2)
    plt.yticks(**font2)
    plt.grid(zorder=0)
    plt.show() 
    return                                        
    
    
def population_vs_co2(population_df, co2_df ):
    '''Function compares the population distribution for 5 countries 
    for the year 2019 and the CO2 emission for the year 2019 and compares
    the both values.''' 
    #Setting the font size
    font1 = {'fontsize' : 18}
    font2 = {'fontsize' : 15}
    #Changing the sheet size.
    plt.rcParams['figure.figsize'] = (12, 6) 
    plt.ticklabel_format(style = 'plain')
    #Creating the partitions for subplots
    plt.subplot(1, 2, 1)
    plt.title('POPULATION DISTRIBUTION of 2019', **font1 )
    #Plotting the pie chart.
    plt.pie(x = population_df['2019 [YR2019]'], shadow = True,
    labels = population_df['Country Name'], autopct = '%1.1f%%', 
    textprops = {'fontsize' : 15})
    plt.text(1.4, -1.8, "POPULATION DISTRIBUTION vs CO2 EMISSION FOR 2019", 
             ha = 'center', **font2, fontweight = 'bold')
    #Making a donut chart.
    circle = plt.Circle(xy = (0, 0), radius = 0.80, facecolor = 'white')
    plt.gca().add_artist(circle)
    
    #Creating the partition for subplots.
    plt.subplot(1, 2, 2) 
    #Displays the title and the label for x axis.
    plt.title('CO2 EMISSION of 2019', **font1)
    plt.xlabel('COUNTRIES', **font2)
    #Displays the exact values on the y axis instead of exponential forms.
    plt.ticklabel_format(style = 'plain')
    #Plotting the bar chart.
    plt.bar(co2_df['Country Name'], co2_df['2019 [YR2019]'], label = '2019')
    plt.xticks(**font2)
    #Changing the values on the y axis from millions to another form.
    plt.yticks([2000000, 4000000, 6000000, 8000000, 10000000], 
               ["2M", "4M", "6M", "8M", "10M"], **font2)
    plt.grid(zorder=0)
    plt.show()
    return
    
#Reading all the data.
co2_df = pd.read_csv("C:/Users/anton/Desktop/Clean files/Co2_5.txt") 
methane_df = pd.read_csv("C:/Users/anton/Desktop/Clean files/Methane_5.txt") 
pop_df = pd.read_csv("C:/Users/anton/Desktop/Clean files/Population_5.txt")   
#Calling the functions.
co2(co2_df)
methane(methane_df) 
population_vs_co2(pop_df, co2_df) 