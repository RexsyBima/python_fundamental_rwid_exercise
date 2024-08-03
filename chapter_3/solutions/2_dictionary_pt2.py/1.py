ktp = {"NIK" : 1234567890,
       "Nama" : "Remote W. Indonesia",
       "TempatLahir" : "Banyumas",
       "TanggalLahir" : "10-02-1999",
       "JenisKelamin" : "Laki-Laki",
       "Alamat" : {"Desa" : "Wisata Tanjung",
                   "RT" : 4,
                   "RW" : 8,
                   "Kecamatan" : "Purwokerto"},
       "Agama" : "Islam",
       "isMenikah" : False,
       "isBekerja" : True,
       "isWNI" : True,
       "isValidforLife" : True,
       "Hobi" : ["Memancing", "Membaca", "Belajar"]
       }

nik = ktp['NIK']
nama = ktp['Nama']
tempatlahir = ktp['TempatLahir']
tanggallahir = ktp['TanggalLahir']
jeniskelamin = ktp['JenisKelamin']
alamat = ktp['Alamat']
desa = alamat['Desa']
rt = alamat['RT']
rw = alamat['RW']
kecamatan = alamat['Kecamatan']
agama = ktp['Agama']
ismenikah = ktp['isMenikah']
isbekerja = ktp['isBekerja']
iswni = ktp['isWNI']
isvalidforlife = ktp['isValidforLife']
hobi = ktp['Hobi']
hobi1 = hobi[0]
hobi2 = hobi[1]
hobi3 = hobi[2]


print(f"My name is {nama}, i was born in {tempatlahir}, {tanggallahir}. I am a {jeniskelamin}. {agama} is my religion, currently {'' if ismenikah else 'not '}married, {'' if isbekerja else 'not '}working, {'' if iswni else 'not '}indigenous, {'' if isvalidforlife else 'not '}valid for life. I like to {hobi1}, {hobi2}, {hobi3}. My address is {alamat} {desa}, {rt} RT, {rw} RW, {kecamatan}.")

#check if else statement one liner