class CompanyClass:
    companyName = "ABC"
    companyRegistration = "PVT LTD"
    companyAddress = "XYZ"
    companySize = 100
    companyLocation = "ABCDEFGH"

#This is a default constructor
#if not given values it checks for default values in init. Should be assigned from right to left in init
    def __int__(self,cmpName,cmpReg,cmpAdd,cmpSize,cmploc):
        self.companyName = cmpName
        self.companyRegistration = cmpReg
        self.companyAddress = cmpAdd
        self.companySize = cmpSize
        self.companyLocation = cmploc


    def DisplayCompanyDetails(self):
        print("The Company Details are: ", "\n",self.companyName, "\n", self.companyRegistration, "\n", self.companyAddress, "\n", self.companySize, "\n", self.companyLocation)

    def UpdateCompanyAddress(self):
        self.companyAddress = input("Enter the new Company Addresss:")
        print("The new Company Address is:",self.companyAddress)

    def CompanyEmpCount(self):
        print("The number of employess in the company are:", self.companySize)

#This is User Defined Constructor
companyObj = CompanyClass()
companyObj.companyName = "EKIP IT"
companyObj.companyRegistration = "MCA Registration"
companyObj.companyAddress = "Banjara"
companyObj.companySize = 150
companyObj.companyLocation = "Hitech City"


companyObj.DisplayCompanyDetails()
