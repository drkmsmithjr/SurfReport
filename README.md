# SurfReport
Surf Report Python Code

Check out the full blog at www.surfncircuits.com
**"Creating the "Surf Checker".  An Amazon Echo Skill"**

This file shows a stand along python code that will generate the surf report and tide information.   While a stand along project, it is also used to develope the underlying python datastructure and code for the Lambda function portion of the Amazon Surf Checker skill .         

New surf locations are added to the surfspot.cvs file.  You need the following:
* "location name"
* the SpotID
* regional ID
* NOAA Tide locater ID.    
 
The location name, SpotID, and regional ID can be taken from the HTTP address of the corresponding surfline.com surf report and the NOAA tide database located at https://tidesandcurrents.noaa.gov.  After adding, please submit a pull request and I'll add to master.   

defining the surf spots:

* Getting the SurfSpotID:
** The web report address for Salt Creek is: http://www.surfline.com/surf-report/salt-creek-southern-california_4233/
The SurfSpotID = 4233

* Getting the RegionalID:
  *  The RegionalID is found by going to the REgional web report.  For Salt Creek, this is :
http://www.surfline.com/surf-forecasts/southern-california/south-orange-county_2950/
The RegionalIP = 2950

* Getting the NOAA Tide ID location: 
  * go to the following WEb page:
 https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1393
find the closest Tide Sensor ID for salt Creek.   This will be San Clemente. 
the NOAA_TideID = TWC0419 

** verify you get tide data using the following format
 https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20171104&end_date=20171105&datum=MLLW&station=XXXXXX&time_zone=lst_ldt&units=english&interval=hilo&format=json 
   where you replace XXXXXX with the NOAA_TideID name: (i.e. TWC0419)
  
By Mark Smith, www.Surfncircuits.com
copyright (c) 2017 www.surfncircuits.com

Code was  uses the www.surfline.com API
 
The surfline API code was modified from 
Code Written by Colin Karpfinger
https://github.com/PunchThrough/BeanSurfMap

copyright (c) 2014 Punch Through Design

