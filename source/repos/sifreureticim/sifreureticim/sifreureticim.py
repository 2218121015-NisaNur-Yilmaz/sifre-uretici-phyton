import random
import string

def generate_password(length=16, use_uppercase=False, use_numbers=False, use_symbols=False):
    """
    Rastgele þifre üreten bir fonksiyon.

    :param length: Þifrenin uzunluðu (varsayýlan 16)
    :param use_uppercase: Büyük harf kullanýlsýn mý? (varsayýlan False)
    :param use_numbers: Sayýlar kullanýlsýn mý? (varsayýlan False)
    :param use_symbols: Semboller kullanýlsýn mý? (varsayýlan False)
    :return: Rastgele üretilmiþ bir þifre.
    """
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("En az bir karakter türü seçmelisiniz!")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Þifre Üreticiye Hoþ Geldiniz!")
    try:
        length = int(input("Þifrenizin uzunluðunu girin (varsayýlan 16): ") or 16)
        use_uppercase = input("Büyük harf kullanýlsýn mý? (E/h): ").strip().lower() != 'h'
        use_numbers = input("Sayýlar kullanýlsýn mý? (E/h): ").strip().lower() != 'h'
        use_symbols = input("Semboller kullanýlsýn mý? (E/h): ").strip().lower() != 'h'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Oluþturulan þifre: {password}")
    except ValueError as e:
        print(f"Hata: {e}")

