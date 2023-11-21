import unittest
import pytest
from codeFile.spectra import Spectra


@pytest.fixture
def testFile():
    return Spectra("spectra_data.csv")

def test_readData(testFile):
    wavelength, flux, wavelengthCut, fluxCut = testFile.readData()