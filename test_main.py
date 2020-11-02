import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sample_var(self) : 
        for i in range(5) : 
            tdata = np.random.normal(0,1,size=100)
            mu = sum(tdata) / len(tdata)
            var = (len(tdata) / (len(tdata)-1))*( sum(tdata*tdata) / len(tdata) - mu*mu )
            self.assertTrue( np.abs( var - sample_variance(tdata) )<1e-7, "Your code for calculating the sample variance is not correct" )
            
    def test_testStatistic(self) : 
        var1, var2 = sample_variance(data1), sample_variance(data2)
        if var1>var2 : T = var1 / var2 
        else : T = var2 / var1
        self.assertTrue( testStatistic(data1, data2)>1, "The test statistic should be greater than one.  Read the note at the end of the explanation of the exercise." )
        self.assertTrue( np.abs( T - testStatistic(data1, data2))<1e-7, "Your code for calculating the test statistic is not correct"  )
        
    def test_pvalue(self) : 
        stat = testStatistic( data1, data2 )
        if sample_variance( data1) > sample_variance(data2) : 
           pval = 1 - scipy.stats.f.cdf( stat, len(data1)-1, len(data2)-1 )
        else :
           pval = 1 - scipy.stats.f.cdf( stat, len(data2)-1, len(data1)-1 )
        self.assertTrue( np.abs( pvalue(data1,data2) - pval)<1e-7, "Your code for calculating the p-value is not correct" )
        stat = testStatistic( data1, data2 )
        if sample_variance( data1) > sample_variance(data2) : 
           pval = 1 - scipy.stats.f.cdf( stat, len(data2)-1, len(data1)-1 )
        else :
           pval = 1 - scipy.stats.f.cdf( stat, len(data1)-1, len(data2)-1 )
        self.assertFalse( np.abs( pvalue(data1,data2) - pval)<1e-7, "Notice that you need to account for the number of degrees of freedom for the two variances correctly.  The first number of degrees of freedom you pass to f is related to the number of variables that were used to calculate the variance in the numerator.  The second number is related to the number of variables that were used to calculate the variance in the denominator.  As you are checking which is the larger variance and ensuring it is in the numerator you need to ensure that the degrees of freedom are set correctly." )
