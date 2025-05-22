import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display



university_df = pd.read_csv('university_admission.csv')
#print(university_df.head(6))
#display(university_df.head(6))
university_df.hist(bins = 30, figsize = (20,20), color = 'r');
#plt.ion()
#plt.show()
plt.savefig("histograma.png")  # Guarda la imagen
plt.close() 