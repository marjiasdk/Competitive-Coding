dict_pm_to_am = {
    "01": "13",
    "02": "14",
    "03": "15",
    "04": "16",
    "05": "17",
    "06": "18",
    "07": "19",
    "08": "20",
    "09": "21",
    "10": "22",
    "11": "23",
    "12": "12"
}

dict_am_to_am = {
    "12" : "00"
}

def timeConversion(s):
    s = s.split(":")
    if s[2][2:] == "PM":
        s[0] = dict_pm_to_am[s[0]]
        s[2] = s[2].replace("PM", "")
    else:
        s[2] = s[2].replace("AM", "")
        if s[0] == "12":
            s[0] = dict_am_to_am[s[0]]
    return ":".join(s)

if __name__ == '__main__':
    pm_time = input()
    result = timeConversion(pm_time)
    print(result)