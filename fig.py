from matplotlib import pyplot as plt
import numpy as np
from matplotlib import gridspec 


def fraw(xf, yf):
	gs=gridspec.GridSpec(2,2)
	x=np.arange(-np.pi, np.pi, 0.001)
	y1=np.sin(x*xf)
	y2=np.sin(x*yf)
	y3=y1*y2
	fig = plt.figure()
	p1 = fig.add_subplot(gs[0,0])
	p1.set_xlabel(f"y=sin({xf}x)")
	p1.plot(x,y1)
	p2 = fig.add_subplot(gs[0,1])
	p2.plot(x, y2)
	p2.set_xlabel(f"y=cos({yf}x)")
	p3 = fig.add_subplot(gs[1,:])
	p3.set_xlabel(f"y=sin({xf}x) * cos({yf}x)")
	p3.plot(x,y3)
	fig.align_labels() 
	plt.show()