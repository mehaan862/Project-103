import pandas as pd
import plotly.express as px
df = pd.read_csv('csv files\Coviddata.csv')
fig=px.scatter(df,x='date',y='cases',title='Covid Data',color='country')
fig.show()