import unittest
import pytest
import numpy as np
import os


from codeFile.spectra import Spectra
from codeFile.extension import changeFileExtensions


@pytest.fixture
def testFile():
    return Spectra("spectra_data.csv")


def test_readData(testFile):
    wavelength, flux, wavelengthCut, fluxCut = testFile.readData()

    assert isinstance(wavelength, np.ndarray)
    assert isinstance(flux, np.ndarray)
    assert isinstance(wavelengthCut, np.ndarray)
    assert isinstance(fluxCut, np.ndarray)


@pytest.fixture
def data(testFile):
    wavelength, flux, wavelengthCut, fluxCut = testFile.readData()
    return wavelength, flux, wavelengthCut, fluxCut


def test_getSpectra(data):
    wavelength = data[0]
    flux = data[1]
    assert len(wavelength) == len(flux)


def test_getFit(data):
    wavelengthCut = data[2]
    fluxCut = data[3]
    assert len(wavelengthCut) == len(fluxCut)


@pytest.fixture
def statistics(testFile):
    _, _, wavelength, flux = testFile.readData()
    popt, _ = testFile.fit(wavelength, flux)
    return popt


def test_getOffset(statistics):
    offset = statistics[0]
    assert offset >= 0.0


def test_getAmplitude(statistics):
    amplitude = statistics[1]
    assert amplitude <= 0.0


def test_getMean(statistics, data):
    wavelengthCut = data[2]
    fluxCut = data[3]
    mean = statistics[2]
    expectedMean = sum(wavelengthCut * fluxCut) / sum(fluxCut)
    assert abs(mean - expectedMean) <= expectedMean * 0.05


def test_getFWHM(statistics, data):
    wavelengthCut = data[2]
    sigma = statistics[3]
    FWHM = 2.355 * sigma
    assert FWHM < (wavelengthCut[-1] - wavelengthCut[0])


def test_getSigma(statistics, data):
    wavelengthCut = data[2]
    fluxCut = data[3]
    sigma = statistics[3]
    expectedMean = sum(wavelengthCut * fluxCut) / sum(fluxCut)
    expectedSigma = np.sqrt(
        sum(fluxCut * (wavelengthCut - expectedMean) ** 2) / sum(fluxCut)
    )
    assert abs(expectedSigma - sigma) / sigma <= 0.8


# Above tests validate the accuracy of the gauss function and fit function as well.


def test_changeFileExtensions():
    folder = "../spectrum"
    changeFileExtensions(folder, ".csv")
    files = os.listdir(folder)

    for file in files:
        assert is_csv(file) is True


def is_csv(file):
    _, extension = os.path.splitext(file)
    return extension == ".csv"
