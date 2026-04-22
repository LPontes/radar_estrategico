# Template — sa Slides

> The complete HTML skeleton for starting a new slide deck. Copy this and fill in the slides.

## Full Template

Replace `{{LESSON_CODE}}`, `{{LESSON_TITLE}}`, `{{LESSON_SUBTITLE}}`, `{{MODULE_NUM}}`, `{{MODULE_NAME}}`, `{{DURATION}}` with actual values.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{LESSON_CODE}} — {{LESSON_TITLE}}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,800;1,600;1,800&family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&display=swap" rel="stylesheet">
<style>
  /* Paste full CSS from design-system.md + component-library.md + animation-patterns.md */
</style>
</head>
<body>

<!-- sa BRANDING BAR -->
<div class="sa-bar">
  <div class="sa-bar__left">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
    SPRINT ANALÍTICA™
  </div>
  <div class="sa-bar__center">Lucas Pontes, PhD — Fluência Analítica</div>
  <div class="sa-bar__right">
    DOC. MASTER V6 &middot; 2026
  </div>
</div>

<!-- NAV CHROME -->
<div class="deck-progress" id="progress"></div>
<nav class="deck-dots" id="dots"></nav>
<div class="deck-counter" id="counter"></div>
<div class="deck-hints" id="hints">&larr; &rarr; ou scroll</div>

<div class="deck" id="deck">

<!-- SLIDE 1 — TITLE -->
<section class="slide slide--title">
  <svg class="slide__decor" style="top:0;left:0;" width="200" height="200" viewBox="0 0 200 200">
    <line x1="0" y1="0" x2="0" y2="60" stroke="var(--accent)" stroke-width="2" opacity="0.15"/>
    <line x1="0" y1="0" x2="60" y2="0" stroke="var(--accent)" stroke-width="2" opacity="0.15"/>
  </svg>
  <svg class="slide__decor" style="bottom:0;right:0;" width="200" height="200" viewBox="0 0 200 200">
    <line x1="200" y1="140" x2="200" y2="200" stroke="var(--gold)" stroke-width="2" opacity="0.15"/>
    <line x1="140" y1="200" x2="200" y2="200" stroke="var(--gold)" stroke-width="2" opacity="0.15"/>
  </svg>
  <div class="reveal">
    <p class="slide__subtitle" style="margin-bottom:clamp(4px,1vh,8px); letter-spacing:3px; font-size:0.72rem;">MÓDULO {{MODULE_NUM}} &mdash; {{MODULE_NAME}}</p>
  </div>
  <div class="reveal" style="margin-bottom:clamp(8px,1.5vh,16px);">
    <span class="tag tag-accent" style="font-size:0.82rem; padding:0.4rem 1.2rem; border-radius:100px;">{{LESSON_CODE}}</span>
    <span class="tag tag-gold" style="font-size:0.72rem; padding:0.3rem 0.8rem; border-radius:100px; margin-left:0.5rem;">{{DURATION}}</span>
  </div>
  <h1 class="slide__display reveal" style="font-size:clamp(40px,8vw,100px);">{{LESSON_TITLE_LINE1}}<br><span class="electric-text">{{LESSON_TITLE_LINE2}}</span></h1>
  <div class="reveal" style="margin-top:clamp(12px,2vh,20px);">
    <p style="font-family:var(--font-editorial); font-size:clamp(20px,3vw,34px); font-style:italic; color:var(--text-dim);">{{LESSON_SUBTITLE}}</p>
  </div>
  <div class="reveal" style="margin-top:clamp(20px,3vh,32px); display:flex; align-items:center; justify-content:center; gap:clamp(12px,2vw,20px);">
    <div style="width:clamp(56px,7vw,80px); height:clamp(56px,7vw,80px); border-radius:50%; overflow:hidden; border:2px solid var(--accent); flex-shrink:0;">
      <img src="../../../images/lucas-pontes.png" alt="Lucas Pontes" style="width:100%; height:100%; object-fit:cover; object-position:center -5%; transform:scale(1.3);">
    </div>
    <div style="text-align:left;">
      <p style="font-family:var(--font-display); font-size:1.2rem; font-weight:600;"><span style="color:var(--text-dim);">Instrutor:</span> <span style="color:var(--accent);">Lucas Pontes, PhD</span></p>
      <p style="font-family:var(--font-editorial); font-size:0.9rem; font-style:italic; color:var(--text-dim); margin-top:0.1rem;">Sábio Rebelde &middot; Fluência Analítica</p>
    </div>
  </div>
  <div class="reveal" style="margin-top:clamp(12px,2vh,20px); display:flex; gap:0.75rem; justify-content:center; flex-wrap:wrap;">
    <span class="tag tag-accent">Radar Estratégico™</span>
    <span class="tag tag-brand">Sábio Rebelde</span>
    <span class="tag tag-gold">Sprint Analítica</span>
  </div>
</section>

<!-- ADD CONTENT SLIDES HERE -->
<!-- Use slide types from slide-types.md -->
<!-- Use components from component-library.md -->
<!-- Follow rules from quality-rules.md -->

<!-- CLOSING SLIDE -->
<section class="slide slide--quote">
  <div class="reveal"><div class="slide__quote-mark" style="color:var(--brand);">&ldquo;</div></div>
  <div class="reveal">
    <blockquote>{{CLOSING_QUOTE}}</blockquote>
  </div>
  <div class="reveal" style="margin-top:clamp(20px,3vh,32px); display:flex; gap:0.75rem; justify-content:center;">
    <span class="tag tag-accent" style="font-size:0.82rem; padding:0.4rem 1.2rem; border-radius:100px;">Próximo: {{NEXT_LESSON}}</span>
  </div>
  <div class="reveal" style="margin-top:clamp(24px,4vh,36px);">
    <p style="font-family:var(--font-mono); font-size:0.68rem; color:var(--text-dim); letter-spacing:0.15em;">RADAR ESTRATÉGICO™ · SPRINT ANALÍTICA · LUCAS PONTES, PhD · 2026</p>
  </div>
</section>

</div><!-- /deck -->

<script>
/* Paste SlideEngine from slide-engine.md */
</script>
</body>
</html>
```

## Checklist Before Generating

Before writing any HTML, verify:

- [ ] Read `quality-rules.md` — especially screen filling and accent rules
- [ ] Read the Lesson Map/Roteiro
- [ ] Map every content item to a slide type (from `slide-types.md`)
- [ ] Plan 15-20 slides minimum for a 90-120 min lesson
- [ ] Every content slide has a bottom explanation panel (Sábio voice)
- [ ] Every card has a practical example (Rebelde voice)
- [ ] All Portuguese text uses proper accents
