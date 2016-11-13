import os, random,subprocess,sys
for i in range(sys.argv[1]):
	string = "F:\TV series\F.R.I.E.N.D.S"
	str1 = random.choice(os.listdir(string))
	string = string + "\\"+str1
	str2 = random.choice(os.listdir(string))
	string = string + "\\"+ str2
	fo = open("friendsplaylist.m3u8","a")
	fo.write("\n"+string)
	fo.close()
	del string
p = subprocess.Popen([r"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",r"C:\Users\KUNAL\friendsplaylist.m3u8"])

p.wait()
if(p.returncode == 0):
	os.remove("friendsplaylist.m3u8") #delete the generated file so that theres always a (new)random number of episodes to watch
	
