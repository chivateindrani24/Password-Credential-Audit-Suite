def identify_hash(h):
    l=len(h)
    if l==32: return "MD5"
    if l==40: return "SHA1"
    if l==64: return "SHA256"
    if l==128: return "SHA512"
    return "Unknown"
