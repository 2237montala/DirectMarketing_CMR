class Ingestor:
    def __init__(self,fileLocation, requiredHeaders):
        filename = fileLocation



        reqHeaders=listToDict(requiredHeaders,-1)

    def listToDict(self,list,defaultVal):
        dict = {}

        for item in list:
            dict[item] = -1

        return dict
