from def2 import gönderilen

şifrex = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
          "h": "8", "ı": "9", "j": "0", "k": "10", "l": "11", "m": "12", "n": "13", "o": "14",
          "p": "15", "r": "16", "s": "17", "t": "18", "u": "19", "v": "20", "w": "21", "x": "22",
          "y": "23", "z": "24", "ç": "25", "ğ": "26", "i": "27", "ö": "28", "ş": "29", "ü": "30", 1: 2, 2:3,
          3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:0, 0:1, " ":"00"}
şifrey = {}
for harf, sayı in şifrex.items():
    şifrey[str(sayı)] = harf
def çözüm (gönderilen):
    şifrem = ""
    parçalar = gönderilen.split("-")
    gönderilen = gönderilen.lower()
    for sayılar in parçalar:
        if sayılar in şifrey:
            şifrem = şifrem + şifrey[sayılar]
        elif sayılar == "":
            continue
        else:
            şifrem = şifrem + sayılar
    return şifrem

print(çözüm(gönderilen))

