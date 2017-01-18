from datetime import datetime
from  dateutil.parser import parse
import json
import csv 

INPUT_FILE = '../data/net-full.json'
OUTPUT_FILE  = '../data/net.csv'

#DATE IS IN ISO-8601 FORMAT
with open( INPUT_FILE ) as fh, open( OUTPUT_FILE , 'w') as out:
    writer = csv.writer(out)
    writer.writerow(['created'])
    data = json.load(fh)
    for complain in data['complainResult']['complains']['data']:
        created = datetime.strftime(parse(complain['created']), '%m/%d/%Y')
        writer.writerow([created])
