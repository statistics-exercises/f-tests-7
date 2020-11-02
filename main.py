import numpy as np
import scipy.stats

def sample_variance( data ) : 
  # Your code to calculate the sample variance from the data in 
  # the numpy array called data goes here
  
  
def testStatistic( data1, data2 ) : 
  # Your code to compute the test statistic should be inserted here.
  # Remember to use calls to sample_variance to lower the ammount of
  # code you are writing
  
def pvalue( data1, data2 ) : 
  F = testStatistic( data1, data2 )
  # Your code to calculate the  p-value given the value of the 
  # test statistic (F) should go here.
  

data1 = np.array([-0.90, -0.12, 1.92, 1.68, -2.74])
data2 = np.array([-1.04, -0.97, -0.95, -1.01, -1.28, -0.21, -0.98, -0.22, 1.71, -1.73])
print("Null hypothesis: the distribution that was sampled to generate the data in the")
print("numpy array data1 has a variance that is 8 times the variance of the distribution")
print("that was sampled to generate the values in the NumPy array data2.")
print("Alternative hypothesis: the distribution that was sampled to generate the data in the")
print("numpy array data1 has a variance that is not 8 times the variance of the distribution")
print("that was sampled to generate the values in the NumPy array data2.")
print("The p-value for this hypothesis test is", pvalue( data1, data2 ) )
