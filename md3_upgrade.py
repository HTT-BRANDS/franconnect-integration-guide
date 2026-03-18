#!/usr/bin/env python3
import re, os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'troubleshooting-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Add Material Symbols font to <head> ──────────────────────────────────
SYMBOLS = '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">'
html = html.replace(
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n' + SYMBOLS,
    1
)

# ── 2. Inject new CSS before </style> ───────────────────────────────────────
NEW_CSS = """
/* ═══ MD3 Material Symbols ═══ */
.material-symbols-outlined{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;font-size:24px;line-height:1;display:inline-flex;align-items:center;justify-content:center;user-select:none;flex-shrink:0}
.icon-xs{font-size:16px!important}.icon-sm{font-size:18px!important}.icon-lg{font-size:32px!important}.icon-xl{font-size:40px!important}
.icon-filled{font-variation-settings:'FILL' 1,'wght' 400,'GRAD' 0,'opsz' 24}
.icon-w300{font-variation-settings:'FILL' 0,'wght' 300,'GRAD' 0,'opsz' 24}

/* ═══ MD3 State Layers ═══ */
.md3-btn,.expand-btn,.ba-tab,.disclosure-btn,.rail-item,.expr-copy,.copy-btn{position:relative;overflow:hidden}
.md3-btn::after,.expand-btn::after,.ba-tab::after,.disclosure-btn::after,.rail-item::after,.expr-copy::after,.copy-btn::after{content:'';position:absolute;inset:0;border-radius:inherit;background:currentColor;opacity:0;transition:opacity .15s;pointer-events:none}
.md3-btn:hover::after,.expand-btn:hover::after,.ba-tab:hover::after,.disclosure-btn:hover::after,.rail-item:hover::after,.expr-copy:hover::after,.copy-btn:hover::after{opacity:.08}
.md3-btn:focus-visible::after,.expand-btn:focus-visible::after,.ba-tab:focus-visible::after,.disclosure-btn:focus-visible::after,.rail-item:focus-visible::after{opacity:.12}
.md3-btn:active::after,.expand-btn:active::after,.ba-tab:active::after,.expr-copy:active::after,.copy-btn:active::after{opacity:.16}

/* ═══ MD3 Button System ═══ */
.md3-btn{display:inline-flex;align-items:center;gap:8px;border-radius:var(--shape-full);font:500 14px/1 var(--font);cursor:pointer;border:none;text-decoration:none;white-space:nowrap;transition:box-shadow .2s;padding:10px 24px;letter-spacing:.01em}
.md3-btn .material-symbols-outlined{font-size:18px!important}
.md3-btn--filled{background:var(--md-primary);color:var(--md-on-primary)}
.md3-btn--filled:hover{box-shadow:var(--elev-1)}
.md3-btn--tonal{background:var(--md-secondary-container);color:var(--md-on-secondary-container)}
.md3-btn--tonal:hover{box-shadow:var(--elev-1)}
.md3-btn--outlined{background:transparent;color:var(--md-primary);border:1px solid var(--md-outline)}
.md3-btn--text{background:transparent;color:var(--md-primary);padding:10px 12px}
.md3-btn--elevated{background:var(--md-surface-lowest);color:var(--md-primary);box-shadow:var(--elev-1)}
.md3-btn--elevated:hover{box-shadow:var(--elev-2)}
.md3-btn--icon{padding:8px;border-radius:var(--shape-full);background:none;color:var(--md-on-surface-variant)}
.md3-btn--icon .material-symbols-outlined{font-size:24px!important}

/* ═══ MD3 FAB (Extended) ═══ */
.md3-fab{position:fixed;bottom:24px;right:24px;z-index:200;background:var(--md-primary-container);color:var(--md-on-primary-container);border:none;border-radius:var(--shape-lg);padding:16px 20px;display:flex;align-items:center;gap:12px;font:500 14px/1 var(--font);cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.3),0 4px 8px 3px rgba(0,0,0,.15);transition:box-shadow .2s,transform .15s;text-decoration:none;letter-spacing:.01em}
.md3-fab:hover{box-shadow:0 2px 6px rgba(0,0,0,.3),0 6px 16px 3px rgba(0,0,0,.15);transform:translateY(-2px)}
.md3-fab .material-symbols-outlined{font-size:24px!important}
@media(max-width:640px){.md3-fab span:last-child{display:none}.md3-fab{padding:16px;border-radius:var(--shape-full)}}

/* ═══ MD3 Snackbar ═══ */
.md3-snackbar{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(140px);background:var(--md-inverse-surface);color:var(--md-inverse-on-surface);padding:14px 16px 14px 12px;border-radius:var(--shape-xs);font:400 14px/1.4 var(--font);display:flex;align-items:center;gap:8px;box-shadow:0 3px 5px rgba(0,0,0,.2),0 6px 10px rgba(0,0,0,.14);transition:transform .3s cubic-bezier(.05,.7,.1,1);z-index:300;pointer-events:none;min-width:200px;max-width:420px;white-space:nowrap}
.md3-snackbar.is-visible{transform:translateX(-50%) translateY(0);pointer-events:auto}
.md3-snackbar .material-symbols-outlined{color:var(--md-inverse-primary);font-size:18px!important;flex-shrink:0}

/* ═══ MD3 Navigation Rail ═══ */
.md3-rail{display:none;position:fixed;left:0;top:0;bottom:0;width:80px;background:var(--md-surface-container);z-index:90;flex-direction:column;align-items:center;padding:80px 0 24px;gap:0;border-right:1px solid var(--md-outline-variant)}
@media(min-width:1100px){.md3-rail{display:flex}.container{margin-left:80px}.md3-fab{right:32px;bottom:32px}}
.rail-item{display:flex;flex-direction:column;align-items:center;gap:4px;width:100%;padding:6px 0 8px;cursor:pointer;color:var(--md-on-surface-variant);text-decoration:none;transition:color .15s;border:none;background:none;overflow:visible}
.rail-item:hover{color:var(--md-on-surface)}
.rail-item.active{color:var(--md-primary)}
.rail-indicator{width:56px;height:32px;border-radius:var(--shape-full);display:flex;align-items:center;justify-content:center;transition:background .15s;position:relative}
.rail-item.active .rail-indicator{background:var(--md-secondary-container)}
.rail-item:hover:not(.active) .rail-indicator{background:rgba(0,0,0,.08)}
.rail-label{font:500 11px/1 var(--font);text-align:center;letter-spacing:.04em;padding:0 4px}

/* ═══ MD3 Chip icon sizing ═══ */
.md3-chip .material-symbols-outlined{font-size:16px!important}

/* ═══ MD3 Card icon ═══ */
.md3-card__icon .material-symbols-outlined{font-size:28px!important}

/* ═══ MD3 Callout icon ═══ */
.md3-callout__icon .material-symbols-outlined{font-size:20px!important}

/* ═══ MD3 Pros/Cons via CSS ═══ */
.pros li::before{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 1,'wght' 400,'GRAD' 0,'opsz' 20;font-size:14px;line-height:1.6}
.cons li::before{font-family:'Material Symbols Outlined';font-variation-settings:'FILL' 1,'wght' 400,'GRAD' 0,'opsz' 20;font-size:14px;line-height:1.6}

/* ═══ Rail scrollspy active state ═══ */
.rail-item .material-symbols-outlined{font-size:20px!important;transition:font-variation-settings .15s}
.rail-item.active .material-symbols-outlined{font-variation-settings:'FILL' 1,'wght' 400,'GRAD' 0,'opsz' 24}

/* ═══ Expand icon transition ═══ */
.expand-icon .material-symbols-outlined{transition:transform .25s cubic-bezier(.4,0,.2,1)}
.expand-btn[aria-expanded="true"] .expand-icon .material-symbols-outlined{transform:rotate(180deg)}
"""
html = html.replace('</style>', NEW_CSS + '\n</style>', 1)

# ── 3. Fix pros/cons CSS content property ───────────────────────────────────
html = html.replace(
    ".pros li::before{content:'✓';position:absolute;left:0;color:var(--color-success)}",
    ".pros li::before{content:'check';position:absolute;left:0;color:var(--color-success)}"
)
html = html.replace(
    ".cons li::before{content:'✗';position:absolute;left:0;color:var(--md-error)}",
    ".cons li::before{content:'close';position:absolute;left:0;color:var(--md-error)}"
)

# ── 4. Icon helper ───────────────────────────────────────────────────────────
def icon(name, cls='', filled=False):
    fill_class = ' icon-filled' if filled else ''
    extra = (' ' + cls) if cls else ''
    return f'<span class="material-symbols-outlined{fill_class}{extra}">{name}</span>'

# ── 5. Header icon ───────────────────────────────────────────────────────────
html = html.replace(
    '<div class="site-header__icon">🤝</div>',
    f'<div class="site-header__icon">{icon("handshake", "icon-sm", True)}</div>'
)

# ── 6. Stepper completed check ───────────────────────────────────────────────
html = html.replace(
    '<div class="step__node">✓</div>',
    f'<div class="step__node">{icon("check", "icon-sm", True)}</div>'
)

# ── 7. Confidence banner card icon ──────────────────────────────────────────
html = html.replace(
    '<div class="md3-card__icon" style="background:var(--md-primary-container);font-size:28px">🎉</div>',
    f'<div class="md3-card__icon" style="background:var(--md-primary-container);color:var(--md-on-primary-container)">{icon("celebration", "", True)}</div>'
)

# ── 8. Phase 2 card icon ─────────────────────────────────────────────────────
html = html.replace(
    '<div class="md3-card__icon" style="background:var(--md-error-container);font-size:28px">🔴</div>',
    f'<div class="md3-card__icon" style="background:var(--md-error-container);color:var(--md-on-error-container)">{icon("error", "", True)}</div>'
)

# ── 9. Chips ─────────────────────────────────────────────────────────────────
replacements = [
    ('>✅ 3 of 4 Steps Complete<', f'>{icon("task_alt","icon-xs",True)} 3 of 4 Steps Complete<'),
    ('>⚡ Flow is Running<',       f'>{icon("bolt","icon-xs",True)} Flow is Running<'),
    ('>📬 Emails Arriving<',       f'>{icon("mark_email_read","icon-xs",True)} Emails Arriving<'),
    ('>⏱ Fastest fix: ~15 minutes<', f'>{icon("schedule","icon-xs")} Fastest fix: ~15 min<'),
    ('>🔴 Active Issue<',          f'>{icon("error","icon-xs",True)} Active Issue<'),
    ('>📍 Compose Actions<',       f'>{icon("edit","icon-xs")} Compose Actions<'),
    ('>⏱ ~15 min to fix<',        f'>{icon("schedule","icon-xs")} ~15 min to fix<'),
    ('>🔧 Option A<',              f'>{icon("build","icon-xs")} Option A<'),
    ('>⏱ ~15 minutes<',           f'>{icon("schedule","icon-xs")} ~15 minutes<'),
    ('>💰 Free<',                  f'>{icon("payments","icon-xs")} Free<'),
    ('>👤 Olivia<',                f'>{icon("person","icon-xs")} Olivia<'),
    ('>👤 Tyler<',                 f'>{icon("person","icon-xs")} Tyler<'),
    ('>⭐ Newly Discovered<',      f'>{icon("star","icon-xs",True)} Newly Discovered<'),
    ('>🏆 Recommended Short-Term<', f'>{icon("emoji_events","icon-xs",True)} Recommended Short-Term<'),
    ('>⏱ ~30–60 minutes<',        f'>{icon("schedule","icon-xs")} ~30–60 minutes<'),
    ('>🏗️ Option C<',             f'>{icon("construction","icon-xs")} Option C<'),
    ('>🏆 Best Long-Term<',        f'>{icon("emoji_events","icon-xs",True)} Best Long-Term<'),
    ('>⏱ 1–2 days (Tyler\'s work)<', f'>{icon("schedule","icon-xs")} 1–2 days (Tyler\'s work)<'),
    ('>💰 Depends on FranConnect plan<', f'>{icon("payments","icon-xs")} FranConnect plan dependent<'),
]
for old, new in replacements:
    html = html.replace(old, new)

# ── 10. Comparison panel headers ─────────────────────────────────────────────
html = html.replace('>❌ What FranConnect Is Getting (Broken)<', f'>{icon("cancel","icon-xs",True)} What FranConnect Gets (Broken)<')
html = html.replace('>✅ What FranConnect Should Get (Fixed)<',  f'>{icon("check_circle","icon-xs",True)} What FranConnect Gets (Fixed)<')
html = html.replace('>❌ Current (Wrong) Expression<',           f'>{icon("cancel","icon-xs",True)} Current (Wrong) Expression<')
html = html.replace('>✅ Fixed (Two-Stage Split)<',              f'>{icon("check_circle","icon-xs",True)} Fixed (Two-Stage Split)<')

# ── 11. Before/After tab buttons ─────────────────────────────────────────────
html = html.replace('>❌ Before (Broken)<', f'>{icon("cancel","icon-xs",True)} Before (Broken)<')
html = html.replace('>✅ After (Fixed)<',   f'>{icon("check_circle","icon-xs",True)} After (Fixed)<')

# ── 12. FranConnect record title ─────────────────────────────────────────────
html = html.replace('>👤 Primary Info — Bishops Test Lead<', f'>{icon("person","icon-xs")} Primary Info — Bishops Test Lead<')

# ── 13. Callout icons ────────────────────────────────────────────────────────
callout_icons = [
    ('<div class="md3-callout__icon">⚠️</div>', f'<div class="md3-callout__icon">{icon("warning","",True)}</div>'),
    ('<div class="md3-callout__icon">✅</div>',  f'<div class="md3-callout__icon">{icon("check_circle","",True)}</div>'),
    ('<div class="md3-callout__icon">💡</div>',  f'<div class="md3-callout__icon">{icon("lightbulb","",True)}</div>'),
    ('<div class="md3-callout__icon">📋</div>',  f'<div class="md3-callout__icon">{icon("assignment","")}</div>'),
    ('<div class="md3-callout__icon">📌</div>',  f'<div class="md3-callout__icon">{icon("push_pin","")}</div>'),
]
for old, new in callout_icons:
    html = html.replace(old, new)

# ── 14. Expand/collapse arrows → expand_more icon ───────────────────────────
html = html.replace(
    '<span class="expand-icon">▼</span>',
    f'<span class="expand-icon">{icon("expand_more","icon-sm")}</span>'
)
html = html.replace(
    '<span class="disclosure-icon">▼</span>',
    f'<span class="disclosure-icon">{icon("expand_more","icon-sm")}</span>'
)

# ── 15. Gotchas button icon ──────────────────────────────────────────────────
html = html.replace(
    '<span>🔍 Common Gotchas',
    f'<span>{icon("search","icon-sm")} Common Gotchas'
)

# ── 16. Disclosure section labels ────────────────────────────────────────────
html = html.replace(
    '<span>📋 Phase 1 Reference',
    f'<span>{icon("assignment","icon-sm")} Phase 1 Reference'
)
html = html.replace(
    '<span>📌 Quick Reference',
    f'<span>{icon("push_pin","icon-sm")} Quick Reference'
)

# ── 17. Phase badges ─────────────────────────────────────────────────────────
html = html.replace('>🔴 Phase 0 — NOW<',       f'>{icon("error","icon-xs",True)} Phase 0 — NOW<')
html = html.replace('>🟡 Phase 1 — This Week<', f'>{icon("schedule","icon-xs",True)} Phase 1 — This Week<')
html = html.replace('>🟢 Phase 2 — This Month<',f'>{icon("check_circle","icon-xs",True)} Phase 2 — This Month<')

# ── 18. Escalation avatar ────────────────────────────────────────────────────
html = html.replace(
    '<div class="esc-avatar">👨‍💻</div>',
    f'<div class="esc-avatar">{icon("support_agent","icon-xl icon-filled",True)}</div>'
)

# ── 19. Platform card headings ───────────────────────────────────────────────
html = html.replace(
    '<h4>🪟 Windows</h4>',
    f'<h4>{icon("laptop_windows","icon-sm")} Windows</h4>'
)
html = html.replace(
    '<h4>🍎 Mac</h4>',
    f'<h4>{icon("laptop_mac","icon-sm")} Mac</h4>'
)

# ── 20. CTA buttons → MD3 button system ─────────────────────────────────────
html = html.replace(
    '<a href="#phase2" style="background:var(--md-primary);color:var(--md-on-primary);display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:var(--shape-full);font:500 14px/1 var(--font,sans-serif);text-decoration:none">↑ Jump to Fix Steps &amp; Expressions</a>',
    f'<a href="#phase2" class="md3-btn md3-btn--filled">{icon("arrow_upward","icon-sm")} Jump to Fix Steps</a>'
)
html = html.replace(
    '<a href="https://app.hubspot.com" target="_blank" rel="noopener" style="background:var(--md-primary);color:var(--md-on-primary);display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:var(--shape-full);font:500 14px/1 var(--font,sans-serif);text-decoration:none">Open HubSpot →</a>',
    f'<a href="https://app.hubspot.com" target="_blank" rel="noopener" class="md3-btn md3-btn--filled">{icon("open_in_new","icon-sm")} Open HubSpot</a>'
)

# ── 21. FAB + Snackbar + Navigation Rail (insert before </body>) ─────────────
FAB_HTML = f"""
<!-- MD3 Navigation Rail -->
<nav class="md3-rail" aria-label="Guide sections" id="md3-rail">
  <a href="#phase2" class="rail-item active" title="Fix the Data" data-section="phase2">
    <div class="rail-indicator">{icon("build","icon-sm")}</div>
    <span class="rail-label">Fix</span>
  </a>
  <a href="#option-a" class="rail-item" title="Option A — Quick Fix" data-section="option-a">
    <div class="rail-indicator">{icon("bolt","icon-sm")}</div>
    <span class="rail-label">Quick</span>
  </a>
  <a href="#option-f" class="rail-item" title="Option F — Recommended" data-section="option-f">
    <div class="rail-indicator">{icon("star","icon-sm")}</div>
    <span class="rail-label">Best</span>
  </a>
  <a href="#option-c" class="rail-item" title="Option C — API" data-section="option-c">
    <div class="rail-indicator">{icon("api","icon-sm")}</div>
    <span class="rail-label">API</span>
  </a>
  <a href="#escalation" class="rail-item" title="Get Help" data-section="escalation">
    <div class="rail-indicator">{icon("support_agent","icon-sm")}</div>
    <span class="rail-label">Help</span>
  </a>
</nav>

<!-- MD3 Extended FAB -->
<a href="#phase2" class="md3-fab" aria-label="Jump to fix">
  {icon("build","")}
  <span>Jump to Fix</span>
</a>

<!-- MD3 Snackbar -->
<div class="md3-snackbar" id="md3-snackbar" role="status" aria-live="polite">
  {icon("check_circle","icon-filled")}
  <span id="snackbar-msg">Copied to clipboard</span>
</div>
"""
html = html.replace('</body>', FAB_HTML + '\n</body>', 1)

# ── 22. Update JavaScript — Snackbar + Rail scrollspy ───────────────────────
OLD_COPY_FN = """function initCopyButtons() {
  document.querySelectorAll('[data-copy]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var text = btn.getAttribute('data-copy');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() {
          var orig = btn.textContent;
          btn.textContent = '✓ Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.textContent = orig;
            btn.classList.remove('copied');
          }, 2000);
        });
      } else {
        // Fallback for older browsers
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.focus();
        ta.select();
        try { document.execCommand('copy'); } catch(e) {}
        document.body.removeChild(ta);
        var orig = btn.textContent;
        btn.textContent = '✓ Copied!';
        btn.classList.add('copied');
        setTimeout(function() {
          btn.textContent = orig;
          btn.classList.remove('copied');
        }, 2000);
      }
    });
  });

  // expr-copy buttons
  document.querySelectorAll('.expr-copy').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var text = btn.getAttribute('data-copy');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() {
          btn.textContent = '\\u2713 Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.textContent = 'Copy';
            btn.classList.remove('copied');
          }, 2000);
        });
      }
    });
  });
}"""

NEW_COPY_FN = """var _sbTimer = null;
function showSnackbar(msg) {
  var sb = document.getElementById('md3-snackbar');
  var ml = document.getElementById('snackbar-msg');
  if (ml) ml.textContent = msg || 'Copied';
  if (sb) {
    sb.classList.add('is-visible');
    clearTimeout(_sbTimer);
    _sbTimer = setTimeout(function() { sb.classList.remove('is-visible'); }, 2800);
  }
}
function doCopy(text, label) {
  function done() { showSnackbar((label || 'Item') + ' copied'); }
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(done).catch(function() { fallback(text); done(); });
  } else { fallback(text); done(); }
}
function fallback(text) {
  var t = document.createElement('textarea');
  t.value = text; t.style.cssText = 'position:fixed;opacity:0;pointer-events:none';
  document.body.appendChild(t); t.focus(); t.select();
  try { document.execCommand('copy'); } catch(e) {}
  document.body.removeChild(t);
}
function initCopyButtons() {
  document.querySelectorAll('[data-copy]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      doCopy(btn.getAttribute('data-copy'), btn.getAttribute('data-label') || 'Content');
    });
  });
  document.querySelectorAll('.expr-copy').forEach(function(btn) {
    btn.addEventListener('click', function() {
      doCopy(btn.getAttribute('data-copy'), 'Expression');
    });
  });
}
function initRailScrollspy() {
  var sections = ['phase2','option-a','option-f','option-c','escalation'];
  var railItems = document.querySelectorAll('.rail-item[data-section]');
  if (!railItems.length) return;
  function update() {
    var scrollY = window.scrollY + 120;
    var active = sections[0];
    sections.forEach(function(id) {
      var el = document.getElementById(id);
      if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) active = id;
    });
    railItems.forEach(function(item) {
      item.classList.toggle('active', item.getAttribute('data-section') === active);
    });
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
}"""

html = html.replace(OLD_COPY_FN, NEW_COPY_FN)

# Add initRailScrollspy() to DOMContentLoaded
html = html.replace(
    'document.addEventListener(\'DOMContentLoaded\', function() {\n  initCopyButtons();\n  initSmoothScroll();\n});',
    'document.addEventListener(\'DOMContentLoaded\', function() {\n  initCopyButtons();\n  initSmoothScroll();\n  initRailScrollspy();\n});'
)

# ── 23. Write updated file ───────────────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 24. Verify ───────────────────────────────────────────────────────────────
with open(path, 'r', encoding='utf-8') as f:
    result = f.read()

checks = {
    'Material Symbols font link': 'Material+Symbols+Outlined' in result,
    'icon() spans present': 'material-symbols-outlined' in result,
    'State layer CSS': 'md3-btn::after' in result,
    'FAB present': 'md3-fab' in result,
    'Snackbar present': 'md3-snackbar' in result,
    'Navigation Rail present': 'md3-rail' in result,
    'Snackbar JS': 'showSnackbar' in result,
    'Rail scrollspy JS': 'initRailScrollspy' in result,
    'No stray 🎉 in card icon': '<div class="md3-card__icon" style="background:var(--md-primary-container);font-size:28px">🎉</div>' not in result,
    'No stray 🔴 in card icon': '<div class="md3-card__icon" style="background:var(--md-error-container);font-size:28px">🔴</div>' not in result,
    'No stray ⚠️ callout icon': '<div class="md3-callout__icon">⚠️</div>' not in result,
    'Pros uses Material Symbols content': "content:'check'" in result,
    'Cons uses Material Symbols content': "content:'close'" in result,
    'MD3 button system': 'md3-btn--filled' in result,
    'CTA uses md3-btn': 'class="md3-btn md3-btn--filled"' in result,
}

print('\n╔══ MD3 Upgrade Verification ══╗')
all_pass = True
for name, passed in checks.items():
    status = '✓' if passed else '✗ FAIL'
    if not passed: all_pass = False
    print(f'  {status}  {name}')

lines = result.count('\n') + 1
print(f'\n  File: {lines} lines, {len(result)//1024}KB')
print('╚' + '═'*30 + '╝')
print('\nAll checks passed!' if all_pass else '\nSome checks failed — review above.')
