import os

PAGES_DIR = "pages"

for filename in os.listdir(PAGES_DIR):
    if filename.endswith(".py"):

        path = os.path.join(PAGES_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # skip se già convertito
        if "def render(" in content:
            continue

        print(f"Fixing {filename}")

        new_content = "import streamlit as st\n\n"
        new_content += "def render():\n"

        for line in content.splitlines():
            new_content += "    " + line + "\n"

        new_content += "\nif __name__ == '__main__':\n    render()\n"

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
