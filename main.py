import random #random oʻyin
import os
LEVELS = [
           (1, 1, 10, 3, 50),
           (2, 10, 20, 7, 100),
           (3, 15, 30, 7, 100),
           (4, 10, 30, 10, 150),
           (5, 25, 50, 10, 150),
]
def get_level_data(current_level):
    for lvl in LEVELS:
        if lvl[0] == current_level:
            return lvl
    return None
def restart( ):
    while True:
        javob = input("\nQayta boshlash uchun [ X ] | Chiqish [ O ] : ") .strip( ) .lower( )
        if javob == "x":
            return True
        elif javob == "o":
            return False
        else:
            print("iltimos, faqat X yoki O yozing")
def hint_2(guess, attemps, coin):
            if guess !=999:
                return False, attemps, coin
            if coin < 50:
                print("\ncoin yetarli emas")
                return True, attemps, coin
            coin -= 50
            attemps +=2
            print("\nsizga ikkita urinishlar berildi")
            print("urinishlar soni: " , attemps)
            return True, attemps, coin
def hint_1(guess, secret, coin):
            if guess !=777:
                return False, coin
            if coin < 50:
                print("\ncoin yetarli emas")
                return True, coin
            coin -= 50
            if secret % 2 == 0:
                print("\nYordam: yashirin son JUFT")
            else:
                print("\nYordam: yashirin son TOQ")
            return True, coin
def pause_2( ):
    while True:
        x = input("\nBoshlash uchun [ OK ] deb yozing:") .strip( ) .lower( )
        if x == "ok" :
            break
        else:
            print("Iltimos OK deb yozing")
def intro(level, min_son, max_son, attemps, coin):
    clear( )
    print(f"=== LEVEL {level} ===\n")
    print(f"men {min_son} dan {max_son} gacha son oʻylayman")
    print(f"urinishlar soni: {attemps}")
    print(f"coin:", coin)
    pause_2( )
def pause( ):
    while True:
        x = input("\nDavom etish uchun [ OK ] deb yozing:") .strip( ) .lower( )
        if x == "ok" :
            break
        else:
            print("Iltimos OK deb yozing")       
def clear( ): #sahifani tozalash
    os.system('cls' if os.name == 'nt' else 'clear')
def chegara(guess, min_son, max_son):
    if not (min_son <= guess <= max_son):
        print(f"\n{min_son} va {max_son} orasidagi son kiriting")
        return False
    return True
def son( ):
    try:
        return int(input("\nMen qaysi sonni oʻyladim?")) #savol soʻrash
    except ValueError:
            print("\niltimos, faqat son kiriting")
            return None
def devmode(guess, secret, attemps, coin):
    dev_code = 4566
    if guess == dev_code:
        print("\ndeveloper rejimi ishga tushdi!")
        print("cheksiz urinishlar qoʻshildi")
        print("cheksiz coin qoʻshildi")
        print("dastur oʻylagan son" , secret)
        return True, 9999, 9999
    return False, attemps, coin #devmode
def taqqosla(guess , secret):
    if guess == secret:
        return "teng"
    elif guess < secret:
        return "katta"
    else:
        return "kichik"
        #taqqoslash mexanizmi

def play_level(level, min_son, max_son, attemps, coin, bonus_attemps, bonus_coin):
    secret = random.randint(min_son, max_son)
    intro(level, min_son, max_son, attemps, coin)
    while attemps > 0:
        print("\nMen oʻylagan sonni top!")
        print("Doʻkon: ")
        print("2ta urinishlar - 50 coin. olish uchun 999 kodini kiriting")
        print("Yordam - 50 coin. olish uchun 777 kodini kiriting")
        guess = son( )
        if guess is None:
            continue
        dev, attemps, coin = devmode(guess, secret, attemps, coin)
        if dev:
            continue
        used, coin = hint_1(guess, secret, coin)
        if used:
            continue
        used, attemps, coin = hint_2(guess, attemps, coin)
        if used:
            continue
        if not chegara(guess, min_son, max_son):
            continue
        natija = taqqosla(guess, secret)
        if natija == "teng":
            print(f"\nToʻgʻri! {level}-bosqichdan oʻtding")
            print(f"senga {bonus_attemps} urinishlar va {bonus_coin} coin berildi")
            pause( )
            return "win", attemps + bonus_attemps, coin + bonus_coin
        elif natija == "katta":
            print("\nNotoʻgʻri javob! men oʻylagan son katta")
            attemps -=1
            print("urinishlar soni: " , attemps)
            print("coin: " , coin)
        else:
            print("\nNotoʻgʻri javob! men oʻylagan son kichik")
            attemps -=1
            print("urinishlar soni: " , attemps)
            print("coin: " , coin)
    return "lose", attemps, coin
def main( ):
    current_level = 1
    attemps = 3
    coin = 50
    while True:
        lvl = get_level_data(current_level)
        if lvl is None:
            print("==BARCHA BOSQICHLAR TUGADI==")
            print("=== LEVEL 6 ===")
            print("coming soon...")
            if restart( ):
                current_level = 1
                attemps = 3
                coin = 50
                continue
            else:
                break
        level, min_son, max_son, bonus_attemps, bonus_coin = lvl
        print(f"\n=== LEVEL {current_level} ==")
        result, attemps, coin = play_level(
                level,
                min_son,
                max_son,
                attemps,
                coin,
                bonus_attemps,
                bonus_coin
        )
        if result == "win":
            current_level +=1
            continue
        if result == "lose":
            print("\nUrinishlar tugadi")
            if restart( ):
                current_level = 1
                attemps = 3
                coin = 50
                continue
            else:
                break
if __name__ == "__main__":
    main( )
