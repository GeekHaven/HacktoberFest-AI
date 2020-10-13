import pandas as pd
import numpy as np
import warnings

#Dataframe for array
df = pd.read_csv('../datasets/ratings.csv')

#Getting out the required column for the array
df = df[['userId','movieId','rating']]

#Using Pandas Pivot for Generating The Required DataFrame
df = df.pivot('userId','movieId','rating')

#Filling nan values
df = df.fillna(0)
df

#Converting The DataFrame to Array
arr = np.array(df)

#Displaying the Array
print(arr)

#Installing SparseSVD
#pip install sparsesvd

#Importing Required Libraries, i.e., Scipy and SparseSVD for computing Singular Value Decomposition
import scipy.sparse
from sparsesvd import sparsesvd

smat = scipy.sparse.csc_matrix(arr) # convert to sparse CSC format

ut, s, vt = sparsesvd(smat, 50) # do SVD, asking for 55 factors

print(s.size)

#Calculating the predicted ratings
predicted_Ratings = np.dot(ut.T, np.dot(np.diag(s), vt))
print(predicted_Ratings)

#Using mean_squared_error to compute the RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt

#Calculating RMSE and MSE
rmse = sqrt(mean_squared_error(arr, predicted_Ratings,squared = False))
mse = sqrt(mean_squared_error(arr, predicted_Ratings,squared = True))

#Printing RMSE and MSE
print(rmse) #0.5532597908485468
print(mse) #0.30609639616977774

