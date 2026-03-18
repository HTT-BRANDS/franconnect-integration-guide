#!/usr/bin/env python3
import os, re

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'troubleshooting-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Replace the broken media query (only shifted .container) ──────────────
# with a page-shell approach that shifts ALL page content
html = html.replace(
    '@media(min-width:1100px){.md3-rail{display:flex}.container{margin-left:80px}.md3-fab{right:32px;bottom:32px}}',
    '@media(min-width:1100px){.md3-rail{display:flex}}'
)
# Also remove the duplicate FAB rule that was inside this media query
html = html.replace(
    '@media(min-width:1100px){.md3-rail{display:flex}.container{margin-left:0}}',
    '@media(min-width:1100px){.md3-rail{display:flex}}'
)

# ── 2. Add page-shell CSS + rail/layout fixes ────────────────────────────────
LAYOUT_CSS = """
/* ═══ Page Shell — offsets ALL content away from the fixed rail ═══ */
.page-shell { min-height: 100vh; transition: margin-left .25s; }
@media(min-width: 1100px) {
  .page-shell { margin-left: 80px; }
  .md3-fab   { right: 32px; bottom: 32px; }
}

/* ═══ Rail refinements ═══ */
.md3-rail {
  overflow: hidden;
  border-right: 1px solid var(--md-outline-variant);
}
.rail-item { padding: 8px 0 10px; }
.rail-indicator { width: 56px; height: 32px; }

/* ═══ Stepper — prevent connector line overflow ═══ */
.step:not(:last-child)::after {
  width: calc(100% - 40px);
  left: calc(50% + 20px);
  right: 0;
}

/* ═══ Container — full-width within shell ═══ */
@media(min-width: 1100px) {
  .container { max-width: 900px; }
}

/* ═══ Header + Stepper stay full-width of shell (no extra tweaks needed) ═══ */
.stepper-bar { width: 100%; }

/* ═══ Snackbar stays centered in viewport, not shell ═══ */
.md3-snackbar { left: calc(50% + 40px); }
@media(max-width: 1099px) { .md3-snackbar { left: 50%; } }

/* ═══ Mockup overflow guard ═══ */
.ui-mockup { overflow: hidden; }
.pa-app, .owa-app { overflow: hidden; }
.pa-sidebar { min-width: 0; }
.pa-sidebar-item { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* ═══ Expression table — prevent horizontal blowout ═══ */
.expr-table-wrap { max-width: 100%; }
.expr-cell { min-width: 0; }
.expr-cell code { min-width: 0; overflow-wrap: anywhere; }

/* ═══ Comparison grid — min-width guard ═══ */
.comp-panel__body { overflow-wrap: anywhere; word-break: break-all; }

/* ═══ Option card — consistent padding ═══ */
.option-card__hdr, .option-card__body, .option-card__cta { padding: 20px 24px; }

/* ═══ Pros/cons — icon alignment ═══ */
.pros li, .cons li { padding-left: 22px; }
.pros li::before, .cons li::before { width: 18px; line-height: 1.55; }

/* ═══ Code block — always scrollable ═══ */
.code-block { overflow-x: auto; }
.code-block pre { white-space: pre; word-break: normal; overflow-wrap: normal; }

/* ═══ Escalation avatar — use icon correctly ═══ */
.esc-avatar .material-symbols-outlined { font-size: 40px !important; color: white; }

/* ═══ Section heading spacing ═══ */
.section-heading { margin-top: 8px; }

/* ═══ Disclosure content — smooth open ═══ */
.disclosure-content { background: var(--md-surface-lowest); }

/* ═══ Table responsive ═══ */
.md3-table-wrap, .expr-table-wrap { border-radius: var(--shape-md); }
.md3-table td, .md3-table th { word-break: normal; }

/* ═══ Remove double border on featured option card ═══ */
.option-card.featured { box-shadow: var(--elev-2); }
"""
if 'Page Shell' not in html:
    html = html.replace('</style>', LAYOUT_CSS + '\n</style>', 1)

# ── 3. Wrap header + stepper + main in .page-shell ───────────────────────────
# Find the opening <body> tag and insert the shell open div after it
html = html.replace('<body>\n<header', '<body>\n<div class="page-shell">\n<header', 1)

# Close the shell before the nav rail (which must stay outside — it's fixed)
html = html.replace(
    '\n<!-- MD3 Navigation Rail -->',
    '\n</div><!-- /.page-shell -->\n<!-- MD3 Navigation Rail -->'
)

# ── 4. Fix the stepper connector line CSS (it uses left/right that conflict) ──
# The existing ::after uses left:50% right:-50% which causes overflow
# Replace with a cleaner version
html = html.replace(
    '.step:not(:last-child)::after{content:\'\';position:absolute;top:20px;left:50%;right:-50%;height:2px;background:var(--md-outline-variant);z-index:0}',
    '.step:not(:last-child)::after{content:\'\';position:absolute;top:20px;left:calc(50% + 20px);right:calc(-50% + 0px);height:2px;background:var(--md-outline-variant);z-index:0}'
)

# ── 5. Fix "All Done! 🎉" — replace emoji with a tasteful party icon ─────────
html = html.replace(
    '<div class="step__label">All Done! 🎉</div>',
    '<div class="step__label">All Done!</div>'
)

# ── 6. Fix the pa-sidebar width on small mockups ─────────────────────────────
# Reduce sidebar width so it doesn't crowd the content in narrow containers
html = html.replace(
    '.pa-sidebar{width:190px;background:#1b2a3b;flex-shrink:0}',
    '.pa-sidebar{width:160px;background:#1b2a3b;flex-shrink:0;min-width:0}'
)

# ── 7. Fix Outlook mockup sidebar width ──────────────────────────────────────
html = html.replace(
    '.owa-nav{width:170px;background:#0078d4;padding:8px 0;flex-shrink:0}',
    '.owa-nav{width:150px;background:#0078d4;padding:8px 0;flex-shrink:0;min-width:0}'
)

# ── 8. Ensure the HubSpot step min-width is responsive ───────────────────────
html = html.replace(
    '.hs-step{background:#fff;border:2px solid #e5e7eb;border-radius:var(--shape-md);padding:12px 20px;min-width:260px;text-align:center}',
    '.hs-step{background:#fff;border:2px solid #e5e7eb;border-radius:var(--shape-md);padding:12px 16px;min-width:0;width:100%;max-width:280px;text-align:center}'
)

# ── 9. Fix the stepper bar — it should span full width of shell ───────────────
# Make sure max-width on the inner .stepper doesn't cut things off
html = html.replace(
    '.stepper{display:flex;align-items:center;max-width:600px;width:100%}',
    '.stepper{display:flex;align-items:center;max-width:560px;width:100%;margin:0 auto}'
)

# ── 10. Verify ───────────────────────────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(path, 'r', encoding='utf-8') as f:
    result = f.read()

checks = {
    'page-shell div present':              'class="page-shell"' in result,
    'page-shell closed before rail':       '</div><!-- /.page-shell -->' in result,
    'page-shell margin media query':       '.page-shell { margin-left: 80px; }' in result,
    'No old container margin-left 80px':   '.container{margin-left:80px}' not in result,
    'Layout CSS injected':                 'Page Shell' in result,
    'All Done emoji removed':              'All Done! 🎉' not in result,
    'Mockup overflow hidden':              '.ui-mockup { overflow: hidden; }' in result,
    'Snackbar centered in viewport':       '.md3-snackbar { left: calc(50% + 40px); }' in result,
}

print('\n╔══ Layout Fix Verification ══╗')
all_pass = True
for name, passed in checks.items():
    status = '✓' if passed else '✗ FAIL'
    if not passed: all_pass = False
    print(f'  {status}  {name}')

lines = result.count('\n') + 1
print(f'\n  File: {lines} lines, {len(result)//1024}KB')
print('╚' + '═'*30 + '╝')
print('\nAll checks passed!' if all_pass else '\nSome checks FAILED — review above.')
