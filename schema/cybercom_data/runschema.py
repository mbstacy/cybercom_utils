#!/home/mstacy/bin/python
from multiprocessing import Process, Queue,Pool
from pymongo import Connection
import commands
from datetime import datetime

dbcon=Connection('129.15.41.76')
databases = dbcon.database_names()
d=[]
c=[]

for dbs in databases:
    for col in dbcon[dbs].collection_names():
        d.append(dbs)
        c.append(col)

print "*******************" + str(datetime.now()) + "**********************************\n"

def mongo_stats(data):
    dbs=data[0]
    col=data[1]
    cmd='''mongo 129.15.41.76:27017/%s --eval "var collection = '%s', limit=1 " /home/mstacy/crontab/schema/cybercom_data/variety.js''' % (dbs,col)
    return commands.getoutput(cmd)    

if __name__ == '__main__':
    pool = Pool(processes=21)              # start 21 worker processes
    print pool.map(mongo_stats, zip(d,c))
