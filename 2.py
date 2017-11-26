        x = 0
        y = 0
        for i in range(len(nums)):
            y = y + nums[i]
            if (y < 0):
                y = 0
            if (x < y):
                x = y
        if (x==0):
            return max(nums)

        return x
