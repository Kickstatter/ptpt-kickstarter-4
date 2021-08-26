from flask_app.predict import wrangle
import pandas as pd

#Load dataframe
path = '../../../kickstarter/data/ks-projects-201801.csv'
df = pd.read_csv(path)
wrangled_df = wrangle(df)