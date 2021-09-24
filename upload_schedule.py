import shutil, os
#This script pushes the field schedules to my onedrive, which syncs to sharepoint. This lets the display computer view the sheets as html.
#I set this script to run as a task every 4 hours

file = "\\\\utilities\\Administration\\Shared\\Schedules\\2021 MSO FIELD OPS ON CALL SCHEDULE - USE THIS ONE.xlsx"    
file2 = "\\\\utilities\\Administration\\Shared\Schedules\\2021 MSO-UT Field Ops 10 hour Shift Work Schedule.xls"
file3 = "\\\\utilities\\Administration\\Shared\Schedules\\2022 MSO-UT Field Ops 10 hour Shift Work Schedule.xls"

destination = "C:\\Users\\dsmith\\City of Lawrence KS\\Utilities SpvrsMgrs - Schedules" 

shutil.copy2(file, destination)
shutil.copy2(file2, destination)
shutil.copy2(file3, destination)