#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('diabetes.csv')


# In[3]:


# Basic Exploration
print(data.head())  # Display the first few rows of the dataset
print(data.info())  # Summary information about the dataset (data types, non-null values, etc.)
print(data.describe())  # Summary statistics of numerical columns


# In[4]:


# Check for missing values
print(data.isnull().sum())


# In[5]:


# Data Visualization

# Pairplot to visualize relationships between variables
sns.pairplot(data, hue='Outcome')
plt.show()


# In[6]:


# Correlation heatmap to visualize correlation between variables
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[7]:


# Distribution of Outcome variable
sns.countplot(x='Outcome', data=data)
plt.title('Distribution of Outcome')
plt.show()


# In[ ]:




