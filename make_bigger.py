import re

file_path = 'presentation/ra-01-slides.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# --- SLIDE 3 FIXES ---
# We will use re.sub to target the specific clamp values in the Slide 3 section.
# First, let's extract slide 3 to avoid touching other slides
slide3_match = re.search(r'(<!-- SLIDE 3 — PHASE FLOW -->.*?</section>)', html, re.DOTALL)
if slide3_match:
    slide3 = slide3_match.group(1)
    # Box padding
    slide3 = slide3.replace('padding:clamp(18px,3vh,30px) clamp(12px,1.5vw,20px)', 'padding:clamp(28px,4vh,44px) clamp(20px,2vw,32px)')
    # Encontro font size
    slide3 = slide3.replace('font-size:clamp(1.05rem,1.5vw,1.25rem)', 'font-size:clamp(1.4rem,2.5vw,1.8rem)')
    # Description font size
    slide3 = slide3.replace('font-size:clamp(.75rem,.9vw,.85rem)', 'font-size:clamp(0.95rem,1.5vw,1.15rem)')
    # HOJE label font size
    slide3 = slide3.replace('font-size:.65rem', 'font-size:.85rem')
    # SVG Arrows
    slide3 = slide3.replace('width="24" height="24"', 'width="32" height="32"')
    
    html = html.replace(slide3_match.group(1), slide3)

# --- SLIDE 9 FIXES ---
slide9_match = re.search(r'(<!-- SLIDE 9 — FLOW ARCHITECTURE -->.*?</section>)', html, re.DOTALL)
if slide9_match:
    slide9 = slide9_match.group(1)
    
    # 1. Update viewBox to zoom in
    slide9 = slide9.replace('viewBox="0 0 1000 400"', 'viewBox="80 100 840 280"')
    # 2. Increase max-height of SVG
    slide9 = slide9.replace('max-height:clamp(300px,40vh,400px)', 'max-height:clamp(400px,55vh,550px); margin: 2rem 0')
    
    # 3. Increase fonts
    slide9 = slide9.replace('font-size="16"', 'font-size="20"')
    slide9 = slide9.replace('font-size="18"', 'font-size="24"')
    slide9 = slide9.replace('font-size="11"', 'font-size="14"')
    slide9 = slide9.replace('font-size="12"', 'font-size="15"')
    
    # Let's make the rect boxes a bit taller to fit the larger text
    # Original rects: height="80", y="160". If we make them 90, they will drop by 5px (y=155). 
    # But since it's an SVG, it's fine.
    slide9 = slide9.replace('height="80"', 'height="90"')
    slide9 = slide9.replace('height="70"', 'height="80"')
    slide9 = slide9.replace('y="160"', 'y="155"')
    slide9 = slide9.replace('y="300"', 'y="295"')

    html = html.replace(slide9_match.group(1), slide9)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Slides 3 and 9 updated successfully.')
