import os
import numpy as np

class presetGen():
    def __init__(self,presetCount, directory):
        self.presetCount = presetCount
        self.directory = directory
        self.presetValue = []
    
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
        }

        for i in parameters.keys():
            if parameters[i] > 0:
                parameters[i] = '+{}'.format(parameters[i])

        parameters['name'] = name

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
            # f = open(f"{os.path.join(os.path.realpath(os.getcwd()),self.directory,i)}.xmp", "w")
            # f.write(writePreset)
        # return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,i)}.jpg"


if __name__ == '__main__':
    genPreset = presetGen(5, 'test')
    genPreset.createPreset()
    genPreset.exportPreset()
