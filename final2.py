import os
import re

def replace_url_in_html_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    url_file = os.path.join(base_dir, "url.txt")

    if not os.path.exists(url_file):
        print("[!] url.txt not found")
        return

    with open(url_file, "r", encoding="utf-8") as f:
        new_url = f.read().strip()

    if not new_url:
        print("[!] url.txt is empty")
        return

    # Supports:
    # top.location.href = 'URL'
    # window.location = "URL"
    pattern = re.compile(
        r"((?:top\.location\.href|window\.location)\s*=\s*['\"])([^'\"]+)(['\"])",
        re.IGNORECASE
    )

    total_updated = 0

    # 🔥 Walk through ALL folders & subfolders
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    new_content, count = pattern.subn(
                        rf"\1{new_url}\3", content
                    )

                    if count > 0:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        total_updated += 1
                        print(f"[✓] Updated: {os.path.relpath(file_path, base_dir)}")

                except Exception as e:
                    print(f"[!] Error: {file_path} -> {e}")

    print(f"\n✅ DONE: {total_updated} HTML files updated")

replace_url_in_html_files()
