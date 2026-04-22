import sys
import re

file_path = 'presentation/ra-01-slides.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: .slide css
# height: 100dvh; -> min-height: 100dvh;
# justify-content: center; -> justify-content: flex-start;
html = re.sub(r'(\.slide\s*\{[^}]*)height:\s*100dvh;', r'\1min-height: 100dvh;', html)
html = re.sub(r'(\.slide\s*\{[^}]*)justify-content:\s*center;', r'\1justify-content: flex-start;', html)
# Add some extra bottom padding just in case
html = re.sub(r'(\.slide\s*\{[^}]*)padding:\s*74px\s+clamp\([^)]+\)\s+40px;', r'\1padding: 74px clamp(40px, 6vw, 120px) 80px;', html)

# Fix 2: the wrappers
old_wrapper_style1 = 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: 0 auto; flex: 1; justify-content: center;"'
new_wrapper_style1 = 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: auto; flex: 0 1 auto; justify-content: center;"'

old_wrapper_style2 = 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: 0 auto; flex: 1; justify-content: center; "'
new_wrapper_style2 = 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: auto; flex: 0 1 auto; justify-content: center; "'

html = html.replace(old_wrapper_style1, new_wrapper_style1)
html = html.replace(old_wrapper_style2, new_wrapper_style2)


# Fix 3: Restore slide count format and ensure visibility
# JS replace
old_js_line = "if (this.counter) this.counter.textContent = (this.current + 1) + ' / ' + this.total;"
new_js_line = "if (this.counter) this.counter.textContent = String(this.current + 1).padStart(2, '0') + ' / ' + String(this.total).padStart(2, '0');"
html = html.replace(old_js_line, new_js_line)

# CSS replace for .deck-counter to make it prominent and definitely visible
old_css_counter = '.deck-counter { position: fixed; bottom: clamp(12px,2vh,24px); right: clamp(12px,2vw,24px); font-family: var(--font-mono); font-size: 12px; color: var(--text-dim); z-index: 100; }'
new_css_counter = '.deck-counter { position: fixed; bottom: clamp(20px,3vh,30px); right: clamp(20px,3vw,30px); font-family: var(--font-mono); font-size: 14px; font-weight: 600; color: var(--accent); z-index: 9999; }'
html = html.replace(old_css_counter, new_css_counter)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixes applied successfully.')
