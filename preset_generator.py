import os
import numpy as np
import pandas as pd

class presetGen():
    def __init__(self,presetCount, directory):
        self.presetCount = presetCount
        self.directory = directory
        self.presetValue = []
        self.parametersCSV = {
            'exposure' : [],
            'contrast': [],
            'highlights' : [],
            'shadows' : [],
            'whites' : [],
            'blacks' : [],
            'vibrance' : [],
            'saturation' : [],
            'hueRed':[],
            'hueOrange':[],
            'hueYellow':[],
            'hueGreen':[],
            'hueAqua':[],
            'hueBlue':[],
            'huePurple':[],
            'hueMagenta':[],
            'satRed':[],
            'satOrange':[],
            'satYellow':[],
            'satGreen':[],
            'satAqua':[],
            'satBlue':[],
            'satPurple':[],
            'satMagenta':[],
            'lumiRed':[],
            'lumiOrange':[],
            'lumiYellow':[],
            'lumiGreen':[],
            'lumiAqua':[],
            'lumiBlue':[],
            'lumiPurple':[],
            'lumiMagenta':[]
        }

    
    def randomParemeter(self,name):
    
        parameters = {
        'exposure' : float('{:.2f}'.format(np.random.uniform(low=-5.0, high=5.0, size=None))),
        'contrast' : np.random.randint(low=-100, high=100),
        'highlights' : np.random.randint(low=-100, high=100),
        'shadows' : np.random.randint(low=-100, high=100),
        'whites' : np.random.randint(low=-100, high=100),
        'blacks' : np.random.randint(low=-100, high=100),
        'vibrance' : np.random.randint(low=-100, high=100),
        'saturation' : np.random.randint(low=-100, high=100),
        'hueRed':np.random.randint(low=-100, high=100),
        'hueOrange':np.random.randint(low=-100, high=100),
        'hueYellow':np.random.randint(low=-100, high=100),
        'hueGreen':np.random.randint(low=-100, high=100),
        'hueAqua':np.random.randint(low=-100, high=100),
        'hueBlue':np.random.randint(low=-100, high=100),
        'huePurple':np.random.randint(low=-100, high=100),
        'hueMagenta':np.random.randint(low=-100, high=100),
        'satRed':np.random.randint(low=-100, high=100),
        'satOrange':np.random.randint(low=-100, high=100),
        'satYellow':np.random.randint(low=-100, high=100),
        'satGreen':np.random.randint(low=-100, high=100),
        'satAqua':np.random.randint(low=-100, high=100),
        'satBlue':np.random.randint(low=-100, high=100),
        'satPurple':np.random.randint(low=-100, high=100),
        'satMagenta':np.random.randint(low=-100, high=100),
        'lumiRed':np.random.randint(low=-100, high=100),
        'lumiOrange':np.random.randint(low=-100, high=100),
        'lumiYellow':np.random.randint(low=-100, high=100),
        'lumiGreen':np.random.randint(low=-100, high=100),
        'lumiAqua':np.random.randint(low=-100, high=100),    
        'lumiBlue':np.random.randint(low=-100, high=100),
        'lumiPurple':np.random.randint(low=-100, high=100),
        'lumiMagenta':np.random.randint(low=-100, high=100)
        }

        for key in parameters.keys():
            self.parametersCSV[key].append(parameters[key])

        for i in parameters.keys():
            if parameters[i] > 0:
                parameters[i] = '+{}'.format(parameters[i])

        parameters['name'] = name
        print('======================================================')
        print(parameters)
        print('======================================================')
        return parameters

    def save_path(self,i):
        directory = self.directory
        if not os.path.exists((directory)):
            os.mkdir(directory)
        return f"{os.path.join(os.path.realpath(os.getcwd()),directory,str(i))}.xmp"

    def writeFile(self, parameter):
        xmp = open('01.txt', 'r')
        content = xmp.read()
        content = content%parameter
        return content

    def createPreset(self):
        for i in range(self.presetCount):
            self.presetValue.append(self.randomParemeter(i))

    def exportPreset(self):
        for i, parameter in enumerate(self.presetValue):
            filepath = self.save_path(i)
            writePreset = self.writeFile(parameter)

            with open(filepath,"w") as f:
                f.write(writePreset)

        df = pd.DataFrame(self.parametersCSV)
        df.to_csv('{}/parameter.csv'.format(self.directory))
            # f = open(f"{os.path.join(os.path.realpath(os.getcwd()),self.directory,i)}.xmp", "w")
            # f.write(writePreset)
        # return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,i)}.jpg"


if __name__ == '__main__':
    genPreset = presetGen(3000, 'preset2')
    genPreset.createPreset()
    genPreset.exportPreset()
