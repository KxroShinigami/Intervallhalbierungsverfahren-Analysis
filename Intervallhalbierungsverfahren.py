#--> Intervallhalbierungsverfahren
#-> Intervallhalbierungsverfahren für Polynome bis x^6.

# Input:
# grenz1 = Intervallgrenze negativ
# grenz2 = Intervallgrenze positiv
# m_neg = x negativ
# m_pos = x positiv
# x0
# x1
# x2
# x3
# x4
# x5
# x6
# a0
# a1
# a2
# a3
# a4
# a5
# a6
# genauigkeit

try: # grenz1
        grenz1 = int(input("grenz1: "))
except Exception as e:
        print("\nError: ", e)

try: # grenz2
        grenz2 = int(input("grenz2: "))
except Exception as e:
        print("\nError: ", e)

try: # x0
        x0 = int(input("x0: "))
except Exception as e:
        print("\nError: ", e)
try: # x1
        x1 = int(input("x1: "))
except Exception as e:
        print("\nError: ", e)
try: # x2
        x2 = int(input("x2: "))
except Exception as e:
        print("\nError: ", e)
try: # x3
        x3 = int(input("x3: "))
except Exception as e:
        print("\nError: ", e)
try: # x4
        x4 = int(input("x4: "))
except Exception as e:
        print("\nError: ", e)
try: # x5
        x5 = int(input("x5: "))
except Exception as e:
        print("\nError: ", e)
try: # x6
        x6 = int(input("x6: "))
except Exception as e:
        print("\nError: ", e)


try: # genauigkeit
        genauigkeit = float(input("genauigkeit: "))
except Exception as e:
        print("\nError: ", e)


def Funktion(x):
    return (x6 * (x**6) + x5 * (x**5) + x4 * (x**4) + x3 * (x**3) + x2 * (x**2) + x1 * (x**1) + x0)



def Intervallhalbierungsverfahren():
    m_neg = grenz1
    m_pos = grenz2
    
    print("Anfangswert negativ: ", Funktion(grenz1))
    print("Anfangswert positiv: ", Funktion(grenz2))

    i = 1 # Laufvariable für m
    
    zwischenergebnis = 100

    while(zwischenergebnis < -genauigkeit or zwischenergebnis > genauigkeit):
        m_neu = (m_neg + m_pos) / 2

        zwischenergebnis = Funktion(m_neu)
        
        if(zwischenergebnis == 0):
                print("m", i, " ist: ", m_neu, " und genau dem Nullpunkt.")
                break
        elif(zwischenergebnis > 0): m_pos = m_neu
        else: m_neg = m_neu

        print("\nm", i, "ist: ", m_neu)
        print("Das Ergebnis für f(m", i, ") ist: ", zwischenergebnis)
        print("Neues m_neg: ", m_neg)
        print("Neues m_pos: ", m_pos)

        i = i + 1
    
    print("Bei m", i-1, " mit dem Zwischenergebnis f(m", i-1, ") = ", zwischenergebnis, " und so ist die Genauigkeit abgedeckt.")        

print(Intervallhalbierungsverfahren())