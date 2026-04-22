# Component Library — sa Slides

> Biblioteca de componentes CSS reutilizáveis da **Sprint Analítica**. Estes componentes formam a base do sistema visual "Sábio Rebelde".

---

## Tags (Color-Coded Badges)

O estilo padrão de tags: Fira Code mono, 0.68rem, cantos arredondados, fundo suave. Elegância e tecnicidade.

```css
.tag { font-family: var(--font-mono); font-size: 0.68rem; font-weight: 600; padding: 0.22rem 0.65rem; border-radius: 6px; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 0.3rem; }
.tag-accent { background: var(--accent-dim); color: var(--accent); } /* Electric Cyan */
.tag-brand  { background: var(--brand-dim);  color: var(--brand); }  /* Electric Orange */
.tag-gold   { background: var(--gold-dim);   color: var(--gold); }
.tag-green  { background: var(--green-dim);  color: var(--green); }
.tag-blue   { background: var(--blue-dim);   color: var(--blue); }
.tag-purple { background: var(--purple-dim); color: var(--purple); }
.tag-red    { background: var(--red-dim);    color: var(--red); }
```

**REGRAS:**
- NUNCA use `border` ou `box-shadow` em tags.
- NUNCA use outras fontes além de `var(--font-mono)` (Fira Code).
- NUNCA adicione estilos inline em tags (font-size, padding, etc).

## Stat Cards (3-column grid)

```css
.stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: clamp(10px,1.8vw,20px); margin-top: clamp(16px,3vh,32px); }
.stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; text-align: center; padding: clamp(18px,3vh,32px) clamp(12px,2vw,20px); position: relative; overflow: hidden; }
.stat-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: var(--accent); }
.stat-val { font-family: var(--font-display); font-size: clamp(36px,6vw,64px); font-weight: 800; line-height: 1; letter-spacing: -0.03em; }
.stat-lbl { font-family: var(--font-mono); font-size: clamp(9px,1.1vw,12px); color: var(--text-dim); margin-top: 0.4rem; text-transform: uppercase; letter-spacing: 1.5px; }
```

## Tier Cards (3-column comparison)

```css
.tier-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: clamp(16px,3vh,28px); }
.tier-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: clamp(20px,3vh,32px); position: relative; overflow: hidden; }
.tier-card h4 { font-family: var(--font-display); font-size: 1.5rem; font-weight: 600; margin-bottom: 0.3rem; }
.tier-card .tier-sub { font-family: var(--font-mono); font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.8rem; }
.tier-card p { font-size: 0.88rem; color: var(--text-dim); line-height: 1.5; }
```

## Glass Card (Destaque)

```css
.glass-card { 
  background: rgba(3, 6, 22, 0.6); 
  border: 1px solid var(--border-bright); 
  border-radius: 16px; 
  padding: clamp(24px, 4vh, 40px); 
  box-shadow: 0 8px 40px rgba(0,0,0,0.3); 
  backdrop-filter: blur(10px);
}
```

## Method Grid (2-column panels)

```css
.method-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(16px,2.5vw,32px); margin-top: clamp(16px,3vh,28px); }
.method-panel { background: var(--surface); border-radius: 16px; padding: clamp(20px,3vh,32px); border: 1px solid var(--border); }
.method-panel.panel-accent { border-color: rgba(10, 171, 236, 0.2); }
.method-panel.panel-brand  { border-color: rgba(255, 153, 0, 0.2); }
.method-panel h3 { font-family: var(--font-mono); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 1rem; color: var(--text-dim); }
```

## Bottom Explanation Panel (Voz do Sábio)

```html
<div class="bottom-panel mta">
  <p class="bottom-panel__label">Por que isso importa?</p>
  <p class="bottom-panel__text">Fundamentação técnica e contexto de negócio (PhD mindset)...</p>
</div>
```

```css
.bottom-panel { border-top: 1px solid var(--border); padding-top: clamp(12px, 1.8vh, 20px); }
.bottom-panel__label { font-family: var(--font-display); font-size: 1rem; font-weight: 600; font-style: italic; color: var(--accent); margin-bottom: 0.2rem; }
.bottom-panel__text { font-size: 0.82rem; color: var(--text-dim); line-height: 1.5; }
.mta { margin-top: auto; }
```

## Practical Example Box (Voz do Rebelde)

```html
<div style="margin-top:auto; padding-top:0.6rem;">
  <p style="font-family:var(--font-mono); font-size:0.55rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.3rem;">Na prática:</p>
  <div style="background:var(--brand-dim); border:1px solid rgba(255, 153, 0, 0.12); border-radius:8px; padding:0.5rem 0.6rem;">
    <p style="font-size:0.72rem; color:var(--text); line-height:1.45;">Aplicação direta no mercado / workflow.</p>
  </div>
</div>
```

## Code Block (Fira Code)

```css
.code-block { 
  background: var(--code-bg); border: 1px solid var(--border); border-radius: 10px; 
  padding: 0.75rem 1rem; font-family: var(--font-mono); font-size: 0.82rem; 
  line-height: 1.5; color: var(--code-text); overflow-x: auto;
}
.code-block .kw { color: var(--purple); }
.code-block .fn { color: var(--accent); }
.code-block .str { color: var(--green); }
.code-block .num { color: var(--brand); }
```
