# Data Analysis
import pandas as pd
import numpy as np
# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# ML
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Set up Data
df = pd.read_csv('USA_Housing.csv')

df.head()
df.info()
df.describe()
df.columns

# plt.figure()

# Quick plot of all data
sns.pairplot(df)
# Predict Price of House
sns.displot(df['Price'])
# Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(), annot =True)

# LR P1
# Feature Set
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
# What is trying to be predicted
y = df['Price']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)
# print(lm.intercept_)

# lm.coef_
# X_train.columns

# If we hold all other vars fixed, a one unit increase in X increases Coeff Price by #
cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

# LR P2
# Predict with test data
predictions = lm.predict(X_test)

# Show Diff
plt.figure()
plt.scatter(y_test, predictions)
sns.displot((y_test-predictions))

# Error
# MAE
print(f"Mean Absolute Error: {metrics.mean_absolute_error(y_test, predictions)}")
# MSE
print(f"Mean Squared Error: {metrics.mean_squared_error(y_test, predictions)}")
# RMSE
print(f"Root Mean Squared Error: {np.sqrt(metrics.mean_squared_error(y_test, predictions))}")


plt.show()
#%%
