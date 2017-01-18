import dateutil
import utils
import sys

from utils import week_of_month

INPUT_FILE = '../data/net.csv'
OUTPUT_FILE = '../data/net-count-by-week-of-month.csv'

df = pandas.read_csv( INPUT_FILE , sep=',', engine='c')
df['date'] = df['created'].apply(dateutil.parser.parse, dayfirst=False)
df['first_day_of_week'] = df['date'].apply(week_of_month)
da = df['first_day_of_week'].value_counts()
da.to_csv( OUTPUT_FILE )
