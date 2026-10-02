# Original inline SVG icons for the Harvest concept site (no Lucid artwork).
HARVEST_MARK = ('<svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true" focusable="false">'
  '<rect x="1.5" y="7" width="13" height="13" rx="1.5" fill="#ff8f8f" transform="rotate(-10 8 13.5)"/>'
  '<rect x="6.5" y="2.5" width="13" height="13" rx="1.5" fill="#ffe342"/>'
  '<rect x="11" y="10" width="13.5" height="13.5" rx="1.5" fill="#eb5a00"/>'
  '<path d="M14.3 16.9l2.6 2.6 4.6-5" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHEV = '<svg class="chev" viewBox="0 0 10 10" aria-hidden="true"><path d="M1.5 3.5L5 7l3.5-3.5" stroke="currentColor" stroke-width="1.4" fill="none"/></svg>'
CAPTURE = ('<svg viewBox="0 0 56 56" aria-hidden="true"><rect x="4" y="9" width="48" height="36" rx="3" fill="#edf5ff" stroke="#1071e5" stroke-width="2"/>'
  '<rect x="4" y="9" width="48" height="7" rx="3" fill="#1071e5"/><rect x="10" y="22" width="20" height="4" fill="#b5d6ff"/><rect x="10" y="30" width="30" height="3" fill="#cfe4ff"/>'
  '<rect x="10" y="36" width="12" height="5" fill="#282c33"/><path d="M19 37l0 14 3.6-3.4 2.6 5.6 2.4-1.1-2.6-5.5 5-.3z" fill="#fff" stroke="#282c33" stroke-width="1.6" stroke-linejoin="round"/></svg>')
REVIEW = ('<svg viewBox="0 0 56 56" aria-hidden="true"><rect x="3" y="6" width="50" height="40" rx="3" fill="#fff" stroke="#3a414a" stroke-width="2"/>'
  '<rect x="10" y="13" width="26" height="18" fill="#dfe3e8"/><rect x="31" y="10" width="15" height="15" fill="#ff8f8f" transform="rotate(6 38 17)"/>'
  '<rect x="8" y="27" width="14" height="14" fill="#ffe342" transform="rotate(-5 15 34)"/><rect x="34" y="29" width="13" height="13" fill="#a3d4ff"/>'
  '<path d="M24 38c3-4 6 2 9-2" stroke="#eb5a00" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')
HARVEST = ('<svg viewBox="0 0 56 56" aria-hidden="true"><rect x="6" y="5" width="12" height="12" fill="#ff8f8f"/><rect x="22" y="3" width="12" height="12" fill="#ffe342"/>'
  '<rect x="38" y="6" width="12" height="12" fill="#a3d4ff"/><path d="M12 20l9 9M28 18v11M44 21l-9 8" stroke="#6f7681" stroke-width="2" stroke-dasharray="3 3"/>'
  '<rect x="10" y="30" width="36" height="22" rx="2" fill="#fff3d9" stroke="#eb5a00" stroke-width="2"/>'
  '<path d="M16 37h16M16 42h22M16 47h12" stroke="#cc4e00" stroke-width="2" stroke-linecap="round"/></svg>')
SHIP = ('<svg viewBox="0 0 56 56" aria-hidden="true"><circle cx="15" cy="12" r="5" fill="#fff" stroke="#3a414a" stroke-width="2.4"/>'
  '<circle cx="15" cy="44" r="5" fill="#fff" stroke="#3a414a" stroke-width="2.4"/><circle cx="41" cy="44" r="5" fill="#1d7a3d" stroke="#1d7a3d" stroke-width="2.4"/>'
  '<path d="M15 17v22M41 39V24a6 6 0 0 0-6-6h-9" stroke="#3a414a" stroke-width="2.4" fill="none"/><path d="M30 13l-5 5 5 5" stroke="#3a414a" stroke-width="2.4" fill="none"/>'
  '<path d="M38.5 44l2 2 3.5-4" stroke="#fff" stroke-width="2" fill="none"/></svg>')
def ico(kind, color):
    paths = {
      'people': '<circle cx="15" cy="16" r="6"/><circle cx="31" cy="16" r="6"/><path d="M4 38c0-7 5-11 11-11s11 4 11 11M22 38c0-7 4-11 9-11s10 4 10 11"/>',
      'pin': '<rect x="6" y="6" width="32" height="24" rx="2"/><path d="M14 30v8l8-8"/><path d="M14 15h16M14 21h10"/>',
      'trail': '<path d="M8 8h28v30H8z"/><path d="M14 16h4M22 16h8M14 23h4M22 23h8M14 30h4M22 30h8"/>',
      'batch': '<rect x="6" y="18" width="20" height="20"/><rect x="12" y="12" width="20" height="20"/><rect x="18" y="6" width="20" height="20"/>',
      'flag': '<path d="M10 40V6M10 8h22l-5 7 5 7H10"/>',
      'chart': '<path d="M6 38h34M10 32V20M18 32V12M26 32V24M34 32V16"/>',
    }[kind]
    return (f'<svg class="ico" viewBox="0 0 44 44" fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{paths}</svg>')
CHECK_BIG = ('<svg class="check" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="#dcf5e3"/>'
  '<path d="M19 33l9 9 17-19" stroke="#1d7a3d" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
