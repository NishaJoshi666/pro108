import csv
import pandas as pd
import scipy
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg"],show_hist = False)
fig.show()