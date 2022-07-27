from brokers.beans.HYCDXBrokerBeans import HYCDXBrokerBeans


class BigExpiryModuleBean(HYCDXBrokerBeans):
    dateentry = None
    product = None

    def setBigExpiryHeader(self, expiry_name):
        itemsToTokenize = expiry_name.removeprefix("EXPIRY ").split(" ")
        self.dateentry = itemsToTokenize[0]
