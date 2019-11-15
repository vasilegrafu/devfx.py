import numpy as np
import devfx.mathematics as math
from .. import distributions
from .. import series

""" Confidence intervals
"""
class ci(object):
    """================================================================================================
    """
    class mean(object):
        """--------------------------------------------------------------------------------------------
        """ 
        class normal(object):
            def __init__(self, data):       
                self.data = np.asarray(data)

            @property
            def data(self):
                return self.__data
            
            @data.setter   
            def data(self, data):
                self.__data = data


            def two_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0-ccoef/100.0
                if(sigma is not None): 
                    d = distributions.normal().icdf(1.0-alpha/2.0)
                    thetaL = mean-d*sigma/math.sqrt(n)
                    thetaU = mean+d*sigma/math.sqrt(n)
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha/2.0)
                    S = series.stddev(self.data)
                    thetaL = mean-d*S/math.sqrt(n)
                    thetaU = mean+d*S/math.sqrt(n)
                return (thetaL, thetaU)
                            
            def lower_one_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0-ccoef/100.0
                if(sigma is not None): 
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = mean-d*sigma/math.sqrt(n)
                    thetaU = +math.inf
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha)
                    S = series.stddev(self.data)
                    thetaL = mean-d*S/math.sqrt(n)
                    thetaU = +math.inf
                return (thetaL, thetaU)
                
            def upper_one_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0-ccoef/100.0
                if(sigma is not None): 
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = -math.inf
                    thetaU = mean+d*sigma/math.sqrt(n)
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha)
                    S = series.stddev(self.data)
                    thetaL = -math.inf
                    thetaU = mean+d*S/math.sqrt(n)
                return (thetaL, thetaU)
        
        """--------------------------------------------------------------------------------------------
        """
        class unknown(normal):
            def __init__(self, data):
                super().__init__(data)
         

    """================================================================================================
    """         
    class mean_difference(object):
        """--------------------------------------------------------------------------------------------
        """ 
        class normal(object):
            def __init__(self, data1, data2):       
                self.data1 = np.asarray(data1)
                self.data2 = np.asarray(data2)
            
            
            @property 
            def data1(self):
                return self.__data1
            
            @data1.setter   
            def data1(self, data1):
                self.__data1 = data1
        
            @property 
            def data2(self):
                return self.__data2
            
            @data2.setter   
            def data2(self, data2):
                self.__data2 = data2
        
        
            def two_sided(self, ccoef=95, sigmas=None):
                (n1, n2) = (self.data1.size, self.data2.size)
                (mean1, mean2) = (series.mean(self.data1), series.mean(self.data2))
                alpha = 1.0-ccoef/100.0
                if(sigmas is not None):
                    (sigma1, sigma2) = sigmas
                    d = distributions.normal().icdf(1.0-alpha/2.0)
                    thetaL = (mean1-mean2)-d*math.sqrt(sigma1**2/n1+sigma2**2/n2)
                    thetaU = (mean1-mean2)+d*math.sqrt(sigma1**2/n1+sigma2**2/n2)
                else:
                    (S1, S2) = (series.stddev(self.data1), series.stddev(self.data2))
                    n = math.floor((S1**2/n1+S2**2/n2)**2/((1.0/(n1-1))*(S1**2/n1)**2+(1.0/(n2-1))*(S2**2/n2)**2))
                    d = distributions.student(n).icdf(1.0-alpha/2.0)
                    thetaL = (mean1-mean2)-d*math.sqrt(S1**2/n1+S2**2/n2)
                    thetaU = (mean1-mean2)+d*math.sqrt(S1**2/n1+S2**2/n2)
                return (thetaL, thetaU)
                         
            def lower_one_sided(self, ccoef=95, sigmas=None):           
                (n1, n2) = (self.data1.size, self.data2.size)
                (mean1, mean2) = (series.mean(self.data1), series.mean(self.data2))
                alpha = 1.0-ccoef/100.0
                if(sigmas is not None):
                    (sigma1, sigma2) = sigmas
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = (mean1-mean2)-d*math.sqrt(sigma1**2/n1+sigma2**2/n2)
                    thetaU = +math.inf
                else:
                    (S1, S2) = (series.stddev(self.data1), series.stddev(self.data2))
                    n = math.floor((S1**2/n1+S2**2/n2)**2/((1.0/(n1-1))*(S1**2/n1)**2+(1.0/(n2-1))*(S2**2/n2)**2))
                    d = distributions.student(n).icdf(1.0-alpha)
                    thetaL = (mean1-mean2)-d*math.sqrt(S1**2/n1+S2**2/n2)
                    thetaU = +math.inf
                return (thetaL, thetaU)
                
            def upper_one_sided(self, ccoef=95, sigmas=None):           
                (n1, n2) = (self.data1.size, self.data2.size)
                (mean1, mean2) = (series.mean(self.data1), series.mean(self.data2))
                alpha = 1.0 - ccoef/100.0
                if(sigmas is not None):
                    (sigma1, sigma2) = sigmas
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = -math.inf
                    thetaU = (mean1-mean2)+d*math.sqrt(sigma1**2/n1+sigma2**2/n2)
                else:
                    (S1, S2) = (series.stddev(self.data1), series.stddev(self.data2))
                    n = math.floor((S1**2/n1+S2**2/n2)**2/((1.0/(n1-1))*(S1**2/n1)**2+(1.0/(n2-1))*(S2**2/n2)**2))
                    d = distributions.student(n).icdf(1.0-alpha)
                    thetaL = -math.inf
                    thetaU = (mean1-mean2)+d*math.sqrt(S1**2/n1+S2**2/n2)
                return (thetaL, thetaU)
        
        """--------------------------------------------------------------------------------------------
        """ 
        class unknown(normal):
            def __init__(self, data1, data2):       
                super().__init__(data1, data2)


    """================================================================================================
    """      
    class variance(object):
        """--------------------------------------------------------------------------------------------
        """ 
        class normal(object):
            def __init__(self, data):       
                self.data = np.asarray(data)
            
            
            @property 
            def data(self):
                return self.__data
            
            @data.setter   
            def data(self, data):
                self.__data = data
                
            
            def two_sided(self, ccoef=95):
                n = self.data.size
                S2 = series.var(self.data)
                alpha = 1.0-ccoef/100.0
                dL = distributions.chisquare(n-1).icdf(alpha/2.0)
                dU = distributions.chisquare(n-1).icdf(1.0-alpha/2.0)
                thetaL = (n-1)*S2/dU
                thetaU = (n-1)*S2/dL
                return (thetaL, thetaU)
                                       
            def lower_one_sided(self, ccoef=95):
                n = self.data.size
                S2 = series.var(self.data)
                alpha = 1.0-ccoef/100.0
                dU = distributions.chisquare(n-1).icdf(1.0-alpha)
                thetaL = (n-1)*S2/dU
                thetaU = +math.inf
                return (thetaL, thetaU)
                
            def upper_one_sided(self, ccoef=95):
                n = self.data.size
                S2 = series.var(self.data)
                alpha = 1.0-ccoef/100.0
                dL = distributions.chisquare(n-1).icdf(alpha)
                thetaL = math.zero
                thetaU = (n-1)*S2/dL
                return (thetaL, thetaU)
                
                    
    """================================================================================================
    """  
    class variance_ratio(object):
        pass
