"""Check a published prediction: python3 verify.py prediction.json salt.txt <hash>. Standard library only."""
import hashlib
import sys

if len(sys.argv) != 4:
    sys.exit("usage: python3 verify.py <prediction.json> <salt.txt> <hash>")
file_bytes = open(sys.argv[1], "rb").read()
salt = open(sys.argv[2], encoding="utf-8").read().strip()
digest = hashlib.sha256((salt + "\n").encode() + file_bytes).hexdigest()
ok = digest == sys.argv[3].strip().lower()
print("OK" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
