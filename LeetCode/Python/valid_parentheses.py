class Solution:
    def isValid(self, s: str) -> bool:
        # while True is a loop that will run until the break statement is executed
        # it is used when we want to loop indefinitely, and break out of the loop when a condition is met
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                break
        """
        if len(s) == 0:
            return True
        else:
            return False
        """
        # len(s) == 0 would mean that it would be empty, i.e. ""
        return len(s) == 0