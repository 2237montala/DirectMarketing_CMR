class Ingestor:
    def __init__(self,fileLocation, requiredHeaders):
        filename = fileLocation



        reqHeaders={"Site Address":-1,"Site City":-1,"Site Zip Code":-1}

    def listToDict(self,list,dict):
        dict = {}

        for item in list:
            dict[item] = -1
