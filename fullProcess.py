import os
import re
import subprocess

import re

def remove_emojis_from_html_list(html_content_list):
    """
    Removes all emojis from a list of HTML content without using external libraries.
    
    Args:
        html_content_list (list): List of HTML content strings with potential emojis
        
    Returns:
        list: List of HTML content strings with emojis removed
    """
    # Unicode emoji patterns
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0000257F"  # Enclosed characters
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "\U0000FE00-\U0000FE0F"  # Variation Selectors
        "\U0001F000-\U0001F02F"  # Mahjong tiles
        "\U0001F0A0-\U0001F0FF"  # Playing cards
        "\U0001F100-\U0001F1FF"  # Enclosed Alphanumeric Supplement
        "\U0001F200-\U0001F2FF"  # Enclosed Ideographic Supplement
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "]+", 
        flags=re.UNICODE
    )
    
    # Process each HTML string in the list
    cleaned_html_list = []
    for html_content in html_content_list:
        cleaned_html = emoji_pattern.sub('', html_content)
        cleaned_html_list.append(cleaned_html)

    pattern = re.compile(
        r'<div style="position: relative; padding-bottom: 56\.25%.*?</div>',
        re.DOTALL  # Allow the pattern to match across multiple lines
    )
    double_cleaned_html_list = []
    for content in cleaned_html_list:
        Cleanedcontent = pattern.sub('', content)
        double_cleaned_html_list.append(Cleanedcontent)
    
    return double_cleaned_html_list

def extract_body(html_content):
    """Extract content inside <body> tags, remove trailing <script> tags."""
    match = re.search(r"<body[^>]*>(.*?)</body>", html_content, re.DOTALL | re.IGNORECASE)
    body = match.group(1) if match else html_content

    # Remove all <script>...</script> blocks, especially at the end
    body = re.sub(r"<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>", "", body, flags=re.DOTALL | re.IGNORECASE)
    return body.strip()

def combine_html_files(html_files, css_path="myStyles.css",output_html="combined.html"):
    combined_content = []
    mathjax_scripts = '''
    <script>
    window.MathJax = {
        jax: ["input/TeX","output/HTML-CSS"],
        extensions: ["tex2jax.js"],
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\\\(","\\\\)"] ],
            displayMath: [ ['$$','$$'], ["\\\\[","\\\\]"] ],
            processEscapes: true,
            ignoreClass: "nostem|no-math",
            processClass: "math|tex"
        },
        TeX: {
            extensions: ["AMSmath.js", "AMSsymbols.js"]
        },
        "HTML-CSS": {
            availableFonts: ["TeX"],
            scale: 200
        },
        showProcessingMessages: false,
        messageStyle: "none",
        skipStartupTypeset: false
    };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
'''

    # Add HTML and HEAD section with optional CSS
    combined_content.append("<html>")
    combined_content.append("<head>")
    combined_content.append(mathjax_scripts)
    if os.path.exists(css_path):
        combined_content.append(f'<link rel="stylesheet" href="{css_path}">')
    else:
        print("couldnt find css sheet")
    combined_content.append("</head><body>")

    # Add body content from each file
    for filename in html_files:
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
            body = extract_body(html)
            combined_content.append(f"<!-- Start of {filename} -->")
            combined_content.append(body)
            combined_content.append(f"<!-- End of {filename} -->")

    # Close HTML
    combined_content.append("</body></html>")

    combined_content = remove_emojis_from_html_list(combined_content)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write("\n".join(combined_content))

    print(f"Combined HTML written to {output_html}")
    print(f"File Location: {os.path.abspath(output_html)}")
    return output_html


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build relative paths from the script's location
    submodule_dir = os.path.join(script_dir, "_build",  "aqua_blue")
    local_html = os.path.join(script_dir, "_build",  "aqua_blue.html")

    # Get HTML files from submodule
    html_files = [os.path.join(submodule_dir, f) for f in os.listdir(submodule_dir) if f.endswith('.html')]

    # Add the local HTML file
    html_files.insert(0, local_html)

    # Combine HTML files
    combined_html = combine_html_files(html_files)

    # command = "wkhtmltopdf --enable-javascript --disable-smart-shrinking --no-stop-slow-scripts --debug-javascript --enable-local-file-access --print-media-type --javascript-delay 3000 --user-style-sheet myStyles.css \"combined.html\" documentation.pdf"
    command = [
    "/usr/local/bin/wkhtmltopdf",  # or just "wkhtmltopdf" if PATH is correct
    "--enable-javascript",
    "--disable-smart-shrinking",
    "--no-stop-slow-scripts",
    "--debug-javascript",
    "--enable-local-file-access",
    "--print-media-type",
    "--javascript-delay", "3000",
    "--user-style-sheet", "myStyles.css",
    "combined.html",
    "documentation.pdf"
    ]
    subprocess.call(command)

    print("job is completed and pdf has been created")

    print(f"PDF file created at: {os.path.abspath("documentation.pdf")}")