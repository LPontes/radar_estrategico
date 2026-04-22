# Animation Patterns — sa Slides

> All animation keyframes and timing patterns. The master easing curve is `cubic-bezier(0.16,1,0.3,1)`.

## Master Easing Curve

`cubic-bezier(0.16,1,0.3,1)` — snappy, modern bounce. Use for ALL entrance and transition animations.

## Corrente Elétrica de Borda (SVG Pattern — Premium)

> Efeito "Sábio Rebelde" definitivo: uma corrente elétrica que percorre o contorno das letras de um lado a outro, acompanhada de um preenchimento com gradiente animado.

```css
@keyframes border-run {
  from { stroke-dashoffset: 1000; }
  to { stroke-dashoffset: 0; }
}

@keyframes fill-shimmer {
  0% { stop-color: var(--color); stop-offset: 0%; }
  50% { stop-color: #fff; stop-offset: 50%; }
  100% { stop-color: var(--color); stop-offset: 100%; }
}

@keyframes electric-flicker-borda {
  0%, 100% { filter: drop-shadow(0 0 10px var(--color)) drop-shadow(0 0 20px var(--color)); opacity: 1; }
  50% { filter: drop-shadow(0 0 15px var(--color)) drop-shadow(0 0 35px var(--color)) brightness(1.6); opacity: 0.85; }
}

.electric-path {
  fill: none;
  stroke-width: 1.8;
  stroke-dasharray: 120 480; /* Faísca longa que percorre a palavra */
  stroke-linecap: round;
  animation: border-run 6s linear infinite, electric-flicker-borda 4s infinite;
}

.electric-path--accent { --color: var(--accent); stroke: var(--accent); }
.electric-path--brand  { --color: var(--brand);  stroke: var(--brand); }

/* Container para garantir alinhamento */
.electric-container { position: relative; display: inline-block; vertical-align: middle; }
```

### Exemplo de Uso (Título Completo):
```html
<div class="electric-container">
  <svg viewBox="0 0 800 120" style="width:100%; height:auto; overflow:visible;">
    <defs>
      <linearGradient id="electric-grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="var(--accent)">
          <animate attributeName="offset" values="-1; 2" dur="6s" repeatCount="indefinite" />
        </stop>
        <stop offset="0%" stop-color="#fff">
          <animate attributeName="offset" values="-0.5; 2.5" dur="6s" repeatCount="indefinite" />
        </stop>
        <stop offset="0%" stop-color="var(--accent)">
          <animate attributeName="offset" values="0; 3" dur="6s" repeatCount="indefinite" />
        </stop>
      </linearGradient>
    </defs>
    <!-- Camada 1: Preenchimento com Gradiente Animado -->
    <text x="50%" y="70%" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="80" 
          fill="url(#electric-grad)" style="opacity: 0.9;">INSIGHT</text>
    <!-- Camada 2: Corrente Elétrica de Borda -->
    <text x="50%" y="70%" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="80" 
          class="electric-path electric-path--accent">INSIGHT</text>
  </svg>
</div>
```

## Pulse Glow (Card/Node Emphasis — Infinite Loop)

```css
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 15px rgba(10,171,236,0.15), 0 0 30px rgba(10,171,236,0.05); }
  50% { box-shadow: 0 0 25px rgba(10,171,236,0.3), 0 0 50px rgba(10,171,236,0.1); }
}

@keyframes pulse-brand {
  0%, 100% { box-shadow: 0 0 15px rgba(255,153,0,0.15); }
  50% { box-shadow: 0 0 25px rgba(255,153,0,0.3); }
}
```

Usage: `animation: pulse-glow 4s ease-in-out infinite` on a highlighted card.

## Bar Fill (Progressive Reveal — One Shot)

```css
@keyframes bar-fill { from { width: 0; } }
/* Usage: animation: bar-fill 1.4s cubic-bezier(0.16,1,0.3,1) both; */
```

## Reveal Stagger (Entrance — Triggered by IntersectionObserver)

The `.reveal` class is the core entrance animation. Elements start invisible and slide up when the slide enters the viewport.

```css
.slide .reveal {
  opacity: 0; transform: translateY(24px);
  transition: opacity 0.5s cubic-bezier(0.16,1,0.3,1), transform 0.5s cubic-bezier(0.16,1,0.3,1);
}
.slide.visible .reveal { opacity: 1; transform: none; }
```

**Stagger delays:** Each nth-child gets +0.1s delay (0.1s, 0.2s, ... up to 1.0s for 10 children).

**Usage:** Add `class="reveal"` to each top-level content block in a slide. The first block appears at 0.1s, second at 0.2s, etc.

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  .slide, .slide .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
}
```
