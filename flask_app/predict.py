import pandas as pd
from datetime import datetime

#Load the model







#Load Kickstarter Dataframe
path = '../data/ks-projects-201801.csv'
df = pd.read_csv(path)

def date_from_string(string):
    string = str(string)
    return string[0:10]

def str_to_dt(string):
    dt = datetime.strptime(string, '%Y-%m-%d')
    return dt

def days_only(timedelta):
    str_delta = str(timedelta)
    return str_delta[0:2]

def wrangle(data):
    #drop null values
    data = data.dropna()
    #restrict to USD currency
    data = data[data['currency'] == 'USD']
    #drop duplicates
    data = data.drop_duplicates(subset=['ID'], keep='first')
    #Reduce features in dataset
    features = ['ID', 'name', 'main_category', 'currency', 'deadline', 'goal', 'launched', 'pledged', 'backers']
    data = data[features]
    #Extract date only from launched column and remove launch column
    data['start_date'] = data['launched'].apply(date_from_string)
    data.drop('launched', axis=1)
    #convert to Datetime
    data['deadline'] = data['deadline'].apply(str_to_dt)
    data['start_date'] = data['start_date'].apply(str_to_dt)
    #new column for campaign_duration
    data['campaign_duration'] = data['deadline']-data['start_date']
    #make campaign_duration an integer value
    data['campaign_duration'] = data['campaign_duration'].apply(days_only)
    #reset index
    data = data.set_index('ID')
    return data

data = wrangle(df)
categoryList = data['main_category'].unique().tolist()

def kickstarter_prediction(main_category, deadline, goal, launched):
    """Uses params to return if results will be successful or not"""
