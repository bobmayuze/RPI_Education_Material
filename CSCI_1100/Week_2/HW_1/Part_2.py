# Input time and distance
Minutes = input('Minutes ==> ') 
print(Minutes)
Seconds = input('Seconds ==> ') 
print(Seconds)
Miles = input('Miles ==> ') 
print(Miles)

# Calculate the total amount of time
Total_Seconds = int(Minutes)*60 + int(Seconds)

# Output the result
print('Pace is ',int(Total_Seconds / float(Miles)) // 60 ,'minutes and ',int(Total_Seconds / float(Miles) % 60),' seconds per mile.')
print('Speed is ',float(Miles)/Total_Seconds*3600,' miles per hour.')
