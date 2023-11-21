import unittest
import pytest
import numpy as np
from codeFile.spectra import Spectra


@pytest.fixture
def testFile():
    return Spectra("spectra_data.csv")

def test_readData(testFile):
    wavelength, flux, wavelengthCut, fluxCut = testFile.readData()
    
    assert isinstance(wavelength, np.ndarray)
    assert isinstance(flux, np.ndarray)
    assert isinstance(wavelengthCut, np.ndarray)
    assert isinstance(fluxCut, np.ndarray)
    assert len(wavelength) == len(flux)
    assert len(wavelengthCut) == len(fluxCut)
    