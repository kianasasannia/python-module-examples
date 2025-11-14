import time
'''
The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT),
January 1, 1970
(Coordinated Universal Time | UTC)
'''

seconds = time.time()
print("Seconds since epoch =", seconds)

seconds = 000000000000
local_time = time.ctime(seconds)
print("Local time:", local_time)

print("This is printed immediately.")
time.sleep(3)
print("This is printed after 3 seconds.")

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)

seconds = 1545925769

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)

