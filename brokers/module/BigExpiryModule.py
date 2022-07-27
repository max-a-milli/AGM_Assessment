import logging
from brokers.HYCDXBrokers import HYCDXBrokers
from brokers.beans.HYCDXBrokerBeans import HYCDXBrokerBeans

'''
This class represents brokers that send EXPIRARY
'''
class BigExpiryModule(HYCDXBrokers):
    def __init__(self,header):
        self.headers = header
        super.self.broker_type= "BigExpiry"

    '''
    Generate output data. Should fetch the expected columns based on the beans
    '''
    def generateOutput(self, fileOutput):
        cleanTable = self.createHYCDXOutputRecord()
        self.tokenizeHeader()
        for each in self.dataElements:
            cleanTable["date"] = self.headers["date"]
            cleanTable["time"] = self.headers["date"]
            cleanTable["firm"] = self.headers["to"]
            '''cleanTable["expiration"] = each[None]
            cleanTable["option_type"] = each[None]
            cleanTable["strike_px"] = each["Stk"]
            cleanTable["strike_spd"] = each["Sprd"]
            cleanTable["bid_price"] = each[None]
            cleanTable["ask_price"] = each[None]
            cleanTable["delta"] = each["Delta"]
            cleanTable["implied_vol_spd"] = each[None]
            cleanTable["implied_vol_bps"] = each["Vol BPD"]
            cleanTable["implied_vol_px"] = each[None]
            cleanTable["ref_px"]'''
    def tokenizeHeader(self):
        header_str = self.headers["from"]
        from_Str=header_str[header_str.find("From:")+5:header_str.find("At:")].strip()
        datetime_str=header_str[header_str.find("At:")+3:len(header_str)].strip()
        self.headers["from"]=from_Str
        self.headers["to"] =""
        self.headers['date']=datetime_str
        self.headers["subject"]=datetime_str


    def processData(self,fileInputStread,label):
        headerProcessedFirstTime = False
        returnData = self.createHYCDXOutputRecord()
        for line in fileInputStread:
            if line.find("\n") == 0:
                logging.debug("Blank line. do noting")
                continue
            if line.startswith("EXPIRY"):
                currentLabel = line
                continue
            data = [i.strip() for i in line.split()]
            expiryBean = BigExpiryModuleBean(data)
            expiryBean.setBigExpiryHeader(currentLabel)

            if (headerProcessedFirstTime == False):
                returnData["header"] = data
                headerProcessedFirstTime = True
                expiryBean.setHeaderFields(data)
                continue
            expiryBean.setHeaderFields(returnData["header"])
            expiryBean.setHeaderValues(data)
            self.addDataElement(expiryBean)