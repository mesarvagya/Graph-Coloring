def mapcolour(inpulist):
  colors=[0,1,2,3,4,5]
  colorset=set(colors)
  final={}
  nodes=[0]*len(inpulist)
  adj=[0]*len(inpulist)
  flag=[0]*len(inpulist)
  assigncol=[0]*len(inpulist)
  colord=[0]*len(inpulist)
  i=0
  j=0
  m=0
  while(i<len(inpulist)):
    nodes[i]=i
    flag[i]=0
    adj[i]=inpulist[i] 
    i+=1
  while(j<len(inpulist)):
    for a in adj[j]:
      if flag[a] == 1 :
        colord.append(assigncol[a])
        colordset=set(colord)
        availset=colorset-colordset
        availlist=list(availset)
        assigncol[j]=availlist[0]
        flag[j]=1
        final[j]=assigncol[j]
        colord=[0]*len(inpulist)
        j+=1
  return final.values()
print mapcolour({'a':['b','c'],'b':['c','d']})