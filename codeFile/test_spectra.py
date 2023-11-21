import unittest
from spectra import Spectra


@pytest.fixture
def testFile():
    return Spectra("spectra_data.csv")

def test_readData(testFlie):
    wavelength, flux, wavelengthCut, fluxCut = testFile.readData()