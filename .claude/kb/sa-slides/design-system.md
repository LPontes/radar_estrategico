# Design System — Sprint Analítica™ (SA)
> Brand Identity for Lucas Pontes, PhD — Fluência Analítica. A fusion of academic rigor (PhD/USP) and market execution.

## Color Palette (CSS Custom Properties)

```css
:root {
  /* BACKGROUNDS — Deep Dark Space */
  --bg: #030616;              /* Dark Navy */
  --surface: #0a0e24;          /* Card backgrounds */
  --surface2: #121836;         /* Elevated surfaces */
  --surface-elevated: #1a234a; /* Highest elevation */

  /* BORDERS — Cyan/Orange tinted */
  --border: rgba(10, 171, 236, 0.08);
  --border-bright: rgba(10, 171, 236, 0.20);
  --border-action: rgba(255, 153, 0, 0.30);

  /* TEXT */
  --text: #f3f4f6;             /* Clean White (off-white) */
  --text-dim: #94a3b8;         /* Muted Slate / Secondary */

  /* PRIMARY ACCENTS */
  --accent: #0aabec;          /* Electric Cyan (Data/IA) */
  --accent-dim: rgba(10, 171, 236, 0.10);
  
  --brand: #ff9900;           /* Electric Orange (Action/Results) */
  --brand-dim: rgba(255, 153, 0, 0.10);

  /* SEMANTIC */
  --gold: #d4af37;
  --red: #ef4444;
  --green: #10b981;
  --purple: #8b5cf6;

  /* CODE */
  --code-bg: #010411;
  --code-text: #e2e8f0;
}
```

## Typography Stack

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,800;1,600;1,800&family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&display=swap" rel="stylesheet">
```

| Variable | Font | Role | Usage |
|----------|------|------|-------|
| `--font-display` | Montserrat | Headlines | Weights 600, 800. Bold and Authoritative. |
| `--font-body` | Inter | Body paragraphs | Weights 400, 500. Highly readable. |
| `--font-editorial` | Newsreader | Mentorship/Quotes | Italic for the "Sábio" (PhD) voice. |
| `--font-mono` | Fira Code | Data/Prompts | Technical execution. |

## Typography Scale

```css
.slide__display  { font-size: clamp(48px,10vw,120px); font-weight: 800; letter-spacing: -2px; line-height: 0.95; }
.slide__heading  { font-size: clamp(32px,6vw,64px); font-weight: 600; letter-spacing: -1px; }
.slide__body     { font-size: clamp(18px,2.4vw,24px); line-height: 1.6; }
.slide__label    { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--accent); }
```

## SA Branding Bar

```html
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
```

```css
.sa-bar {
  position: fixed; top: 0; left: 0; right: 0; height: 48px; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 clamp(20px,4vw,60px);
  background: rgba(3,6,22,0.9); border-bottom: 1px solid var(--border);
  font-family: var(--font-body); font-size: 0.7rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;
}
.sa-bar__left { color: var(--brand); display: flex; align-items: center; gap: 10px; }
.sa-bar__center { color: var(--text); font-weight: 500; opacity: 0.8; font-style: italic; font-family: var(--font-editorial); font-size: 0.9rem; text-transform: none; }
.sa-bar__right { color: var(--text-dim); }
```

## Visual Language

1.  **Gradients:** Use `Electric Cyan` to `Electric Orange` for "Transformation" flows. Use `Dark Navy` to `Surface` for backgrounds.
2.  **Sábio Rebelde Style:**
    *   **Sábio (Academic):** Use `Newsreader` (Editorial) for complex explanations and PhD quotes.
    *   **Rebelde (Market):** Use `Montserrat 800` and `Electric Orange` for hitting the "pain points" and "industry lies".
3.  **Background FX:** Radial gradients at corners to simulate depth.

```css
/* Background Gradient */
background-image: radial-gradient(circle at 0% 0%, rgba(10,171,236,0.05) 0%, transparent 40%),
                  radial-gradient(circle at 100% 100%, rgba(255,153,0,0.04) 0%, transparent 40%);
```

## Branding Assets

*   **Instructor Image:** `../../../images/lucas-pontes.png`
*   **Title Logic:** Short, punchy, "Survivor" based for front-end. "Ambition" based for back-end.

## Golden Rules for SA
- NEVER use generic icons. Use high-quality stroke icons.
- NEVER use blue/green combos. It's Navy/Cyan/Orange.
- ALWAYS use Portuguese accents correctly.
- ALWAYS maintain a tone of authority and speed.
