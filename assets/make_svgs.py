import base64, pathlib

fonts = pathlib.Path("/Users/sohamjadhav/sohamvjadhav/assets/fonts")
b64 = base64.b64encode((fonts / "albertsans-latin.woff2").read_bytes()).decode()

font_faces = f"""@font-face {{
  font-family: 'Albert Sans';
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url(data:font/woff2;base64,{b64}) format('woff2');
}}"""

header = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="170" viewBox="0 0 1000 170" role="img" aria-label="Soham Jadhav">
  <defs>
    <style>{font_faces}
      text {{ font-family: 'Albert Sans', 'Helvetica Neue', Arial, sans-serif; }}
    </style>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0e5232"/>
      <stop offset="100%" stop-color="#1a2b22"/>
    </linearGradient>
    <path id="wave" d="M0,150 C120,118 250,118 370,138 C490,158 610,160 730,142 C850,124 930,128 1000,138 L1000,170 L0,170 Z" fill="#faf9f6" opacity="0.08"/>
    <path id="wave2" d="M0,160 C140,136 300,136 420,152 C540,168 680,168 810,154 C890,146 950,150 1000,156 L1000,170 L0,170 Z" fill="#e8d575" opacity="0.12"/>
  </defs>
  <rect width="1000" height="170" fill="url(#bg)"/>
  <use href="#wave"/>
  <use href="#wave2"/>
  <text x="500" y="86" text-anchor="middle" fill="#faf9f6" font-size="46" font-weight="700" letter-spacing="1">Soham Jadhav</text>
  <text x="500" y="124" text-anchor="middle" fill="#e8d575" font-size="18" font-weight="400" letter-spacing="4">CLEAR THINKING · CLEAN CODE · CALM EXECUTION</text>
</svg>"""

footer = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="90" viewBox="0 0 1000 90" role="img">
  <defs>
    <style>{font_faces}
      text {{ font-family: 'Albert Sans', 'Helvetica Neue', Arial, sans-serif; }}
    </style>
    <linearGradient id="fbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0e5232"/>
      <stop offset="100%" stop-color="#1a2b22"/>
    </linearGradient>
    <path id="fwave" d="M0,30 C120,62 250,62 370,42 C490,22 610,20 730,38 C850,56 930,52 1000,42 L1000,90 L0,90 Z" fill="#faf9f6" opacity="0.08"/>
    <path id="fwave2" d="M0,20 C140,44 300,44 420,28 C540,12 680,12 810,26 C890,34 950,30 1000,24 L1000,90 L0,90 Z" fill="#e8d575" opacity="0.12"/>
  </defs>
  <rect width="1000" height="90" fill="url(#fbg)"/>
  <use href="#fwave"/>
  <use href="#fwave2"/>
  <text x="500" y="72" text-anchor="middle" fill="#faf9f6" font-size="15" font-weight="400" letter-spacing="3">BUILT WITH CURIOSITY · PUNE, INDIA</text>
</svg>"""

out = pathlib.Path("/Users/sohamjadhav/sohamvjadhav/assets")
(out / "header.svg").write_text(header)
(out / "footer.svg").write_text(footer)
print("header.svg:", len(header), "bytes")
print("footer.svg:", len(footer), "bytes")
