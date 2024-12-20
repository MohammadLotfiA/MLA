#! /bin/python3
"""
Written by Mohammad Lotfi Akbarabadi: MLA-IT Education
Last updated: DEC 2024
"""
import os
import random
import shutil
import base64

# Set to true if you want to know where the flag is located
SHOW_FLAG_PLACE = False

FLAG_CONST = "TUxBe0ZVWloxTjZfMEZfN0gzX04wVjR9Cg=="

def generate_website(base_path="100nova"):
    # Clean up any existing data
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path)

    # Generate the landing page
    index_content = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Lost Robot</title><style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial,sans-serif;background:linear-gradient(to bottom right,#020024,#090979,#00d4ff);color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:20px;overflow:hidden}.story-container{max-width:600px;background:rgba(255,255,255,.1);padding:20px;border-radius:10px;box-shadow:0 8px 15px rgba(0,0,0,.2);text-align:center;animation:float 3s ease-in-out infinite}@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}h1{font-size:2em;margin-bottom:10px;color:#ffdd57}p{font-size:1.2em;line-height:1.5;margin-bottom:20px}.robot{font-size:3em;margin-bottom:15px;animation:blink 2s infinite}@keyframes blink{0%,100%{color:#ffdd57}50%{color:#1e90ff}}.prize{font-weight:700;font-size:1.5em;color:#00e676;margin-top:10px}</style></head><body><div class="story-container"><div class="robot">🤖</div><h1>The Lost Robot</h1><p>Once upon a time, in the heart of the digital realm, there roamed a small, curious robot named Nova. Nova was known for its dazzling lights and quirky beeps, and it had a secret to share.</p><p>Legend has it that if you ever find Nova, it will reward you with a prize, something rare and precious from the depths of cyberspace.</p><p>But beware... Nova is a master of hide-and-seek, and only the cleverest can uncover its hiding spot.</p><div class="prize">Will you be the one to find Nova and claim the prize?</div></div></body></html>
    <!--/flag.txt-->
"""
    with open(os.path.join(base_path, "index.html"), "w") as index_file:
        index_file.write(index_content)

    # Generate random folders
    folders = []
    for _ in range(100):
        folder_name = ''.join(random.choices('0123456789abcdef', k=8))
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path)
        folders.append(folder_name)

    # Place the flag in a random folder
    flag_folder = random.choice(folders)
    flag_file_path = os.path.join(base_path, flag_folder, "flag.txt")
    with open(flag_file_path, "w") as flag_file:
        flag_file.write(base64.b64decode(FLAG_CONST).decode("utf-8"))

    # Create robots.txt
    robots_content = "\n".join([f"Disallow: /{folder}" for folder in folders])
    with open(os.path.join(base_path, "robots.txt"), "w") as robots_file:
        robots_file.write(robots_content)

    if SHOW_FLAG_PLACE == True:
        print(f"Flag is in folder: {flag_folder} (shh, don't tell!)", "\n")

    print(f"Website generated at: {os.path.abspath(base_path)}","\n")
    print("Happy Hacking, MLA-IT Education", "(^_^)")

if __name__ == "__main__":
    generate_website()
