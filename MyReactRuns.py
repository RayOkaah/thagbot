#!/usr/bin/env python2
# -*- coding: utf-8 -*- #
#Author:	Ray Okaah

from TwitterFollowBot import TwitterBot

#Below, Raybotlist is Depreciated
#Raybotlist = "m1.txt,m2.txt,m3.txt,m4.txt,m5.txt,m6.txt,m7.txt,m8.txt,,m9.txt,m10.txt,m11.txt,m12.txt,m13.txt,m14.txt,m15.txt,m16.txt,m17.txt,m18.txt,m19.txt,m20.txt,m21.txt,m22.txt,m23.txt,m24.txt,m25.txt,m26.txt,m27.txt,m28.txt,m29.txt,m30.txt,m31.txt,m32.txt,m33.txt,m34.txt,m35.txt,m36.txt,m37.txt,m38.txt,m39.txt,m40.txt,m41.txt,m42.txt,m43.txt,m44.txt,m45.txt,m46.txt,m47.txt,m48.txt,m49.txt,m50.txt"

def main():
	#workingdir = os.getcwd()
	#Raybotdir = os.listdir(workingdir+"/AllBotConfig/")
	Raybotdir = os.listdir("https://guarded-chamber-8525.herokuapp.com/AllBotConfig/")
	for ig in Raybotdir:
		my_bot = TwitterBot("/AllBotConfig/"+ig)
		my_bot.auto_fav("#Rayviewz", count=30) #Automatically favourite any tweet with a specitfic phrase.
		my_bot.auto_rt("#Rayviewz", count=10) # Automatically retweet any tweet with a specitfic phrase.
		
main()
if __name__ == '__main__':
    bot = MyReactRuns()
    bot.run()