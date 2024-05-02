n = input()
mon = n[:3]
date = n[3:]
dian = {'Jan':'1','Feb':'2','Mar':'3','Apr':'4','May':'5','Jun':'6','Jul':'7','Aug':'8','Sep':'9','Oct':'10','Nov':'11','Dec':'12'}
if date[0]=='0':
    date = date[1:]
print(dian[mon],date)
