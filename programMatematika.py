import math

def volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    return 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma

def luas_permukaan_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    return 2 * (0.5 * alas_segitiga * tinggi_segitiga) + (alas_segitiga * tinggi_prisma)

def luas_permukaan_limas_segitiga(alas_limas_segitiga, tinggi_segitiga_limas, tinggi_limas_segitiga):
    return (0.5 * alas_limas_segitiga * tinggi_segitiga_limas) + (3 * alas_limas_segitiga * tinggi_limas_segitiga)

def volume_limas_segitiga(alas_limas_segitiga, tinggi_segitiga_limas, tinggi_limas_segitiga):
    return (1.0 / 3.0) * (alas_limas_segitiga * tinggi_segitiga_limas * tinggi_limas_segitiga)

def luas_permukaan_limas_segiempat(sisi_alas_limas, tinggi_limas_segiempat):
    return sisi_alas_limas * sisi_alas_limas + 4 * (0.5 * sisi_alas_limas * tinggi_limas_segiempat)

def volume_limas_segiempat(sisi_alas_limas, tinggi_limas_segiempat):
    return (1.0 / 3.0) * sisi_alas_limas * sisi_alas_limas * tinggi_limas_segiempat

def luas_permukaan_bola(jari_jari):
    return 4.0 * math.pi * jari_jari * jari_jari

def volume_bola(jari_jari):
    return (4.0 / 3.0) * math.pi * jari_jari * jari_jari * jari_jari

def luas_permukaan_segiempat(panjang_sisi_prisma, tinggi_prisma_segiempat):
    return 2 * (panjang_sisi_prisma * panjang_sisi_prisma + panjang_sisi_prisma * tinggi_prisma_segiempat)

def volume_prisma_segiempat(panjang_sisi_prisma, tinggi_prisma_segiempat):
    return panjang_sisi_prisma * panjang_sisi_prisma * tinggi_prisma_segiempat

def luas_segitiga(alas_segitiga, tinggi_segitiga):
    return 0.5 * alas_segitiga * tinggi_segitiga

def keliling_segitiga(sisi_a, sisi_b, sisi_c):
    return sisi_a + sisi_b + sisi_c

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def luas_permukaan_limas_segienam(sisi_alas_limas_segienam, tinggi_limas_segienam):
    return 3 * sisi_alas_limas_segienam * sisi_alas_limas_segienam * tinggi_limas_segienam / 2

def volume_limas_segienam(sisi_alas_limas_segienam, tinggi_limas_segienam):
    return (1.0 / 3.0) * sisi_alas_limas_segienam * sisi_alas_limas_segienam * tinggi_limas_segienam

def luas_permukaan_prisma_segilima(sisi_alas_prisma_segilima, tinggi_prisma_segilima):
    return 5 * (sisi_alas_prisma_segilima * tinggi_prisma_segilima)

def luas_jajar_genjang(alas_jajar_genjang, tinggi_jajar_genjang):
    return alas_jajar_genjang * tinggi_jajar_genjang

def keliling_jajar_genjang(alas_jajar_genjang, sisi_miring_jajargenjang):
    return 2 * (alas_jajar_genjang + sisi_miring_jajargenjang)

def luas_belah_ketupat(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def keliling_belah_ketupat(sisi_belah_ketupat):
    return 4 * sisi_belah_ketupat

def luas_trapesium(alas_trapesium1, alas_trapesium2, tinggi_trapesium):
    return 0.5 * (alas_trapesium1 + alas_trapesium2) * tinggi_trapesium

def keliling_trapesium(sisi_trapesium1, sisi_trapesium2, sisi_trapesium3, sisi_trapesium4):
    return sisi_trapesium1 + sisi_trapesium2 + sisi_trapesium3 + sisi_trapesium4

def luas_layang_layang(diagonal_layang1, diagonal_layang2):
    return (diagonal_layang1 * diagonal_layang2) / 2

def keliling_layang_layang(sisi_layang1, sisi_layang2):
    return 2 * (sisi_layang1 + sisi_layang2)

def main():
    print("||=====================================================================================||")
    print("||                  Pilihlah Salah Satu yang Ingin Anda Gunakan                        ||")
    print("||=====================================================================================||")
    print("||          1. Volume Prisma Segitiga                                                  ||")
    print("||          2. Luas Permukaan Prisma Segitiga                                          ||")
    print("||          3. Luas Permukaan Limas Segitiga                                           ||")
    print("||          4. Volume Limas Segitiga                                                   ||")
    print("||          5. Luas Permukaan Limas Segiempat                                          ||");
    print("||          6. Volume Limas Segiempat                                                  ||");
    print("||          7. Luas Permukaan Bola                                                     ||");
    print("||          8. Volume Bola                                                             ||");
    print("||          9. Luas Permukaan Prisma Segiempat                                         ||");
    print("||          10. Volume Prisma Segiempat                                                ||");
    print("||          11. Luas Segitiga                                                          ||");
    print("||          12. Keliling Segitiga                                                      ||");
    print("||          13. Luas Lingkaran                                                         ||");
    print("||          14. Keliling Lingkaran                                                     ||");
    print("||          15. Luas Permukaan Limas Segienam                                          ||");
    print("||          16. Volume Limas Segienam                                                  ||");
    print("||          17. Luas Permukaan Prisma Segilima                                         ||");
    print("||          18. Luas Jajar Genjang                                                     ||");
    print("||          19. Keliling Jajar Genjang                                                 ||");
    print("||          20. Luas Belah Ketupat                                                     ||");
    print("||          21. Keliling Belah Ketupat                                                 ||");
    print("||          22. Luas Trapesium                                                         ||");
    print("||          23. keliling Trapesium                                                     ||");
    print("||          24. Luas Layang Layang                                                     ||");
    print("||          25. Keliling Layang Layang                                                 ||");
    print("||=====================================================================================||")

    pilihan = int(input("Masukkan Pilihan Anda : "))

    if pilihan == 1:
        alas_segitiga = float(input("Masukkan Panjang Alas Segitiga : "))
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga : "))
        tinggi_prisma = float(input("Masukkan Tinggi Prisma Segitiga : "))
        v_p_s = volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
        print(f"Volume Prisma Segitiga Adalah : {v_p_s:.2f}\n\n")
    elif pilihan == 2:
        alas_segitiga = float(input("Masukkan Panjang Alas Segitiga : "))
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga : "))
        tinggi_prisma = float(input("Masukkan Tinggi Prisma Segitiga : "))
        l_p_p_s = luas_permukaan_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
        print(f"Luas Permukaan Prisma Segitiga Adalah : {l_p_p_s:.2f}\n\n")
    elif pilihan == 3:
        alas_limas_segitiga = float(input("Masukkan Panjang Alas Segitiga : "))
        tinggi_segitiga_limas = float(input("Masukkan Tinggi Segitiga : "))
        tinggi_limas_segitiga = float(input("Masukkan Tinggi Limas Segitiga : "))
        l_p_l_s = luas_permukaan_limas_segitiga(alas_limas_segitiga, tinggi_segitiga_limas, tinggi_limas_segitiga)
        print(f"Luas Permukaan Limas Segitiga Adalah : {l_p_l_s:.2f}\n\n")
    elif pilihan == 4:
        alas_limas_segitiga = float(input("Masukkan Panjang Alas Limas Segitiga : "))
        tinggi_segitiga_limas = float(input("Masukkan Tinggi Segitiga dari Limas Tersebut : "))
        tinggi_limas_segitiga = float(input("Masukkan Tinggi dari Limas Segitiga Tersebut : "))
        v_l_s = volume_limas_segitiga(alas_limas_segitiga, tinggi_segitiga_limas, tinggi_limas_segitiga)
        print(f"Volume dari Limas Segitiga Adalah : {v_l_s:.2f}\n\n")
    elif pilihan == 5:
        sisi_alas_limas = float(input("Masukkan Panjang Sisi Alas Limas Segiempat : "))
        tinggi_limas_segiempat = float(input("Masukkan Tinggi dari Limas Segiempat : "))
        l_p_l_s_e = luas_permukaan_limas_segiempat(sisi_alas_limas, tinggi_limas_segiempat)
        print(f"Luas Permukaan Limas Segiempat Adalah : {l_p_l_s_e:.2f}\n\n")
    elif pilihan == 6:
        sisi_alas_limas = float(input("Masukkan Panjang Sisi Alas Limas Segiempat : "))
        tinggi_limas_segiempat = float(input("Masukkan Tinggi dari Limas Segiempat : "))
        v_l_s_e = volume_limas_segiempat(sisi_alas_limas, tinggi_limas_segiempat)
        print(f"Volume dari Limas Segiempat Tersebut Adalah : {v_l_s_e:.2f}\n\n")
    elif pilihan == 7:
        jariJari = float(input("Masukkan Panjang Jari-jari Bola : "))
        l_p_b = luas_permukaan_bola(jariJari)
        print(f"Luas Permukaan Bola Adalah : {l_p_b:.2f}\n\n")
    elif pilihan == 8:
        jariJari = float(input("Masukkan Panjang Jari-jari Bola : "))
        v_b = volume_bola(jariJari)
        print(f"Volume Bola Adalah : {v_b:.2f}\n\n")
    elif pilihan == 9:
        panjang_sisi_prisma = float(input("Masukkan Panjang Sisi Prisma Segiempat : "))
        tinggi_prisma_segiempat = float(input("Masukkan Tinggi Prisma Segiempat : "))
        l_p_p_s_e = luas_permukaan_segiempat(panjang_sisi_prisma, tinggi_prisma_segiempat)
        print(f"Luas Permukaan Prisma Segiempat Adalah : {l_p_p_s_e:.2f}\n\n")
    elif pilihan == 10:
        panjang_sisi_prisma = float(input("Masukkan Panjang Sisi Prisma Segiempat : "))
        tinggi_prisma_segiempat = float(input("Masukkan Tinggi Prisma Segiempat : "))
        v_p_s_e = volume_prisma_segiempat(panjang_sisi_prisma, tinggi_prisma_segiempat)
        print(f"Volume Prisma Segiempat Adalah : {v_p_s_e:.2f}\n\n")
    elif pilihan == 11:
        alas_b_d_segitiga = float(input("Masukkan Panjang Alas Segitiga : "))
        tinggi_b_d_segitiga = float(input("Masukkan Tinggi Segitiga : "))
        l_s= luas_segitiga(alas_b_d_segitiga, tinggi_b_d_segitiga)
        print(f"Luas Segitiga Adalah : {l_s:.2f}\n\n")
    elif pilihan == 12:
        sisi_a = float(input("Masukkan Panjang Sisi Pertama dari Segitiga : "))
        sisi_b = float(input("Masukkan Panjang Sisi Kedua dari Segitiga : "))
        sisi_c = float(input("Masukkan Panjang Sisi Ketiga dari Segitiga : "))
        kl_s = keliling_segitiga(sisi_a, sisi_b, sisi_c)
        print(f"Keliling Segitiga Adalah : {kl_s:.2f}\n\n")
    elif pilihan == 13:
        jariJari_bd = float(input("Masukkan Panjang Jari-jari Lingkatan : "))
        ls_l = luas_lingkaran(jariJari_bd)
        print(f"Luas Lingkaran Adalah : {ls_l:.2f}\n\n")
    elif pilihan == 14:
        jariJari_bd = float(input("Masukkan Panjang Jari-jari Lingkaran : "))
        kl_s = keliling_lingkaran(jariJari_bd)
        print(f"Keliling Lingkaran Adalah : {kl_s:.2f}\n\n")
    elif pilihan == 15:
        sisi_alas_limas_segienam = float(input("Masukkan Panjang Sisi Alas Limas Segienam : "))
        tinggi_limas_segienam = float(input("Masukkan Tinggi dari Limas Segienam : "))
        l_p_l_s_enam = luas_permukaan_limas_segienam(sisi_alas_limas_segienam, tinggi_limas_segienam)
        print(f"Luas Permukaan Limas Segienam Adalah : {l_p_l_s_enam:.2f}\n\n")
    elif pilihan == 16:
        sisi_alas_limas_segienam = float(input("Masukkan Panjang Sisi Alas Limas Segienam : "))
        tinggi_limas_segienam = float(input("Masukkan Tinggi dari Limas Segienam : "))
        v_l_s_enam = volume_limas_segienam(sisi_alas_limas_segienam, tinggi_limas_segienam)
        print(f"Volume Limas Segienam Adalah : {v_l_s_enam:.2f}\n\n")
    elif pilihan == 17:
        sisi_alas_prisma_segilima = float(input("Masukkan Panjang Sisi Alas Prisma Segilima : "))
        tinggi_prisma_segilima = float(input("Masukkan Tinggi Prisma Segilima : "))
        l_p_p_segilima = luas_permukaan_prisma_segilima(sisi_alas_prisma_segilima, tinggi_prisma_segilima)
        print(f"Luas Permukaan Prisma Segilima Adalah : {l_p_p_segilima:.2f}\n\n")
    elif pilihan == 18:
        alas_jajar_genjang = float(input("Masukkan Panjang Alas Jajar Genjang : "))
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang : "))
        ls_jg = keliling_jajar_genjang(alas_jajar_genjang, tinggi_jajar_genjang)
        print(f"Luas Jajar Genjang Adalah : {ls_jg:.2f}\n\n")
    elif pilihan == 19:
        alas_jajar_genjang = float(input("Masukkan Panjang Alas Jajar Genjang : "))
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang : "))
        kl_jg = keliling_jajar_genjang(alas_jajar_genjang, tinggi_jajar_genjang)
        print(f"Keliling Jajar Genjang Adalah : {kl_jg:.2f}\n\n")
    elif pilihan == 20:
        diagonal1 = float(input("Masukkan Panjang Diagonal 1 dari Belah Ketupat : "))
        diagonal2 = float(input("Masukkan Panjang Diagonal 2 dari Belah Ketupat : "))
        diagonal3 = float(input("Masukkan Panjang Diagonal 3 dari Belah Ketupat : "))
        ls_bk = luas_belah_ketupat(diagonal1, diagonal2, diagonal3)
        print(f"Luas Belah Ketupat Adalah : {ls_bk:.2f}\n\n")
    elif pilihan == 21:
        sisi_belah_ketupat = float(input("Masukkan Panjang Sisi dari Belah Ketupat : "))
        kl_bk = keliling_belah_ketupat(sisi_belah_ketupat)
        print(f"Keliling Belah Ketupat Adalag : {kl_bk:.2f}\n\n")
    elif pilihan == 22:
        alas_trapesium1 = float(input("Masukkan Panjang Alas Atas dari Trapesium : "))
        alas_trapesium2 = float(input("Masukkan Panjang Alas Bawah dari Trapesium : "))
        tinggi_trapesium = float(input("Masukkan Tinggi dari Trapesium : "))
        ls_tr = luas_trapesium(alas_trapesium1, alas_trapesium2, tinggi_trapesium)
        print(f"Luas Trapesium Adalah : {ls_tr:.2f}\n\n")
    elif pilihan == 23:
        sisi_trapesium1 = float(input("Masukkan Panjang Sisi Atas pada Trapesium : "))
        sisi_trapesium2 = float(input("Masukkkan Panjang Sisi Bawah pada Trapesium : "))
        sisi_trapesium3 = float(input("Masukkan Panjang Sisi Samping A pada Trapesium : "))
        sisi_trapesium4 = float(input("Masukkan Panjang Sisi Samping B pada Trapesium : "))
        kl_tr = keliling_trapesium(sisi_trapesium1, sisi_trapesium2, sisi_trapesium3, sisi_trapesium4)
        print(f"Keliling Trapesium Adalah : {kl_tr:.2f}\n\n")
    elif pilihan == 24:
        diagonal_layang1 = float(input("Masukkan Panjang Diagonal 1 pada Layang-layang : "))
        diagonal_layang2 = float(input("Masukkan Panjang Diagonal 2 pada Layang-layang :"))
        ls_ly = luas_layang_layang(diagonal_layang1, diagonal_layang2)
        print(f"Luas Layang-layang Adalah : {ls_ly:.2f}\n\n")
    elif pilihan == 25:
        sisi_layang1 = float(input("Masukkan Panjang Sisi Layang-layang 1 : "))
        sisi_layang2 = float(input("Masukkan Panjang Sisi Layang-layang 2 : "))
        kl_ly = keliling_layang_layang(sisi_layang1, sisi_layang2)
        print(f"Keliling Layang-layang Adalah : {kl_ly:.2f}\n\n")
    else:
        print("Pilihan Tidak Valid : ")

if __name__ == "__main__":
    main()
