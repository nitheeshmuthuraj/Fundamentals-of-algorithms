	ih=len(triangle[-1])-1 
        il=ih
        j=0
              
        for v in range(ih,0,-1):
            for i in range(0,v,1):
                triangle[v-1][j]=triangle[v-1][j]+min(triangle[il][i],triangle[il][i+1])
                j=j+1
            il=il-1
            j=0
        return triangle[0][0]
