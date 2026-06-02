from modules.dictionary_generator import generate_words
from modules.hash_analyzer import identify_hash
from modules.password_strength import analyze_password

print("Password Credential Audit Suite")
print(generate_words("Indrani","2004"))
print(identify_hash("5f4dcc3b5aa765d61d8327deb882cf99"))
print(analyze_password("Admin123"))
