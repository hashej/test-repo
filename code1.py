marks = int(input("Enter your marks: "))

if marks==90:
    print("very good")
elif marks==80:
    print("not good")
elif marks==70:
    print("bad")
else:
    print("garak")

shop_open=True
basmati_rice=False

if shop_open:
    print("shop is open")
    if basmati_rice:
        print("basmati rice is available")
    else:
        print("basmati not available")
else:
    print("shop is closed")