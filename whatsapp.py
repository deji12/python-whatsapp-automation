# pywhatkit.sendwhatmsg("Number", "Message", hour(integer), minute(integer))

import pywhatkit
num = input('> Enter recipients number: ')
print()
msg = input('> Enter message: ')
print()
tod = input('> Enter time of delivery(8:45): ')
print()
splitted_time = tod.split(":")
hour = int(splitted_time[0])
minute = int(splitted_time[1])
pywhatkit.sendwhatmsg(num, msg, hour, minute)

