"""
mySurfReport

#Written by Mark Smith, www.surfncircuits.com

"""
#
from surfreport import SurfSpot,spots, getsurfspots
import time
#from surfreport import spots

if __name__ == "__main__":
    reports = []
    # add more surf spots to spots
    spots = getsurfspots(spots)
    # create an array of surf report objects
    #sName = 'steamer lane'
    #report = SurfSpot(sName,spots[sName][0],spots[sName][1],spots[sName][2],spots[sName][3])
    #report.getReport()
    #print(report.printReport(0))
    #report.getWaterTemp()
    #print(report.printWaterTemp())
    
    numsurfreports = 0
    numbestday = 0
    numtidereports = 0
    numwatertemps = 0
    errorMsg = ""
    getMsg = ""
    failedreportmessages = []
    
    for spot in spots:
        report = SurfSpot(spot, spots[spot][0], spots[spot][1], spots[spot][2], spots[spot][3])
        reports.append(report)  
     
    for r in reports:
        # we need to call tehse reports to get info and search
        #try:
        print(r.spotName)
        try:
           r.getReport()
           numsurfreports += 1
           for x in range(0,6):
              print("  " + r.printReport(x))
        except:
           errorMsg = "ERROR getting surf report/best day for " + r.spotName 
           print(errorMsg) 
           failedreportmessages.append(errorMsg)
        try:      
           print("  " + r.printBestDayToSurf())
           numbestday += 1
        except:
           errorMsg = "ERROR getting surf BEST DAY for " + r.spotName
           print(errorMsg)
           failedreportmessages.append(errorMsg)
        #time.sleep(0.5)   
   
    for r in reports:
       # we need to call tehse reports to get info and search
       #try:
       print(r.spotName) 
       try:         
          r.getTideReport()
          for x in range(0,6):
             print("  " + r.printTideReport(x))
          numtidereports += 1
       except:
          errorMsg = "ERROR getting the tide report for " + r.spotName
          print(errorMsg)
          failedreportmessages.append(errorMsg)
          TEST_FAILED = True
       #time.sleep(0.5)
    for r in reports:
       # we need to call tehse reports to get info and search
       #try:
       print(r.spotName)
       #r.getWaterTemp()
       #print("  " + r.printWaterTemp())         
       try:
          r.getWaterTemp()
          getMsg = "  " + r.printWaterTemp()
          if "Sorry" in getMsg:
             getMsg = "ERROR getting the water temp for " + r.spotName
             failedreportmessages.append(getMsg)
          else:
             numwatertemps += 1   
          print(getMsg)         
       except:
          errorMsg = "ERROR getting the water temp for " + r.spotName
          print(errorMsg)
          failedreportmessages.append(errorMsg)
       #time.sleep(0.5) 
    print("The total reports available: " + str(len(reports)))          
    print("Successful Surf reports : " + str(numsurfreports))
    print("Successful best Day reports: " + str(numbestday))
    print("Successful tide reports: " + str(numtidereports))
    print("Successful water temp reports: " + str(numwatertemps))
    for x in failedreportmessages:
       print (x)
       
    
    