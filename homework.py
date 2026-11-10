
num=[1,4,5,7,9]

search = int(input("enter search number"))
found = False
l=0
mid=len(num)//2
h=len(num)-1


while l<=h and found==False: 
    if num[mid] == search:
        print("found at location "+str(mid))
        found=True
        break
    elif num[mid]>search:
        h=mid-1
        mid=(l+h)//2
    else:
        l=mid+1
        mid=(l+h)//2

if found == False:
    l=num[l]
    h=num[h]
    print("it belogs between "+str(h)+" and "+str(l))
