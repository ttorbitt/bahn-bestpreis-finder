---
name: Bahn-Bestpreis-Finder v2
description: Die Fahrkarte. Every connection is a ticket for the whole route; only the paid middle piece is printed.
colors:
  ground: "#e6ece7"
  thermal-ink: "#121514"
  card-white: "#f8faf7"
  ticket-mint: "#cfe9da"
  ticket-edge: "#a9cdb9"
  muted-stock: "#dbe3dd"
  faded-ink: "#4a5a52"
  validation-stamp: "#b00d4f"
  stamp-wash: "rgba(176,13,79,.10)"
  perforation: "#4a6558"
  hairline: "rgba(18,21,20,.16)"
  rule-strong: "rgba(18,21,20,.32)"
  void-red: "#b3122e"
  signal-green: "#17603c"
  signal-green-wash: "#d3ecdd"
  signal-amber: "#704800"
  signal-amber-wash: "#f6e2ae"
typography:
  display:
    fontFamily: "Barlow Semi Condensed, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(2.6rem, 12vw, 4.4rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "0"
  headline:
    fontFamily: "Barlow Semi Condensed, system-ui, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Barlow Semi Condensed, system-ui, sans-serif"
    fontSize: "1.4rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  body:
    fontFamily: "Barlow Semi Condensed, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.45
  label:
    fontFamily: "Barlow Semi Condensed, system-ui, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.06em"
  numeral:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.03em"
    fontFeature: "tnum"
  microprint:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.66rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.04em"
rounded:
  print: "2px"
  xs: "3px"
  stamp: "4px"
  ticket: "6px"
  punch: "50%"
spacing:
  hair: "4px"
  xs: "6px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  section: "22px"
components:
  button-primary:
    backgroundColor: "{colors.thermal-ink}"
    textColor: "{colors.card-white}"
    rounded: "{rounded.ticket}"
    padding: "0.6rem 1rem"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.thermal-ink}"
    rounded: "{rounded.ticket}"
    padding: "0.6rem 1rem"
  button-pressed:
    backgroundColor: "{colors.stamp-wash}"
    textColor: "{colors.validation-stamp}"
    rounded: "{rounded.ticket}"
  input:
    backgroundColor: "{colors.card-white}"
    textColor: "{colors.thermal-ink}"
    rounded: "{rounded.ticket}"
    padding: "0.7rem 0.8rem"
    typography: "{typography.body}"
  tab-active:
    backgroundColor: "{colors.thermal-ink}"
    textColor: "{colors.ground}"
    padding: "0.6rem 0.8rem"
  chip:
    backgroundColor: "{colors.card-white}"
    textColor: "{colors.thermal-ink}"
    rounded: "{rounded.ticket}"
    padding: "0.38rem 0.7rem"
  chip-selected:
    backgroundColor: "{colors.thermal-ink}"
    textColor: "{colors.ground}"
    rounded: "{rounded.ticket}"
  ticket-row:
    backgroundColor: "{colors.ticket-mint}"
    textColor: "{colors.thermal-ink}"
    rounded: "{rounded.ticket}"
    padding: "14px 14px 14px 12px"
  paid-piece:
    backgroundColor: "{colors.thermal-ink}"
    textColor: "{colors.ground}"
    rounded: "{rounded.xs}"
    height: "28px"
  torn-stub:
    backgroundColor: "{colors.muted-stock}"
    textColor: "{colors.perforation}"
    rounded: "{rounded.xs}"
    height: "28px"
  stamp:
    backgroundColor: "transparent"
    textColor: "{colors.validation-stamp}"
    rounded: "{rounded.stamp}"
    padding: "0.28rem 0.5rem 0.22rem"
---

# Design System: Bahn-Bestpreis-Finder v2

Scope: this file documents only the v2 world "Die Fahrkarte" (served at `/v2/`, styles in `v2.css` + `v2-fonts.css`, intro in `v2-intro.html`); v1 at the root keeps its older Romanesque kit and is not documented here.

## Overview

**Creative North Star: "Die Fahrkarte"**

Every result is a train ticket for the whole route, but only the piece the traveller actually buys is printed in black; the stretches before and after ride on the Deutschland-Ticket and are torn off at the perforation. The interface is ticket ephemera: cool mint card stock on a grey-green ground, black thermal ink, slate perforations, and exactly one magenta validation stamp that lands on the trick. It is a working tool, not a poster; density is high, type is condensed, and numbers read like a thermal printout.

Depth is printed, not lit. Edges come from hairlines, inset card-stock edges, dashed perforation rules and punched notches, never from soft ambient shadows. The guilloche security tint appears only on the paid piece, so the eye finds "what to buy" before anything else. The world refuses the category default of white cards, a blue accent and a price-first list, and it never borrows DB's red corporate identity.

Light and dark are both first-class: dark mode inverts to a near-black ground with dark-green stock and a brighter pink stamp; the ink/stub/stamp roles stay identical.

**Key Characteristics:**
- Mint ticket stock on a grey-green ground; black thermal ink for everything printed.
- The paid piece is the only solid-black, guilloche-tinted surface on a ticket.
- Torn D-Ticket stubs are paler, dashed in perforation slate, slightly displaced.
- One magenta stamp, reserved for the trick/recommendation, focus and selection.
- Hairlines, dashed perforations and punched notches instead of shadows.
- Condensed grotesk for words, tabular monospace for times and minutes.

## Colors

A cool, nearly monochrome ticket palette (green-grey neutrals plus black ink) with a single hot magenta stamp.

### Primary
- **Thermal Ink** (thermal-ink): the printing color. Text, primary buttons, active tabs and selected chips (ink fill, ground-colored text), the paid piece of every ticket, the sticky hour rule and card hairlines. In dark mode it inverts to #e6eee8.

### Secondary
- **Validation Stamp Magenta** (validation-stamp): the one accent. The "TRICK" stamp on the example ticket, the "Unser Tipp" recommendation badge, the focus ring (`--ring`), text selection, caret, pressed toggle buttons, punched selection circles, filter counts, the compare-bar action, and the brand train icon. Dark mode uses #ff4d92. Its pale wash (stamp-wash) backs pressed buttons and input focus halos.

### Neutral
- **Grey-Green Ground** (ground): page background; also the color punched through notches and the perforation half-circles.
- **Mint Ticket Stock** (ticket-mint): ticket rows, the search form blank and the example ticket parts. Dark: #1b2a23.
- **Stock Edge** (ticket-edge): 1–1.5px inset edge on ticket stock and the internal rule in the search form. Dark: #2d4438.
- **Card White** (card-white): inputs, chips, secondary buttons, help/price/alt panels, popovers. Dark: #151c19.
- **Muted Stock** (muted-stock): progress track, skeleton lines. Dark: #1f2924.
- **Faded Ink** (faded-ink): supporting text, labels, stub text, footer. Dark: #a2b3a9.
- **Perforation Slate** (perforation): dashed perforation rules, torn-stub outlines and text, link underlines, unchecked punch circles. Dark: #86a596.
- **Hairline / Strong Rule** (hairline, rule-strong): ink at 16% and 32% for dividers, field and chip outlines.

### Signals
- **Void Red** (void-red), **Signal Green** (signal-green, wash signal-green-wash), **Signal Amber** (signal-amber, wash signal-amber-wash): the risk traffic light only, shown as 8–9px dots and punctuality bars, never as fills on tickets.

### Named Rules
**The One Stamp Rule.** Magenta marks the trick, the recommendation, focus and selection, nothing else. One stamp lands per results view, on the pinned recommendation.

**The Printed Piece Rule.** Solid ink plus guilloche is reserved for the segment the user pays for. D-Ticket segments are never filled; they are pale stock with a dashed perforation outline.

## Typography

**Display Font:** Barlow Semi Condensed (self-hosted, weights 500–800; fallback system-ui, -apple-system, Segoe UI, Roboto, sans-serif)
**Body Font:** Barlow Semi Condensed 500
**Label/Mono Font:** JetBrains Mono 500 (fallback ui-monospace, SF Mono, Menlo, Consolas)

**Character:** A workhorse condensed grotesk, like the printed legends on a ticket, paired with a thermal-printer monospace for every time, minute and serial number.

### Hierarchy
- **Display** (800, clamp(2.6rem, 12vw, 4.4rem), 0.9, uppercase, max 12ch, balanced): the intro headline only.
- **Headline** (800, 1.5rem, 1.15): results heading (route).
- **Title** (800, 1.4rem, 1.2): section titles, brand line at 1.05rem.
- **Body** (500, 16px, 1.45): running text; lead at 1.02rem/1.5 capped at 46ch, explanatory text capped at 62ch.
- **Label** (700, 0.72rem, 0.06em, uppercase): form field legends, ticket field legends ("D-Ticket", "Nur kaufen"), filter group names, hour-chip headers.
- **Numeral** (JetBrains Mono 500, tabular figures): departure/arrival times at 1.25rem, hour headers at 1.05rem, timeline times, waits, counts.
- **Microprint** (JetBrains Mono 500, 0.66rem, 0.04em, uppercase content): the serial line under the example ticket.

### Named Rules
**The Thermal Numerals Rule.** Every clock time, duration and count is set in the mono with `font-variant-numeric: tabular-nums`; words never are.

**The Ticket Legend Rule.** Uppercase tracked labels are ticket field legends naming a field or a ticket part. They label content directly below or beside them; they never float above a heading as decoration.

## Layout

Mobile-first single column (max 660px, padding 18px 16px 64px, 22px gap between blocks, 16px base). At 980px and up the wrap grows to 1120px and splits into intro left (sticky at 24px) and the search form right (max 520px, 56px column gap); results, FAQ and footer then span the full grid but cap at 780px, left-aligned. At 480px and below, ticket actions move from a right-hand perforated stub to a bottom perforated strip, D-Ticket segments in the chain collapse to 10px slivers and the paid piece keeps its full label. Internal rhythm steps through 4, 6, 8, 12, 16, 22px. Results are grouped by hour under a sticky hour header ruled in ink; the recommendation is pinned on top. Touch targets are 44px (48px for fields) on coarse pointers.

## Elevation & Depth

Flat and printed. Depth comes from ink contrast (black paid piece on mint), inset 1–1.5px stock edges (`box-shadow: inset 0 0 0 1px` in ticket-edge), dashed perforation rules and masked punch-outs. Inputs get a 3px stamp-wash halo on focus. Nothing casts a soft shadow: the station suggestion popover is separated by its 1.5px ink border alone, and everything sits flat on the ground.

### Shadow Vocabulary
- **Stock edge** (`box-shadow: inset 0 0 0 1.5px var(--ticket-edge)`): ticket rows (1px on the search form and example parts).
- **Focus halo** (`box-shadow: 0 0 0 3px var(--stamp-soft)`): focused inputs, with a stamp-colored border.

### Named Rules
**The Hairline Rule.** Separate with lines, not light: 1px ink or ticket-edge for containers, 1.5px dashed perforation for tear lines, 1.5px solid ink for section heads.

## Shapes

Gently rounded ticket corners (6px) on cards, rows, fields, buttons and chips; 3px on chain segments, badges and small swatches; 2px on the printed "Nur kaufen" ink tag; 4px on the stamp. Full circles for the swap button, punch inputs and risk dots. Ticket rows carry 7px half-circle notches punched into both sides at mid-height (radial-gradient mask). The search form's action area sits below a dashed perforation with 18px ground-colored half-circles at both ends. Example-ticket stubs have a 9px-pitch row of punched holes on the edge facing the paid piece and are displaced (±3px, ±3deg) as if torn.

## Components

### Buttons
- **Shape:** ticket corners (6px), 1.5px border, 600 weight at 0.875rem.
- **Primary:** ink fill, card-white text (0.6rem 1rem; large 0.85rem 1.4rem for the search action).
- **Hover / Focus:** primary mixes 14% stamp into the ink on fine-pointer hover; outline/secondary darken their border to ink; ghost gets a 6% ink wash. Focus is a 2px stamp outline at 2px offset. Active nudges down 1px.
- **Secondary / Outline / Ghost:** card-white or transparent with a rule-strong border; ghost has none. Pressed toggles turn stamp: stamp-wash fill, stamp border and text.

### Chips
- **Style:** card-white, rule-strong 1.5px border, 0.8125rem/600.
- **State:** selected chips print solid ink with ground-colored text. Counts inside chips are faded ink.

### Cards / Containers
- **Corner Style:** 6px.
- **Background:** card-white with a 1px ink border for general cards; help, price and alternative panels use a rule-strong border.
- **Shadow Strategy:** none (see Elevation & Depth).
- **Internal Padding:** 16px; panels 11–14px.

### Inputs / Fields
- **Style:** card-white, 1.5px rule-strong border (1px inside the search blank), 6px, 1rem/500, uppercase field legend above.
- **Focus:** border turns stamp plus a 3px stamp-wash halo; hover darkens border to ink.
- **Error / Valid:** border void-red with a red hint line; valid fields take a green-tinted border.

### Navigation (segmented tabs)
- **Style:** inked 1.5px frame, ink dividers between tabs, card-white body; the active tab is printed solid ink with ground-colored text. Used for trip type, search mode and direction.

### Ticket Row (signature)
One connection as a mint ticket: punch circle to select (dashed slate at rest, stamp ring when checked), mono times, a route chain where the paid piece prints black with guilloche and D-Ticket stubs show as dashed slate slivers, a plain-text "Nur kaufen" line led by a small ink tag, and actions behind a dashed perforation on the right (bottom on mobile). Expanded detail reads like the ticket's back: a timeline with solid ink bars for paid legs and dashed slate bars for D-Ticket legs.

### Example Ticket and Stamp (signature)
Three parts on a 1 : 1.35 : 1 grid: two pale torn stubs and the printed paid piece, a microprint serial below, and the rotated (-9deg) "TRICK" stamp in the heaviest loaded weight (800) caps at 1.05rem with 0.1em tracking, 2.5px stamp border, multiply blend on light. On load the stubs tear outward (0.9s, cubic-bezier(.16,1,.3,1)) and the stamp lands from 1.9x scale; on results the recommendation's smaller stamp badge (-4deg) lands once. Reduced motion shows the torn end state without animation.

### Search Blank
The form is a mint ticket blank with a stock edge; the primary action sits on a stub below a dashed perforation with punched half-circles.

## Do's and Don'ts

### Do:
- **Do** print only the paid segment in solid ink with the guilloche tint; draw D-Ticket segments as pale stock with a 1.5px dashed perforation outline.
- **Do** set every time, duration and count in JetBrains Mono with tabular figures.
- **Do** separate with hairlines (1px ink or ticket-edge) and tear lines (1.5px dashed perforation slate).
- **Do** keep magenta for the trick/recommendation stamp, focus, selection and pressed state.
- **Do** keep both color schemes; the dark scheme swaps values, never roles.
- **Do** honour reduced motion by showing the torn/stamped end state statically.

### Don't:
- **Don't** use soft ambient shadows to lift cards; depth comes from ink, stock edges and punched notches.
- **Don't** add a second accent hue or use magenta as a generic link or button color.
- **Don't** fill D-Ticket segments with ink or tint, or put the guilloche anywhere except the paid piece.
- **Don't** fall back to the category default: white cards, a blue accent, a price-first list.
- **Don't** borrow DB branding (DB red, DB logo, DB corporate type).
- **Don't** let the stamp land more than once per view.
