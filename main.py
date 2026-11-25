from pathlib import Path

ROAST = "Operator, kamu minta agent kerja 24/7 lalu masih ngecek progress tiap 5 menit—bahkan cron job-mu punya work-life balance lebih baik."

Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ROAST + "\n", encoding="utf-8")
