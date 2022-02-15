
import random # Gas Level Functiondef gasLevelGauge():

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()