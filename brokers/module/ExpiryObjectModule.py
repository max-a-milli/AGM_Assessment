import os.path

from brokers.HYCDXBrokers import HYCDXBrokers
from brokers.beans.ExpiryObjectModelBean import  ExpiryObjectModuleBean
import csv
from os.path import exists
'''
Expiry object. Looking for a expiry object with Expiry (case sensitive
'''

class ExpiryObjectModel(HYCDXBrokers):

    def __init__(self,headers):
        self.broker_type = "Expiry"
    def __new(self):
        None

    def generateOutput(self, fileOutput):
       cleanTable = self.createHYCDXOutputRecord()

    #Todo: Populate cleanTable with data that will be extract to output. Mapping file
    # should be used that is read from a database and processed

       with open(fileOutput, 'a') as f:
           # create the csv writer
           writer = csv.writer(f)

           for each in self.dataElements:
               cleanTable["date"] = each.dateRef
               # write a row to the csv file
               # writer.writerow(row)

       return cleanTable
    def processData(self, fileInputStream, label):
        currentLabel=label

        returnData = self.createHYCDXOutputRecord()
        headerProcessedFirstTime=False;

        for line in fileInputStream:
            if line.startswith("Expiry"):
                currentLabel=line
                continue
            data = [i.strip() for i in line.split()]
            expiryBean=ExpiryObjectModuleBean(data)
            expiryBean.setExpiryHeader(currentLabel)

            if (headerProcessedFirstTime == False):

                returnData["header"] = data
                headerProcessedFirstTime = True
                expiryBean.setHeaderFields(data)
                continue
            expiryBean.setHeaderFields(returnData["header"])
            expiryBean.setHeaderValues(data)
            self.addDataElement(expiryBean)