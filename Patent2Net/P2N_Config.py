import os
import sys

class P2NConfig:
    def __init__(self):

        # Initiate all empty attributes
        self.requete = ""
        self.ndf = ""
        self.GatherContent = False
        self.GatherBiblio = False
        self.GatherPatent = False
        self.GatherFamilly = False
        self.GatherIramuteq = False
        # Networks config loading
        self.InventorNetwork = False
        self.ApplicantNetwork = False
        self.ApplicantInventorNetwork = False
        self.InventorCrossTechNetwork = False
        self.ApplicantCrossTechNetwork = False
        self.CountryCrossTechNetwork = False
        self.CrossTechNetwork = False
        self.CompleteNetwork = False
        self.FamiliesNetwork = False
        self.FamiliesHierarchicNetwork = False
        self.References = False
        self.Citations = False
        self.Equivalents = False
        self.FormateExportCountryCartography = False
        self.FormateExportBiblio = False
        self.FreePlane = False
        self.FusionCarrot2 = False

        #opening request file, reading parameters
        content = self.readInputFile()

        for line in content:
            ### General config loading
            if line.count('request:') > 0:
                self.requete = self.getStr(line)
            elif line.count('DataDirectory:') > 0:
                self.ndf = self.getStr(line)
            elif line.count('GatherContent') > 0:
                self.GatherContent = self.getBoolean(line)
            elif line.count('GatherBiblio') > 0:
                self.GatherBiblio = self.getBoolean(line)
            elif line.count('GatherPatent') > 0:
                self.GatherPatent = self.getBoolean(line)
            elif line.count('GatherFamilly') > 0:
                self.GatherFamilly = self.getBoolean(line)
            elif line.count('OPSGatherContentsv2-Iramuteq') > 0:
                self.GatherIramuteq = self.getBoolean(line)

            # Networks config loading
            elif line.count('InventorNetwork') > 0:
                self.InventorNetwork = self.getBoolean(line)
            elif line.count('ApplicantNetwork') > 0:
                self.ApplicantNetwork = self.getBoolean(line)
            elif line.count('ApplicantInventorNetwork') > 0:
                self.ApplicantInventorNetwork = self.getBoolean(line)
            elif line.count('InventorCrossTechNetwork') > 0:
                self.InventorCrossTechNetwork = self.getBoolean(line)
            elif line.count('ApplicantCrossTechNetwork') > 0:
                self.ApplicantCrossTechNetwork = self.getBoolean(line)
            elif line.count('CountryCrossTechNetwork') > 0:
                self.CountryCrossTechNetwork = self.getBoolean(line)
            elif line.count('CrossTechNetwork') > 0:
                self.CrossTechNetwork = self.getBoolean(line)
            elif line.count('CompleteNetwork') > 0:
                self.CompleteNetwork = self.getBoolean(line)
            elif line.count('FamiliesNetwork') > 0:
                self.FamiliesNetwork = self.getBoolean(line)
            elif line.count('FamiliesHierarchicNetwork') > 0:
                self.FamiliesHierarchicNetwork = self.getBoolean(line)
            elif line.count('References') > 0:
                self.References = self.getBoolean(line)
            elif line.count('Citations') > 0:
                self.Citations = self.getBoolean(line)
            elif line.count('Equivalents') > 0:
                self.Equivalents = self.getBoolean(line)
            elif line.count('FormateExportCountryCartography') > 0:
                self.FormateExportCountryCartography = self.getBoolean(line)
            elif line.count('FormateExportBiblio') > 0:
                self.FormateExportBiblio = self.getBoolean(line)
            elif line.count('P2N-FreePlane') > 0:
                self.FreePlane = self.getBoolean(line)
            elif line.count('FusionCarrot2') > 0:
                self.FusionCarrot2 = self.getBoolean(line)

        self.generatePaths()

    def readInputFile(self):
        if len(sys.argv) > 1:
            for arg in sys.argv:
                if ".cql" in arg.lower():
                    return open(arg, "r").readlines()
        return open("..//requete.cql", "r").readlines()

    def generatePaths(self):
        self.ResultPath = '..//DATA//' + self.ndf
        self.ListPatentPath = self.ResultPath+'//PatentLists'
        self.ResultPathBiblio = self.ResultPath+'//PatentBiblios'
        self.ResultContents = self.ResultPath+'//PatentContents'
        self.temporPath = self.ResultPath+'//tempo'
        self.ResultAbstractPath = self.ResultContents+'//Abstract'
        self.ResultFamiliesAbstractPath = self.ResultContents+'//FamiliesAbstract'
        self.ResultPathGephi = self.ResultPath + '//GephiFiles'

        for path in [
            self.ListPatentPath,
            self.ResultPathBiblio,
            self.ResultContents,
            self.temporPath,
            self.ResultAbstractPath,
            self.ResultFamiliesAbstractPath,
            self.ResultPathGephi,
        ]:
            if not os.path.isdir(path):
                os.makedirs(path)

    def getStr(self, line):
        return line.split(':')[1].strip()

    def getBoolean(self, line):
        s = self.getStr(line)
        if s.count('True') > 0 or s.count('true') > 0:
            return True # to gather contents
        else:
            return False

def LoadConfig():
    return P2NConfig()
