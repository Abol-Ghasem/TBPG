import hashlib
import json
from datetime import datetime


second_values = {
    "00": "a#A",
    "01": "#dR",
    "02": "X*c",
    "03": "B#N",
    "04": "Z$A",
    "05": "&lD",
    "06": "N&f",
    "07": "*qX",
    "08": "zA#",
    "09": "a#L",
    "10": "M&z",
    "11": "cD*",
    "12": "#pQ",
    "13": "Y$b",
    "14": "rN#",
    "15": "*Fz",
    "16": "a&W",
    "17": "#Xg",
    "18": "C$q",
    "19": "&Aq",
    "20": "o#Y",
    "21": "*NZ",
    "22": "L$w",
    "23": "#mD",
    "24": "x&A",
    "25": "d#T",
    "26": "V*B",
    "27": "$Cn",
    "28": "R&q",
    "29": "#Pb",
    "30": "W*z",
    "31": "g$X",
    "32": "t#R",
    "33": "F&L",
    "34": "D*P",
    "35": "$Wm",
    "36": "Z&q",
    "37": "l#N",
    "38": "X*A",
    "39": "p$C",
    "40": "#Lb",
    "41": "*nX",
    "42": "v&A",
    "43": "m$Y",
    "44": "C#T",
    "45": "&Dx",
    "46": "W*q",
    "47": "$fN",
    "48": "#vZ",
    "49": "*Ag",
    "50": "X$r",
    "51": "n#T",
    "52": "&Fz",
    "53": "b*C",
    "54": "$Wm",
    "55": "A&Z",
    "56": "#qN",
    "57": "*LX",
    "58": "Y$R",
    "59": "t#F",
    "60":"V&T"
}



minute_values = {
    "00": "1AB",
    "01": "X7G",
    "02": "Z2L",
    "03": "M8C",
    "04": "4YD",
    "05": "P9T",
    "06": "6QR",
    "07": "B3F",
    "08": "W5N",
    "09": "7JK",
    "10": "A2L",
    "11": "8XM",
    "12": "3CZ",
    "13": "Y4R",
    "14": "9TP",
    "15": "Q6F",
    "16": "5WN",
    "17": "B7L",
    "18": "4XJ",
    "19": "M8D",
    "20": "Z3R",
    "21": "Y5N",
    "22": "2TP",
    "23": "9QC",
    "24": "W6F",
    "25": "3ML",
    "26": "J7Z",
    "27": "D9R",
    "28": "4XN",
    "29": "Y2F",
    "30": "8CQ",
    "31": "R6T",
    "32": "P7W",
    "33": "F3Z",
    "34": "L9N",
    "35": "X4M",
    "36": "Y6P",
    "37": "T7C",
    "38": "2FQ",
    "39": "8WR",
    "40": "N9L",
    "41": "Z3D",
    "42": "X5R",
    "43": "P6F",
    "44": "9TM",
    "45": "Y4W",
    "46": "N7Z",
    "47": "C8R",
    "48": "L2P",
    "49": "Q5F",
    "50": "8WN",
    "51": "M9L",
    "52": "X7C",
    "53": "Y3T",
    "54": "6FR",
    "55": "N4P",
    "56": "Z9W",
    "57": "R2M",
    "58": "X6T",
    "59": "F8Q"
}



hour_values = {
    "00": "aXb",
    "01": "LmT",
    "02": "nOc",
    "03": "XyW",
    "04": "qBd",
    "05": "jGt",
    "06": "ZfL",
    "07": "mWk",
    "08": "RvA",
    "09": "oPh",
    "10": "TcK",
    "11": "fMq",
    "12": "XsN",
    "13": "pJt",
    "14": "LbX",
    "15": "KcF",
    "16": "mYr",
    "17": "NvQ",
    "18": "ZoT",
    "19": "WyP",
    "20": "RqL",
    "21": "TsM",
    "22": "BnK",
    "23": "XfR"
}

day_values = {
    "01": "Mf",
    "02": "Tn",
    "03": "Wv",
    "04": "Tz",
    "05": "Fa",
    "06": "es",
    "07": "nb",
    "08": "Gh",
    "09": "Tue",
    "10": "Jg",
    "11": "fG",
    "12": "Gb",
    "13": "Fh",
    "14": "fF",
    "15": "Bm",
    "16": "Hr",
    "17": "Lo",
    "18": "Mr",
    "19": "Gq",
    "20": "Dn",
    "21": "Bg",
    "22": "Fi",
    "23": "Mg",
    "24": "Gx",
    "25": "sE",
    "26": "Cz",
    "27": "Yt",
    "28": "Su",
    "29": "No",
    "30": "Ya",
    "31": "Ba"
}

month_values = {
    "01": "Ft",
    "02": "ds",
    "03": "Ng",
    "04": "Aj",
    "05": "JH",
    "06": "xx",
    "07": "xN",
    "08": "ug",
    "09": "Ko",
    "10": "Bo",
    "11": "SA",
    "12": "Gl"
}

import hashlib

def year_to_password(year):

    hash_object = hashlib.md5(year.encode())
    hash_hex = hash_object.hexdigest()  
    letters_only = ''.join([char for char in hash_hex if char.isalpha()])
    
    return letters_only[:2]



def generaten_now_time_password():
    now = datetime.now()

    current_hour = f"{now.hour:02d}"
    current_minute = f"{now.minute:02d}"
    current_second = f"{now.second:02d}"
    current_month = f"{now.month:02d}"
    current_day = f"{now.day:02d}"
    current_year = f"{now.year}"

    hour_value = hour_values.get(current_hour, "unknown_hour")
    minute_value = minute_values.get(current_minute, "unknown_minute")
    second_value = second_values.get(current_second, "unknown_second")
    month_value = month_values.get(current_month, "unknown_month")
    day_value = day_values.get(current_day, "unknown_day")

    year_value = year_to_password(current_year)

    final_value = f"{month_value}{day_value}{hour_value}{minute_value}{second_value}{year_value}"

    output = {
        "Created at": now.strftime("%Y-%m-%d %H:%M:%S"),
        "Password": final_value
    }

    return json.dumps(output, ensure_ascii=False, indent=4)

def convert_time(input_time):
    try:
        input_datetime = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S")
        
        current_hour = f"{input_datetime.hour:02d}"
        current_minute = f"{input_datetime.minute:02d}"
        current_second = f"{input_datetime.second:02d}"
        current_month = f"{input_datetime.month:02d}"
        current_day = f"{input_datetime.day:02d}"
        current_year = f"{input_datetime.year}"
        
        hour_value = hour_values.get(current_hour, "unknown_hour")
        minute_value = minute_values.get(current_minute, "unknown_minute")
        second_value = second_values.get(current_second, "unknown_second")
        month_value = month_values.get(current_month, "unknown_month")
        day_value = day_values.get(current_day, "unknown_day")

        year_value = year_to_password(current_year)

        final_value = f"{month_value}{day_value}{hour_value}{minute_value}{second_value}{year_value}"

        output = {
            "Created at": input_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "Password": final_value
        }

        return json.dumps(output, ensure_ascii=False, indent=4)
    
    except ValueError:
        return "Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS' format."
