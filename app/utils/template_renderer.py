def make_html_body(
    english_word: str,
    english_word_pronunciation: str,
    english_example: str,
    german_word: str,
    german_example: str,
) -> str:
    """Returns an HTML template as string for the Daily Language Dose email with an extreme neon retro style."""

    # Cat avatar made of text symbols
    cat_avatar = r"""/\_/\
( o.o )
> ^ <"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daily Language Dose</title>
  <style>
    /* Global resets & animated neon background */
    body, html {{
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #ff00ff, #00ffff, #ffff00, #ff00ff);
      background-size: 400% 400%;
      animation: gradientShift 10s ease infinite;
      font-family: 'Courier New', Courier, monospace;
      color: #ffffff; /* Explicitly set text color to white */
    }}
    @keyframes gradientShift {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}
    /* Container for email content */
    .container {{
      max-width: 600px;
      margin: 30px auto;
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.95); /* Dark background for readability */
      border: 5px dashed #ff00ff;
      border-radius: 15px;
      box-shadow: 0 0 25px #00ffff, inset 0 0 15px #ffff00;
      position: relative;
      color: #ffffff; /* Explicitly set text color to white */
    }}
    /* Header styling */
    .header {{
      text-align: center;
      font-size: 2rem;
      font-weight: bold;
      margin-bottom: 20px;
      text-shadow: 3px 3px 8px #000;
      color: #ff69b4; /* Rosa/purple color for the header */
    }}
    /* Section styling */
    .section {{
      margin-bottom: 25px;
      color: #ffffff; /* Explicitly set text color to white */
    }}
    .label {{
      font-size: 14px;
      color: #00ff00; /* Green for labels */
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 8px;
    }}
    .value {{
      font-size: 20px;
      line-height: 1.6;
      color: #ffffff; /* Explicitly set text color to white */
      text-shadow: 1px 1px 3px #000;
      margin-bottom: 10px;
    }}
    /* Divider for section separation */
    .divider {{
      border-top: 2px dotted #00ff00;
      margin: 20px 0;
    }}
    /* Footer with cat avatar */
    .footer {{
      text-align: center; /* Center horizontally */
      margin-top: 20px;
      color: #ffffff; /* Explicitly set text color to white */
    }}
    /* Cat avatar styling */
    .cat-avatar {{
      font-family: 'Courier New', Courier, monospace;
      color: #00ffff; /* Cyan color for retro vibe */
      margin: 0 auto; /* Center horizontally */
      white-space: pre-wrap; /* Preserve spacing and line breaks while wrapping */
      text-align: left; /* Align text to the left within the centered block */
      display: inline-block; /* Ensure the avatar doesn't stretch full width */
    }}
    /* Responsive tweaks */
    @media only screen and (max-width: 620px) {{
      .container {{
        margin: 20px;
        padding: 15px;
      }}
      .header {{
        font-size: 1.75rem;
      }}
      .value {{
        font-size: 18px;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Header -->
    <div class="header">
      Daily Language Dose
    </div>
    
<!-- ASCII Art using a <pre> tag to preserve line breaks -->
    <pre style="white-space: pre-wrap; font-size: 16px; line-height: 1.2; margin: 20px 0; text-align: center; color: #00ffff;">
{cat_avatar}
    </pre>
    <!-- Content Sections -->
    <div class="section">
      <div class="label">English</div>
      <div class="value">{english_word}</div>
    </div>
    <div class="section">
      <div class="label">Pronunciation</div>
      <div class="value">{english_word_pronunciation}</div>
    </div>
    <div class="section">
      <div class="label">Example (EN)</div>
      <div class="value">{english_example}</div>
    </div>
    <div class="divider"></div>
    <div class="section">
      <div class="label">German</div>
      <div class="value">{german_word}</div>
    </div>
    <div class="section">
      <div class="label">Example (DE)</div>
      <div class="value">{german_example}</div>
    </div>
  </div>
</body>
</html>
"""
