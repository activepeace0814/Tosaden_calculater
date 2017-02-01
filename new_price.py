#!/usr/bin/env python
# -*- coding: utf-8 -*-
# price.py
import codecs
def inputstation(a):
	global flag
	flag = False
	while 1:												#乗車駅の入力
		if a==1:
			print('乗車駅を入力してください:', end='')
		if a==2:
			print('降車駅を入力してください:', end='')
		stname = input()

		if not stname:
			flag = True
		if not stname or stname in station:				#入力された文字が空か辞書stationにあるときbreak
			break
		print("その駅は存在しません")
		print('******************')
	return stname

print ('*** とさでん運賃計算 ***')
f = codecs.open('new_stationlist.dat', 'r', 'utf-8')
station = {}    #辞書station
st = 1
while 1:
    s = f.readline().strip()
    if not s:
        break

    s, u, snumride, snumoff = s.split()    #駅名、均一区間の種類、整理券番号の順に読み取り
    u = int(u)    #均一区間の種類を文字列から数字に型変換
    snumride = int(snumride)    #整理券番号を文字列から数字に型変換
    snumoff = int(snumoff)    #整理券番号を文字列から数字に型変換

    station[s] = (st, u, snumride, snumoff)    #辞書[駅名] = (駅番号, 均一区間の種類, 乗車時に考える整理券番号, 降車時の整理券番号)の要素にタプルとして登録
    st = st + 1    #駅番号のカウンター+1
f.close()

while 1:
	s1 = inputstation(1)
	if flag:
		break

	s2 = inputstation(2)
	if flag:
		break

	u = station[s1][1]+ station[s2][1]    #均一区間の判定
	if u>2:
		print ('運賃は均一区間200円です')
	else:
		if station[s1][0] < station[s2][0]:    #駅番号の判定
			sa = station[s1][2]
			sb = station[s2][3]
		else:                                  #駅の順番を入れ替える
			sa = station[s2][2]
			sb = station[s1][3]

		a = sb-sa							   #整理券番号の差をとる
		if a==1:      #整理券番号の差が1であれば常に120円
			print ('運賃は120円です')

		elif sa==1:
			if sb<=3:
				print ('運賃は220円です')
			elif sb==4 and station[s2][1]<=1:
				print ('運賃は300円です')
			else:
				print ('運賃は460円です')

		elif sa==2:
			if sb==4 and u==1:
				print ('運賃は220円です')
			elif sb==4 and u==2:
				print ('運賃は400円です')
			else:
				print ('運賃は460円です')

		elif sa==3:
			if sb==4 or sb==5:
				print ('運賃は300円です')
			elif sb==6:
				print ('運賃は400円です')
			else:
				print ('運賃は460円です')

		elif sa==4:
			if sb==6:
				print ('運賃は300円です')
			elif sb==7:
				print ('運賃は400円です')
			else:
				print ('運賃は460円です')

		elif sa==5:
			if sb==7:
				print ('運賃は220円です')
			else:
				print ('運賃は300円です')

		elif sa==6:
			print ('運賃は220円です')

print ('*** さよなら ***')
