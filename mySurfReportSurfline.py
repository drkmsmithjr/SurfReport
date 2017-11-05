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
from surfreport import SurfSpot,spots
#from surfreport import spots

if __name__ == "__main__":
    reports = []
    # create an array of surf report objects
    for spot in spots:
        report = SurfSpot(spot, spots[spot][0], spots[spot][1], spots[spot][2])
        reports.append(report)
        print(spot)
    for r in reports:
        # we need to call tehse reports to get info and search
        r.getReport()
        r.getTideReport()
        
        print(r.printReport(0))
        print(r.printTideReport(0))
        print(r.printBestDayToSurf())
        print("On this day ")
        print(r.printReport(r.bestdaytosurf))     
        break