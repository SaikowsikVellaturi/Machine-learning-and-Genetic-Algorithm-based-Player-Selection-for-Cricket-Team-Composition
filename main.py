import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_excel(r'C:\Users\91728\Desktop\MS_Dhoni_ODI_record.xlsx')
data['opposition'] = data['opposition'].apply(lambda x: x[2:])
data['year'] = data['date'].dt.year.astype(int)
data['score'] = data['score'].apply(str)
data['not_out'] = np.where(data['score'].str.endswith('*'), 1, 0)
data.drop(columns='odi_number', inplace=True)
data_new = data.loc[((data['score'] != 'DNB') & (data['score'] != 'TDNB')), 'runs_scored':]
data_new['runs_scored'] = data_new['runs_scored'].astype(int)
data_new['balls_faced'] = data_new['balls_faced'].astype(int)
data_new['strike_rate'] = data_new['strike_rate'].astype(float)
data_new['fours'] = data_new['fours'].astype(int)
data_new['sixes'] = data_new['sixes'].astype(int)
data_new
number_of_matches = data.shape[0] 
print('Number of matches played:', number_of_matches)
number_of_inns = data_new.shape[0]
print('Number of innings played:', number_of_inns)
not_outs = data_new['not_out'].sum()
print('Not outs:', not_outs)
runs_scored = data_new['runs_scored'].sum() 
print('Runs scored in career:', runs_scored)
balls_faced = data_new['balls_faced'].sum() 
print('Balls faced in career:', balls_faced)
career_sr = (runs_scored / balls_faced)*100
print('Career strike rate: {:.2f}'.format(career_sr))
career_avg = (runs_scored / (number_of_inns - not_outs))
print('Career average: {:.2f}'.format(career_avg))
highest_score_date = data_new.loc[data_new.runs_scored == data_new.runs_scored.max(), 'date'].values[0]
highest_score = data.loc[data.date == highest_score_date, 'score'].values[0] 
print('Highest score in career:', highest_score)
hundreds = data_new.loc[data_new['runs_scored'] >= 100].shape[0] 
print('Number of 100s:', hundreds)
fifties = data_new.loc[(data_new['runs_scored']>=50)&(data_new['runs_scored']<100)].shape[0]
print('Number of 50s:', fifties)
fours = data_new['fours'].sum() 
print('Number of 4s:', fours)
sixes = data_new['sixes'].sum() 
print('Number of 6s:', sixes)

