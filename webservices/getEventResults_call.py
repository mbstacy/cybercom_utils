from xmlrpclib import ServerProxy 
from datetime import datetime

URL = 'http://test.cybercommons.org/dataportal/RPC2/'
                    
s = ServerProxy(URL)
results = s.catalog.getEventResult_time(1448132, datetime(2011,5,1), datetime(2011,5,10))
print results
#********Param Call***********
'''
    parm={'cat_id':<int-required>,'start_date':<required>,'end_date':<optional>,var_id':<optional>}
    
'''

param={'cat_id':1448132,'start_date':datetime(2011,5,1),'var_id':'URL'}
results = s.catalog.getEventResult_time_Param(param)

print results

#added for country pull
#print results
param={'cat_id':1452141,'country':'US','start_date':datetime(2001,5,1),'end_date':datetime(2001,5,1),'var_id':'URL'}
results= s.catalog.getEventResult_Country(param)
print results
