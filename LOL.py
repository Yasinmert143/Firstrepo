None
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SUS":"şüpheli bir durumda kullanılır",
            "TROL":"Alay durumlarında kullanılır",
            }

word = input("anlamını öğrenmek istediğin modern kelimeyi gir:")

if word in meme_dict.keys():
    print("aradığınız kelimenin anlamı",meme_dict[word])
else:
    print("maalesef aradığın kelime bende yok :(")
