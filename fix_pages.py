import os

PAGES_DIR = "pages"

for filename in os.listdir(PAGES_DIR):
    if filename.endswith(".py"):

        path = os.path.join(PAGES_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # se già convertito → skip
        if "def render(" in content:
            continue

        print(f"Fixing {filename}")

        new_content = f"""
import streamlit as st

def render():
{chr(10).join(['    ' + line for line in content.splitlines()])}

# fallback
if __name__ == "__main__":
    render()
"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
