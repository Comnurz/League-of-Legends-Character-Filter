import sys
import sqlite3

# Check Python version
_2x_="""
Python 2.x sürümlerinden birini kullanmaktasınız.
Programın doğru çalışabilmesi için 3.x sürümlerinden
biri kurulu olmalıdır.
"""
_3x_="Hoşgeldiniz. "
try:
    if sys.version_info.major<3:
        print(_2x_)
    else:
        print(_3x_)
except AttributeError:
    print(_2x_)


# connection database
vt=sqlite3.connect('LoLDb')
im=vt.cursor()

class database():
    # create table for users in database
    def dbolustur():
        im.execute("CREATE TABLE IF NOT EXISTS kayit(kullaniciadi,sifre,ad)")

    # check user
    def giris():
        kontrol=True
        while kontrol:
            kullaniciadi=input("kullanıcı adı: ")
            sifre=input("şifre: ")
            im.execute("""SELECT * FROM kayit WHERE
            kullaniciadi = ? AND sifre = ?""", (kullaniciadi, sifre))
            data = im.fetchone()
            if data:
                print("Programa hoşgeldin {}!".format(data[0]))
                kontrol=False
            else:
                ygiris=input("Parola veya kullanıcı adı yanlış!Üye olmak için 1, tekrar denemek için 2 ye basın.")
                if ygiris=="1":
                    database.kayitekle()
                else:
                    pass

    # create user account
    def kayitekle():
        kullaniciadi=input("kullanıcı adınızı giriniz: ")
        sifre=input("Şifrenizi giriniz: ")
        ad=input("isminizi giriniz: ")
        im.execute("""INSERT INTO kayit VALUES (?,?,?)""",(kullaniciadi,sifre,ad))
        print("kayit basarili")
        vt.commit()


def yazdir(parametre):
    print("{} şampiyonlar".format(parametre))

def gecersiz(parametre):
    print("{} karakteri geçersiz bir karakterdir. Lütfen gecerli bir karakter giriniz:".format(giris))

kaynak="şçöğüıŞÖĞÜİÇ" #turkish unique characters
hedef="scoguiSOGUIC"
ceviri=str.maketrans(kaynak,hedef)#turkish unique characters translate english characters


# open and read .txt files
with open ("1suikastci.txt") as suikastci:
    suikastci_s=suikastci.readlines()

with open ("1nisanci.txt") as nisanci:
    nisanci_s=nisanci.readlines()

with open ("1dovuscu.txt") as dovuscu:
    dovuscu_s=dovuscu.readlines()

with open ("2suikastci.txt") as suikastci2:
    suikastci2_s=suikastci2.readlines()

with open ("2nisanci.txt") as nisanci2:
    nisanci2_s=nisanci2.readlines()

with open ("2dovuscu.txt") as dovuscu2:
    dovuscu2_s=dovuscu2.readlines()

database.dbolustur()

while True:
    # user authentication
    uyelik=input("Üye isen 1, üye değil isen 2.")
    if uyelik=="1":
        database.giris()
        break
    elif uyelik=="2":
        database.kayitekle()
        database.giris()
        break
    else:
        print ("hatali giris!")

while True:
    giris=input("""
suikastci şampiyonlar
nişancı şampiyonlar
dövüşçü şampiyonlar
Her iki özelliğe sahip şampiyonlar için "2" yazınız.
çıkmak için çıkış yazınız.
""")
    giris2=giris.translate(ceviri).lower() # if input has turkish unique characters this characters translated.
    if giris2.isalpha():
        if giris2 == "cikis":
            print("{} yapılıyor...".format(giris))
            break
        elif giris2 == "suikastci":
            yazdir(giris)
            for k in suikastci_s:
                print(k)
        elif giris2 == "nisanci":
            yazdir(giris)
            for f in nisanci_s:
                print(f)
        elif giris2 == "dovuscu":
           yazdir(giris)
           for d in dovuscu_s:
                print(d)
        else:
            gecersiz(giris)
    elif not giris2=="2":
        gecersiz(giris)
        continue
    elif giris2.isdigit():
        if giris2 == "2":
            ilkrol=input("1. Rolü seçiniz: ")
            ilkrol2=ilkrol.translate(ceviri).lower()
            ikincirol=input("2. Rolü seçiniz:  ")
            ikincirol2=ikincirol.translate(ceviri).lower()
            if ilkrol2=="suikastci":
                if ikincirol2 == "nisanci":
                    for s in suikastci_s:
                        if s in nisanci2_s:
                            print(s)
                elif ikincirol2=="dovuscu":
                    for d in suikastci_s:
                        if d in dovuscu2_s:
                            print(d)
                else:
                    gecersiz(giris)

            elif ilkrol2 =="nisanci":
                if ikincirol2 =="suikastci":
                    for h in nisanci_s:
                        if h in suikastci2_s:
                            print(h)
                elif ikincirol2 == "dovuscu":
                    for k in nisanci_s:
                        if k in dovuscu2_s:
                            print(k)
                else:
                    gecersiz(giris)
            elif ilkrol2 == "dovuscu":
                if ikincirol2=="suikastci":
                    for t in dovuscu_s:
                        if t in suikastci2_s:
                             print(t)
                elif ikincirol2 == "nisanci":
                    for y in dovuscu_s:
                        if y in nisanci2_s:
                            print(y)
                else:
                    gecersiz(giris)
            else:
                gecersiz(giris)
    else:
        gecersiz(giris)
        continue
