#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in 
#a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
#Any values that fall out of that range must be rounded to the closest valid value.
#
#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
#Examples (input --> output):
#255, 255, 255 --> "FFFFFF"
#255, 255, 300 --> "FFFFFF"
#0, 0, 0       --> "000000"
#148, 0, 211   --> "9400D3"

#solution

def rgb(r, g, b):
    list=[r,g,b]
    for i in range(0,3):
        if list[i]<0:
            list[i]=0
        elif list[i]>255:
            list[i]=255

    rh=hex(list[0])[2:].zfill(2).upper()
    gh=hex(list[1])[2:].zfill(2).upper()
    bh=hex(list[2])[2:].zfill(2).upper()
    res=rh+gh+bh
    return res
    pass

#test

print(rgb(255,255,255)) #should be "FFFFFF"
print(rgb(255,255,300)) #should be "FFFFFF"
print(rgb(0,0,0)) #should be "000000"
print(rgb(148,-6,211)) #should be "9400D3"