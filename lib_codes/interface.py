while True:
    print("""

    1) Kullanici Yüz Tanıma
    2) Kullanıcı Kitap Alma
    3) Kullanıcı Kitap Verme
    4) QR Code Olusturma
    5) Kitap Sorgulama
    6) Cikis

    """)

    sec = int(input("Secim yapınız: "))

    if sec == 1:
        import lib_face_reg
    elif sec == 2:
        import lib_qrcode_get_reader
    elif sec == 3:
        import lib_qrcode_give_reader
    elif sec == 4:
        import lib_qrcode_generator
    elif sec == 5:
        import book_query
    elif sec == 6:
        exit()
    else:
        print("Hatalı numara secimi!!!")

    secim = input("Cıkmak istiyor musunuz?(y/n)")
    
    if secim == "y":
        exit()
    elif secim == "n":
        pass
    else:
        print("Hatalı secim yaptınız!!!")