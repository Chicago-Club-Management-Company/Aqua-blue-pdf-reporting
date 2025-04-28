import os
import re
import subprocess

import re


# command = "wkhtmltopdf --enable-javascript --disable-smart-shrinking --no-stop-slow-scripts --debug-javascript --enable-local-file-access --print-media-type --javascript-delay 3000 --user-style-sheet myStyles.css \"combined.html\" documentation.pdf"
command = [
"/usr/local/bin/wkhtmltopdf",  # or just "wkhtmltopdf" if PATH is correct
"--enable-javascript",
"--disable-smart-shrinking",
"--debug-javascript",
"--no-stop-slow-scripts",
"--enable-local-file-access",
"--print-media-type",
"--javascript-delay", "3000",
"--user-style-sheet", "myStyles.css",
"combined.html",
"documentation.pdf"
]
with open("wkhtmltopdf.log", "w") as log_file:
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        log_file.write(result.stdout + result.stderr)  # Capture all output
        print("✅ wkhtmltopdf executed successfully!")
    except subprocess.CalledProcessError as e:
        log_file.write(f"ERROR: Subprocess failed with exit code {e.returncode}\n")
        log_file.write(e.stdout + e.stderr)
        print(f"❌ Error! Check wkhtmltopdf.log for details.")