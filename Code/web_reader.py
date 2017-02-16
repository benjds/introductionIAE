# web
import pandas_datareader.data as web
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib import style

# set starting and end date to import
start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2017, 2, 27)

# import stock data for 'GOOGL'
df = web.DataReader("GOOGL", 'yahoo', start, end)


df['dates'] = df.index.map(lambda x: str(x)[:10])

#style.use('fivethirtyeight')
#df['High'].plot()
#plt.show()


import plotly
import plotly.graph_objs as go

plotpath = os.path.abspath("../Results/GOOGL.html")
trace = go.Scatter( x=df['dates'], y=df['High'] )
data = [trace]
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)

