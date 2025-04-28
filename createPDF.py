import os
import re
import subprocess

import re


command = "/usr/local/bin/wkhtmltopdf --log-level info --enable-javascript --disable-smart-shrinking --no-stop-slow-scripts --debug-javascript --enable-local-file-access --print-media-type --javascript-delay 3000 --user-style-sheet myStyles.css \"combined.html\" documentation.pdf"
# command = [
# "wkhtmltopdf",
# # "/usr/local/bin/wkhtmltopdf",
# "--log-level info", # or just "wkhtmltopdf" if PATH is correct
# "--enable-javascript",
# "--debug-javascript",
# "--disable-smart-shrinking",
# "--no-stop-slow-scripts",
# "--enable-local-file-access",
# "--print-media-type",
# "--javascript-delay", "3000",
# "--user-style-sheet", "myStyles.css",
# "combined.html",
# "documentation.pdf"
# ]


subprocess.run(command)