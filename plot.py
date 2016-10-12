import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv
import string
from datetime import datetime

def plotTempRhData():
	f = csv.DictReader(open('temp_data.csv'))

	rh = []
	temp = []
	date = []
	for row in f:
		dateStr = string.strip(row['date'])
		date.append(datetime.strptime(dateStr, '%d %b %Y %H:%M:%S'))
		rh.append(float(row['rh']))
		temp.append(float(row['temp']))


	# Create a trace
	tempGraph = go.Scatter(x = date, y = temp)
	rhGraph = go.Scatter(x = date, y = rh)

	data = [tempGraph, rhGraph]

	# Plot and embed in ipython notebook!
	plotly.tools.set_credentials_file(username='nlbutts', api_key='v917g0at4c')
	py.iplot(data, filename='Sensor 1')
