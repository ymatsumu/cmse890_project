import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
import numpy as np
import scipy
# from scipy.stats import norm
from scipy.optimize import curve_fit 
# from scipy import optimize


class Spectra:
    def __init__(self, filePath):
        self.filePath = filePath

    def readData(self, cutOffLeft=6020, cutOffRight=6420):
        df = pd.read_csv(self.filePath, delim_whitespace=True)
        header = ['Wavelength', 'Flux']
        df.columns = header
        wavelength = df.Wavelength.values
        flux = df.Flux.values

        dfCut = df[(df.Wavelength > cutOffLeft) & (df.Wavelength < cutOffRight)]
        dfCut.columns = header
        wavelengthCut = dfCut.Wavelength.values
        fluxCut = dfCut.Flux.values

        return wavelength, flux, wavelengthCut, fluxCut
    

    def getSpectra(self, spectrumPath=None):
        wavelength, flux, _, _ = self.readData()

        plt.figure()
        plt.plot(wavelength, flux, 'k-')
        plt.xlabel('Rest Wavelength ($\AA$)')
        plt.ylabel('Scaled $f_\lambda$ + Constant')

        if spectrumPath:
            plt.savefig(spectrumPath)
        else:
            plt.show()



    def getFit(self, fitPath=None):
        _, _, wavelength, flux = self.readData()
        popt, _ = self.fit(wavelength, flux)

        plt.plot(wavelength, flux, 'k-', label='Data')
        plt.plot(wavelength, self.gauss(wavelength, *popt), 'r-', label='Gaussian fit')
        plt.xlabel('Rest Wavelength ($\AA$)')
        plt.ylabel('Scaled $f_\lambda$ + Constant')
        plt.legend()

        if fitPath:
            plt.savefig(fitPath)
        else:
            plt.show()

    
    def getOffset(self):
        _, _, wavelength, flux = self.readData()
        popt, _ = self.fit(wavelength, flux)
        return popt[0]
    
    def getAmplitude(self):
        _, _, wavelength, flux = self.readData()
        popt, _ = self.fit(wavelength, flux)
        return popt[1]
    
    def getMean(self):
        _, _, wavelength, flux = self.readData()
        popt, _ = self.fit(wavelength, flux)
        return popt[3]
    
    def getFWHM(self):
        _, _, wavelength, flux = self.readData()
        popt, _ = self.fit(wavelength, flux)
        sigma = popt[3]
        return 2.35482 * sigma
        

    def fit(self, xdata, ydata):
        """This fits the data with gaussian function. 

        Args:
        xdata (list): Independent variable of the data to fit.
        ydata (list): Dependent variable of the data to fit.
        """
        mean = sum(xdata * ydata) / sum(ydata)
        sigma = np.sqrt(sum(ydata * (xdata - mean) ** 2) / sum(ydata))
        # popt: optimal values for the parameters 
        # pcov: estimated approximate covariance of popt
        popt, pcov = curve_fit(self.gauss, xdata, ydata, p0=[min(ydata), max(ydata), mean, sigma])
        # perr: one standard deviation errors on the parameters
        perr = np.sqrt(np.diag(pcov))
        return popt, perr

    def gauss(self, x, offset, A, mu, sigma):
        """This is a gaussian function. 
        It takes an independent variable as the first argument and the parameters to fit as separate remaining arguments.

        Args:
        x (list): Independent variable of the gaussian function.
        offset (float): Offset of the gaussian function.
        A (float): Amplitude of the gaussian function.
        mu (flaot): Mean of the x values.
        sigma (flaot): Standard deviation of the x values.
        """
        return offset + A * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    

        
    
    


