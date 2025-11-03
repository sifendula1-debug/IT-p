y=int(input("How old are you?: "))
def classify_person():
    if 0<y<=12:
        print("You are categorized under child")
    elif 13<y<=17:
        print("You are categorized under teenager")
    elif 18<y<=64:
        print("You are categorized under adult")
    elif y>64:
        print("You are categorized under Senior")
classify_person()
