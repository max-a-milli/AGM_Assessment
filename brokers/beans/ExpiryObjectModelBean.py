from brokers.beans.HYCDXBrokerBeans import HYCDXBrokerBeans

'''
Only handle data
'''
class ExpiryObjectModuleBean(HYCDXBrokerBeans):

    dateRef=None
    strike=None
    spread=None
    data=[]
    def setExpiryHeader(self,expiry_name):
        itemsToTokenize = expiry_name.removeprefix("Expiry ").split(" ")
        self.dateRef=itemsToTokenize[0]
        self.strike=itemsToTokenize[1].removeprefix("(")
        self.spread=itemsToTokenize[2].removesuffix(")").removesuffix("\r\n")

