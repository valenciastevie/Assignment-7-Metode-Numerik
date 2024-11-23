import numpy as np
import scipy
import matplotlib.pyplot as plt


def my_poly(x):
    c0 = 4
    c1 = 0.45
    c2 = -0.967361111
    c3 = -0.0546875
    c4 = 0.0933159722
    c5 = 0.001171875
    c6 = -0.00193142362

    return c0 + c1 * x + c2 * x**2 + c3 * x**3 + c4 * x**4 + c5 * x**5 + c6 * x**6

x_no1 = np.linspace(start=-6, stop=6, num=1000)
y_no1 = my_poly(x_no1)
I1 = scipy.integrate.simpson (y=y_no1, x=x_no1)
print(f'(1) Analylitical value (approximation): {I1}')
# uncomment the plt.plot and plt.show to show the plot
# plt.plot(x_no1, y_no1)
# plt.show()


x_no2 = np.array([-6, 6])
y_no2 = my_poly(x_no2)
I2 = scipy.integrate.trapezoid (y=y_no2, x=x_no2)
print(f'(2) Trapezoidal: {I2}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no2, y_no2)
# plt.show()
# plt.legend()

# to find the exact same width for each segment (h: width of each segment, b:stop point, a:start point, n:segment)
# h = (a-b)/n
# h = (6-(-6))/6 = +2

# x0=-6
# x1=-4
# x2=-2
# x3=0
# x4=2
# x5=4
# x6=6

x_no3 = np.array([-6, -4, -2, 0, 2, 4, 6])
y_no3 = my_poly(x_no3)
I3 = scipy.integrate.trapezoid(y=y_no3, x=x_no3)
print(f'(3) Multiple Trapezoidal: {I3}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no3, y_no3)
# plt.show()
# plt.legend()

x_no4 = np.array ([-6, 0, 6])
y_no4 = my_poly(x_no4)
I4 = scipy.integrate.simpson(y=y_no4, x=x_no4)
print(f'(4) Simpson 1/3: {I4}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no4, y_no4)
# plt.show()
# plt.legend()

x_no5 = np.array ([-6, -4, -2, 0, 2, 4, 6])
y_no5 = my_poly(x_no5)
I5 = scipy.integrate.simpson(y=y_no5, x=x_no5)
print(f'(5) multiple Simpson 1/3: {I5}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no5, y_no5)
# plt.show()
# plt.legend()

x_no6 = np.array ([-6, -2, 2, 6])
y_no6 = my_poly(x_no6)
I6 = ((x_no6[-1] - x_no6[0])/8)*(y_no6[0] + 3*y_no6[1] + 3*y_no6[2] + y_no6[3])
print(f'(6) Simpson 3/8: {I6}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no6, y_no6)
# plt.show()
# plt.legend()

# The combination of multiple-application Simpson’s 1/3 Rule and Simpson’s 3/8 Rule, where the integration span is divided into 9 segments with equal length:
# h = (6-(-6))/9 = 4/3
# x0=-6
# x1=-14/3
# x2=-10/3
# x3=-2
# x4=-2/3
# x5=2/3
# x6=2
# x7=10/3
# x8=14/3
# x9=6

x_no7a = np.array ([-6, -14/3, -10/3, -2, -2/3, 2/3, 2])

# x_no7a = np.array ([-4, -3, -2, -1, 0, 1, 2])
y_no7a = my_poly(x_no7a)
I_13 = scipy.integrate.simpson(y=y_no7a, x=x_no7a)



x_no7b = np.array ([2, 10/3, 14/3, 6])

# x_no7b = np.array ([2, 3, 4, 5])
y_no7b= my_poly(x_no7b)
I_38 = ((x_no7b[-1] - x_no7b[0])/8)*(y_no7b[0] + 3*y_no7b[1] + 3*y_no7b[2] + y_no7b[3])

I7 = I_13+I_38
print(f'(7) Combination of Simpson 1/3 and 3/8: {I7}')
# uncomment the plt.plot and plt.show and plt.legend to show the plot
# plt.plot (x_no1, y_no1)
# plt.plot(x_no5, y_no5)
# plt.plot(x_no6, y_no6)
# plt.show()
# plt.legend()