"""
mySurfReport

#Written by Mark Smith, www.surfncircuits.com
#Based on Code Written by Colin Karpfinger
# http://punchthrough.com/bean
# http://punchthrough.com/bean/examples/surf-report-notifier/
# https://github.com/PunchThrough/BeanSurfMap
# copyright (c) 2014 Punch Through Design
"""

#
from surfreport import SurfSpot,spots, getsurfspots
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
    for spot in spots:
        report = SurfSpot(spot, spots[spot][0], spots[spot][1], spots[spot][2], spots[spot][3])
        reports.append(report)
        #print(spot)
        #break
        
     
    for r in reports:
        # we need to call tehse reports to get info and search
        #try:
        print(r.spotName)
        r.getReport()
        r.getTideReport()
        for x in range(0,6):
           print("  " + r.printReport(x))
        for x in range(0,6):
           print("  " + r.printTideReport(x))
        r.getWaterTemp()
        print("  " + r.printWaterTemp())
           
        #except:
        #   print("there was an issue getting the tide report: please try later") 
        
           #print(r.printBestDayToSurf())
        #print("On this day ")
        #print(r.printReport(r.bestdaytosurf))  
        #try:
        #   r.getTideReport()
        #   print(r.printTideReport(2))
        #except:
        #   print("there was an issue getting the tide report: please try later")
                
           #break