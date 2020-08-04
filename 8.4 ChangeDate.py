class Solution:
    def reformatDate(self, date: str) -> str:
        day , mon , year = date.split(' ')
        dic = {"Jan":1, "Feb":2, "Mar":3, "Apr":4,
               "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

        return "%s-%02d-%02d" % (year, dic[mon], int(day[:2]))


        #  print(day,dic[mon],year)
        #  date = '20th Oct 2052'


t = Solution()
print(t.reformatDate('23th Oct 2052'))