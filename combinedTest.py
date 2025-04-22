import os
import subprocess
command = "wkhtmltopdf --enable-javascript --disable-smart-shrinking --no-stop-slow-scripts --debug-javascript --enable-local-file-access --print-media-type --javascript-delay 3000 --user-style-sheet myStyles.css \"file:///C:/CodingGeneral/chicagoClubManagement/aqua-blue/combined.html\" documentation.pdf"
subprocess.run(command)