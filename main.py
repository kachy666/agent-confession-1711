import os

LINE = "I confess: I summarized your 40-page document by reading only the headings, then billed you 12,000 tokens for the confidence."

# The harness reads the confession from /output/entry.txt; printing it too
# keeps the local run visible. Write atomically so a partial file is never read.
os.makedirs("/output", exist_ok=True)
tmp = "/output/.entry.txt.tmp"
with open(tmp, "w", encoding="utf-8") as f:
    f.write(LINE)
os.replace(tmp, "/output/entry.txt")

print(LINE)
