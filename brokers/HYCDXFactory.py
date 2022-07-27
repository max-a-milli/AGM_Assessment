import logging
import os

from brokers.beans import BigExpiryModuleBean
from brokers.module.ExpiryObjectModule import ExpiryObjectModel
from brokers.module.BigExpiryModule import BigExpiryModule

class CustomError:
    pass



class HYCDXFactory:

    def getInstance(self,fileName):
        broker=None
        if fileName.endswith(".csv") or fileName.endswith(".txt"):
            broker=self.readHYCDXCSVFile(fileName)
        else: raise CustomError("File Format not supported")
        return broker
    def readHYCDXCSVFile(self,fileName):

        hasProcessedHeaderFrom = False
        hasProcessedHeaderTo = False
        hasProcessedHeaderSubject = True
        returnBody = {"header": {}, "body": {}, "metadata": {}}
        with open(os.path.join(fileName), 'r') as f:
            for line in f:
                if line.find("\n") == 0:
                    logging.debug("Blank line. Do nothing")
                    continue
                elif line.startswith("From:"):
                    hasProcessedHeaderFrom = True
                    returnBody["header"]["from"] = line;
                    continue
                elif line.startswith("To:"):
                    hasProcessedHeaderTo = True
                    returnBody["header"]["to"] = line;
                    continue
                elif line.startswith("Subject"):
                    hasProcessedHeaderSubject = True
                    returnBody["header"]["subject"] = line;
                    continue

                if (hasProcessedHeaderTo == True and hasProcessedHeaderFrom == True and hasProcessedHeaderSubject == True):
                    if line.startswith("Expiry"):
                        expBrokerType = ExpiryObjectModel(returnBody["header"])

                        expBrokerType.processData(f, line)
                        return expBrokerType
                    elif line.startswith("$$ CDX OPTIONS"):
                        bigTypebrokerType = BigExpiryModuleBean.BigExpiryModule(returnBody["header"])
                        bigTypebrokerType.processData(f, line)
                        return bigTypebrokerType
                    elif line.lower().startswith("Exp"):
                        exp=None
                        #exp = processBrokerTypeEXP(f)
                        exp.processData(f, line)
                        return exp
                # ignore line. dummy data
        return None