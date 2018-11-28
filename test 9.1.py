#KEGIATAN 1
#!usr/bin/python
#menulis data diri kedalam berkas
berkas = open("L200180150.txt", "w")
berkas.write("Nimku = L200180150\n")
berkas.write("Tanggal lahirku = 24-07-2001\n")
berkas.write("Nama lengkapku = Yudha Gana Prasetyo Wibowo\n")
berkas.close()


#KEGIATAN 2
#!usr/bin/python
#menulis data diri kedalam berkas
berkas = open("L200180150.txt", "w")
berkas.write("Nimku = L200180150\n")
berkas.write("Tanggal lahirku = 07-24-2001\n")
berkas.write("Nama lengkapku = Yudha Gana Prasetyo Wibowo\n")
berkas.close()

#!usr/bin/python
#membaca data didalam berkas
berkas = open("L200180150.txt", "a")
berkas.write("Kota kelahiranku = Klaten\n")
berkas.close()

import shelve
b = open('L200180150.txt', 'r')
NIM = b.readline()
TL = b.readline()
Nama = b.readline()
kota = b.readline()
print Nama
print kota, TL
print NIM
berkas.close()



##KEGIATAN 3 & 4
##!usr/bin/python
##membaca data dari berkas teks dan menyimpan ke shelve
import shelve
a = open('L200180150.txt', 'r')
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a = shelve.open("Yudha")
a['b'] = [NIM, TL, Nama]
print a['b'][0]
print a['b'][1]
print a['b'][2]
a.close()


