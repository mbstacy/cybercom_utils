#!/home/mstacy/bin/python
from multiprocessing import Process, Queue,Pool
from pymongo import Connection
import commands
from datetime import datetime
#dbcon=Connection('129.15.41.76')
dbcon=Connection('mongodb://admin:******@129.15.41.76:27027')
databases = dbcon.database_names()
#databases.remove('admin')
d=[]
c=[]
for dbs in databases:
    for col in dbcon[dbs].collection_names():
        d.append(dbs)
        c.append(col)
user='admin'
psswd='*******'

print "*******************" + str(datetime.now()) + "**********************************\n" 
def mongo_stats(data):
    dbs=data[0]
    col=data[1]
    #print dbs , col, user, psswd
    cmd='''mongo 129.15.41.76:27027/admin --eval "var database='%s';var collection= '%s';var user='%s';var password='%s';" /home/mstacy/crontab/schema/cybercom_catalog/authvariety.js''' % (dbs,col,user,psswd)
    #print cmd
    return commands.getoutput(cmd)
    

if __name__ == '__main__':
    pool = Pool(processes=14)              # start 14 worker processes
    print pool.map(mongo_stats, zip(d,c))
