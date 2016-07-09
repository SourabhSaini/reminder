import os, re
import time, notify2
def Main():
	while True:
		try:
			remFile = open('reminder','r')
			for line in remFile:
				data = re.match('(.*)\:(.*)\#(.*)\#(.*)',line)
				hour = data.group(1)
				mins = data.group(2)
				title = data.group(3)
				note = data.group(4)
				if int(hour) == time.localtime().tm_hour and int(mins) == time.localtime().tm_min:
					notify2.init('Reminder')
					n = notify2.Notification(title, note)
					n.show()
					os.system('aplay /home/minion/Desktop/Python/Reminder/beep.wav')
					with open("tempFile","w") as tempFile: 
						for w_line in remFile:
							if w_line!=line:
								tempFile.write(w_line)
					os.system('rm reminder | mv tempFile reminder')
		except Exception:
			print('File not Found/Invalid String Found')
		
		time.sleep(60)

if __name__ == '__main__':
	while True:
		secs = time.localtime().tm_sec
		if secs == 0:
			Main()
		else:
			time.sleep(60 - secs)
