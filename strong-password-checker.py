# Leetcode strong password checker
# https://leetcode.com/problems/strong-password-checker/

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

        self.count = 0

        if self.checkContain(pwd, lower):
            self.count = self.count + 1
        if self.checkContain(pwd, upper):
            self.count = self.count + 1
        if self.checkContain(pwd, digit):
            self.count = self.count + 1


        if 6 <= len(pwd) and len(pwd) <= 20:
            # no need to insert/delete
            # min digit requirement can merge with repeating character replacement
            repeat = self.checkRepeat(pwd)
            return max(repeat, self.count)
        # need some inserts to make len(pwd) >= 6
        # insert, repeat, missing char can all be fixed at the same time
        if len(pwd) < 6:
            repeat = self.checkRepeat(pwd)
            return max(6 - len(pwd), self.count, repeat)
        if len(pwd) > 20:
            self.delete = len(pwd) - 20
            self.step = 0
            pwd, solved = self.tradeDelete(pwd, 0)
            if solved == True:
                return pwd # answer
            pwd, solved = self.tradeDelete(pwd, 1)
            if solved == True:
                return pwd # answer
            after, solved = self.tradeDelete(pwd, 2)
            while solved != True and len(after) < len(pwd):
                pwd = after
                after, solved = self.tradeDelete(pwd, 2)
            if solved:
                return after # answer
            else:
                return self.count + self.step + self.delete


    def tradeDelete(self, pwd, mod):
        i = 0
        while i < len(pwd):
            next = self.findRepeat(pwd, i)
            temp = pwd[i:next]
            if (len(temp) > 2):
                if len(temp) % 3 == mod:
                    if self.delete <= (mod+1):
                        pwd = pwd[0:i] + temp[self.delete:] + pwd[next:]
                        self.step = self.step + self.delete
                        self.delete = 0
                        repeat = self.checkRepeat(pwd)
                        return max(repeat, self.count) + self.step, True
                        # done
                    else:
                        prev = pwd[0:i] + temp[(mod+1):]
                        pwd = prev + pwd[next:]
                        self.delete = self.delete - (mod+1)
                        self.step = self.step + (mod+1)
                        next = len(prev)
            i = next;
        return pwd, False

    def findRepeat(self, pwd, start):
        i = start
        if i < len(pwd):
            c = str(pwd[i])
            temp = c
            for j in range(i + 1, len(pwd)):
                if str(pwd[j]) != c:
                    return j
            return len(pwd)
        else:
            return len(pwd)

    def checkContain(self, pwd, chars):
        for c in pwd:
            if c in chars:
                return 0
        return 1;

    def checkRepeat(self, pwd):
        if (len(pwd) < 3):
            return 0
        p1 = pwd[0]
        p2 = pwd[1]
        step = 0
        for c in pwd[2:]:
            if (c == p2 and c == p1):
                step = step + 1;
                p1 = None
                p2 = None
            else:
                p1 = p2
                p2 = c
        return step
