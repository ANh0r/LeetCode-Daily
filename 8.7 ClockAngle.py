# # class Solution {
#     public double angleClock(int hour, int minutes) {
#         /*
#             整个盘 360 度，有 12 个小时，那么每个小时占 30 度
#             每个小时占 30 度，每个小时有 60 分钟，那么对于时针来说，每走过一分钟时针就走过 0.5 度
#
#             整个盘 360 度，有 60 分钟，那么每分钟占 6 度
#
#             整个盘分钟走过的读书 minPoint = minutes * 6
#             时针所在的度数 hourPoint = 小时数 hour * 30 + 分针 minutes * 0.5
#
#             然后求两者之差，要保证小于等于 180 度，如果超过 180 度，那么求其对于 360 度的补角
#         */
#         int minPoint = minutes * 6;
#         double hourPoint = hour * 30 + minutes * 0.5;
#         double diffPoint = Math.abs(minPoint - hourPoint);
#         return diffPoint > 180 ? 360 - diffPoint : diffPoint;
#     }
# }

#  上边是C的解法

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour %= 12
        # m = 6*minutes
        # h = 30*hour + minutes/2
        # ans = abs(m - h)
        # return min(ans, 360 - ans)
        a = 30 * hour + 30 * minutes / 60
        b = 6 * minutes
        res = abs(a - b)
        return  res if res <= 180 else 360 - res