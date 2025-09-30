#!/usr/bin/env python3
import csv
from datetime import datetime

rows = list(csv.DictReader(open("airdrops.csv")))
total = sum(float(r["points"]) for r in rows)

print(f"airdrop-tracker-lite — {datetime.utcnow().isoformat()}Z")
for r in rows:
    print(f"{r['project']:10} {r['symbol']:6} {r['points']:>6}  {r['notes']}")
print(f"total_points: {total}")
