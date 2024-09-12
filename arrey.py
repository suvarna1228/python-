def rev_arrey(a,s,e):
    if s>=e:
        a[s],a[e]=a[e],a[s]
        rev_arrey(a,s+1,e-1)
a=[1,2,3,4,5]
rev_arrey(a,0,len(a)-1)
print(a)