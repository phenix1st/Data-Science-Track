import numpy as np
import matplotlib.pyplot as plt 

year = [100,200,500,600,900]
pop = [1.2, 1.5, 1.9, 2.5 ,3]
 
plt.plot(year, pop) # this will make a line chart in which pop is the vertical line and year is the horizontal line 
plt.scatter(year,pop) # it gives tha same result as plot the difference is the dots are not connected it gives every point and its value 
plt.show()

# --- challnege ---
#Now that you've built your first line plot, let's start working on the data that professor Hans Rosling used to build his beautiful bubble chart. It was collected in 2007. Two lists are available for you:
#life_exp which contains the life expectancy for each country and
#gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.
#GDP stands for Gross Domestic Product. It basically represents the size of the economy of a country. Divide this by the population and you get the GDP per capita.
#matplotlib.pyplot is already imported as plt, so you can get started straight away.
#--- solution ---
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

#--- challenge 2---
"""When you have a time scale along the horizontal axis, the line plot is your friend. But in many other cases, when you're trying to assess if there's a correlation between two variables, for example, the scatter plot is the better choice. Below is an example of how to build a scatter plot.

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()
Let's continue with the gdp_cap versus life_exp plot, the GDP and life expectancy data for different countries in 2007. Maybe a scatter plot will be a better alternative?

Again, the matplotlib.pyplot package is available as plt."""
#--- solution -- 
# Import package
import matplotlib.pyplot as plt 

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

#---- histogram ---
"""life_exp, the list containing data on the life expectancy for different countries in 2007, is displayed.

To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.

matplotlib.pyplot is already available as plt."""
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# --- challnege ---
"""plt.clf() in Python refers to matplotlib.pyplot.clf(), a function used to clear the entire current figure in Matplotlib."""
import matplotlib.pyplot as plt

# Create a figure and plot some data
plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Original Plot")
plt.show(block=False) # Keep the window open for demonstration

# Clear the figure and plot new data
plt.clf()
plt.plot([1, 2, 3], [6, 5, 4])
plt.title("New Plot after clf()")
plt.show() 

# --- challnege ---
"""
In Python, the choice between a histogram, a scatter plot, or a general plot using plt.plot() depends on the type of data and the insights one aims to extract:
1. Histogram:
When to use: Histograms are used to visualize the distribution of a single numerical variable. They divide the data into "bins" and show the frequency or count of data points falling within each bin.
Purpose: To understand the shape, spread, and central tendency of a dataset, identify outliers, or check if the data follows a particular distribution (e.g., normal distribution).
Example: Visualizing the distribution of student test scores, heights of individuals, or response times in an experiment.
2. Scatter Plot:
When to use: Scatter plots are used to visualize the relationship between two numerical variables. Each point on the plot represents a pair of values for these two variables.
Purpose: To identify patterns, trends, correlations (positive, negative, or no correlation), or clusters between two variables.
Example: Plotting the relationship between study hours and exam scores, or between advertising spend and sales revenue. 
3. plt.plot() (for line plots and general 2D plots):
When to use: The plt.plot() function in Matplotlib is versatile and can be used for various 2D plots, most commonly line plots to show changes over time or continuous trends. It can also be used to create simple scatter plots if only markers are specified without a connecting line.
Purpose:
Line plots: To visualize trends or changes in a variable over a continuous axis, typically time.
General 2D plots: To plot data points, customize line styles, markers, and colors for diverse visualizations. """

# --- challnege ---
"""The customizations you've coded up to now are available in the script, in a more concise form.

In the video, Hugo has demonstrated how you could control the y-ticks by specifying two arguments:

plt.yticks([0,1,2], ["one","two","three"])
In this example, the ticks corresponding to the numbers 0, 1 and 2 will be replaced by one, two and three, respectively.

Let's do a similar thing for the x-axis of your world development chart, with the xticks() function. The tick values 1000, 10000 and 100000 should be replaced by 1k, 10k and 100k. To this end, two lists have already been created for you: tick_val and tick_lab."""

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

# -- challenge ----
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop= np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# challenge 
"""Sizes
Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population?

To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country expressed in millions. You can see that this list is added to the scatter method, as the argument s, for size.

"""
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop= np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

#--------------------------
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col,  alpha = 0.8 )

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show() 
"""The code you've written up to now is available in the script.

The next step is making the plot more colorful! To do this, a list col has been created for you. It's a list with a color for each corresponding country, depending on the continent the country is part of.

How did we make the list col you ask? The Gapminder data contains a list continent with the continent each country belongs to. A dictionary is constructed that maps continents onto colors:

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
Nothing to worry about now; you will learn about dictionaries in the next chapter."""
"""
Daily XP
1400
Exercise
Exercise
Colors
The code you've written up to now is available in the script.

The next step is making the plot more colorful! To do this, a list col has been created for you. It's a list with a color for each corresponding country, depending on the continent the country is part of.

How did we make the list col you ask? The Gapminder data contains a list continent with the continent each country belongs to. A dictionary is constructed that maps continents onto colors:

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
Nothing to worry about now; you will learn about dictionaries in the next chapter.

Instructions
100 XP
Add c = col to the arguments of the plt.scatter() function.
Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent"""

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China') # it shows the word china in front the bubble of china its self in the plot

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()