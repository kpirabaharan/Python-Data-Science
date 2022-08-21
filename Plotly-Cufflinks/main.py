# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Plotly course is out-of-date
#
# # import plotly
# from plotly import __version__
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# import chart_studio.plotly as py
#
# import cufflinks as cf
#
# init_notebook_mode(connected=True)
# cf.go_offline()
#
# # print(__version__) # requires version >= 1.9.0
#
# df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
# df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
#
# print(df.head())
# print(df2.head())
#
# plt.figure()
# df.iplot()
#
# plt.show()

import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)
plt.figure()
py.iplot(table, filename='jupyter-table1')
plt.show()
