/* Relinquishment HTML Reader — progressive enhancement
   Graceful degradation: if JS fails, reader gets plain HTML with working links. */
(function() {
  'use strict';

  // --- TOC toggle ---
  var toc = document.getElementById('TOC');
  if (toc) {
    var btn = document.createElement('button');
    btn.id = 'toc-toggle';
    btn.textContent = 'Contents';
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', 'TOC');
    btn.style.cssText = 'display:block;width:100%;padding:0.6em;font-size:1em;' +
      'background:#f0f0f0;border:1px solid #ccc;cursor:pointer;text-align:left;' +
      'font-family:inherit;margin-bottom:0;border-radius:4px 4px 0 0;';

    var tocList = toc.querySelector('ul');
    if (tocList) {
      tocList.style.display = 'none';
      tocList.style.borderTop = 'none';
      tocList.style.borderRadius = '0 0 4px 4px';
    }

    toc.insertBefore(btn, toc.firstChild);
    toc.style.padding = '0';
    toc.style.border = 'none';
    toc.style.background = 'none';

    btn.addEventListener('click', function() {
      var open = tocList.style.display !== 'none';
      tocList.style.display = open ? 'none' : 'block';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      btn.style.borderRadius = open ? '4px 4px 0 0' : '4px 4px 0 0';
    });

    // Close TOC when a link is clicked
    tocList.addEventListener('click', function(e) {
      if (e.target.tagName === 'A') {
        tocList.style.display = 'none';
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // --- Collect chapters ---
  var chapters = [];
  document.querySelectorAll('h1').forEach(function(h1) {
    if (h1.id && h1.id !== 'title-block-header') {
      chapters.push(h1);
    }
  });
  // Also grab sections with ids that match TOC links
  if (chapters.length === 0) {
    document.querySelectorAll('[id]').forEach(function(el) {
      if (el.tagName === 'H1' || el.tagName === 'H2') {
        chapters.push(el);
      }
    });
  }

  // --- Floating nav bar ---
  var nav = document.createElement('div');
  nav.id = 'reader-nav';
  nav.style.cssText = 'position:fixed;bottom:0;left:0;right:0;' +
    'background:rgba(248,248,248,0.95);border-top:1px solid #ccc;' +
    'padding:0.4em 0.8em;display:flex;justify-content:space-between;' +
    'align-items:center;font-size:0.85em;z-index:100;backdrop-filter:blur(4px);';

  var prevBtn = document.createElement('a');
  prevBtn.textContent = '\u25C0 Prev';
  prevBtn.href = '#';
  prevBtn.style.cssText = 'text-decoration:none;color:#1a5276;padding:0.3em 0.6em;';

  var chapterLabel = document.createElement('span');
  chapterLabel.style.cssText = 'flex:1;text-align:center;overflow:hidden;' +
    'white-space:nowrap;text-overflow:ellipsis;color:#555;font-size:0.85em;';

  var nextBtn = document.createElement('a');
  nextBtn.textContent = 'Next \u25B6';
  nextBtn.href = '#';
  nextBtn.style.cssText = 'text-decoration:none;color:#1a5276;padding:0.3em 0.6em;';

  var topBtn = document.createElement('a');
  topBtn.textContent = '\u25B2 TOC';
  topBtn.href = '#TOC';
  topBtn.style.cssText = 'text-decoration:none;color:#1a5276;padding:0.3em 0.6em;margin-left:0.5em;';

  nav.appendChild(prevBtn);
  nav.appendChild(chapterLabel);
  nav.appendChild(nextBtn);
  nav.appendChild(topBtn);
  document.body.appendChild(nav);

  // Add bottom padding so nav doesn't cover content
  document.body.style.paddingBottom = '3em';

  // --- Chapter navigation logic ---
  function getCurrentChapter() {
    var scrollY = window.scrollY + 100;
    for (var i = chapters.length - 1; i >= 0; i--) {
      if (chapters[i].offsetTop <= scrollY) return i;
    }
    return 0;
  }

  function updateNav() {
    var idx = getCurrentChapter();
    if (chapters.length === 0) return;

    chapterLabel.textContent = chapters[idx] ?
      chapters[idx].textContent.trim().substring(0, 40) : '';

    if (idx > 0) {
      prevBtn.href = '#' + chapters[idx - 1].id;
      prevBtn.style.visibility = 'visible';
    } else {
      prevBtn.style.visibility = 'hidden';
    }

    if (idx < chapters.length - 1) {
      nextBtn.href = '#' + chapters[idx + 1].id;
      nextBtn.style.visibility = 'visible';
    } else {
      nextBtn.style.visibility = 'hidden';
    }
  }

  // Throttled scroll handler
  var scrollTimer;
  window.addEventListener('scroll', function() {
    if (scrollTimer) return;
    scrollTimer = setTimeout(function() {
      scrollTimer = null;
      updateNav();
    }, 100);
  });
  updateNav();

  // --- Keyboard navigation ---
  document.addEventListener('keydown', function(e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    var idx = getCurrentChapter();
    if (e.key === 'ArrowLeft' && idx > 0) {
      e.preventDefault();
      chapters[idx - 1].scrollIntoView({behavior: 'smooth'});
    } else if (e.key === 'ArrowRight' && idx < chapters.length - 1) {
      e.preventDefault();
      chapters[idx + 1].scrollIntoView({behavior: 'smooth'});
    } else if (e.key === 'Home') {
      e.preventDefault();
      window.scrollTo({top: 0, behavior: 'smooth'});
    }
  });

  // --- Reading progress bar ---
  var progress = document.createElement('div');
  progress.id = 'reading-progress';
  progress.style.cssText = 'position:fixed;top:0;left:0;height:3px;' +
    'background:#1a5276;z-index:101;transition:width 0.2s;width:0%;';
  document.body.appendChild(progress);

  window.addEventListener('scroll', function() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var pct = h > 0 ? (window.scrollY / h * 100) : 0;
    progress.style.width = pct + '%';
  });

  // --- Dark mode for floating nav ---
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    nav.style.background = 'rgba(26,26,26,0.95)';
    nav.style.borderTopColor = '#444';
    chapterLabel.style.color = '#aaa';
    prevBtn.style.color = '#6ba3f7';
    nextBtn.style.color = '#6ba3f7';
    topBtn.style.color = '#6ba3f7';
    progress.style.background = '#6ba3f7';
    if (btn) btn.style.background = '#333';
    if (btn) btn.style.borderColor = '#555';
    if (btn) btn.style.color = '#e0e0e0';
  }
})();
