#!/usr/bin/env python
# coding: utf-8

# In[32]:


import matplotlib.pyplot as plt

# Sample data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
student_grades = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Create scatter plot
plt.scatter(study_hours, student_grades, color='blue', marker='o')

# Add title and labels
plt.title('Correlation between Study Hours and Student Grades')
plt.xlabel('Study Hours')
plt.ylabel('Student Grades')

# Show plot
plt.grid(True)
plt.show()


# In[34]:


import matplotlib.pyplot as plt
import numpy as np
    
    # Sample data: average temperatures over the past 10 years for five cities
cities = ['City A', 'City B', 'City C', 'City D', 'City E']
avg_temperatures = [22.5, 25.3, 19.8, 23.1, 21.7]
    
    # Create a bar chart
fig, ax = plt.subplots()
bars = ax.bar(cities, avg_temperatures, color=['blue', 'green', 'red', 'purple', 'orange'])
    
    # Add labels and title
ax.set_xlabel('Cities')
ax.set_ylabel('Average Temperature (°C)')
ax.set_title('Average Temperatures of Five Cities Over the Past 10 Years')
    
    # Display the values on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 1), ha='center', va='bottom')
    
    # Show the plot
    plt.show()


# In[36]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dummy data for the past 6 months
dates = [datetime.now() - timedelta(days=x) for x in range(0, 180)]
prices = np.cumsum(np.random.normal(0, 2, 180)) + 200  # Simulating stock price variations

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Price': prices})

# Create an interactive line chart
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Price'],
    mode='lines+markers',
    name='Tesla Stock Price',
    hovertemplate='Date: %{x}<br>Price: $%{y:.2f}<extra></extra>'
))

# Customize layout
fig.update_layout(
    title='Tesla Stock Prices Over the Past 6 Months',
    xaxis_title='Date',
    yaxis_title='Stock Price ($)',
    hovermode='x unified',
    xaxis_rangeslider_visible=True,  # Enables zooming
    template='plotly_dark'  # Optional: Dark theme
)

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




