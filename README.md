# Two-tailed f-tests

Now that you have established that you can perform one-tailed hypothesis tests on the ratios of sample variances lets consider how to do a two-tailed test with this distribution.

I want you to test whether there is sufficient evidence to state that I am lying when I tell you that the variance of the distribution from which I generated the data in the NumPy array called data1 is 8 times greater than the variance of the distribution that was sampled in generating the values in data2.  In other words, you are going to have to test:

![](https://render.githubusercontent.com/render/math?math=H_0:\frac{\sigma_1^2}{\sigma_2^2}=1\qquad\textrm{against}\qquad\H_1:\frac{\sigma_1^2}{\sigma_2^2}\ne\1) 

I have laid out the functions that you need to complete in the same way as the functions were laid out in the previous exercises.  __You will need to complete all these functions in order to pass the task.__

Notice that we do two-tail tests differently when we use the f-distribution.  Instead of considering both tails of the distribution we instead __always__ divide the larger of the two calculated sample variances by the smaller.  The test statistic is thus __always__ greater than 1.  You thus only need to consider one tail when you compute the p-value. 
