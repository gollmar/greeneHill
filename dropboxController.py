from prodDropboxII import runWhole
import sys

if __name__ == '__main__':
    csvFilePath = str(sys.argv[1])
    runWhole(csvFilePath)
