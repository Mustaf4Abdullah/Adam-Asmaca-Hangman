#Mustafa Abdullah  / 216051006  / Asmaca adam ödevi

def asmacadam():# fonksiyonu hiçbir şekilde kullanmadım çünkü oyuncunun her seferinde ana ekran gelmesini istiyorum
    while True : #sonsuz dönge yaptım ki her seferinde kendini yenilesin
            import random
            kelime = ["python","kalem", "anahtar","homework","araba","rainbow","kelime"] #list kullandim çünkü değişilebilir ve bazen içine kelime ekliyorum
            kelime_Random = random.choice(kelime)
            yapilan_Tahmin = ""
            yapilan_Tahmin1 = ""
            a= int(input("Hoş geldiniz, oynamak isterseniz 1 ,kelime eklemek isterseniz 2'ye basininz : "))
            if a ==1:
                b= input("Eklmek istediginiz kelimeyi yaziniz :")
                if b.isalpha() == True: #burda eklenen kelimenin yada harfenin bir harf olduğunu emin ettirdm
                    b = b.lower() # burda eklenen kelimenin harfleri küçük yaptırıyorum ki tahmini kolay olsun
                    kelime.append(b)
                else :
                    print("Girdiginiz kelimeyi kontrol ediniz !!")
            else :
                print(len(kelime_Random),"Karakterli bir kelime tahmin etmeniz gerekiyor : ",end='\n')
                j=0
                while j<5: # burda 5 hak veriyorum oyuncuya
                    asil_Kelime = ""
                    print("Kalan hakkiniz :", (5 - j))
                    for karakter in kelime_Random:
                        if karakter in yapilan_Tahmin:
                            asil_Kelime +=karakter
                        else:
                            asil_Kelime += "_"
                    if asil_Kelime == kelime_Random:
                        print("kelime :",asil_Kelime.upper()," ,Tebrikler kazandınız 😃")
                        break
                    print("Kelimeyi tahmin edin:",asil_Kelime)
                    Tahmin = input("Harfi giriniiz : ")
                    yapilan_Tahmin1 +=Tahmin
                    print("(Yapilan tahminler ",yapilan_Tahmin1 ,")")
                    if Tahmin.isalpha()==True:  #burda eklenen kelimenin yada harfenin bir harf olduğunu emin ettirdim
                        Tahmin=Tahmin.lower()
                        yapilan_Tahmin += Tahmin
                    else:
                         print("Girdiğiniz harfi kontrol edin")
                         Tahmin = input("Harfi giriniiz : ")
                         yapilan_Tahmin1 += Tahmin
                    j +=1
                    if j ==5 :
                        print("Maalesef kaybettiniz 😞 ")
asmacadam()
