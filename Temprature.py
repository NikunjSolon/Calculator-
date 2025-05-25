def fun(I, V):
    I = I.upper()
    if (I == "CK") or (I == "ck"):
        K = V + 273.15
        return str(round(K, 3)) + "K"
    elif (I == "KC") or (I == "kc"):
        C = V - 273.15
        return str(round(C, 3)) + "°C"
    elif (I == "FC") or (I == "fc"):
        C = (V - 32) * (5 / 9)
        return str(round(C, 3)) + "°C"
    elif (I == "CF") or (I == "cf"):
        F = V * (9 / 5) + 32
        return str(round(F, 3)) + "°F"
    elif (I == "FK") or (I == "fk"):
        K = (V - 32) * (5 / 9) + 273.15
        return str(round(K, 3)) + "K"
    elif (I == "KF") or (I == "kf"):
        F = (V - 273.15) * (9 / 5) + 32
        return str(round(F, 3)) + "°F"


lines = [
    "Celsius to Kelvin : print -> CK",
    "Kelvin to Celcius : print -> KC",
    "Fahrenheit to Celsius : print -> FC",
    "Celsius to Fahrenheit : print -> CF",
    "Fahrenheit to Kelvin : print -> FK",
    "Kelvin to Fahrenheit : print -> KF",
]
print("\n".join(lines), "\n")
k = 1
while True:
    print(f"{k})")
    k += 1
    I = str(input("Input -> ")).upper()
    if I in ("CK", "KC", "FC", "CF", "FK", "KF"):
        value = float(input("Input value -> "))
        a = fun(I, value)
        print(f"Tempreture {I[0]} to {I[1]} : {a}")
    else:
        print("Invalid input")

    print()
