print("Salom, Mening ismim Avameo !\nYaqindan tanishib olsak, ismingiz nima?")
name = input()
print(name, "! Ajoyib ism, tanishganimdan hursandman \nSir bo\'lmasa agar yoshingiz nechida?")
old = int(input ())
if old < 17:
    print("Hali yosh ekansiz ",name, "! Kelajakda kim bo'lmoqchisiz?" )
    prof = input()
    print(prof, "! Albatta katta ma\'suliyat talab etuvchi kasb. \n Ishlaringizga omad !")
elif 17 <= old <= 19:
    print("Haa 18 ga to\'ldingizmi ! Qachon endi to\'yga harakat")
    wedding = input()
    if wedding == "bilmadim":
        print("hmm")
else :
    print("Ha , ancha katta bo\'lib qolibsiz !" )
    print("Xotiningiz bormi?")
    wife = input()
    if wife == "yoq":
        print("Ehh ", name, "jon haliyam yuribsizmi bo\'ydoq boliiib")
    

