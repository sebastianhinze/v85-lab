# Hashed predictions

This folder holds a SHA-256 commitment to each week's V85 prediction file. The hash is committed before the betting
stop; the file itself and the secret salt used with it are published after the round, so anyone can check that the
prediction was fixed in advance.

To check a round once the file and salt are published, put `prediction.json` and `salt.txt` in one folder and run
`cat salt.txt prediction.json | shasum -a 256`. The result must equal the `hash` in `hashes/<round>.json`. Or run
`python3 verify.py prediction.json salt.txt <hash>`, which prints OK or MISMATCH.

The file holds, for every starter, the number, the horse name, the model's win chance and the crowd's betting share,
plus the model version and code version. Derived numbers only: no odds, no raw data.

The timestamp is GitHub's push time of the commit, not the date written in the commit (a local clock proves nothing).
A round counts only if its hash was pushed before the betting stop, which the manifest lists.

Nothing here is betting advice.
