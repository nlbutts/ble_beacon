import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv
import string
from datetime import datetime
import numpy as np

def plotTempRhData():
	plotly.tools.set_credentials_file(username='nlbutts', api_key='v917g0at4c')
	f = csv.DictReader(open('temp_data.csv'))
	
	sensor = []
	rh = []
	temp = []
	date = []
	for row in f:
		s = string.strip(row['sensor'])
		v = s.split(':')
		sensor.append(int(v[5], 16))
		dateStr = string.strip(row['date'])
		date.append(datetime.strptime(dateStr, '%d %b %Y %H:%M:%S'))
		rh.append(float(row['rh']))
		temp.append(float(row['temp']))

	sensor = np.array(sensor)
	rh     = np.array(rh)
	temp   = np.array(temp)
	date   = np.array(date)
	uniqueSensor = np.unique(sensor)
	data = []
	for i in range(0, uniqueSensor.size):
		validDates = date[sensor == uniqueSensor[i]]
		validTemp  = temp[sensor == uniqueSensor[i]]
		validRh	   = rh[sensor == uniqueSensor[i]]
		# Create a trace
		tempGraph = go.Scatter(x = validDates, y = validTemp)
		rhGraph = go.Scatter(x = validDates, y = validRh)
		data = [tempGraph, rhGraph]

		# Plot and embed in ipython notebook!
		plotTitle = 'Sensor {0}'.format(uniqueSensor[i])
		py.iplot(data, filename=plotTitle)


if __name__ == "__main__":
    plotTempRhData()
