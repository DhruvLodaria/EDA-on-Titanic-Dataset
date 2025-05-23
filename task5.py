# -*- coding: utf-8 -*-
"""Task5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e7rd94KzVisA_i4do0KOvXGc7d5AELVh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/content/Titanic dataset .csv")

data

data.info()

data.describe()

data.isnull().sum()

data["Age"].fillna(data["Age"].mean(), inplace=True)

data.isnull().sum()

data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

data.isnull().sum()

data = data.drop(columns=['Cabin'])

data

#HISTOGRAM
data['Age'].hist(bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')
plt.show()

#COUNT PLOT
sns.countplot(x='Pclass',data=data)
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Passenger Class Distribution')
plt.show()

#SCATTERPLOT
sns.scatterplot(x='Age',y='Fare',data=data)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs Fare')
plt.show()

#BOXPLOT
sns.boxplot(x='Sex',y='Age',data=data)
plt.xlabel('Sex')
plt.ylabel('Age')
plt.title('Age Distribution by Sex')
plt.show()

#COUNT PLOT
sns.countplot(x='Sex',hue='Survived',data=data)
plt.xlabel('Sex')
plt.ylabel('Survived')
plt.title('Passenger Survival Distribution by Sex')
plt.show()

#CORRELATION MATRIX
numerical_data=data.select_dtypes(include=[np.number])
correlation_matrix=numerical_data.corr()
correlation_matrix

#HEATMAP
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

