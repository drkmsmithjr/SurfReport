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
    #report = SurfSpot('salf creek',spots['salt creek'][0],spots['salt creek'][1],spots['salt creek'][2],spots['salt creek'][3])
    #report.getReport()
    #print(report.printReport(0))
    #report.getWaterTemp()
    #print(report.printWaterTemp())
    for spot in spots:
        if len(spots[spot])==4:
           report = SurfSpot(spot, spots[spot][0], spots[spot][1], spots[spot][2], spots[spot][3])
        else:
           report = SurfSpot(spot, spots[spot][0], spots[spot][1], spots[spot][2]) 
        reports.append(report)
        #print(spots)
        #break
        
     
    for r in reports:
        # we need to call tehse reports to get info and search
        #try:
           r.getReport()
        #   print(r.printReport(0))
        #except:
        #   print("there was an issue getting the surf report: please try later")
        #try:
           #r.getTideReport()
           #print(r.printTideReport(0))
           r.getWaterTemp()
           print(r.printWaterTemp())
           
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