# Explanation about a function to change a file extension

<font size="5">[```changeFileExtensions```](functions/changeFileExtensions.md)</font><br />
This changes a file extension in a folder. This is meant to be used for flm files on the CfA Supernova Data Archive, which is tab-separated, and does not change the file type to comma-separaed.
<br/>

# Explanations about each method of Spectra class

<font size="5">[```__init__```](functions/__init__.md)</font><br />
<code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">&lowbar;&lowbar;init__</code> is to initialize the Spectra class object and does not have to be run. A boundary of wavelengths for the Gaussian fit can be defined when a class instance is created by defining <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">cuttOffLeft</code> and <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">cutOffRight</code>.
<br /> 

<font size="5">[```fit```](functions/fit.md)</font><br />
This fits the given data into a Gaussian function. This does not have to be run to get a fit.
<br /> 

<font size="5">[```gauss```](functions/gauss.md)</font><br />
This is a function to define the Gaussian function and is used inside the <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">gauss</code> function above. This also does not have to be run to get a fit.
<br /> 

<font size="5">[```readData```](functions/readData.md)</font><br />
This is another function that does not have to be run and is used for other functions. This reads data 

<font size="5">[```getSpectra```](functions/getSpectra.md)</font><br />

<font size="5">[```getFit```](functions/getFit.md)</font><br />


<font size="5">[```getAmplitude```](functions/getAmplitude.md)</font><br />

<font size="5">[```getMean```](functions/getMean.md)</font><br />

<font size="5">[```getSigma```](functions/getSigma.md)</font><br />

<font size="5">[```getOffset```](functions/getOffset.md)</font><br />

<font size="5">[```getFWHM```](functions/getFWHM.md)</font><br />






