# What is this for?

This is designed for fitting the Silicon absorption line on Type Ia supernova spectra. The Silicon absorption line is a notable feature in the spectra of Type Ia supernovae, serving as a key indicator. The width of the line provides valuable information about the degree of blue shift that has occurred.

Spectra data for Type Ia supernova in .flm format (tab-separated) are available [here](https://lweb.cfa.harvard.edu/supernova/SNarchive.html).

The provided [```changeFileExtensions```](functions/changeFileExtensions.md)
function in the extension.py file facilitates the conversion of .flm files into CSV format. 
Once converted, the <code style="background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px;">Spectra</code> class can be instantiated, and all attributes of the class can be utilized.

## Example Output

<figure markdown style="text-align:center;">
  ![Example fit of Silicon absorption line](example_fit.png){ width="500" }
  <figcaption>Example of Gaussian fit for Silicon absorption line.</figcaption>
</figure>
