from pathlib import Path

folders = [
    "docs", "reports", "data/raw", "data/processed",
    "models/algorithms", "models/saved_model",
    "scripts/data_preparation", "tests",
]
files = [
    "docs/define.md", "docs/design.md", "docs/description.md",
    "reports/data_description.md", "reports/evaluation_report.md", "reports/demo_report.md",
    "scripts/data_preparation/data_collection.py",
    "scripts/data_preparation/EDA.py",
    "scripts/data_preparation/data_preprocessing.py",
    "scripts/data_preparation/feature_engineering.py",
    "scripts/training.py", "scripts/evaluation.py",
    "models/__init__.py", "models/algorithms/__init__.py",
    "tests/test_core.py", "requirements.txt",
]

for d in folders:
    Path(d).mkdir(parents=True, exist_ok=True)
for f in files:
    Path(f).touch()
# Git không lưu thư mục rỗng, nên dùng .gitkeep (mẫu spam-classifier cũng làm vậy)
for d in ["data/raw", "data/processed", "models/saved_model"]:
    (Path(d) / ".gitkeep").touch()
