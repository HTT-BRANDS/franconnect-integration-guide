#!/usr/bin/env python3
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'troubleshooting-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Option F header chips: change Olivia chip → Patti chip + add HTT Brands badge ──
html = html.replace(
    '''      <span class="md3-chip chip-new"><span class="material-symbols-outlined icon-filled icon-xs">star</span> Newly Discovered</span>
      <span class="md3-chip chip-primary"><span class="material-symbols-outlined icon-filled icon-xs">emoji_events</span> Recommended Short-Term</span>
      <span class="md3-chip chip-warning"><span class="material-symbols-outlined icon-xs">schedule</span> ~30–60 minutes</span>
      <span class="md3-chip chip-success"><span class="material-symbols-outlined icon-xs">payments</span> Free</span>
      <span class="md3-chip chip-surface"><span class="material-symbols-outlined icon-xs">person</span> Olivia</span>''',
    '''      <span class="md3-chip chip-primary"><span class="material-symbols-outlined icon-filled icon-xs">emoji_events</span> Recommended Next Step</span>
      <span class="md3-chip chip-warning"><span class="material-symbols-outlined icon-xs">schedule</span> ~30–60 minutes</span>
      <span class="md3-chip chip-success"><span class="material-symbols-outlined icon-xs">payments</span> Free</span>
      <span class="md3-chip chip-info"><span class="material-symbols-outlined icon-xs">corporate_fare</span> HTT Brands Internal</span>
      <span class="md3-chip chip-surface"><span class="material-symbols-outlined icon-xs">manage_accounts</span> Patti Rother</span>'''
)

# ── 2. Option F title ──
html = html.replace(
    '<h3 class="option-card__title">Send a Plain-Text Structured Email from HubSpot</h3>',
    '<h3 class="option-card__title">HTT Brands: Switch HubSpot Notification to Plain-Text Email</h3>'
)

# ── 3. Option F subtitle description ──
html = html.replace(
    '<p style="font:400 14px/1.6 var(--font,sans-serif);color:var(--md-on-surface-variant)">Reconfigure the HubSpot workflow to send a clean plain-text email with predictable formatting. Eliminates image noise and makes the expressions reliable — no more guessing about labels.</p>',
    '<p style="font:400 14px/1.6 var(--font,sans-serif);color:var(--md-on-surface-variant)">If Option A\'s expressions don\'t hold up, HTT Brands can update the HubSpot notification workflow to send a clean plain-text email. This eliminates image noise at the source and makes all parsing permanently reliable. <strong>This is an internal HTT Brands action — Patti Rother configured the current HubSpot workflows and can make this change.</strong></p>'
)

# ── 4. Add a prominent "HTT Brands Internal Action" callout at the top of Option F body ──
# Insert before the opening <p> of the body section
html = html.replace(
    '''  <div class="option-card__body">
    <p style="font:400 14px/1.7 var(--font,sans-serif);margin-bottom:16px">The root problem isn't the expressions — it's that HubSpot\'s default notification emails are full of HTML branding, images, and tracking pixels that pollute the stripped text. If you control what HubSpot sends, you can send a <strong>clean, predictable plain-text email</strong> that always looks exactly the same.</p>

    <h4 style="font:500 14px/1 var(--font,sans-serif);margin-bottom:12px">How to Set This Up in HubSpot</h4>''',
    '''  <div class="option-card__body">
    <div class="md3-callout callout-info" style="margin-bottom:20px">
      <div class="md3-callout__icon"><span class="material-symbols-outlined icon-filled">corporate_fare</span></div>
      <div>
        <div class="md3-callout__title">HTT Brands Internal Action — Patti Rother</div>
        <div class="md3-callout__body">This change is made on the HTT Brands side in HubSpot, not by Olivia in Power Automate. <strong>Patti Rother</strong> configured the current Bishops Lead Notification workflow in HubSpot and can update it. If Option A\'s expressions still produce incorrect results after testing, let Tyler know and he\'ll loop Patti in to make this update.</div>
      </div>
    </div>

    <p style="font:400 14px/1.7 var(--font,sans-serif);margin-bottom:16px">The root problem isn't the expressions — it's that HubSpot\'s default notification emails are full of HTML branding, images, and tracking pixels that pollute the stripped text. Switching to a clean plain-text format at the HubSpot workflow level eliminates this at the source, making Power Automate\'s parsing permanently reliable without any further expression changes.</p>

    <h4 style="font:500 14px/1 var(--font,sans-serif);margin-bottom:12px">How Patti Updates This in HubSpot</h4>'''
)

# ── 5. Update Option F CTA note — reframe as escalation path, not primary action ──
html = html.replace(
    '''    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
      <span style="font:400 13px/1.4 var(--font,sans-serif);color:var(--md-on-surface-variant)">Do Option F first, then apply Option A's expressions — together they're the most reliable free solution.</span>
      <a href="https://app.hubspot.com" target="_blank" rel="noopener" class="md3-btn md3-btn--filled"><span class="material-symbols-outlined icon-sm">open_in_new</span> Open HubSpot</a>
    </div>''',
    '''    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
      <span style="font:400 13px/1.4 var(--font,sans-serif);color:var(--md-on-surface-variant)"><strong>Escalation path:</strong> If Option A doesn\'t fully resolve the data issue after testing, Olivia should let Tyler know — Tyler will then coordinate with Patti Rother to update the HubSpot workflow using the template above.</span>
    </div>'''
)

# ── 6. Add callout-info CSS if not present ──
if 'callout-info' not in html:
    html = html.replace(
        '.callout-success{background:var(--md-primary-container);border-left-color:var(--md-primary)}',
        '.callout-success{background:var(--md-primary-container);border-left-color:var(--md-primary)}\n.callout-info{background:#e8f0fe;border-left-color:#1a73e8}'
    )

# ── 7. Phased Roadmap: Option F row — change owner from Olivia → Patti Rother ──
html = html.replace(
    '''          <td>Within 2–3 days</td>
          <td>Reconfigure the HubSpot workflow to send a plain-text structured email (the template in Option F). Re-run a test lead to confirm the Strip HTML output is now clean. Update expressions if any label strings changed.</td>
          <td>Olivia</td>
          <td><a href="#option-f">Option F</a></td>''',
    '''          <td>Within 2–3 days (if Option A needs reinforcement)</td>
          <td>If Option A expressions still return incorrect values after testing: Olivia notifies Tyler → Tyler coordinates with <strong>Patti Rother (HTT Brands)</strong> to update the Bishops HubSpot notification workflow to plain-text format. Re-run a test lead to confirm Strip HTML output is clean.</td>
          <td>Patti Rother (HTT Brands)</td>
          <td><a href="#option-f">Option F</a></td>'''
)

# ── 8. Decision table: "Fix works but breaks again" row — clarify owner ──
html = html.replace(
    '<tr class="row-phase2"><td><strong>Fix works but breaks again after a few weeks</strong></td><td><strong>HubSpot updated their email template</strong></td><td><strong><a href="#option-f">Option F</a> — switch to plain-text HubSpot email</strong></td></tr>',
    '<tr class="row-phase2"><td><strong>Fix works but breaks again after a few weeks</strong></td><td><strong>HubSpot updated their email template</strong></td><td><strong><a href="#option-f">Option F</a> — Patti Rother (HTT Brands) updates HubSpot workflow to plain-text format</strong></td></tr>'
)

# ── 9. Gotchas accordion: "HubSpot updated their email template" card — add Patti note ──
html = html.replace(
    '<p style="font:400 13px/1.6 var(--font,sans-serif)">This is a known fragility of email-parsing approaches. If HubSpot changes their notification email layout, the labels may shift or new content may be injected. See Option F below — sending a plain-text structured email eliminates this fragility.</p>',
    '<p style="font:400 13px/1.6 var(--font,sans-serif)">This is a known fragility of email-parsing approaches. If HubSpot changes their notification email layout, the labels may shift or new content may be injected. See <a href="#option-f">Option F</a> — switching to a plain-text structured email (coordinated with <strong>Patti Rother at HTT Brands</strong>) eliminates this fragility permanently.</p>'
)

# ── 10. Option A CTA note — update to reflect the escalation chain ──
html = html.replace(
    '<span style="font:400 13px/1.4 var(--font,sans-serif);color:var(--md-on-surface-variant)">Do Option F first, then apply Option A\'s expressions — together they\'re the most reliable free solution.</span>',
    '<span style="font:400 13px/1.4 var(--font,sans-serif);color:var(--md-on-surface-variant)">Start here. If expressions still return incorrect values after testing, let Tyler know — he\'ll coordinate with Patti Rother (HTT Brands) to update the HubSpot workflow.</span>'
)

# ── 11. cons list in Option F — update the HubSpot workflow edit access con ──
html = html.replace(
    '<li>Requires HubSpot workflow edit access</li>',
    '<li>Requires HTT Brands internal action (Patti Rother)</li>'
)

# ── Write ──
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── Verify ──
with open(path, 'r', encoding='utf-8') as f:
    result = f.read()

checks = {
    'Option F chip: HTT Brands Internal':          'HTT Brands Internal' in result,
    'Option F chip: Patti Rother':                 'Patti Rother' in result,
    'Option F title updated':                      'HTT Brands: Switch HubSpot' in result,
    'Option F callout-info box present':           'HTT Brands Internal Action — Patti Rother' in result,
    'Option F CTA is escalation path':             'Escalation path' in result,
    'No "Do Option F first" text remaining':       'Do Option F first' not in result,
    'Phased roadmap owner updated':                'Patti Rother (HTT Brands)' in result,
    'Gotchas card updated with Patti ref':         'Patti Rother at HTT Brands' in result,
    'Decision table updated':                      'Patti Rother (HTT Brands) updates HubSpot' in result,
    'Cons list updated':                           'Requires HTT Brands internal action' in result,
}

print('\n╔══ Patti / Option F Update Verification ══╗')
all_pass = True
for name, passed in checks.items():
    status = '✓' if passed else '✗ FAIL'
    if not passed: all_pass = False
    print(f'  {status}  {name}')

lines = result.count('\n') + 1
print(f'\n  File: {lines} lines, {len(result)//1024}KB')
print('╚' + '═'*44 + '╝')
print('\nAll checks passed!' if all_pass else '\nSome checks FAILED.')
