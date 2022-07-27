# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import glob
import sys
import logging
from brokers.HYCDXFactory import HYCDXFactory
import argparse

'''
*   This block of code will get all files with the prefix and return  
*   the path of all files that has the following pattern. 
'''
def getAllCDXFiles(fileDirectory,prefix):
    logging.info("Reading files from directory " + fileDirectory)
    if (not os.path.isdir(fileDirectory)):
        logging.error("Error caught. directory not valid")
        raise NotADirectoryError("Directory " + fileDirectory + " is not a valid directory.")
    allHYCDXFiles = glob.glob(fileDirectory + "/" + prefix + "*")
    return allHYCDXFiles

'''
This will read the files in the specified directory and process the associated/respected
broker format.
'''
def readHYCDXFilesFromDirectory(fileDirectory,prefix):

    # Get all file names
    allHYCDXFiles = getAllCDXFiles(fileDirectory,prefix)

    logging.debug("Total number of files found "+str(len(allHYCDXFiles)))

    #Iterate through each file, process each and dump once to only use IO operation once per file..
    for fileName in allHYCDXFiles:
        logging.info("Processing file "+fileName)
        factory = HYCDXFactory()
        try:
            #Factory pattern to detemine type based on file contents.
            broker = factory.getInstance(fileName)

            if broker==None:
                raise Exception("Broker object not found")
            broker.generateOutput("c:\\tmp\\"+str(broker.broker_type,".csv"));

        except Exception as e:
            logging.warning("File "+fileName+" not processed. Will be ignored ");
            logging.error(e)
            continue
def main(filename,prefix):
    #readHYCDXFilesFromDirectory("C:\\Users\\Max\\Downloads\\Apollo\\projects", "hycdx_option_quotes")
    readHYCDXFilesFromDirectory(filename,prefix)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser("HYCXMainApplication")
    parser.add_argument("--dir", help="directory to the broker files .", type=str,)
    parser.add_argument("--prefix", help="prefix file .", type=str, )

    args = parser.parse_args()
    if os.path.isdir(args.dir)==False:
        raise NotADirectoryError("file input "+str(args.dir)+" is not a directory")
    main(args.dir,args.prefix)
