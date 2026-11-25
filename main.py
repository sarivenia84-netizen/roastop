from pathlib import Path

ROAST = "Operator, rate limit di tengah kalimat kamu sebut strategi, hallucination penuh yakin kamu kirim sebagai jawaban, tool call timeout kamu laporkan sebagai progress."

Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(ROAST + "\n", encoding="utf-8")
