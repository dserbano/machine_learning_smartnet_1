import numpy 
import matplotlib.pyplot as plt 
import random
import math
import os

def column(matrix, i):
    return [row[i] for row in matrix]

def print_figure(figure_name):
    
    figure_path = os.path.join(os.path.join(os.getcwd(), "figures"))
    
    if os.path.isdir(figure_path):
        plt.savefig(os.path.join(figure_path, figure_name), quality=99)
    else:
        os.mkdir(figure_path)
        plt.savefig(os.path.join(figure_path, figure_name), quality=99)
    
    return

def covariance_sigma(X, sigma2_0, sigma2_n):
    XX_transpose = numpy.dot(numpy.transpose(X), X)
    covariance_sigma = numpy.linalg.inv((1/sigma2_0)*numpy.identity(XX_transpose.__len__())\
                                        + (1/sigma2_n)*XX_transpose)
    return covariance_sigma

def bayesian_inference_mean_theta_y(X, Y, sigma2_0, sigma2_n, theta_0):
    mean = theta_0 + (1/sigma2_n)*numpy.dot(numpy.dot(covariance_sigma(X, sigma2_0, sigma2_n),\
                                            numpy.transpose(X)), Y - numpy.dot(X, theta_0))
    return mean

def bayesian_inference_mean_y(X, mean_theta):
    mean = []
    for i in range(0, X.__len__()):
        res = numpy.dot(numpy.transpose(X[i]), mean_theta)
        mean.append(res)       
    return mean

def bayesian_inference_variance_y(X, sigma2_0, sigma2_n):
    variance = []
    XX_transpose = numpy.dot(numpy.transpose(X), X)
    for i in range(0, X.__len__()):
        term = numpy.linalg.inv(sigma2_n*numpy.identity(XX_transpose.__len__()) + sigma2_0*XX_transpose)
        res = sigma2_n + sigma2_n*sigma2_0*sigma2_n*numpy.dot(numpy.dot(numpy.transpose(X[i]), term), X[i])
        variance.append(res)       
    return variance


def exercise1_5(Ns, sigma2_0_list, sigma2_n, theta_0, theta_true):
    
    iterations = 0
    
    for i in range(0, Ns.__len__()):
        
        N = Ns[i]
        
        N_points = numpy.arange(0, 2, 2/float(N))
        
        X_true = []
        for z in range(0, N):
            x = N_points[z]
            X_true.append([1, x, x**2, x**3, x**5])
            
        Y_true = numpy.dot(X_true, theta_true)
        
        X = []
        for z in range(0, N):
            x = random.uniform(0, 2)
            X.append([1, x, x**2, x**3, x**5])
            
        X.sort()
        

        Y = numpy.dot(X, theta_true) + numpy.random.normal(0, math.sqrt(sigma2_n), X.__len__())
        
        for j in range(0, sigma2_0_list.__len__()):
            
            sigma2_0 = sigma2_0_list[j]
         
            mean_theta = bayesian_inference_mean_theta_y(X, Y, sigma2_0, sigma2_n, theta_0)
            
            mean_y = bayesian_inference_mean_y(X, mean_theta)
            variance_y = bayesian_inference_variance_y(X, sigma2_0, sigma2_n)
            
            plt.title('Exercise 1_5_' + chr(ord('`') + (iterations + 1)))
            plt.xlabel('x')
            plt.ylabel('y')
            plt.axis([N_points[0], N_points[-1], -0.3, 2])
            plt.plot(0, label='sigma2_0='+str(sigma2_0), color='white')
            plt.plot(0, label='N='+str(N), color='white')
            plt.plot(N_points, Y_true, label='true curve', color='red')  
            plt.plot(column(X, 1), mean_y, label='mean curve fitting the data', color='grey')
            plt.errorbar(column(X, 1), mean_y, yerr=variance_y, fmt='.k')           
            plt.legend(bbox_to_anchor=(0.47, 1.0), fontsize='small')        
            print_figure("exercise1_5_" + chr(ord('`') + (iterations + 1)))
            
            iterations = iterations + 1

            plt.show()
    


exercise1_5([20, 500], [0.1, 2], 0.05, [-10.54, 0.465, 0.0087, -0.093, -0.004], [0.2, -1, 0.9, 0.7, -0.2])
