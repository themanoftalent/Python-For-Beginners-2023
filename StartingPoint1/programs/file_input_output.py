# yazi = open ('sample.text', 'w')
# yazi.write('I like swimming')
# yazi.close ()
#
# oku = open ('sample.text', 'r')
# content = oku.read ()
# print (content)
# oku.close ()

# yazma=open('patasana.text','w')
# yazma.write('Patasana, a good book, is by Ahmet Umit')
# yazma.close()
#
#
# okuma=open('patasana.text','r')
# icindenevar=okuma.read()
# print(icindenevar)
# okuma.close()

# myText=open('PusluAda.rtf','w')
# myText.write('This is another great book by John the'
#              ' doorbell and he deveoted it to his beloved wife Jenny.')
#
# myText.close()
#
# readMytext=open('PusluAda.rtf','r')
# icinde=readMytext.read()
# print(icinde)
# readMytext.close()

dosya_olustur = open ('Dosya_adi.txt', 'w+')
dosya_olustur.write ('Buaraya istedigimizi yaziyorus okuturken okunuyor.')
dosya_olustur.close ()  # kapat

dosyami_oku = open ('Dosya_adi.txt', 'r+')  # sadece okusun ondan r
icerik_ne = dosyami_oku.read ()
print (icerik_ne)
dosyami_oku.close ()


yeniBirdosya=open('hosca.trf','w')
yeniBirdosya.write('Ne yazarsak o okunur sanirim')
yeniBirdosya.close()

okuyalim=open('Dosya_adi.txt','r') #ayni dosyayi okuttuk
ne_oksun=okuyalim.read()
print(ne_oksun)
okuyalim.close()


okuyalim=open('hosca.trf','r') #ayni dosyayi okuttuk
ne_oksun=okuyalim.read()
print(ne_oksun)
okuyalim.close()