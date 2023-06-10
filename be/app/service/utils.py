import re

def validate_email(email: str) -> str:
    allowed_domains = ["gmail.com", "hotmail.com", "yahoo.com"]  # Daftar domain yang diizinkan

    regex_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(regex_pattern, email):
        raise ValueError("Format email tidak valid")

    domain = email.split("@")[1]
    if domain not in allowed_domains:
        raise ValueError("Domain email tidak diizinkan")

    return email

def validate_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password harus memiliki panjang minimal 8 karakter")

    regex_pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]+$"
    if not re.match(regex_pattern, password):
        raise ValueError("Password harus terdiri dari minimal 1 huruf kapital, 1 huruf kecil, dan 1 angka")
    
    if any(char.isalnum() is False for char in password):
        raise ValueError("Password tidak boleh mengandung karakter khusus")
    return password