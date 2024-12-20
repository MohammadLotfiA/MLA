#! /bin/bash
<<EOF
Written by Mohammad Lotfi Akbarabadi: MLA-IT Education
Last updated: DEC 2024
EOF
# Set to 1 to show the place of the flag
SHOW_FLAG_PLACE=0

FLAG_CONST="TUxBe0ZVWloxTjZfMEZfN0gzX04wVjR9Cg=="
# Base path for the site
BASE_PATH="100nova"

# Function to generate random 8-character hexadecimal string
generate_hex() {
  printf "%08x" $((RANDOM * RANDOM))
}

# Clean up existing directory if it exists
if [ -d "$BASE_PATH" ]; then
  rm -rf "$BASE_PATH"
fi

# Create base directory
mkdir -p "$BASE_PATH"

# Create index.html
cat > "$BASE_PATH/index.html" <<EOF
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Lost Robot</title><style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial,sans-serif;background:linear-gradient(to bottom right,#020024,#090979,#00d4ff);color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:20px;overflow:hidden}.story-container{max-width:600px;background:rgba(255,255,255,.1);padding:20px;border-radius:10px;box-shadow:0 8px 15px rgba(0,0,0,.2);text-align:center;animation:float 3s ease-in-out infinite}@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}h1{font-size:2em;margin-bottom:10px;color:#ffdd57}p{font-size:1.2em;line-height:1.5;margin-bottom:20px}.robot{font-size:3em;margin-bottom:15px;animation:blink 2s infinite}@keyframes blink{0%,100%{color:#ffdd57}50%{color:#1e90ff}}.prize{font-weight:700;font-size:1.5em;color:#00e676;margin-top:10px}</style></head><body><div class="story-container"><div class="robot">🤖</div><h1>The Lost Robot</h1><p>Once upon a time, in the heart of the digital realm, there roamed a small, curious robot named Nova. Nova was known for its dazzling lights and quirky beeps, and it had a secret to share.</p><p>Legend has it that if you ever find Nova, it will reward you with a prize, something rare and precious from the depths of cyberspace.</p><p>But beware... Nova is a master of hide-and-seek, and only the cleverest can uncover its hiding spot.</p><div class="prize">Will you be the one to find Nova and claim the prize?</div></div></body></html>
    <!--/flag.txt-->
EOF

# Create folders and populate robots.txt
ROBOTS_FILE="$BASE_PATH/robots.txt"
> "$ROBOTS_FILE"

for i in {1..100}; do
  FOLDER_NAME=$(generate_hex)
  mkdir -p "$BASE_PATH/$FOLDER_NAME"
  echo "Disallow: /$FOLDER_NAME" >> "$ROBOTS_FILE"
  FOLDERS+=("$FOLDER_NAME")
done

# Place the flag in a random folder
FLAG_FOLDER=${FOLDERS[$RANDOM % 100]}
echo $FLAG_CONST | base64 -d > "$BASE_PATH/$FLAG_FOLDER/flag.txt"

if [ $SHOW_FLAG_PLACE == 1 ]; then
echo -e "Flag is in folder: $FLAG_FOLDER (shh, don't tell!)\n"
fi

echo -e "Website generated at: $(realpath "$BASE_PATH")\n"
echo "Happy Hacking, MLA-IT Education", "(^_^)"
