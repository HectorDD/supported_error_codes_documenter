

def getCarrierErrorAndCanonicalError(fileName,fileName2):
    f= open(fileName,"r")
    f2=open(fileName2,"w+")
    f1=f.readlines()
    listOfErrors=[]
    for i in f1:
        carrierError=""
        canonicalError=""
        quoteCounter=0
        findDot=False
        findComma=False
        error=[]
        for j in i:
            if quoteCounter==1 and j!='"':
                    carrierError+=j
            if findDot and not findComma and j!=",":
                canonicalError+=j
            if j=='"':
                quoteCounter+=1
            elif j==".":
                findDot=True
            elif j=="," and findDot:
                findComma=True
        f2.write(carrierError+","+canonicalError+"\n")
        error.append(carrierError)
        error.append(canonicalError)
        listOfErrors.append(error)
    return listOfErrors

def supportedErrors(listOfErrors,fileWithErrors,resultFile):
    f=open(fileWithErrors,"r")
    f2=open(resultFile,"w+")
    f1=f.readlines()
    acErrors=[]
    for i in f1:
        acErrors.append(i)
        supported=False
        for j in listOfErrors:
            if j[0] in i:
                supported=True
                f2.write("supported,"+j[1]+"\n")
                break
        if not supported:
            f2.write("unsupported,undefined\n")
    return acErrors
            
def diffErrors(pamErrors,ACErrors):
    f=open("carrier.txt","r")
    f1=f.readlines()
    for i in pamErrors:
        found=False
        for j in f1:
            if i[0] in j:
                found=True
        if not found:
            print(i[0])
            

listOfErrors=getCarrierErrorAndCanonicalError("enum.txt","enum.csv")
acErrors=supportedErrors(listOfErrors,"carrier.txt","carrier.csv")
diffErrors(listOfErrors,acErrors)



