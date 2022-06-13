from math import log
sozlukx = ["₀","₁","₂","₃","₄","₅","₆","₇","₈","₉","₁₀","₁₁","₁₂","₁₃","₁₄","₁₅","₁₆","₁₇","₁₈","₁₉","₂₀","₂₁","₂₂","₂₃","₂₄","₂₅","₂₆","₂₇","₂₈","₂₉","₃₀","₃₁","₃₂","₃₃","₃₄","₃₅","₃₆"]

def decimal(sayi,taban):
    a = int(sayi,taban)
    return a

def convert(sayi,taban):
    sozluk = {i:"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i] for i in range(36)}
    kuvvet = int(log(sayi,taban))
    yenisayi = ""
    
    for k in range(kuvvet,-1,-1):
        yenisayi += sozluk[sayi//(taban**k)]
        sayi %= taban**k
    return yenisayi

while True:
    sayi=input("sayı girin(programı sonlandırmak için x yazın): ")
    if sayi=="x":
        exit()
    elif sayi !="x":
        a=int(input("hangi tabanda olduğunu yazın(max 36): "))
        if (a<37):
            b = int(input("hangi tabana çevirmek istediğinizi yazın(max 36): "))
            if (b<37):
                yenisayi = convert(decimal(sayi, a), b)
                print(""f"({sayi}){sozlukx[a]}", "=", f"({yenisayi}){sozlukx[b]}\n")
                print("Oğuz İmer\n210175085\nBilişim Güvenliği Teknolojisi\n")
            else:
                print("hatalı giriş")
        else:
            print("hatalı giriş")
            continue

