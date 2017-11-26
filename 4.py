	def check(x):
            r1=1
            r2=1
            for i in range(1,len(x)):
                if(x[i-1]=='1' or x[i-1]=='2' and int(x[i])<=6):
                    r1=r2+r1
                    r2=r1-r2
                else:
                    r2=r1
            return r1
            

        n=str(s)
        n=list(n)
        if(len(s)==0):
            return 0
        if(n[0]=='0'):
            return 0
        for i in range(len(n)): 
		if (n[i] == '0' and ((n[i - 1] != '1') and (n[i - 1] != '2'))):
                	return 0 
           	if(n[i]=='0' and ((n[i-1]=='1') or(n[i-1]=='2'))):
	                n[i]='-'
	                n[i-1]='-'
                              
        n=''.join(n)
        n=n.split('--')
        mul=1
        if (len(n)==0):
            return 1
        for i in n:
            mul=mul*check(i)
        return mul

