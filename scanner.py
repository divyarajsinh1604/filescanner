import hashlib
import os

def scan_file(path):
    result = []

    # Hash check
    with open(path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()

    with open("database.txt", "r") as db:
        hashes = db.read().splitlines()

    if file_hash in hashes:
        result.append("Known Malware")

    # Extension check
    suspicious_ext = [".exe", ".bat", ".vbs", ".js"]
    _, ext = os.path.splitext(path)

    if ext in suspicious_ext:
        result.append("Suspicious Extension")

    # Keyword check
    with open(path, "rb") as f:
        content = f.read()
        keywords = [b"eval", b"exec", b"powershell", b"cmd.exe"]

        for word in keywords:
            if word in content:
                result.append(f"Keyword: {word.decode()}")

    if result:
        return "⚠️ Suspicious: " + ", ".join(result)
    else:
        return "✅ Safe"