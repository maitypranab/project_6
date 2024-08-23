import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

nSamples=1000000;
nbins=1000;
h=(nr.normal(0,1,nSamples)+1j*nr.normal(0,1,nSamples))/np.sqrt(2);
a=np.abs(h);
phi=np.angle(h);
x=np.arange(0,5,.01);
theta=np.arange(-np.pi,np.pi,.01);

#PDF of Amplitude of channel
plt.subplot(2,2,1)
plt.hist(a,bins=nbins,density=True,facecolor='green')
plt.title('PDF of Amplitude')
plt.xlabel('a')
plt.ylabel('$f_A$(a)');


#PDF of Phase of channel
plt.subplot(2,2,2)
plt.hist(phi,bins=nbins,density=True,facecolor='green')
plt.title('PDF of Phase')
plt.xlabel('$\phi$')
plt.ylabel('$f_\phi$($\phi$)')


#Superimposed PDF of magnitude
plt.subplot(2,2,3)
plt.hist(a,bins=nbins,density=True,facecolor='green')
plt.plot(x,2*x*np.exp(-x**2),'r')
plt.xlim([0,5])
plt.xlabel('a')
plt.ylabel('$f_A$(a)')
plt.legend(["PDF plot","Histogram"],loc ="upper right")


#Superimposed PDF of phase
plt.subplot(2,2,4)
plt.hist(phi,bins=nbins,density=True,facecolor='green')
plt.plot(theta,.5/np.pi*np.ones(np.shape(theta)),'r')
plt.ylim([0,.25])
plt.xlim([-3.5,3.5])
plt.xlabel('$\phi$')
plt.ylabel('$f_\Phi(\phi)$') 
plt.legend(["PDF Plot","Histogram"],loc ="upper right")

plt.subplots_adjust( top=1.4,wspace=0.8,hspace=0.35)
