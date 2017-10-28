# SurfReport
Surf Report Python Code

Check out the full blog at www.surfncircuits.com
**"Creating the "Surf Checker".  An Amazon Echo Skill"**

This file shows a stand along python code that will generate the surf report and tide information.   While a stand along project, it is also used to develope the underlying python datastructure and code for the Lambda function portion of the Amazon Surf Checker skill .         

By Mark Smith, www.Surfncircuits.com
copyright (c) 2017 www.surfncircuits.com

Code was  uses the www.surfline.com API

New surf locations are shown in the spots DICT definition .   You need the following:
* "location name"
* the SpotID
* regional ID
* NOAA Tide locater ID.    
 
The location name, SpotID, and regional ID can be taken from the HTTP address of the corresponding surfline.com surf report and the NOAA tide database located at https://tidesandcurrents.noaa.gov


The surfline API code was modified from 

Code Written by Colin Karpfinger
https://github.com/PunchThrough/BeanSurfMap

copyright (c) 2014 Punch Through Design

