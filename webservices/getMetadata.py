from xmlrpclib import ServerProxy # Standard Python Library
from rpc4django.utils import CookieTransport # pip install rpc4django
        
#username = ''
#password =''
            
URL = 'http://www2.cybercommons.org/catalog/RPC/'
                    
s = ServerProxy(URL, transport=CookieTransport())

# Login Required Operation need!
#if s.system.login(username, password):
print  "Get catalog data. Can also send column=[list] for needed columns. code: s.catalog.getCatalogMetadata(814)\n"
print s.catalog.getCatalogMetadata(814)#Commons ID 814 is Cybercommons Application Data Commons
print "\nGet event data.Can also send column=[list] for needed columns. code s.catalog.getEventMetadata(1463194)\n"
print s.catalog.getEventMetadata(1463194)#Catalog ID 1463194 is the Graph Appplication
print "\nGet result data.Can also send column=[list] for needed columns. code s.catalog.getResultMetadata(5756582)\n"
print s.catalog.getResultMetadata(5756582)#Event ID 5756582 is the TECO Version 2 Model Metadata results
