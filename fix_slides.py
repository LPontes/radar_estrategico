import sys
import re

file_path = 'presentation/ra-01-slides.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# [E1] Deprecated Layout Classes Used
html = html.replace('class="content-center-wrap"', 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: 0 auto; flex: 1; justify-content: center;"')
html = html.replace('class="content-center-wrap ', 'style="display: flex; flex-direction: column; gap: 2rem; width: 100%; max-width: 1400px; margin: 0 auto; flex: 1; justify-content: center;" class="')

html = html.replace('class="bottom-panel mta reveal"', 'class="reveal" style="border-top: 1px solid var(--border); padding-top: clamp(12px, 1.8vh, 20px); margin-top: auto;"')
html = html.replace('class="bottom-panel__label"', 'style="font-family: var(--font-display); font-size: 1rem; font-weight: 600; font-style: italic; color: var(--accent); margin-bottom: 0.2rem;"')
html = html.replace('class="bottom-panel__text"', 'style="font-family: var(--font-editorial); font-style: italic; font-size: 0.82rem; color: var(--text-dim); line-height: 1.5;"')

# remove css definitions
html = re.sub(r'\.content-center-wrap \{[^}]+\}\n?', '', html)
html = re.sub(r'\.bottom-panel \{[^}]+\}\n?', '', html)
html = re.sub(r'\.bottom-panel__label \{[^}]+\}\n?', '', html)
html = re.sub(r'\.bottom-panel__text \{[^}]+\}\n?', '', html)
html = re.sub(r'\.mta \{[^}]+\}\n?', '', html)

# [E2] Inline Style Overrides on Tags
html = html.replace('style="font-size:0.82rem; padding:0.4rem 1.2rem; border-radius:100px;"', '')
html = html.replace('style="font-size:0.72rem; padding:0.3rem 0.8rem; border-radius:100px; margin-left:0.5rem;"', 'style="margin-left:0.5rem;"')

# [W1] Slide Level
html = html.replace('height: 100vh;', 'height: 100dvh;')

# [W2] Slide 16: Plain text arrows
svg_arrow_accent = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
svg_arrow_brand = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--brand)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
svg_arrow_dim = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'

html = html.replace('<div style="font-size:clamp(18px,2.5vw,26px);color:var(--accent);flex-shrink:0">→</div>', f'<div style="flex-shrink:0">{svg_arrow_accent}</div>')
html = html.replace('<div style="font-size:clamp(18px,2.5vw,26px);color:var(--brand);flex-shrink:0">→</div>', f'<div style="flex-shrink:0">{svg_arrow_brand}</div>')
html = html.replace('<div style="font-size:clamp(18px,2.5vw,26px);color:var(--text-dim);flex-shrink:0">→</div>', f'<div style="color:var(--text-dim);flex-shrink:0">{svg_arrow_dim}</div>')

# [W3] Glass and stat cards hover
html = html.replace('class="glass-card"', 'class="glass-card" style="transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 40px rgba(10,171,236,0.2)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'0 8px 40px rgba(0,0,0,0.3)\'"')
# Fix duplicate replacements on "glass-card reveal"
html = html.replace('class="glass-card" style="transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 40px rgba(10,171,236,0.2)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'0 8px 40px rgba(0,0,0,0.3)\'" reveal"', 'class="glass-card reveal" style="transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 40px rgba(10,171,236,0.2)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'0 8px 40px rgba(0,0,0,0.3)\'"')

# Stat cards
html = html.replace('<div style="background: rgba(10,171,236,0.05); border: 1px solid rgba(10,171,236,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative;">', '<div style="background: rgba(10,171,236,0.05); border: 1px solid rgba(10,171,236,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative; transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 30px rgba(10,171,236,0.15)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'none\'">')
html = html.replace('<div style="background: rgba(255,153,0,0.05); border: 1px solid rgba(255,153,0,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative;">', '<div style="background: rgba(255,153,0,0.05); border: 1px solid rgba(255,153,0,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative; transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 30px rgba(255,153,0,0.15)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'none\'">')
html = html.replace('<div style="background: rgba(212,175,55,0.05); border: 1px solid rgba(212,175,55,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative;">', '<div style="background: rgba(212,175,55,0.05); border: 1px solid rgba(212,175,55,0.2); border-radius: 16px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; position: relative; transition: all 0.3s;" onmouseenter="this.style.transform=\'translateY(-5px)\';this.style.boxShadow=\'0 12px 30px rgba(212,175,55,0.15)\'" onmouseleave="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'none\'">')

# [E3] SlideEngine JS
slide_engine_js = """class SlideEngine {
  constructor() {
    this.deck = document.getElementById('deck');
    this.slides = [...document.querySelectorAll('.slide')];
    this.dots = document.getElementById('dots');
    this.progress = document.getElementById('progress');
    this.counter = document.getElementById('counter');
    this.hints = document.getElementById('hints');
    this.total = this.slides.length;
    this.current = 0;

    // Create dot buttons
    this.slides.forEach((_, i) => {
      const d = document.createElement('button');
      d.className = 'deck-dot';
      d.setAttribute('aria-label', 'Ir para slide ' + (i + 1));
      d.addEventListener('click', () => this.goTo(i));
      this.dots.appendChild(d);
    });

    // Visibility observer — triggers reveal animations
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          this.current = this.slides.indexOf(e.target);
          this.updateChrome();
        }
      });
    }, { root: this.deck, threshold: 0.5 });
    this.slides.forEach(s => obs.observe(s));

    // Keyboard navigation
    document.addEventListener('keydown', e => {
      if (['ArrowDown','ArrowRight','Space','PageDown'].includes(e.code)) { e.preventDefault(); this.next(); }
      if (['ArrowUp','ArrowLeft','PageUp'].includes(e.code)) { e.preventDefault(); this.prev(); }
      if (e.code === 'Home') { e.preventDefault(); this.goTo(0); }
      if (e.code === 'End') { e.preventDefault(); this.goTo(this.total - 1); }
    });

    // Touch navigation (50px swipe threshold)
    let touchY = 0;
    this.deck.addEventListener('touchstart', e => { touchY = e.touches[0].clientY; }, { passive: true });
    this.deck.addEventListener('touchend', e => {
      const dy = touchY - e.changedTouches[0].clientY;
      if (Math.abs(dy) > 50) dy > 0 ? this.next() : this.prev();
    }, { passive: true });

    // Auto-fade hints after 4s
    if (this.hints) {
        setTimeout(() => this.hints.classList.add('faded'), 4000);
    }
    this.updateChrome();
    if (this.slides[0]) this.slides[0].classList.add('visible');
  }

  goTo(i) { this.slides[i]?.scrollIntoView({ behavior: 'smooth' }); }
  next() { this.goTo(Math.min(this.current + 1, this.total - 1)); }
  prev() { this.goTo(Math.max(this.current - 1, 0)); }

  updateChrome() {
    const pct = ((this.current + 1) / this.total) * 100;
    if (this.progress) this.progress.style.width = pct + '%';
    if (this.counter) this.counter.textContent = (this.current + 1) + ' / ' + this.total;
    if (this.dots) [...this.dots.children].forEach((d, i) => d.classList.toggle('active', i === this.current));
  }
}
new SlideEngine();"""

script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
html = script_pattern.sub(f'<script>\n{slide_engine_js}\n</script>', html)

# Fix CSS for deck-dots since we removed the old js but we also need to ensure the CSS is updated.
css_additions = """
    /* Navigation Chrome CSS */
    .deck-progress { position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, var(--accent), var(--brand)); z-index: 100; transition: width 0.3s ease; pointer-events: none; }
    .deck-dots { position: fixed; right: clamp(12px,2vw,24px); top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 7px; z-index: 100; padding: 7px; background: rgba(10,15,26,0.6); border-radius: 20px; backdrop-filter: blur(8px); }
    .deck-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--text-dim); opacity: 0.3; border: none; padding: 0; cursor: pointer; transition: all 0.2s; }
    .deck-dot:hover { opacity: 0.6; }
    .deck-dot.active { opacity: 1; transform: scale(1.5); background: var(--accent); box-shadow: 0 0 8px rgba(0,180,255,0.4); }
    .deck-counter { position: fixed; bottom: clamp(12px,2vh,24px); right: clamp(12px,2vw,24px); font-family: var(--font-mono); font-size: 12px; color: var(--text-dim); z-index: 100; }
    .deck-hints { position: fixed; bottom: clamp(12px,2vh,24px); left: 50%; transform: translateX(-50%); font-family: var(--font-mono); font-size: 11px; color: var(--text-dim); opacity: 0.5; z-index: 100; transition: opacity 0.5s; }
    .deck-hints.faded { opacity: 0; pointer-events: none; }
"""

# Insert CSS right before </style>
html = html.replace('</style>', f'{css_additions}\n  </style>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
