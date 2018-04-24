import os
import pandas as pd
import numpy as np
import seaborn as sns

# set working directory
os.chdir("C:/Users/Stephen/Desktop/Python/seaborn")
os.getcwd()
os.listdir(".")

arrests = pd.read_csv("us_arrests.csv")
arrests.shape
arrests.head(5)

# histogram
sns.distplot(arrests.Rape)
sns.distplot(arrests.Rape, kde = False, rug = True)

# scatterplot
sns.jointplot(x = arrests.UrbanPop, y = arrests.Assault)

# correlation matrix / corrplot
sns.pairplot(arrests)

# boxplot
arrests.UrbanPop.max()
arrests.UrbanPop.min()
arrests = arrests.assign(high_pop = "no")
arrests.loc[arrests.UrbanPop > 50, "high_pop"] = "yes"

sns.boxplot(x = arrests.high_pop, y = arrests.Murder)

# barplot
sns.barplot(x = "high_pop", y = "Murder", data = arrests)

