"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


class Observation:
    """An observation made in an inflammation study"""
    
    
    def __init__(self, day, value):
        """ 
        initialisation of object. Day & values loaded as attributes.
        """
        self.day = day
        self.value = value

        
    def __str__(self):
        """
        Dunder function to read value when call object.
        """
        return str(self.value)

    
class Person:
    """Stores values for a person, inherited by doctors and patients
    in inflammation studies."""
    
    
    def __init__(self, name: str):
        """
        Person class initialisation. read in name of type str.
        """
        self.name = name
    
    
    def __str__(self):
        """
        str dunder func calls object name when object called
        """
        return self.name


class Doctor(Person):
    """A doctor managing patients in an inflammation study"""
    
    
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

        
    @property
    def patient_names(self):
        return [p.name for p in self.patients]

    
class Patient(Person):
    """A patient in an inflammation study"""
    
    
    def __init__(self, name: str):
        super().__init__(name)
        self.observations = []

        
    @property
    def last_observation(self):
        return self.observations[-1]


    def add_observation(self, value, day=None):
        if day is None:
            if self.observations:
                day = self.observations[-1].day + 1
            else:
                day = 0

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation

    
def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: np.loadtxt
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :returns: np.mean
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)


def daily_std(data):
    """Calculate standard deviation"""
    return np.std(data, axis=0)


def patient_normalise(data):
    '''Normalise patient data from 2D array of inflammation data'''
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative.')
    maxes = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxes[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
