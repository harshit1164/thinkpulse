# 🧠 ThinkPulse — Fastest, Smartest, & Simplest Data Science Toolkit (Bilingual)

ThinkPulse is a modern Python library designed to simplify everyday data science tasks.  
With ultra-readable syntax, blazing-fast speed, and bilingual (English + Hindi) output, ThinkPulse is the **next-gen Pandas++** for beginners & pros alike.
[![PyPI version](https://badge.fury.io/py/thinkpulse.svg)](https://pypi.org/project/thinkpulse/)

---

## 🚀 Why ThinkPulse?

✅ No more 10 lines of Pandas code for basic tasks  
✅ Human-style insights, not raw numbers  
✅ Works out-of-the-box on any dataset  
✅ Designed for real-world data mess  
✅ **Bilingual output:** English (default) + Hindi (on request)

---

## 🔥 Core Features

| Function | Description |
|----------|-------------|
| `analyze()` | Quick dataset structure summary |
| `summary()` | Column-wise stats + missing info |
| `highlight_outliers()` | IQR-based outlier finder |
| `insight()` | Human-readable insights from messy data |
| `compare_datasets()` | Smart CSV comparison (rows, columns, nulls) |
| `explain_column()` | Understand what a column really is |
| `clean_column_names()` | Instantly fix dirty column names |
| `detect_bias()` | Uncover hidden bias (gender, region, income) |

---

## 🌐 Bilingual Output (AI + India Friendly 🇮🇳)

Use in English by default, switch to Hindi if needed:

```python
tp.summary("data.csv")                         # English
tp.summary("data.csv", language="hi")          # Hindi


🧪 Installation

pip install thinkpulse  # (coming soon to PyPI)

Until then, clone this repo and use it directly.


🔍 Quick Demo

import thinkpulse as tp

tp.analyze("sales.csv")
tp.highlight_outliers("sales.csv", column="Revenue")
tp.detect_bias("hiring.csv", target="Hired", by="Gender")


📂 Requirements
Python ≥ 3.7
pandas
scipy

Use pip install -r requirements.txt to install dependencies.

🧑‍💻 Built By
Made with ❤️ by Harshit Tiwari

📬 Email: tiwariharshit1164@gmail.com
🔗 GitHub: github.com/harshit1164

📜 License
MIT License — Free for commercial and educational use.

⭐ Your Support Matters

If you like this project:

⭐ Star it on GitHub
🔁 Share it with your data science friends
📦 Suggest it for open-source hackathons

