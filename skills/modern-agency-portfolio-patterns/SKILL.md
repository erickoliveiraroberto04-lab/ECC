---
name: modern-agency-portfolio-patterns
description: >-
  Use when building a portfolio, agency, or studio site that wants a modern,
  "premium AI-builder" feel — magnetic hover buttons, scroll-triggered fade-in
  sections, animated headline text, and a marquee logo/skill strip — without
  reaching for a full WebGL/Three.js setup. Covers the section structure and
  the handful of interaction primitives that carry the "3D-ish" feel most
  cheaply. Technique and stack choices are informed by inspecting a
  Lovable-generated portfolio template's package.json and file layout (no
  license file, so no source code from it is included); all code here is
  original.
---

# Modern Agency Portfolio Patterns

A lightweight recipe for the "modern agency portfolio" look that's common in
Lovable/Bolt/v0-generated sites: not actual 3D (no WebGL), but a handful of
motion primitives that read as premium — magnetic buttons, staged fade-ins,
animated text reveals, and a marquee strip.

## When to Use

- Building a portfolio, agency, or studio site and the brief says "modern",
  "premium", "3D feel", or references sites made with Lovable/Bolt/v0.
- Want scroll-triggered section reveals without a heavy animation library.
- Want a button/CTA that feels "alive" on hover (magnetic pull toward cursor).
- Want a looping logo/skill/client marquee strip.
- Stack is React + Tailwind — these patterns assume that, but the same ideas
  port to plain CSS/vanilla JS with minor changes.

## How It Works

### Typical section order

Hero → About → Services → Projects (grid) → Contact — each section is its
own component, wrapped in the same fade-in primitive so the whole page feels
consistent without hand-tuning each section's entrance separately.

### Recommended stack

React + Tailwind CSS + shadcn/ui (Radix primitives) for structure, plus
**Framer Motion** for the motion layer — this combination gets the "premium
AI-builder" feel without any 3D/WebGL library. Radix gives accessible
primitives (dialog, accordion, tooltip) for free; Framer Motion handles the
handful of interactions below.

### Primitive 1 — Scroll fade-in

Wrap any section content in a component that animates from `opacity:0,
translateY(24px)` to resting state once it enters the viewport, using
`whileInView` so it never gets stuck invisible if JS is slow (per general
artifact/animation hygiene: always render a visible resting state, animate
from it).

```tsx
import { motion } from "framer-motion";

export function FadeIn({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

### Primitive 2 — Magnetic button

A button/CTA that pulls slightly toward the cursor on hover, then snaps back
on leave — reads as tactile without any 3D engine.

```tsx
import { useRef, useState } from "react";
import { motion } from "framer-motion";

export function Magnet({ children, strength = 0.3 }: { children: React.ReactNode; strength?: number }) {
  const ref = useRef<HTMLDivElement>(null);
  const [pos, setPos] = useState({ x: 0, y: 0 });

  function handleMove(e: React.MouseEvent) {
    const el = ref.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) * strength;
    const y = (e.clientY - rect.top - rect.height / 2) * strength;
    setPos({ x, y });
  }

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMove}
      onMouseLeave={() => setPos({ x: 0, y: 0 })}
      animate={{ x: pos.x, y: pos.y }}
      transition={{ type: "spring", stiffness: 150, damping: 12 }}
    >
      {children}
    </motion.div>
  );
}
```

### Primitive 3 — Animated headline text

Split a headline into words/characters and stagger their entrance — cheaper
than a canvas-based text effect and reads as intentional.

```tsx
import { motion } from "framer-motion";

export function AnimatedText({ text }: { text: string }) {
  const words = text.split(" ");
  return (
    <span>
      {words.map((word, i) => (
        <motion.span
          key={i}
          initial={{ opacity: 0, y: "60%" }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: i * 0.06, ease: [0.22, 1, 0.36, 1] }}
          style={{ display: "inline-block", marginRight: "0.25em" }}
        >
          {word}
        </motion.span>
      ))}
    </span>
  );
}
```

### Primitive 4 — Marquee strip

A CSS-only looping strip (client logos, skills, tags) — no JS animation loop
needed, just a duplicated track and a keyframe translate.

```css
.marquee { overflow: hidden; white-space: nowrap; }
.marquee__track {
  display: inline-flex;
  gap: 3rem;
  animation: marquee 22s linear infinite;
}
@keyframes marquee {
  to { transform: translateX(-50%); }
}
```

Render the track's content twice back-to-back (duplicate the same list) so
the `-50%` translate loops seamlessly.

## Examples

- "Preciso de um portfólio que pareça premium mas não quero mexer com
  Three.js" → use FadeIn nas seções + Magnet nos CTAs + AnimatedText no
  headline. Zero WebGL, mesma sensação de "site feito com IA moderna".
- "Quero uma faixa de clientes/tecnologias passando" → Primitive 4 (marquee
  CSS puro, sem lib).
- "O botão de contato está sem graça" → envolve ele em `<Magnet>`.

## Anti-Patterns

- **Calling this "3D" to a client.** These are 2D motion effects — if a
  client specifically wants real 3D (rotating product models, WebGL scenes),
  this skill is not enough; that needs Three.js/React Three Fiber.
- **Skipping `viewport={{ once: true }}`.** Without it, `whileInView`
  re-triggers every time a section re-enters view on scroll-up, which reads
  as glitchy rather than polished.
- **Animating everything at once.** Stagger delays (as in the AnimatedText
  example) matter — simultaneous entrance of every element reads as a slide
  transition, not a crafted reveal.
- **No reduced-motion fallback.** Wrap motion values in a
  `prefers-reduced-motion` check or Framer Motion's `useReducedMotion` hook
  for accessibility.
