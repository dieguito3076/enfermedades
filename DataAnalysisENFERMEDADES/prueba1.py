#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataFrameCO2 = pd.read_csv('CO2EmissionsWB.csv')
dataFrameCO2.set_index('Country Name', inplace = True)
dataFrameCO2 = dataFrameCO2[['Mexico', 'China', 'Estados Unidos', 'Japon', 'Dinamarca', 'Portugal', 'Espana']]
#dataFrameCO2[['Espana', 'Portugal']].plot()
dataFrameCO2[['Estados Unidos', 'Mexico']].plot()
dataFrameCO2.plot()
dataFrameCO2.dropna(inplace = True)
dataFrameCO2['Mexico'] = (dataFrameCO2['Mexico'] - dataFrameCO2['Mexico'][1971]) / dataFrameCO2['Mexico'][1971] * 100.00
dataFrameCO2['China'] = (dataFrameCO2['China'] - dataFrameCO2['China'][1971]) / dataFrameCO2['China'][1971] * 100.00
dataFrameCO2['Japon'] = (dataFrameCO2['Japon'] - dataFrameCO2['Japon'][1971]) / dataFrameCO2['Japon'][1971] * 100.00
dataFrameCO2['Portugal'] = (dataFrameCO2['Portugal'] - dataFrameCO2['Portugal'][1971]) / dataFrameCO2['Portugal'][1971] * 100.00
dataFrameCO2['Espana'] = (dataFrameCO2['Espana'] - dataFrameCO2['Espana'][1971]) / dataFrameCO2['Espana'][1971] * 100.00
dataFrameCO2['Dinamarca'] = (dataFrameCO2['Dinamarca'] - dataFrameCO2['Dinamarca'][1971]) / dataFrameCO2['Dinamarca'][1971] * 100.00
dataFrameCO2['Estados Unidos'] = (dataFrameCO2['Estados Unidos'] - dataFrameCO2['Estados Unidos'][1971]) / dataFrameCO2['Estados Unidos'][1971] * 100.00
print dataFrameCO2
dataFrameCO2.plot(legend=None)
plt.show()
