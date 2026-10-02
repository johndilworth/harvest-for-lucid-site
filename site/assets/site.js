// Harvest concept site: mobile menu, before/after tabs, non-submitting beta form.
(function () {
  var nav = document.getElementById('gnav');
  var burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', String(open));
  });

  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = [].slice.call(root.querySelectorAll('[role=tab]'));
    function select(t) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', String(on));
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t) });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { var n = tabs[(i + d + tabs.length) % tabs.length]; select(n); n.focus(); e.preventDefault() }
      });
    });
  });

  // Beta form: validates and shows a success state. Never sends data anywhere (no action, no fetch).
  var form = document.getElementById('beta-form');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true;
    [['f-name', function (v) { return v.trim().length > 0 }], ['f-email', function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) }]]
      .forEach(function (p) {
        var el = document.getElementById(p[0]); var good = p[1](el.value);
        el.closest('.field').classList.toggle('invalid', !good);
        el.setAttribute('aria-invalid', String(!good));
        if (!good && ok) { el.focus(); ok = false }
      });
    if (!ok) return;
    var first = document.getElementById('f-name').value.trim().split(/\s+/)[0];
    document.getElementById('s-name').textContent = first ? ', ' + first : '';
    document.getElementById('beta-root').classList.add('is-success');
    document.title = "You're on the list | Harvest beta | Lucid";
    window.scrollTo(0, 0);
    var h = document.querySelector('#done h1'); h.tabIndex = -1; h.focus({ preventScroll: true });
  });
})();
