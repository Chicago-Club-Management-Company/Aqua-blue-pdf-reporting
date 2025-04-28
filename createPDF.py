import os
import re
import subprocess

import re


# command = "wkhtmltopdf --enable-javascript --disable-smart-shrinking --no-stop-slow-scripts --debug-javascript --enable-local-file-access --print-media-type --javascript-delay 3000 --user-style-sheet myStyles.css \"combined.html\" documentation.pdf"
command = [
"/usr/local/bin/wkhtmltopdf",
"--debug",  # or just "wkhtmltopdf" if PATH is correct
"--enable-javascript",
"--disable-smart-shrinking",
"--debug-javascript"
"--no-stop-slow-scripts",
"--enable-local-file-access",
"--print-media-type",
"--javascript-delay", "3000",
"--user-style-sheet", "myStyles.css",
"combined.html",
"documentation.pdf"
]
try:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print(result.stdout.decode())
    print(result.stderr.decode())

    print("job is completed and pdf has been created")
    print(f"PDF file created at: {os.path.abspath('documentation.pdf')}")

    # **Debug: Check if PDF file exists**
    if os.path.exists("documentation.pdf"):
        print("DEBUG: documentation.pdf EXISTS")
    else:
        print("DEBUG: documentation.pdf NOT FOUND")

except subprocess.CalledProcessError as e:
    print("ERROR: Subprocess failed with exit code", e.returncode)
    print("STDOUT:", e.stdout.decode())
    print("STDERR:", e.stderr.decode())