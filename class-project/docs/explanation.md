# Explanation about a function to change a file extension

<font size="5">[```changeFileExtensions```](functions/changeFileExtensions.md)</font><br />
This changes a file extension in a folder. This is meant to be used for flm files on [CfA Supernova Data Archive](https://lweb.cfa.harvard.edu/supernova/SNarchive.html), which is tab-separated, and does not change the file type to comma-separaed.
<br/>

# Explanations about Spectra class

<font size="5">[```__init__```](functions/__init__.md)</font><br />
<code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">&lowbar;&lowbar;init__</code> is to initialize the Spectra class object and does not have to be run. A default boundary of wavelengths for the Gaussian fit is 6020 to 6420 angstrum. The boundary can be changed when a class instance is created by defining <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">cuttOffLeft</code> and <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">cutOffRight</code>.
<br /> 

<font size="5">[```fit```](functions/fit.md)</font><br />
This fits the given data into a Gaussian function. This does not have to be run to get a fit.
<br /> 

<font size="5">[```gauss```](functions/gauss.md)</font><br />
This is a method to define the Gaussian function and is used inside the <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">fit</code> method above. This also does not have to be run to get a fit. [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function) is given by 
$$
f(x) = Ae^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$
where $x$ is a continuous variable, $A$ is the amplitude, $\mu$ is a mean, and $\sigma$ is a standard deviation.
<br /> 

<font size="5">[```readData```](functions/readData.md)</font><br />
This is another method that does not have to be run and is used for other methods. 
<br /> 

<font size="5">[```getSpectra```](functions/getSpectra.md)</font><br />
This method gives a spectrum plot from the imput data without trancating any data points. By defining <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">spectrumPath</code> parameter, the spectrum plot can be saved to the path specified.
<br /> 

<font size="5">[```getFit```](functions/getFit.md)</font><br />
This method gives a Gaussian fit plot. By defining <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">fitPath</code> parameter, the fit plot can be saved to the path specified.
<br /> 

<font size="5">[```getAmplitude```](functions/getAmplitude.md)</font><br />
This gives the amplitude of the Gaussian function, which corresponds to a depth of the Silicon apsorption.
<br /> 

<font size="5">[```getMean```](functions/getMean.md)</font><br />
This gives the mean of the Gaussian function, which is also mode and median, and should correspond to the Silicon absorption peak.
<br /> 

<font size="5">[```getSigma```](functions/getSigma.md)</font><br />
This gives the standard deviation of the Gaussian function. The standard deviation is given by 
$$
\sigma = \sqrt{\frac{\sum_{i=1}^{N}\left(x_i - \mu\right)^2}{N}} 
$$
where $N$ is the number of $x$.
<br /> 

<font size="5">[```getOffset```](functions/getOffset.md)</font><br />
This gives the offset of the Gaussian function from the y axis.

<font size="5">[```getFWHM```](functions/getFWHM.md)</font><br />
This gives full width at half maximum (FWHM) of the Gaussian function. For Gaussian distribution, 
FWHM is given by $2\sqrt{2\text{ln}2}\sigma$.
 





