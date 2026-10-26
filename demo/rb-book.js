/* Richard Brokaw – interactive book sample. Each .rb-book holds a cover image and a hidden list of .rb-page sections. */
(function () {
  function setup(root) {
    var src = root.querySelector('.rb-src');
    var pages = [].slice.call(src.querySelectorAll('.rb-page')).map(function (p) { return p.innerHTML; });
    var classes = [].slice.call(src.querySelectorAll('.rb-page')).map(function (p) { return p.getAttribute('data-kind') || ''; });
    var cover = root.getAttribute('data-cover'), alt = root.getAttribute('data-cover-alt') || '';
    var title = root.getAttribute('data-title') || 'this book';

    var clip = document.createElement('div'); clip.className = 'rb-clip';
    var stage = document.createElement('div'); stage.className = 'rb-stage';
    var book = document.createElement('div'); book.className = 'rb-book3d';
    stage.appendChild(book); clip.appendChild(stage);
    var hint = document.createElement('p'); hint.className = 'rb-hint';
    var controls = document.createElement('div'); controls.className = 'rb-controls'; controls.hidden = true;
    controls.innerHTML = '<button type="button" data-act="prev">← Previous</button><span class="rb-count" aria-live="polite"></span>' +
      '<button type="button" data-act="next">Next →</button><button type="button" data-act="close">Close Book</button>';
    root.insertBefore(controls, src); root.insertBefore(hint, controls); root.insertBefore(clip, hint);

    var leaves = [], cur = 0, narrow = null, list = pages, kinds = classes;

    function face(side, html, kind) {
      var f = document.createElement('div');
      if (kind === 'cover') { f.className = 'rb-face front cover'; f.innerHTML = '<img src="' + cover + '" alt="' + alt.replace(/"/g, '&quot;') + '">'; return f; }
      f.className = 'rb-face paper ' + side + (kind === 'blank-cover' ? ' inside-cover' : '');
      if (html != null) f.innerHTML = '<div class="rb-pg ' + (kind || '') + '">' + html + '</div>';
      return f;
    }

    function build() {
      book.innerHTML = '<div class="rb-block"></div>';
      leaves = [];
      var spec = [];
      list = pages.slice(); kinds = classes.slice();
      // in a two-page spread the last page must land on a right-hand page
      if (!narrow && list.length % 2) { list.splice(list.length - 1, 0, ''); kinds.splice(kinds.length - 1, 0, ''); }
      var pages_ = list, classes_ = kinds;
      if (!narrow) {                      // spread: cover | title, then two pages per leaf
        spec.push([['cover'], [pages_[0], classes_[0]]]);
        for (var i = 1; i < pages_.length; i += 2) spec.push([[pages_[i], classes_[i]], i + 1 < pages_.length ? [pages_[i + 1], classes_[i + 1]] : [null, '']]);
      } else {                            // single page: every page on a front face
        spec.push([['cover'], [null, 'blank-cover']]);
        for (var j = 0; j < pages_.length; j++) spec.push([[pages_[j], classes_[j]], [null, '']]);
      }
      spec.forEach(function (s, idx) {
        var leaf = document.createElement('div'); leaf.className = 'rb-leaf';
        var front = s[0][0] === 'cover' ? face('front', null, 'cover') : face('front', s[0][0], s[0][1]);
        var back = face('back', s[1][0], s[1][1]);
        leaf.appendChild(front); leaf.appendChild(back);
        leaf.addEventListener('click', function () { if (leaf.classList.contains('is-flipped')) go(cur - 1); else go(cur + 1); });
        if (idx === 0) { leaf.classList.add('is-cover'); leaf.tabIndex = 0; leaf.setAttribute('role', 'button'); leaf.setAttribute('aria-label', 'Open a sample of ' + title); }
        book.appendChild(leaf); leaves.push(leaf);
      });
      render(); z();
    }

    function z() {
      var n = leaves.length;
      leaves.forEach(function (l, i) { l.style.zIndex = l.classList.contains('is-flipped') ? i + 1 : n - i + 1; });
    }

    function render() {
      var max = leaves.length - 1, total = list.length;
      leaves.forEach(function (l, i) {
        var flipped = i < cur; l.classList.toggle('is-flipped', flipped);
        // only the two faces in view are exposed to screen readers
        var visible = narrow ? (i === cur) : (i === cur || i === cur - 1);
        l.setAttribute('aria-hidden', cur === 0 ? (i === 0 ? 'false' : 'true') : (visible ? 'false' : 'true'));
      });
      root.classList.toggle('is-closed', cur === 0);
      leaves[0].tabIndex = cur === 0 ? 0 : -1;
      hint.hidden = cur !== 0;
      hint.textContent = (window.matchMedia('(hover: hover)').matches ? 'Click' : 'Tap') + ' the book to read a sample';
      controls.hidden = cur === 0;
      var prev = controls.querySelector('[data-act=prev]'), next = controls.querySelector('[data-act=next]');
      var had = document.activeElement;
      prev.disabled = cur <= 1; next.disabled = cur >= max;
      // keep keyboard focus inside the reader when a button turns off
      if (had === next && next.disabled) prev.focus(); else if (had === prev && prev.disabled) next.focus();
      var label;
      if (narrow) label = 'Page ' + cur + ' of ' + total;
      else { var a = 2 * cur - 1, b = Math.min(2 * cur, total); label = (a === b ? 'Page ' + a : 'Pages ' + a + '–' + b) + ' of ' + total; }
      controls.querySelector('.rb-count').textContent = label;
    }

    function go(to) {
      var max = leaves.length - 1;
      to = Math.max(0, Math.min(max, to));
      if (to === cur) return;
      var n = leaves.length;
      // leaves that change side ride on top while they turn
      if (to > cur) for (var i = cur; i < to; i++) leaves[i].style.zIndex = n + 10 + i;
      else for (var j = cur - 1; j >= to; j--) leaves[j].style.zIndex = n + 10 + (n - j);
      cur = to;
      render();
      clearTimeout(go.t); go.t = setTimeout(z, 950);
    }

    controls.addEventListener('click', function (e) {
      var a = e.target.getAttribute('data-act');
      if (a === 'prev') go(cur - 1);
      else if (a === 'next') go(cur + 1);
      else if (a === 'close') { go(0); leaves[0].focus({ preventScroll: true }); }
    });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(cur + 1); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { go(cur - 1); e.preventDefault(); }
      else if ((e.key === 'Enter' || e.key === ' ') && e.target === leaves[0] && cur === 0) { go(1); e.preventDefault(); }
      else if (e.key === 'Escape' && cur > 0) go(0);
    });
    var sx = null;
    stage.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', function (e) {
      if (sx == null || cur === 0) return; var dx = e.changedTouches[0].clientX - sx; sx = null;
      if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1));
    });

    function size() {
      var avail = root.clientWidth;
      var nowNarrow = avail < 560;
      var w = nowNarrow ? Math.min(avail - 16, 360) : Math.min(Math.floor((avail - 24) / 2), 340);
      root.style.setProperty('--w', w + 'px');
      root.classList.toggle('is-narrow', nowNarrow);
      if (nowNarrow !== narrow) {
        var wasOpen = cur > 0; narrow = nowNarrow; cur = 0; build();
        if (wasOpen) go(1);
      }
    }
    size();
    if ('ResizeObserver' in window) new ResizeObserver(size).observe(root); else window.addEventListener('resize', size);
  }
  function init() { [].forEach.call(document.querySelectorAll('.rb-book:not([data-ready])'), function (b) { b.setAttribute('data-ready', '1'); setup(b); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.rbBookInit = init;
})();
