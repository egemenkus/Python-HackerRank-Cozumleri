# Örnek Giriş
# qA2

# Örnek Çıkış
# True
# True
# True
# True
# True

if __name__ == '__main__':
    giris = input()
    print(any(c.isalnum() for c in giris))
    print(any(c.isalpha() for c in giris))
    print(any(c.isdigit() for c in giris))
    print(any(c.islower() for c in giris))
    print(any(c.isupper() for c in giris))