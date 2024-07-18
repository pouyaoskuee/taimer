import time

z=int(input("saat ra vared konid"))
y=int(input("dagige ra vared konid"))
x=int(input("sanye ra vared konid"))
l=60
q=x+y+z
for i in range(q):
     if x==0:
         y-=1
         break
     x-=1
     print(f"{z}:{y}:{x}")
     time.sleep(1)
while y!=-1:
    for i in range(q):
        l-=1
        print(f"{z}:{y}:{l}")
        if l==0:
            y-=1
            l += 60
        time.sleep(1)
l=60
y=59
z-=1
while z!=-1:
    while y != -1:
        for i in range(q):
            l -= 1
            print(f"{z}:{y}:{l}")
            if l == 0:
                y -= 1
                l += 60
            time.sleep(1)
