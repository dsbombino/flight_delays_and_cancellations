import pandas as pd
import numpy as np

#read_airlines
def read_airlines (stream, csv=True):

    ''' function to read airlines' information
    either from a csv or xlsx file'''

    if csv:
        airlines = pd.read_csv(stream)
    else:
        airlines = pd.read_excel(stream)
    
    return airlines

#read_airports
def read_airports (stream, csv=True):

    ''' function to read airports' information
    either from a csv or xlsx file'''

    if csv:
        airports = pd.read_csv(stream)
    else:
        airports = pd.read_excel(stream)
    
    return airports

#read_flights
def read_flight(stream, csv=True):

    ''' function to read airports' information
        either from a csv or xlsx file'''

    column_types = {'ORIGIN_AIRPORT':np.string_, 
            'DESTINATION_AIRPORT':np.string_, 
            'SCHEDULED_DEPARTURE':np.string_, 
            'DEPARTURE_TIME':np.string_, 
            'WHEELS_OFF':np.string_, 
            'WHEELS_ON':np.string_, 
            'SCHEDULED_ARRIVAL':np.string_,
            'ARRIVAL_TIME':np.string_}

    if csv:
        flights = pd.read_csv(stream, low_memory=True, dtype=column_types)
    else:
        flights = pd.read_excel(stream, engine='openpyxl', dtype=column_types)

    return flights