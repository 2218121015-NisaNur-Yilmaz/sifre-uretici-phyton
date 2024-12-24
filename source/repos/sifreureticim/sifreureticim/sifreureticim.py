import random
import string

def generate_password(length=12 , use_uppercase=False, use_numbers=False, use_symbols=False):
    """
    Rastgele �ifre �reten bir fonksiyon.

    :param length: �ifrenin uzunlu�u (varsay�lan 16)
    :param use_uppercase: B�y�k harf kullan�ls�n m�? (varsay�lan False)
    :param use_numbers: Say�lar kullan�ls�n m�? (varsay�lan False)
    :param use_symbols: Semboller kullan�ls�n m�? (varsay�lan False)
    :return: Rastgele �retilmi� bir �ifre.
    """
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("En az bir karakter t�r� se�melisiniz!")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("�ifre �reticiye Ho� Geldiniz!")
    try:
        length = int(input("�ifrenizin uzunlu�unu girin (varsay�lan 16): ") or 16)
        use_uppercase = input("B�y�k harf kullan�ls�n m�? (E/h): ").strip().lower() != 'h'
        use_numbers = input("Say�lar kullan�ls�n m�? (E/h): ").strip().lower() != 'h'
        use_symbols = input("Semboller kullan�ls�n m�? (E/h): ").strip().lower() != 'h'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Olu�turulan �ifre: {password}")
    except ValueError as e:
        print(f"Hata: {e}")

