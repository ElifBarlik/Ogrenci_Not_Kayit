def notGir():
    adSoyad=input('Ogrencinin adi ve soyadi: ')
    not1=input('1.sinav notu:  ')
    not2=input('2.sinav notu: ')
    not3=input('3.sinav notu: ')

    with open('OgrenciKayit.txt','a',encoding='utf-8') as file:
        file.write(adSoyad+':'+not1+','+not2+','+not3+'\n')

def notHesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')
    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])   

    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf='AA'
    elif ortalama>=85 and ortalama<=89:
        harf='BA'
    elif ortalama>=80 and ortalama<=84:
        harf='BB'
    elif ortalama>=75 and ortalama<=79:
        harf='CB'
    elif ortalama>=70 and ortalama<=74:
        harf='CC'
    elif ortalama>=65 and ortalama<=69:
        harf='DC'
    elif ortalama>=60 and ortalama<=64:
        harf='DD'
    elif ortalama>=50 and ortalama<=59:
        harf='FD'
    else:
        harf='FF'
    
    return f"{ogrenciAdi}: Ortalama: {ortalama}, Harf Notu: {harf}\n"

def ortalamaOku():
    with open('OgrenciKayit.txt','r',encoding='utf-8') as file:
        for satir in file:
            print(notHesapla(satir))

def notKayit():
    with open('OgrenciKayit.txt','r',encoding='utf-8')as file:
        liste=[]
        for i in file:
            liste.append(notHesapla(i))

    with open('OgrenciKayit.txt','w',encoding='utf-8')as file2:
        for i in liste:
            file2.write(i)


while True:
    secim=input('1-Not Gir\n2-Notlari Oku\n3-Notlari Kayit Et\n4-Cikis\n')

    if secim=='1':
        notGir()
    elif secim=='2':
        ortalamaOku()
    elif secim=='3':
        notKayit()
    else:
        break