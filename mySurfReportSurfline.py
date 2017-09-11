"""
mySurfReport

#Written by Mark Smith, www.surfncircuits.com
#Based on Code Written by Colin Karpfinger
# http://punchthrough.com/bean
# http://punchthrough.com/bean/examples/surf-report-notifier/
# https://github.com/PunchThrough/BeanSurfMap
# copyright (c) 2014 Punch Through Design
"""

# defining the surf spots

spots = {
    'uppers':["4738","2950"],
    'upper trestles':["4738","2950"],
    'upper':["4738","2950"],
    'salt creek':["4233","2950"],
    'doheny':["4848","2950"],
    'doheny state beach':["4848","2950"],
    'lowers':["4740","2950"],
    'lower trestles':["4740","2950"],
    'lower':["4740","2950"],
    't-street':["4235","2950"],
    'T. street' :["4235","2950"],
    'san clementi state beach':["4843","2950"],
    'the point':["4237","2950"],
    'old mans':["109918","2950"],
    'hb pier':["4874","2143"],
    'HB pier':["4874","2143"],
    'h. b. pier':["4874","2143"],
    'Huntington beach pier':["4874","2143"],
    '56th street':["43103","2143"],
    'fifty sixth street':["43103","2143"],
    'the wedge':["4232","2143"],
    'goldenwest':["4870","2143"],
    'golden west':["4870","2143"],
    'huntington state beach':["103681","2143"],
    'Huntington state beach':["103681","2143"],
    'seal beach':["4217","2143"],
    'bolsa chica':["4868","2143"],
    'bolsa chica state beach':["4868","2143"],
    'Newport point':["4877","2143"],
    'blackies':["53412","2143"]    
}


# Class Surfspot uses the 
# Surfline API Report Parser 
# modified by Mark Smith
# www.surfncircuit.com
# removed the tide information
# Used surfMax and surfMin from spot report and regional report 
# added SurfText inputs.    

# Based on Code Written by Colin Karpfinger
# http://punchthrough.com/bean
# http://punchthrough.com/bean/examples/surf-report-notifier/
# https://github.com/PunchThrough/BeanSurfMap
# copyright (c) 2014 Punch Through Design

import datetime
import urllib2
import json
import time
from decimal import *
import string

daysInReport = 6
conditionTypes=["","flat", "very poor", "poor","poor to fair","fair","fair to good","good","very good","good to epic","epic"]

class SurfSpot:
    baseUrl="http://api.surfline.com/v1/forecasts/0000?resources=surf,analysis&days=6&getAllSpots=false&units=e&interpolate=false&showOptimal=false"
    heightsMax=[]
    heightsMin=[]

    surflineUrl=""
    tideUrl=""
    surflineRegionalUrl=""
    surflineName=""
    textConditions=[]
    spotName =""
    todaysLocalCondition=0
    regionalConditions=[]
    
    def __init__(self, spotName, spotID, regionalID):
        # create object with the spot name, spotID and regionalID.  Both are available in HTTP addresss associaed with  
        # the surfline.com site.    
        self.spotName = spotName
        self.surflineUrl=self.baseUrl.replace("0000",spotID)
        self.surflineRegionalUrl=self.baseUrl.replace("0000",regionalID)

        self.heightsMax=[]
        self.heightsMin=[]
        self.surfText=[]
        self.regionalConditions=[]
        
    def getReport(self):
        # use the spot API to get the current information
        # use the regional API address (regionalReport) to get the forecast information
        
        webreq = urllib2.Request(self.surflineUrl, None, {'user-agent':'syncstream/vimeo'})
        opener = urllib2.build_opener()
        f = opener.open(webreq)
        fstr = f.read()
        fstr = fstr.replace(')','') #remove closing )
        fstr = fstr.replace(';','') #remove semicolon
        fstr = fstr.strip() #remove any whitespace in start/end
        rep = json.loads(fstr)

        webreq = urllib2.Request(self.surflineRegionalUrl, None, {'user-agent':'syncstream/vimeo'})
        opener = urllib2.build_opener()
        f = opener.open(webreq)
        fstr = f.read()
        fstr = fstr.replace(')','') #remove closing )
        fstr = fstr.replace(';','') #remove semicolon
        fstr = fstr.strip() #rem3ove any whitespace in start/end
        regionalReport=json.loads(fstr)


        self.surflineName=rep["name"]
        for day in range(0,daysInReport):
            daysAvgMax=0
            daysAvgMin=0
            self.regionalConditions.append(conditionTypes.index(regionalReport["Analysis"]["generalCondition"][day]))
            if day == 0:
               if (len(rep["Analysis"]["surfMax"]) > 0) :
                  daysAvgMax=rep["Analysis"]["surfMax"][day]
                  daysAvgMin=rep["Analysis"]["surfMin"][day]
                  self.surfText.append(rep["Analysis"]["surfText"][day])
               else:
                  daysAvgMax=regionalReport["Analysis"]["surfMax"][day]
                  daysAvgMin=regionalReport["Analysis"]["surfMin"][day]
                  self.surfText.append(regionalReport["Analysis"]["surfText"][day])
            else:
               daysAvgMax=regionalReport["Analysis"]["surfMax"][day]
               daysAvgMin=regionalReport["Analysis"]["surfMin"][day]
               self.surfText.append(regionalReport["Analysis"]["surfText"][day])
                               
 
 #           self.heightsMax.append(Decimal(daysAvgMax).quantize(Decimal('1'), rounding=ROUND_UP))
 #           self.heightsMin.append(Decimal(daysAvgMin).quantize(Decimal('1'), rounding=ROUND_UP))
            self.heightsMax.append(daysAvgMax)
            self.heightsMin.append(daysAvgMin)
            
    def printReport(self, day = None):
    # print the day in the report. day 1 is current day
    # when no day is present just show all days in forecast  
        reportText=self.spotName+" is "
        if day == None:
            for day in range(0,daysInReport):
                reportText=reportText+str(self.heightsMin[day])+"-"+str(self.heightsMax[day])+" ft. "+str(conditionTypes[self.regionalConditions[day]])+"  " + str(self.surfText[day])+"  "
        else:
            if day >= daysInReport:
                day = daysInReport - 1
            reportText=reportText+str(self.heightsMin[day])+"-"+str(self.heightsMax[day])+" ft. "+str(conditionTypes[self.regionalConditions[day]])+"  " + str(self.surfText[day])+"  "
        reportText = reportText + "\n"    
        #print reportText
        return reportText

if __name__ == "__main__":
    reports = []
    # create an array of surf report objects
    for spot in spots:
        report = SurfSpot(spot, spots[spot][0], spots[spot][1])
        reports.append(report)
    for r in reports:
        r.getReport()
        print(r.printReport(0))