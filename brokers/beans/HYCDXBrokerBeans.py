'''

Parent Bean here to store broker infromation.
'''

class HYCDXBrokerBeans:

    headerfields=[]
    headervalues=[]
    def __init__(self,fields):
        headerfields = fields

    def setHeaderFields(self,data):
        self.headerfields=data

    def setHeaderValues(self,values):
        self.headervalues=values