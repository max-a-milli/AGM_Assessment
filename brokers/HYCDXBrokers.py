import logging
import csv

class HYCDXBrokers(object):
    headers = []
    dataElements=[]
    broker_type=None
    def __init__(self,headers,brokerT):
        self.headers = headers
        self.dataElements=[]
        self.broker_type=brokerT

    def addDataElement(self, elements):
         self.dataElements.append(elements)

    def processData(self,fileInputStread,label):
        print("hi")
    def processHeader(self,headerString):
        None
    def generateOutput(self,fileOutput):

        output=self.createHYCDXOutputRecord()
        return output

    def writeCSV(self,fileOutput):

        with open(fileOutput, 'w') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            #writer.writerow(row)

    def writeToOutput(self,output):
        logging.info("Need to add output")
    def createHYCDXOutputRecord(self):
        return {"date":"",
                "time":"",
                "firm":"",
                "expiration":"",
                "option_type":"",
                "strike_px":0,
                "strike_spd":0,
                "bid_price":0,
                "ask_price":0,
                "delta":0,
                "implied_vol_spd":0,
                "implied_vol_bps":0,
                "implied_vol_px":0,
                "ref_px":0}