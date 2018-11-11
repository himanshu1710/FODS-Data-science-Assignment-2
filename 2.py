import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
import scipy
from mpl_toolkits.mplot3d import Axes3D

def circle(n,name):
	x=[]
	y=[]
	for i in range(n):
		x.append(np.random.uniform(-2,2))
		y.append(np.random.uniform(-2,2))
	a=0
	r=2
	func=[]
	for i in range(n):
		if(x[i]**2+y[i]**2<=r**2):
			a=a+1
			func.append('b')
		else:
			func.append('r')

	a=a*4
	i=a/n
	plt.title("Estimation from Circle")
	plt.scatter(x ,y , c=func)
	plt.savefig("figure_circle"+str(name)+".png")
	plt.show()
	return i
def sphere(n,name):
	x=[]
	y=[]
	z=[]
	for i in range(n):
		x.append(np.random.uniform(-2,2))
		y.append(np.random.uniform(-2,2))
		z.append(np.random.uniform(-2,2))
	a=0
	r=2
	func=[]
	for i in range(n):
		if(x[i]**2+y[i]**2+z[i]**2<=r**2):
			a=a+1
			func.append('b')
		else:
			func.append('r')

	a=a*6
	i=a/n
	#plt.title("Estimation from Sphere")
	#plt.scatter(x,y,z,c=func)
	#plt.show()
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	ax.scatter(x,y,z,c=func)
	plt.title("Estimation from Sphere")
	plt.savefig("figure_sphere"+str(name)+".png")
	plt.show()
	return i

value=[10,100,1000,10000,100000,1000000,10000000]
name1=1
name2=1
for l in value:
	res_circle=circle(l,name1)
	name1=name1+1
	print("For circle")
	print(res_circle)
	res_sphere=sphere(l,name2)
	name2=name2+1
	print("For sphere")
	print(res_sphere)
	print("Difference of sphere and circle")
	print(res_sphere-res_circle)
	

	
