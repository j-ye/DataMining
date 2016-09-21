import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

"""
GLD data set up
"""
# import data from csv, comma separated, first row is header
# use datatype as str, the default is float
GLD_data = np.genfromtxt('GLD.csv', delimiter=',', skip_header=2, dtype='str')
# only interested in the second column, which is closing price
GLD_X = GLD_data[:, 1]
# gets rid of the quotes, and converts price to float
GLD_X = np.char.strip(GLD_X, '"').astype(float)
# finally, calculate GLD return
GLD_X = np.diff(GLD_X) / GLD_X[1:]

GLD_X_train = GLD_X[:-20]
GLD_X_test = GLD_X[-20:]

"""
DUST data set up
-3X
"""
DUST_data = np.genfromtxt('DUST.csv', delimiter=',', skip_header=2, dtype='str')
DUST = DUST_data[:, 1]
DUST = np.char.strip(DUST, '"').astype(float)
DUST = np.diff(DUST) / DUST[1:]
DUST_train = DUST[:-20]
DUST_test = DUST[-20:]

"""
NUGT data set up
3X
"""
NUGT_data = np.genfromtxt('NUGT.csv', delimiter=',', skip_header=2, dtype='str')
NUGT = NUGT_data[:, 1]
NUGT = np.char.strip(NUGT, '"').astype(float)
NUGT = np.diff(NUGT) / NUGT[1:]
NUGT_train = NUGT[:-20]
NUGT_test = NUGT[-20:]

"""
investigate scatter plot, run regression GLD vs. DUST
"""
#first plot to visiualize the return of DUST against return of GLD
plt.scatter(GLD_X_train, DUST_train)
plt.xlabel('GLD return', fontsize=18)
plt.ylabel('DUST return', fontsize=18)

# the plot shows a strong, negative, linear relationship between GLD and DUST
DUSTvsGLD_regr = linear_model.LinearRegression()
DUSTvsGLD_regr.fit(GLD_X_train.reshape(len(GLD_X_train), 1),
	DUST_train.reshape(len(DUST_train), 1))
plt.draw()
raw_input() # "enter" to continue graphing
print 'Intercept:', DUSTvsGLD_regr.intercept_
print 'Coefficients:', DUSTvsGLD_regr.coef_
# mean squared error
print 'Residual sum of squares: %.2f' %np.mean((DUSTvsGLD_regr.predict(
	GLD_X_test.reshape(len(GLD_X_test), 1)) - DUST_test.reshape(len(DUST_test), 1)) ** 2)
# R squared
print 'R Squared: %.2f' % DUSTvsGLD_regr.score(GLD_X_test.reshape(len(GLD_X_test), 1), DUST_test.reshape(len(DUST_test), 1))
plt.scatter(GLD_X_train, DUST_train, color='black')
plt.plot(GLD_X_test, DUSTvsGLD_regr.predict(GLD_X_test.reshape(len(GLD_X_test), 1)),
	color='blue', linewidth=3)
plt.draw()
raw_input() # "enter" to continue

"""GLD vs NUGT"""
plt.figure() # new plot
#first plot to visiualize the return of DUST against return of GLD
plt.scatter(GLD_X_train, NUGT_train)
plt.draw()
raw_input()

plt.xlabel('GLD return', fontsize=18)
plt.ylabel('NUGT return', fontsize=18)

# the plot shows a strong, negative, linear relationship between GLD and DUST
NUGTvsGLD_regr = linear_model.LinearRegression()
NUGTvsGLD_regr.fit(GLD_X_train.reshape(len(GLD_X_train), 1),
	NUGT_train.reshape(len(NUGT_train), 1))
print 'Intercept:', NUGTvsGLD_regr.intercept_
print 'Coefficients:', NUGTvsGLD_regr.coef_
# mean squared error
print 'Residual sum of squares: %.2f' %np.mean((NUGTvsGLD_regr.predict(
	GLD_X_test.reshape(len(GLD_X_test), 1)) - NUGT_test.reshape(len(NUGT_test), 1)) ** 2)
# R squared
print 'R Squared: %.2f' % NUGTvsGLD_regr.score(GLD_X_test.reshape(len(GLD_X_test), 1), NUGT_test.reshape(len(DUST_test), 1))
plt.scatter(GLD_X_train, NUGT_train, color='black')
plt.plot(GLD_X_test, NUGTvsGLD_regr.predict(GLD_X_test.reshape(len(GLD_X_test), 1)),
	color='red', linewidth=3)
plt.draw()
plt.show()
