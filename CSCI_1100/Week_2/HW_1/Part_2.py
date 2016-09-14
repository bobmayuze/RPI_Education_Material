# Input time and distance
Minutes = int(input('Minutes ==> ')) 
print(Minutes)
Seconds = int(input('Seconds ==> ')) 
print(Seconds)
Miles = float(input('Miles ==> ')) 
print(Miles)

# Calculate the total amount of time
Total_Seconds = Minutes*60 + Seconds

# Output the result
print('\n'+'Pace is ',int(Total_Seconds / Miles) // 60 ,'minutes and ',int(Total_Seconds / Miles % 60),' seconds per mile.')
print('Speed is ',round(float(Miles)/Total_Seconds*3600,2),' miles per hour.')
