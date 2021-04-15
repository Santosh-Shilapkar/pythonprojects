import datetime,time
print("Lets find the time interval between two years |||||...")
datetime1=input("Enter the date1 in the format (yyyy-mm-dd):")
datetime2=input("Enter the date2 in the format (yyyy-mm-dd):")
datetime1 = datetime.datetime.strptime(datetime1,'%Y-%m-%d')
datetime2 = datetime.datetime.strptime(datetime2,'%Y-%m-%d')
difference=datetime2-datetime1
print("Wait for the response-----")
time.sleep(3)
print(difference.days,"days")