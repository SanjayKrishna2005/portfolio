---
name: Silicon Monolith
colors:
  surface: '#f9f9fa'
  surface-dim: '#dadadb'
  surface-bright: '#f9f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeef'
  surface-container-high: '#e8e8e9'
  surface-container-highest: '#e2e2e3'
  on-surface: '#1a1c1d'
  on-surface-variant: '#45474b'
  inverse-surface: '#2f3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#76777b'
  outline-variant: '#c6c6cb'
  surface-tint: '#5b5e66'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#181c22'
  on-primary-container: '#80848c'
  inverse-primary: '#c3c6cf'
  secondary: '#4c5f7e'
  on-secondary: '#ffffff'
  secondary-container: '#c7dbff'
  on-secondary-container: '#4d607f'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#2b0052'
  on-tertiary-container: '#a75dfa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dfe2eb'
  primary-fixed-dim: '#c3c6cf'
  on-primary-fixed: '#181c22'
  on-primary-fixed-variant: '#43474e'
  secondary-fixed: '#d5e3ff'
  secondary-fixed-dim: '#b4c7eb'
  on-secondary-fixed: '#051c37'
  on-secondary-fixed-variant: '#344765'
  tertiary-fixed: '#efdbff'
  tertiary-fixed-dim: '#dbb8ff'
  on-tertiary-fixed: '#2b0052'
  on-tertiary-fixed-variant: '#6600b7'
  background: '#f9f9fa'
  on-background: '#1a1c1d'
  surface-variant: '#e2e2e3'
typography:
  display-xl:
    fontFamily: EB Garamond
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.03em
  display-xl-mobile:
    fontFamily: EB Garamond
    fontSize: 42px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Geist
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 30px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: 0em
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  code-inline:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
  label-nav:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.14em
  label-meta:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 3rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.75rem
  space-xl: 3rem
---

## Brand & Style

This design system embodies the disciplined, high-density intellectual craft of low-level electronics, computer architecture, and hardware engineering. The aesthetic sits at the intersection of brutalist engineering transparency and refined editorial documentation. It rejects superficial gloss in favor of structural clarity, typography-driven hierarchy, and subtle retro-computing artifacts.

The tone is understated, confident, and deeply technical. It communicates mastery of silicon, FPGA fabrication, RTL verification, and embedded physical computing. Key characteristics include:
- **Atmospheric Minimalist Canvas**: Vast expanses of clean light silver-gray canvas that feel like fresh thermal transfer paper or unblemished silicon wafer documentation.
- **Expressive Retro-Tech & Bitmapped Displays**: Dominant, monolithic section headers utilizing stylized serif or bitmapped typographic treatments juxtaposed with precision-tuned monospace metadata.
- **Structural Terminal Navigation**: Fixed micro-navigation with prompt cues (e.g. `> PROJECTS`), bracketed tags, and physical audio utility toggles.
- **Information Density Over Decoration**: Clean typography hierarchies, semantic inline links, dot separators, and restrained hairline framing.

## Colors

The palette is tuned for high legibility, low eye fatigue, and mechanical precision.

- **Primary (`#0D1117`)**: Dense obsidian-charcoal ink, inspired by deep terminal shells and IC packaging substrate. Used for dominant headings, pixel display banners, and primary text.
- **Secondary (`#3A4D6B`)**: Slate phosphor blue. Serves as interactive hover states, active navigation pointers (`>`), metadata delimiters, and hardware specification tags.
- **Tertiary (`#7928CA`)**: Silicon violet. Reserved for subtle micro-accents, chip pin indicators, and highlighted publication accolades.
- **Neutral Surface (`#F4F4F5`)**: High-spec industrial off-white / light silver-gray paper tone. Provides an uncluttered backdrop without the glare of `#FFFFFF`.
- **Muted Canvas Secondary (`#EAECEF`)**: Subtle background tint used for embedded music widgets, code tag chips, and quote sidebars.
- **Border / Divider Tone (`#D0D7DE`)**: Ghost-hairline contrast for structural rules, audio playback tracking rails, and subtle chip boundary lines.

## Typography

Typography establishes the bridge between raw bitstream mechanics and academic rigor:

- **Section Titles & Hero Display (`EB Garamond` / Bitmapped Aesthetic)**: Large section displays emulate bitmapped glyph rendering or high-contrast classical serifs rendered through a CRT phosphor grid. Use bold weights with tight tracking. On displays supporting SVG pixel-rendering filters, titles render with authentic 1-bit or 8-bit stepped pixel masks.
- **Body & Prose (`Geist`)**: Neutral, ultra-sharp grotesque designed for screen legibility. Ensures dense hardware architecture descriptions, papers, and personal statements remain effortless to read.
- **Labels, Metadata & Nav (`JetBrains Mono`)**: Strict, monospaced tabular presentation for top navigation, chip pinouts, FPGA specs, timeline dates, and bracketed links (`[github]`, `[paper]`, `[writeup]`).
- **Punctuation & Syntax**: Monospace prompts (`>`) prefix active links and sub-headers to mirror interactive CLI debuggers.

## Layout & Spacing

The layout is grounded in a restrained, document-style fluid grid with strict vertical cadence:

- **Viewport Constraints**: Content is pinned within a maximum content boundary of `1100px` for optimal body line lengths (`65-75` characters per line) and generous negative margins.
- **Navigation Bar**: Spans full viewport width with flush edge-to-edge padding (`margin` left and right). Navigation items utilize split-justification (left groupings for primary sections, right groupings for external presence and contact).
- **Rhythm & Stacking**: Vertical spacing operates on an 8px base rhythm. Project units are separated by `space-xl`, allowing multi-line specifications to breathe without requiring box containers.
- **Breakpoints**:
  - `Desktop (> 1024px)`: Multi-column splits for hero narratives and portrait headshots; persistent bottom-left audio controller.
  - `Tablet (768px - 1023px)`: Fluid single-column layout with preserved 24px margins.
  - `Mobile (< 768px)`: Navigation collapses into a horizontal scrollable strip with monospace items; display headings drop to mobile scale; margin shrinks to `1.25rem`.

## Elevation & Depth

This design system rejects heavy drop shadows, blur washes, and skeuomorphic plastic layers. Visual depth is established through **architectural stratification**:

- **Planar Baseline (Level 0)**: The base `#F4F4F5` canvas represents the physical substrate.
- **Recessed / Hairline Containment (Level 1)**: Micro-components like the retro audio mini-dock use crisp 1px borders (`#D0D7DE`) with background fill `#EAECEF`, signaling a physical hardware chassis mounted to the viewport.
- **Micro Overlays**: Tooltips, terminal prompt chips, and modal diagrams use solid monochrome boundaries (`1px solid #0D1117`) accompanied by a crisp, zero-blur 2px offset shadow (`box-shadow: 2px 2px 0px #0D1117`).
- **Focus & Selection**: Highlights use high-contrast inverse blocks (`#0D1117` background with `#F4F4F5` text) rather than glowing halos.

## Shapes

The geometric approach reflects precision machining and semiconductor dice:

- **Strict Orthogonal Corners**: Container panels, navigation rails, and interactive buttons feature crisp `0px` to `4px` maximum radius, maintaining a technical, blueprint-like silhouette.
- **Selective Soft Radius (Roundedness 1)**: Badges, author avatar portraits, and audio player docks utilize subtle `4px` corner rounding (`0.25rem`), mitigating harshness while preserving the industrial electronic feel.
- **Pill Exceptions**: Reserved strictly for the single live status indicator dot (e.g. `● online / searching for chips`) and hardware toggle slider knobs.

## Components

### 1. Navigation Bar
- Monospace uppercase links (`12px`, letter spacing `0.14em`).
- Active link marked with a monospace prompt: `> PROJECTS`.
- Hover behavior: Subtle underline offset (`text-underline-offset: 4px`) or instant bracket enclosure (`[ BLOG ]`).

### 2. Project List Item
- **Title**: Bold grotesque (`headline-sm`, `18px`), `#0D1117`.
- **Specs / Architecture Metadata**: Monospace string separated by middle dots (`·`) in `#3A4D6B` (e.g., `8 custom ASICs on Tiny Tapeout 8 · SKY130B 130nm · beamforming`).
- **Actions**: Plain text, persistent underline links (`github`, `writeup`, `paper`) with 1px border underline that darkens on hover. No button containers; purely editorial and fast.

### 3. Retro Mini Audio Controller
- Fixed to bottom-left corner of the viewport.
- Bordered in `1px solid #D0D7DE` on `#EAECEF` substrate.
- Contains an invert-state play/pause button (`#0D1117` square), monophonic track info (`JetBrains Mono`, `11px`), and a minimal linear tracking bar with a square thumb.

### 4. Interactive Callout & Pull Quotes
- Left border accent: `3px solid #D0D7DE`.
- Subtle left indentation with leading prompt indicator: `>`.
- Internal text uses `body-lg` italic or regular weight with bold keyword accents.

### 5. Chips & Architecture Badges
- Compact inline tag style: `JetBrains Mono`, `11px`, uppercase.
- Light gray fill (`#EAECEF`), `1px solid #D0D7DE`, `2px 6px` padding, `2px` border radius.

### 6. Inputs & Terminal Command Inputs
- Transparent background with solid bottom border (`1px solid #0D1117`) or full hairline box.
- Caret styled as a blinking block (`▋`).
- Monospace placeholder text in `#768390`.