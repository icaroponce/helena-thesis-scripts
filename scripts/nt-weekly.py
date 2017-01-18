import dateutil
import pandas

from utils import week_of_month:


INPUT_FILE = '../data/daxweeklyNT.csv'
OUTPUT_FILE = '../data/sum-dax-weekly.csv'

df = pandas.read_csv( INPUT_FILE , sep=',', engine='c')

df['date'] = df['X'].apply(dateutil.parser.parse, dayfirst=True)
df['day'] = df['date'].apply(lambda x: x.day)
df['month'] = df['date'].apply(lambda x: x.month)
df['calendar_wom'] = df['date'].apply(week_of_month)
df['month_year'] = df['X'].apply(lambda x: x[:-3])

df.rename(columns={'DAX..Live..11': 'number_of_transactions'}, inplace=True);
df = df.drop('X', 1)
da = df.groupby(['month_year','calendar_wom'], as_index=False)['number_of_transactions'].sum()
da.to_csv( OUTPUT_FILE , index=False)
