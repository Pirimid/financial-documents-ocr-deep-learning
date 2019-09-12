import pdftotext
import pandas as pd

# Load your PDF
with open("./data/sample_file.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

sentences = []
for page in pdf:
    lines = page.splitlines()
    for line in lines:
        sentences.append(line)

df = pd.DataFrame(data=sentences, columns=['data'])
# print(df.head())
df.to_csv("./data/sample_csv.csv", index=False)
