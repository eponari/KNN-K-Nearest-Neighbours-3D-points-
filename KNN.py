#eponari19
import operator
from classes import *


points,k=[int(x) for x in input().split()]

items=[]

for i in range(points):
  x,y,z,name=[x for x in input().split()]
  items.append(item(point(int(x),int(y),int(z)),name))

requestedKNN=input()
requestedKNN=int(requestedKNN)

for i in range(requestedKNN):
  x,y,z=[int(x) for x in input().split()]
  main_point=point(x,y,z)
  close_items={}
  items.sort(key=lambda x: (x.dist_from_main(main_point),x.name))
  i=0
  while(i<points and i<requestedKNN):
    if items[i].name not in close_items:
      close_items[items[i].name]=1
    else:
      close_items[items[i].name]+=1
    i+=1
  print(max(close_items.items(), key=operator.itemgetter(1,0))[0])