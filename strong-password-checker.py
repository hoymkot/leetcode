# Leetcode strong password checker
# https://leetcode.com/problems/strong-password-checker/
# make it run in 12 ms  92.96 %
class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        pwd = password

        lower = "qwertyuiopasdfghjklzxcvbnm"
        upper = lower.upper()
        digit = "1234567890"

        self.miss = 0

        if self.checkContain(pwd, lower):
            self.miss = self.miss + 1
        if self.checkContain(pwd, upper):
            self.miss = self.miss + 1
        if self.checkContain(pwd, digit):
            self.miss = self.miss + 1

        ans = self.findRepeat(pwd)

        if 6 <= len(pwd) and len(pwd) <= 20:
            # no need to insert/delete
            # min digit requirement can merge with repeating character replacement
            repeat = self.getReplacement(ans)
            return max(repeat, self.miss)
        # need some inserts to make len(pwd) >= 6
        # insert, repeat, missing char can all be fixed at the same time
        if len(pwd) < 6:
            repeat = self.getReplacement(ans)
            return max(6 - len(pwd), self.miss, repeat)
        if len(pwd) > 20:
            self.delete = len(pwd) - 20
            self.step = 0

            while self.delete > 0 and len(ans[0]) > 0:
                self.delete = self.delete - 1
                self.step = self.step + 1
                new = ans[0].pop() - 1
                if new > 2:
                    ans[2].append(new)

            if self.delete == 0:
                return max(self.getReplacement(ans), self.miss) + self.step

            while self.delete > 1 and len(ans[1]) > 0:
                self.delete = self.delete - 2
                self.step = self.step + 2
                new = ans[1].pop() - 2
                if new > 2:
                    ans[2].append(new)

            if self.delete == 1:
                self.step = self.step + 1
                self.delete = self.delete - 1

            if self.delete == 0:
                return max(self.getReplacement(ans), self.miss) + self.step

            while self.delete > 2 and len(ans[2]) > 0:
                self.delete = self.delete - 3
                self.step = self.step + 3
                new = ans[2].pop() - 3
                if new > 2:
                    ans[2].append(new)

            if self.delete > 0:
                self.step = self.step + self.delete
                self.delete = 0

            if self.delete == 0:
                return max(self.getReplacement(ans), self.miss) + self.step


    def getReplacement(self, ans):
        r = 0
        for i in ans[0]:
            r = r + int(i/3)
        for i in ans[1]:
            r = r + int(i/3)
        for i in ans[2]:
            r = r + int(i/3)
        return r

    #O(n)
    def findRepeat(self, pwd):
        c = str(pwd[0])
        count = 1
        ans = [[],[],[]]
        for i in pwd[1:]:
            i = str(i)
            if i == c:
                count = count + 1
            else:
                if count >2 :
                    idx = count % 3
                    ans[idx].append(count)
                count = 1
                c = i
        if  count > 2  :
            idx = count % 3
            ans[idx].append(count)
        return ans;

    #O(n)
    def checkContain(self, pwd, chars):
        for c in pwd:
            if c in chars:
                return 0
        return 1;
