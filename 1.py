        def nnn(n):
            n=str(n)	
            c=list(n)
            c.append('d')
            #print c
            count=1
            i=0
            d=[]
            while (i < len(c) - 1):
                if (c[i] == c[i + 1]):
                    count = count + 1
                    i = i + 1
                else:
                    d.append(count)
                    d.append(int(c[i]))
                    count = 1
                    i = i + 1
                    if (c[i] == d):
                        continue
            f = int(''.join(map(str, d)))
            return f

        number=1
        for i in range(n-1):
            number=nnn(number)
        number=str(number)
        return number
