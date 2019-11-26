import numpy 
import matplotlib.pyplot as plt 
import random
import math
import regression

#   MSE = E[(theta - theta_0)**2]
#   In general E[X] = x_1*p_1 + x_2*p_2 + ... + x_n*p_n which is the average for uniform distribution
#   How to calculate MSE: for every possible value of theta for every training set, subtract it 
#   from theta_0, square it, find the mean for all these theta's
        

def exercise13(N, test, mu, sigma_square, theta_0):
    #Generate N equidistant value points in the interval [0, N]
    N_points = numpy.arange(0, 2, 2/float(N))
    
    #create X using the N points in the interval [0, N]
    X = []
    for i in range(0, N):
        X.append(regression.polynomial_5th_X(N_points[i]))

    Y_true = regression.polynomial_equation(X, theta_0, 0)

    #find Y by multiplying X with theta_0 and adding gaussian eta
    Y_0 = regression.polynomial_equation(X, theta_0, regression.normal_noise(mu, sigma_square, X.__len__()))

    #find the theta using least squares, that is find the regression line using the 20 points and Y
    theta_1 = regression.ridge_regression(X, Y_0, 0.000006)
    theta_2 = regression.ridge_regression(X, Y_0, 0.01)
    theta_3 = regression.ridge_regression(X, Y_0, 0.2)

    Y_ridge_1 = regression.polynomial_equation(X, theta_1, 0)
    Y_ridge_2 = regression.polynomial_equation(X, theta_2, 0)
    Y_ridge_3 = regression.polynomial_equation(X, theta_3, 0)

    #create a test set and correspondent Y
    X_test = []
    for i in range(0, test):
        X_test.append(regression.polynomial_5th_X(random.choice(N_points)))

    #find Y_test
    Y_0_test = regression.polynomial_equation(X_test, theta_0, regression.normal_noise(mu, sigma_square, X_test.__len__()))

    Y_test_1 = regression.polynomial_equation(X_test, theta_1, 0)
    Y_test_2 = regression.polynomial_equation(X_test, theta_2, 0)
    Y_test_3 = regression.polynomial_equation(X_test, theta_3, 0)



    #find mean square error
    mse1 = sum((Y_0 - Y_ridge_1)**2)/20
    mse2 = sum((Y_0 - Y_ridge_2)**2)/20
    mse3 = sum((Y_0 - Y_ridge_3)**2)/20

    mse4 = sum((Y_test_1 - Y_0_test)**2)/1000
    mse5 = sum((Y_test_2 - Y_0_test)**2)/1000
    mse6 = sum((Y_test_3 - Y_0_test)**2)/1000

    print(mse1, mse2, mse3, mse4, mse5, mse6)

    plt.plot(N_points, Y_0, 'o', label='noisy training set points', color='grey')
    plt.plot(N_points, Y_0, label='curve fitting the data', color='black')
    plt.plot(N_points, Y_true, label='true curve', color='blue')

    plt.plot(N_points, Y_ridge_1, label='fitted data ridge with l=0.000006', color='#339900')
    plt.plot(N_points, Y_ridge_2, label='fitted data ridge with l=0.01', color='#33CC66')
    plt.plot(N_points, Y_ridge_3, label='fitted data ridge with l=0.2', color='#33CC66')

    plt.show()




exercise13(20, 1000, 0, 0.1, [0.2, -1, 0.9, 0.7, 0, -0.2])


