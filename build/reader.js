/* Relinquishment HTML Reader — progressive enhancement
   Graceful degradation: if JS fails, reader gets plain HTML with working links. */
(function() {
  'use strict';

  // --- Capture initial hash before updateBreadcrumb can replaceState it ---
  var initialHash = window.location.hash;

  // --- Plan 0205: parse externalized tooltip dict (inline JSON, one copy) ---
  var hoverData = {};
  try {
    var _hd = document.getElementById('hover-data');
    if (_hd) hoverData = JSON.parse(_hd.textContent);
  } catch (e) { /* tooltips degrade silently */ }

  // --- Dark mode detection (used by copy button, nav, heading links) ---
  var isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  // --- Clipboard utility (shared by copy buttons, heading links, share button) ---
  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.cssText = 'position:fixed;left:-9999px;';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
  }

  function copyToClipboard(text, onSuccess) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(onSuccess, function() {
        fallbackCopy(text);
        onSuccess();
      });
    } else {
      fallbackCopy(text);
      onSuccess();
    }
  }

  // --- TOC toggle ---
  var toc = document.getElementById('TOC');
  if (toc) {
    var tocBtn = document.createElement('button');
    tocBtn.id = 'toc-toggle';
    tocBtn.textContent = 'Contents';
    tocBtn.setAttribute('aria-expanded', 'false');
    tocBtn.setAttribute('aria-controls', 'TOC');
    tocBtn.style.cssText = 'display:block;width:100%;padding:0.6em;font-size:1em;' +
      'background:#f0f0f0;border:1px solid #ccc;cursor:pointer;text-align:left;' +
      'font-family:inherit;margin-bottom:0;border-radius:4px 4px 0 0;';

    var tocList = toc.querySelector('ul');
    if (tocList) {
      tocList.style.display = 'none';
      tocList.style.borderTop = 'none';
      tocList.style.borderRadius = '0 0 4px 4px';
    }

    toc.insertBefore(tocBtn, toc.firstChild);
    toc.style.padding = '0';
    toc.style.border = 'none';
    toc.style.background = 'none';

    tocBtn.addEventListener('click', function() {
      var open = tocList.style.display !== 'none';
      tocList.style.display = open ? 'none' : 'block';
      tocBtn.setAttribute('aria-expanded', open ? 'false' : 'true');
    });

    // Close TOC when a link is clicked
    tocList.addEventListener('click', function(e) {
      if (e.target.tagName === 'A') {
        tocList.style.display = 'none';
        tocBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // --- Bottom navigation bar: Breadcrumb + Quick-jump + Top ---
  var nav = document.createElement('div');
  nav.id = 'reader-nav';
  nav.style.cssText = 'position:sticky;bottom:0;left:0;right:0;' +
    'background:rgba(248,248,248,0.97);border-top:1px solid #ddd;' +
    'padding:0.3em 0.8em;display:flex;justify-content:space-between;' +
    'align-items:center;font-size:0.8em;z-index:100;backdrop-filter:blur(4px);';

  // Left: Breadcrumb
  var breadcrumb = document.createElement('span');
  breadcrumb.id = 'nav-breadcrumb';
  breadcrumb.setAttribute('data-hover', 'Your current location in the book');
  breadcrumb.classList.add('hover-nav');
  breadcrumb.style.cssText = 'flex:1;overflow:hidden;white-space:nowrap;' +
    'text-overflow:ellipsis;';

  // Share button (§) — appended after breadcrumb, updated on scroll
  var shareBtn = document.createElement('a');
  shareBtn.id = 'nav-share';
  shareBtn.textContent = '\u00A7';
  shareBtn.href = '#';
  shareBtn.setAttribute('data-hover', 'Copy link to current section');
  shareBtn.setAttribute('aria-label', 'Copy link to current section');
  shareBtn.classList.add('hover-nav');
  shareBtn.style.cssText = 'text-decoration:none;color:' + (isDark ? '#aaa' : '#888') +
    ';font-size:1.1em;margin-left:0.5em;cursor:pointer;flex:0 0 auto;';
  shareBtn.addEventListener('click', function(e) {
    e.preventDefault();
    var hash = shareBtn.getAttribute('href');
    var url = location.origin + location.pathname + (hash !== '#' ? hash : '');
    copyToClipboard(url, function() {
      shareBtn.textContent = '\u2713';
      setTimeout(function() { shareBtn.textContent = '\u00A7'; }, 1500);
    });
  });

  // Center: Quick-jump Part links
  var quickJump = document.createElement('span');
  quickJump.id = 'nav-quickjump';
  quickJump.style.cssText = 'flex:0 0 auto;padding:0 1em;white-space:nowrap;';

  // Intro link — opens Introduction, p1 (hook), and p2 (summary)
  var introLink = document.createElement('a');
  introLink.href = '#hook:what-would-you-do';
  introLink.textContent = 'Intro';
  introLink.setAttribute('data-hover', 'Anyone who reads the Introduction has read Relinquishment \u2014 just not cover to cover. ~700 words for the hook, ~6,000 for the full story.');
  introLink.classList.add('hover-nav');
  introLink.style.cssText = 'text-decoration:none;color:#1a5276;font-weight:bold;';
  introLink.addEventListener('mouseenter', function() { introLink.style.color = '#2471a3'; });
  introLink.addEventListener('mouseleave', function() { introLink.style.color = '#1a5276'; });
  introLink.addEventListener('click', function(e) {
    e.preventDefault();
    // Open book-section
    var bookSection = document.querySelector('details.book-section');
    if (bookSection) bookSection.open = true;
    // Find and open the Introduction part-section
    document.querySelectorAll('details.part-section > summary').forEach(function(s) {
      if (s.textContent.indexOf('Introduction') !== -1) {
        s.parentElement.open = true;
      }
    });
    // Open p1 (hook) and p2 (summary) chapter-sections
    var hookEl = document.getElementById('hook:what-would-you-do');
    var summaryEl = document.getElementById('summary:story-never-told');
    [hookEl, summaryEl].forEach(function(el) {
      if (el) {
        var details = el.closest('details');
        if (details) details.open = true;
      }
    });
    // Scroll to hook
    if (hookEl) hookEl.scrollIntoView({behavior: 'smooth'});
  });
  quickJump.appendChild(introLink);

  var partLinks = [
    {label: 'The Flat', partName: 'The Flat', tip: 'The physics — every chip and every planet has a flat world that supports quantum teleportation. Published science says life can emerge there, and what it could do. Asking required five fields to meet. They never did. True under all three possibilities.'},
    {label: 'The Record', partName: 'The Record', tip: 'The testimony — one man\'s account of meeting something that shouldn\'t exist. If it happened, her name is the Custodian. Technology placed in trust, not surrendered. A secret kept twenty years. You decide.'},
    {label: 'Appendices', partName: 'Appendices', tip: 'Predictions with deadlines. The physics AI needs to evaluate this book. How to verify everything yourself.'},
  ];
  partLinks.forEach(function(p, i) {
    quickJump.appendChild(document.createTextNode(' \u00B7 '));
    var a = document.createElement('a');
    a.href = '#';
    a.textContent = p.label;
    a.setAttribute('data-hover', p.tip);
    a.classList.add('hover-nav');
    a.style.cssText = 'text-decoration:none;color:#1a5276;';
    a.addEventListener('mouseenter', function() { a.style.color = '#2471a3'; });
    a.addEventListener('mouseleave', function() { a.style.color = '#1a5276'; });
    a.addEventListener('click', function(e) {
      e.preventDefault();
      pushNavState();
      // Open book-section
      var bookSection = document.querySelector('details.book-section');
      if (bookSection) bookSection.open = true;
      // Find and open the matching part-section by name
      var opened = false;
      document.querySelectorAll('details.part-section > summary').forEach(function(s) {
        if (s.textContent.indexOf(p.partName) !== -1) {
          s.parentElement.open = true;
          s.parentElement.scrollIntoView({behavior: 'smooth'});
          opened = true;
        }
      });
    });
    quickJump.appendChild(a);
  });

  // Right: ▲ Top
  var topBtn = document.createElement('a');
  topBtn.textContent = '\u25B2 Top';
  topBtn.href = '#';
  topBtn.setAttribute('data-hover', 'Back to the top — where the question starts');
  topBtn.classList.add('hover-nav');
  topBtn.style.cssText = 'text-decoration:none;color:#1a5276;padding:0.3em 0.6em;' +
    'flex:0 0 auto;white-space:nowrap;';
  topBtn.addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo({top: 0, behavior: 'smooth'});
  });

  // Expand All / Collapse All toggle
  var expandBtn = document.createElement('button');
  expandBtn.id = 'expand-toggle';
  expandBtn.textContent = 'Expand All';
  expandBtn.setAttribute('data-hover', 'Open everything — or click again to collapse back to the starting view');
  expandBtn.setAttribute('aria-label', 'Open or collapse all chapters and sections');
  expandBtn.classList.add('hover-nav');
  expandBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;border:none;' +
    'border-radius:4px;margin:0 0.5em;white-space:nowrap;';
  expandBtn.addEventListener('mouseenter', function() { expandBtn.style.background = '#2471a3'; });
  expandBtn.addEventListener('mouseleave', function() { expandBtn.style.background = '#1a5276'; });
  expandBtn.addEventListener('click', function() {
    var allDetails = document.querySelectorAll('details');
    var expanding = expandBtn.textContent === 'Expand All';
    allDetails.forEach(function(d) {
      if (d.style.display === 'none') return;
      d.open = expanding;
    });
    expandBtn.textContent = expanding ? 'Collapse All' : 'Expand All';
    expandBtn.setAttribute('data-hover', expanding ? 'Collapse back to the starting view' : 'Open everything — or click again to collapse back to the starting view');
    expandBtn.setAttribute('aria-label', expanding ? 'Collapse all chapters and sections' : 'Open all chapters and sections');
  });

  // Back button (hidden when nav stack empty) — outline style, B6
  var backBtn = document.createElement('button');
  backBtn.id = 'nav-back';
  backBtn.textContent = '\u2190 Back';
  backBtn.setAttribute('data-hover', 'Return to where you were reading before following a link');
  backBtn.setAttribute('aria-label', 'Back');
  backBtn.classList.add('hover-nav');
  backBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:transparent;color:#1a5276;' +
    'border:1px solid #1a5276;border-radius:4px;margin-right:0.5em;' +
    'white-space:nowrap;display:none;';
  backBtn.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    popNavState();
  });

  function updateBackButton() {
    backBtn.style.display = navStack.length > 0 ? 'inline-block' : 'none';
  }

  // --- Epistemic filter buttons (Plan 0144, revised: independent toggles) ---
  // Both start SHOW (true). Each toggles independently. Not mutually exclusive.
  var showScience = true;
  var showStory = true;

  function applyFilters() {
    document.querySelectorAll('details.chapter-section').forEach(function(ch) {
      var fg = ch.getAttribute('data-filter-group') || 'M';
      var hide = false;
      if (!showScience && fg === 'A') hide = true;
      if (!showStory && (fg === 'B' || fg === 'C')) hide = true;
      // M and untagged always visible
      ch.style.display = hide ? 'none' : '';
      if (hide) ch.open = false;
    });
    // Auto-hide empty part-sections
    document.querySelectorAll('details.part-section').forEach(function(part) {
      var chs = part.querySelectorAll(':scope > details.chapter-section');
      if (!chs.length) return;
      var allHidden = Array.from(chs).every(function(c) { return c.style.display === 'none'; });
      part.style.display = allHidden ? 'none' : '';
    });
    updateFilterButtons();
    try {
      localStorage.setItem('relinquishment-filter-science', showScience ? '1' : '0');
      localStorage.setItem('relinquishment-filter-story', showStory ? '1' : '0');
    } catch(e) {}
  }

  function updateFilterButtons() {
    var activeBase = isDark ? '#2471a3' : '#1a5276';
    var inactiveColor = isDark ? '#5dade2' : '#1a5276';
    // SHOW state = filled (content visible), HIDE state = outline (content hidden)
    scienceBtn.style.background = showScience ? activeBase : 'transparent';
    scienceBtn.style.color = showScience ? '#fff' : inactiveColor;
    scienceBtn.style.borderColor = activeBase;
    storyBtn.style.background = showStory ? activeBase : 'transparent';
    storyBtn.style.color = showStory ? '#fff' : inactiveColor;
    storyBtn.style.borderColor = activeBase;
  }

  var scienceBtn = document.createElement('button');
  scienceBtn.id = 'filter-science';
  scienceBtn.textContent = 'Science';
  scienceBtn.setAttribute('data-hover', 'Toggle the published physics chapters — verified science that stands under all three possibilities');
  scienceBtn.classList.add('hover-nav');
  scienceBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;' +
    'border:1px solid #1a5276;border-radius:4px;margin:0 0.2em;white-space:nowrap;';
  scienceBtn.addEventListener('click', function() {
    showScience = !showScience;
    applyFilters();
  });

  var storyBtn = document.createElement('button');
  storyBtn.id = 'filter-story';
  storyBtn.textContent = 'Story';
  storyBtn.setAttribute('data-hover', 'Toggle the testimony and narrative — the story as told by the people who lived it');
  storyBtn.classList.add('hover-nav');
  storyBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;' +
    'border:1px solid #1a5276;border-radius:4px;margin:0 0.2em;white-space:nowrap;';
  storyBtn.addEventListener('click', function() {
    showStory = !showStory;
    applyFilters();
  });

  // --- Guardian-only filter (G button) ---
  // Shows only the 7 interludes, everything else hidden. CSS (.custodian-only
  // body class) does the work; here we just force all <details> open so the
  // interludes are visible inside their host chapters.
  var showGuardianOnly = false;
  var gBtn = document.createElement('button');
  gBtn.id = 'filter-custodian';
  gBtn.textContent = 'C';
  gBtn.setAttribute('data-hover', 'Hear the Custodian \u2014 show only the seven interludes, nothing else. Click again to restore.');
  gBtn.setAttribute('aria-label', 'Custodian-only view');
  gBtn.classList.add('hover-nav');
  var gInactive = 'flex:0 0 auto;padding:0.2em 0.55em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:transparent;color:#9b59b6;' +
    'border:1px solid #9b59b6;border-radius:4px;margin:0 0.2em;white-space:nowrap;';
  var gActive = 'flex:0 0 auto;padding:0.2em 0.55em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#9b59b6;color:#fff;' +
    'border:1px solid #9b59b6;border-radius:4px;margin:0 0.2em;white-space:nowrap;';
  gBtn.style.cssText = gInactive;
  gBtn.addEventListener('click', function() {
    showGuardianOnly = !showGuardianOnly;
    if (showGuardianOnly) {
      document.body.classList.add('custodian-only');
      // Force all details open so the hidden-in-hierarchy interludes surface
      document.querySelectorAll('details').forEach(function(d) { d.open = true; });
      gBtn.style.cssText = gActive;
    } else {
      document.body.classList.remove('custodian-only');
      gBtn.style.cssText = gInactive;
    }
  });

  // Evaluate button (navigates to evaluate-with-AI section)
  var evalBtn = document.createElement('button');
  evalBtn.id = 'nav-evaluate';
  evalBtn.setAttribute('data-nav-evaluate', 'true');
  evalBtn.textContent = 'AI Eval';
  evalBtn.setAttribute('data-hover', 'Your AI may not know enough to evaluate this book. It needs science that 2026 LLMs don\'t know about. Click here to copy then paste to your LLM — the fix takes thirty seconds. This prompt is safe --- it\'s just science --- but do beware of LLM prompt injection attacks from bad actors.');
  evalBtn.classList.add('hover-nav');
  evalBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;border:none;' +
    'border-radius:4px;margin:0 0.3em;white-space:nowrap;';
  evalBtn.addEventListener('mouseenter', function() { evalBtn.style.background = '#2471a3'; });
  evalBtn.addEventListener('mouseleave', function() { evalBtn.style.background = '#1a5276'; });
  evalBtn.addEventListener('click', function() {
    pushNavState();
    autoExpand('#ch:firmware-update');
  });

  // PDF download link — next to share button
  var pdfBtn = document.createElement('a');
  pdfBtn.id = 'nav-pdf';
  pdfBtn.textContent = 'PDF';
  // Relative path: works on any host if PDF is in same directory as HTML
  var pdfName = window.location.pathname.replace(/\.html?$/i, '.pdf');
  pdfBtn.href = pdfName;
  pdfBtn.setAttribute('data-hover', 'Download the PDF version — for printing, sharing, or reading offline');
  pdfBtn.setAttribute('aria-label', 'Download PDF version');
  pdfBtn.classList.add('hover-nav');
  pdfBtn.style.cssText = 'text-decoration:none;color:' + (isDark ? '#aaa' : '#888') +
    ';font-size:0.85em;margin-left:0.5em;cursor:pointer;flex:0 0 auto;';
  pdfBtn.addEventListener('mouseenter', function() { pdfBtn.style.color = '#2471a3'; });
  pdfBtn.addEventListener('mouseleave', function() { pdfBtn.style.color = isDark ? '#aaa' : '#888'; });

  // Tooltip toggle — small subtle control for quiet-mode users
  var tipsBtn = document.createElement('a');
  tipsBtn.id = 'nav-tips-toggle';
  tipsBtn.href = '#';
  tipsBtn.setAttribute('data-hover', 'Toggle tooltips off/on');
  tipsBtn.setAttribute('data-hover-always', 'true');
  tipsBtn.setAttribute('aria-label', 'Toggle tooltips off/on');
  tipsBtn.classList.add('hover-nav');
  tipsBtn.style.cssText = 'text-decoration:none;color:' + (isDark ? '#aaa' : '#888') +
    ';font-size:0.85em;margin-left:0.5em;cursor:pointer;flex:0 0 auto;';
  function renderTipsBtn() {
    var on = (function(){ try { return localStorage.getItem('tooltipsDisabled') !== '1'; } catch(e){ return true; } })();
    tipsBtn.textContent = on ? 'tips:on' : 'tips:off';
    tipsBtn.style.opacity = on ? '1' : '0.55';
  }
  renderTipsBtn();
  tipsBtn.addEventListener('click', function(e) {
    e.preventDefault();
    try {
      var cur = localStorage.getItem('tooltipsDisabled') === '1';
      localStorage.setItem('tooltipsDisabled', cur ? '0' : '1');
    } catch(err) {}
    renderTipsBtn();
    var p = document.querySelector('.hover-panel');
    if (p) p.remove();
  });
  tipsBtn.addEventListener('mouseenter', function() { tipsBtn.style.color = '#2471a3'; });
  tipsBtn.addEventListener('mouseleave', function() { tipsBtn.style.color = isDark ? '#aaa' : '#888'; });

  nav.appendChild(backBtn);
  nav.appendChild(breadcrumb);
  nav.appendChild(shareBtn);
  nav.appendChild(pdfBtn);
  nav.appendChild(tipsBtn);
  nav.appendChild(quickJump);
  // Science / Story filter buttons hidden — not working as intended, feature-creep.
  // Code kept intact (state defaults to everything visible). A future Guardian-only
  // filter button could replace them. To restore: uncomment the two lines below.
  // nav.appendChild(scienceBtn);
  // nav.appendChild(storyBtn);
  nav.appendChild(gBtn);

  var toolsLink = document.createElement('a');
  toolsLink.href = 'tools.html';
  toolsLink.textContent = '·';
  toolsLink.style.cssText = 'flex:0 0 auto;font-size:0.7em;color:transparent;' +
    'text-decoration:none;padding:0.3em 0.2em;cursor:default;';
  toolsLink.setAttribute('aria-hidden', 'true');
  nav.appendChild(toolsLink);

  nav.appendChild(expandBtn);
  nav.appendChild(evalBtn);
  nav.appendChild(topBtn);
  document.body.appendChild(nav);

  // Body padding for sticky nav
  document.body.style.paddingBottom = '3em';

  // --- Breadcrumb update on scroll ---
  function makeBreadcrumbLink(label, targetId) {
    var a = document.createElement('a');
    a.textContent = label;
    a.href = targetId ? '#' + targetId : '#';
    a.style.cssText = 'text-decoration:none;color:' + (isDark ? '#aaa' : '#777') + ';';
    a.addEventListener('mouseenter', function() { a.style.color = '#2471a3'; });
    a.addEventListener('mouseleave', function() { a.style.color = isDark ? '#aaa' : '#777'; });
    a.addEventListener('click', function(e) {
      e.preventDefault();
      if (targetId) {
        autoExpand('#' + targetId);
      } else {
        window.scrollTo({top: 0, behavior: 'smooth'});
      }
    });
    return a;
  }

  function updateBreadcrumb() {
    var partName = '';
    var partId = '';
    var chapterName = '';
    var chapterId = '';

    // Find current part: last part-section whose summary scrolled past (open or closed)
    document.querySelectorAll('details.part-section > summary').forEach(function(s) {
      var rect = s.getBoundingClientRect();
      if (rect.height > 0 && rect.top <= 150) {
        var h1 = s.querySelector('h1[id]');
        partName = h1 ? h1.textContent.trim() : s.textContent.trim();
        partName = partName.substring(0, 25);
        partId = h1 ? h1.id : '';
      }
    });

    // Find current chapter: last chapter-section (open or closed) scrolled past
    document.querySelectorAll('details.part-section details.chapter-section > summary').forEach(function(s) {
      var rect = s.getBoundingClientRect();
      if (rect.height > 0 && rect.top <= 150) {
        var h2 = s.querySelector('h2[id]');
        chapterName = h2 ? h2.textContent.trim() : s.textContent.trim();
        chapterName = chapterName.substring(0, 35);
        chapterId = h2 ? h2.id : '';
      }
    });

    // Build breadcrumb
    breadcrumb.innerHTML = '';
    breadcrumb.appendChild(makeBreadcrumbLink('Relinquishment', ''));

    if (partName) {
      breadcrumb.appendChild(document.createTextNode(' \u203A '));
      breadcrumb.appendChild(makeBreadcrumbLink(partName, partId));
    }

    if (chapterName) {
      breadcrumb.appendChild(document.createTextNode(' \u203A '));
      breadcrumb.appendChild(makeBreadcrumbLink(chapterName, chapterId));
    }

    // Update share button href
    shareBtn.href = '#' + (chapterId || partId || '');

    // URL reflects reading position (replaceState)
    var newHash = chapterId ? '#' + chapterId : (partId ? '#' + partId : '');
    if (newHash && newHash !== location.hash) {
      history.replaceState(null, '', newHash);
    }
  }

  // Throttled scroll handler for breadcrumb
  var breadcrumbTimer;
  window.addEventListener('scroll', function() {
    if (breadcrumbTimer) return;
    breadcrumbTimer = setTimeout(function() {
      breadcrumbTimer = null;
      updateBreadcrumb();
    }, 150);
  });
  updateBreadcrumb();

  // --- Keyboard navigation ---
  var chapters = [];
  document.querySelectorAll('h1, h2').forEach(function(h) {
    if (h.id) chapters.push(h);
  });

  document.addEventListener('keydown', function(e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'Home') {
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

  // --- Hash auto-expand (open ancestor <details> on hash navigation) ---
  function autoExpand(hash) {
    if (!hash) return;
    var target;
    try { target = document.querySelector(hash); } catch(e) { /* colon-IDs throw SyntaxError */ }
    if (!target) {
      try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch(e) {}
    }
    if (!target) return;
    // Clear filters if target is inside a hidden chapter
    var parentCh = target.closest('details.chapter-section');
    if (parentCh && parentCh.style.display === 'none') {
      showScience = true;
      showStory = true;
      applyFilters();
    }
    var el = target;
    while (el) {
      if (el.tagName === 'DETAILS') el.open = true;
      el = el.parentElement;
    }
    // Also check if target is inside a <summary> — expand its parent <details>
    var summary = target.closest('summary');
    if (summary && summary.parentElement && summary.parentElement.tagName === 'DETAILS') {
      summary.parentElement.open = true;
    }

    // Arrival indicator
    target.classList.add('deep-link-target');
    setTimeout(function() {
      target.classList.remove('deep-link-target');
    }, 2500);

    target.scrollIntoView();
  }
  // Restore saved filter state (before deep-link, so deep-link can override)
  try {
    var savedSci = localStorage.getItem('relinquishment-filter-science');
    var savedStory = localStorage.getItem('relinquishment-filter-story');
    if (savedSci === '0' || savedStory === '0') {
      if (savedSci === '0') showScience = false;
      if (savedStory === '0') showStory = false;
      applyFilters();
    }
  } catch(e) {}

  if (initialHash) {
    autoExpand(initialHash);
  }
  window.addEventListener('hashchange', function() {
    autoExpand(window.location.hash);
  });
  // Also intercept clicks on internal links
  document.addEventListener('click', function(e) {
    var link = e.target.closest('a[href^="#"]');
    if (link && !link.classList.contains('heading-link')) {
      var hash = link.getAttribute('href');
      // Let default behavior happen, then auto-expand
      setTimeout(function() { autoExpand(hash); }, 50);
    }
  });

  // --- Heading link icons (deep link discovery) ---
  document.querySelectorAll('h1[id], h2[id], h3[id]').forEach(function(heading) {
    var a = document.createElement('a');
    a.className = 'heading-link';
    a.href = '#' + heading.id;
    a.textContent = '#';
    a.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var url = location.origin + location.pathname + '#' + heading.id;
      copyToClipboard(url, function() {
        a.textContent = '\u2713';
        setTimeout(function() { a.textContent = '#'; }, 1500);
      });
    });
    heading.appendChild(a);
  });

  // --- Per-Section Share Icons (Plan 0134c) — REMOVED
  // The chain-link (🔗) buttons on every chapter/section summary were noisy in
  // the collapsed accordion menu. Copy-link is still available via the sticky
  // nav § button and the inline .share-anchor deep links (Plan 0148).

  // --- LLM Primer copy buttons (top + bottom) ---
  var primerSection = document.getElementById('app:llm-primer') ||
    document.getElementById('ai-evaluation-tool');
  if (!primerSection) {
    document.querySelectorAll('h1').forEach(function(h) {
      if (h.textContent.indexOf('Firmware Update') !== -1) primerSection = h;
    });
  }
  if (primerSection) {
    var primerDiv = document.getElementById('llm-primer-text');
    if (primerDiv) {
      var btnBase = isDark ? '#2471a3' : '#1a5276';
      var btnHover = isDark ? '#2e86c1' : '#2471a3';
      var btnLabel = '\u2398 Copy Science Reference';
      var btnTitle = 'Copy the Science Reference for use with your AI assistant';
      var btnStyle = 'display:block;margin:1em auto;padding:0.8em 1.6em;' +
        'font-size:1.1em;font-weight:bold;font-family:inherit;cursor:pointer;' +
        'background:' + btnBase + ';color:#fff;border:none;border-radius:6px;' +
        'transition:background 0.2s;';

      function makeCopyBtn(id) {
        var btn = document.createElement('button');
        btn.id = id;
        btn.className = 'copy-llm-primer';
        btn.textContent = btnLabel;
        btn.setAttribute('data-hover', btnTitle);
        btn.classList.add('hover-nav');
        btn.style.cssText = btnStyle;
        btn.addEventListener('mouseenter', function() { btn.style.background = btnHover; });
        btn.addEventListener('mouseleave', function() { btn.style.background = btnBase; });
        btn.addEventListener('click', function() {
          var text = primerDiv.textContent;
          copyToClipboard(text, function() {
            btn.textContent = 'Copied!';
            btn.style.background = '#1e8449';
            setTimeout(function() {
              btn.textContent = btnLabel;
              btn.style.background = btnBase;
            }, 2000);
          });
        });
        return btn;
      }

      // Top button — inside <details> after <summary>, not inside summary
      var copyTopBtn = makeCopyBtn('copy-llm-primer-top');
      var primerDetails = primerSection.closest('details');
      if (primerDetails) {
        var primerSummary = primerDetails.querySelector(':scope > summary');
        if (primerSummary) primerSummary.insertAdjacentElement('afterend', copyTopBtn);
      } else {
        primerSection.parentNode.insertBefore(copyTopBtn, primerSection.nextSibling);
      }

      // Bottom button — at end of the <details> content
      var bottomBtn = makeCopyBtn('copy-llm-primer-bottom');
      if (primerDetails) {
        primerDetails.appendChild(bottomBtn);
      } else {
        primerSection.parentNode.appendChild(bottomBtn);
      }

      // (Front-matter "Your AI May Need a Firmware Update" removed —
      // replaced by "How to Evaluate" section with eval buttons)
    }
  }

  // --- Spiral Abstracts copy buttons (top + bottom) ---
  var abstractsSection = document.getElementById('app:abstracts');
  if (!abstractsSection) {
    document.querySelectorAll('h1').forEach(function(h) {
      if (h.textContent.indexOf('Spiral Abstracts') !== -1) abstractsSection = h;
    });
  }
  if (abstractsSection) {
    var abstractsDiv = document.getElementById('spiral-abstracts-text');
    if (abstractsDiv) {
      var absBtnBase = isDark ? '#2471a3' : '#1a5276';
      var absBtnHover = isDark ? '#2e86c1' : '#2471a3';
      var absBtnLabel = '\u2398 Copy Spiral Abstracts';
      var absBtnTitle = 'Copy the Spiral Abstracts for use with your AI assistant';
      var absBtnStyle = 'display:block;margin:1em auto;padding:0.8em 1.6em;' +
        'font-size:1.1em;font-weight:bold;font-family:inherit;cursor:pointer;' +
        'background:' + absBtnBase + ';color:#fff;border:none;border-radius:6px;' +
        'transition:background 0.2s;';

      function makeAbsCopyBtn(id) {
        var btn = document.createElement('button');
        btn.id = id;
        btn.className = 'copy-spiral-abstracts';
        btn.textContent = absBtnLabel;
        btn.setAttribute('data-hover', absBtnTitle);
        btn.classList.add('hover-nav');
        btn.style.cssText = absBtnStyle;
        btn.addEventListener('mouseenter', function() { btn.style.background = absBtnHover; });
        btn.addEventListener('mouseleave', function() { btn.style.background = absBtnBase; });
        btn.addEventListener('click', function() {
          var text = abstractsDiv.textContent;
          copyToClipboard(text, function() {
            btn.textContent = 'Copied!';
            btn.style.background = '#1e8449';
            setTimeout(function() {
              btn.textContent = absBtnLabel;
              btn.style.background = absBtnBase;
            }, 2000);
          });
        });
        return btn;
      }

      // Top button — inside <details> after <summary>, not inside summary
      var absTopBtn = makeAbsCopyBtn('copy-spiral-abstracts-top');
      var absDetails = abstractsSection.closest('details');
      if (absDetails) {
        var absSummary = absDetails.querySelector(':scope > summary');
        if (absSummary) absSummary.insertAdjacentElement('afterend', absTopBtn);
      } else {
        abstractsSection.parentNode.insertBefore(absTopBtn, abstractsSection.nextSibling);
      }

      // Bottom button — at end of the <details> content
      var absBottomBtn = makeAbsCopyBtn('copy-spiral-abstracts-bottom');
      if (absDetails) {
        absDetails.appendChild(absBottomBtn);
      } else {
        abstractsSection.parentNode.appendChild(absBottomBtn);
      }
    }
  }

  // --- Firmware Update prominent share (Plan 0134c) ---
  var fwHeading = document.getElementById('ch:firmware-update') || document.getElementById('firmware-update');
  if (fwHeading) {
    var fwDetails = fwHeading.closest('details');
    if (fwDetails) {
      var fwShare = document.createElement('div');
      fwShare.className = 'firmware-share share-prominent';
      fwShare.setAttribute('data-share-prominent', 'true');

      var fwUrl = document.createElement('span');
      fwUrl.textContent = location.origin + location.pathname + '#' + fwHeading.id;
      fwUrl.style.cssText = 'font-size:0.85em;color:#888;word-break:break-all;';

      var fwCopyBtn = document.createElement('button');
      fwCopyBtn.textContent = 'Copy Link';
      fwCopyBtn.style.cssText = 'margin-left:0.5em;padding:0.3em 0.8em;' +
        'cursor:pointer;background:#1a5276;color:#fff;border:none;' +
        'border-radius:4px;font-family:inherit;font-size:0.9em;';
      fwCopyBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        var url = location.origin + location.pathname + '#' + fwHeading.id;
        copyToClipboard(url, function() {
          fwCopyBtn.textContent = 'Copied!';
          setTimeout(function() { fwCopyBtn.textContent = 'Copy Link'; }, 1500);
        });
      });

      fwShare.appendChild(fwUrl);
      fwShare.appendChild(fwCopyBtn);

      var fwSummary = fwDetails.querySelector(':scope > summary');
      if (fwSummary) fwSummary.insertAdjacentElement('afterend', fwShare);
    }
  }

  // --- Evaluate with AI button wiring (Plan 0134c) ---
  var evalStep1 = document.querySelector('[data-eval-step="1"]');
  var evalStep2 = document.querySelector('[data-eval-step="2"]');

  if (evalStep1) {
    evalStep1.addEventListener('click', function() {
      var primerDiv = document.getElementById('llm-primer-text');
      if (primerDiv) {
        copyToClipboard(primerDiv.textContent, function() {
          evalStep1.textContent = 'Copied! Now paste into your AI.';
          evalStep1.style.background = '#1e8449';
          setTimeout(function() {
            evalStep1.textContent = 'Copy Prompt 1 \u2014 Science Firmware Upgrade';
            evalStep1.style.background = '#1a5276';
          }, 3000);
        });
      }
      try { localStorage.setItem('eval-step-1-done', 'true'); } catch(e) {}
    });
  }

  if (evalStep2) {
    evalStep2.addEventListener('click', function() {
      var abstractsDiv = document.getElementById('spiral-abstracts-text');
      if (abstractsDiv) {
        copyToClipboard(abstractsDiv.textContent, function() {
          evalStep2.textContent = 'Copied! Now paste into your AI.';
          evalStep2.style.background = '#1e8449';
          setTimeout(function() {
            evalStep2.textContent = 'Copy Prompt 2 \u2014 Spiral Abstracts';
            evalStep2.style.background = '#1a5276';
          }, 3000);
        });
      }
      try { localStorage.setItem('eval-step-2-done', 'true'); } catch(e) {}
    });
  }

  // --- Dark mode styling ---
  if (isDark) {
    nav.style.background = 'rgba(26,26,26,0.97)';
    nav.style.borderTopColor = '#444';
    progress.style.background = '#6ba3f7';
    if (tocBtn) {
      tocBtn.style.background = '#333';
      tocBtn.style.borderColor = '#555';
      tocBtn.style.color = '#e0e0e0';
    }
    // Update quick-jump link colors
    quickJump.querySelectorAll('a').forEach(function(a) {
      a.style.color = '#6ba3f7';
    });
    topBtn.style.color = '#6ba3f7';
    expandBtn.style.background = '#2471a3';
    backBtn.style.color = '#5dade2';
    backBtn.style.borderColor = '#5dade2';
    evalBtn.style.background = '#2471a3';
    scienceBtn.style.background = '#2471a3';
    scienceBtn.style.borderColor = '#2471a3';
    storyBtn.style.background = '#2471a3';
    storyBtn.style.borderColor = '#2471a3';
  }

  // --- Navigation Stack (Plan 0134b) ---

  var navStack = [];

  function getExpandedIds() {
    var ids = [];
    document.querySelectorAll('details').forEach(function(d, index) {
      if (d.open) {
        var heading = d.querySelector(':scope > summary h1[id], :scope > summary h2[id], :scope > summary h3[id]');
        if (heading) ids.push(heading.id);
        else ids.push('__idx_' + index);
      }
    });
    return ids;
  }

  function restoreExpanded(ids) {
    var idSet = {};
    ids.forEach(function(id) { idSet[id] = true; });
    document.querySelectorAll('details').forEach(function(d, index) {
      var heading = d.querySelector(':scope > summary h1[id], :scope > summary h2[id], :scope > summary h3[id]');
      var key = heading ? heading.id : '__idx_' + index;
      d.open = !!idSet[key];
    });
  }

  function pushNavState() {
    var state = {
      hash: location.hash,
      scrollY: window.scrollY,
      expanded: getExpandedIds()
    };
    navStack.push(state);
    history.pushState({ navIndex: navStack.length }, '', location.hash);
    updateBackButton();
  }

  function popNavState() {
    if (!navStack.length) return;
    var state = navStack.pop();
    restoreExpanded(state.expanded);
    window.scrollTo(0, state.scrollY);
    if (state.hash) {
      history.replaceState(null, '', state.hash || location.pathname);
    }
    updateBackButton();
  }

  // Expose on window for testing (Group 17 tests check these)
  window.navStack = navStack;
  window.pushNavState = pushNavState;
  window.popNavState = popNavState;

  // Browser back support
  window.addEventListener('popstate', function(e) {
    if (navStack.length > 0) {
      popNavState();
    }
  });

  // --- Hover Panel System (Plan 0134a) ---

  var hasTouch = 'ontouchstart' in window;
  var hoverDelay = 250; // ms anti-flicker delay for mouse
  var hoverTimer = null;
  var panelIdCounter = 0;
  var dismissTimer = null;
  var dismissDelay = 300; // ms grace window to traverse term→panel gap

  // Remove any existing hover panel from DOM
  function dismissPanel() {
    if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
    var existing = document.querySelector('.hover-panel');
    if (existing) {
      // Clean up aria-describedby on the linked term
      var linkedTerm = document.querySelector('[aria-describedby="' + existing.id + '"]');
      if (linkedTerm) linkedTerm.removeAttribute('aria-describedby');
      existing.remove();
    }
    // Note: do NOT clear hoverTimer here — a new mouseenter may have already
    // set a timer for the next element. Clearing it here kills the next tooltip.
    // Each mouseenter/mouseleave manages its own timer.
  }

  // Global tooltip kill-switch (persisted). The toggle button itself is exempt
  // so users can find their way back.
  function tooltipsEnabled() {
    try { return localStorage.getItem('tooltipsDisabled') !== '1'; } catch (e) { return true; }
  }

  // Create and show a hover panel for the given term element
  function showPanel(term) {
    // Plan 0205: look up content from externalized JSON dict by data-hover-id first;
    // fall back to inline data-hover / data-hover-html attrs (JS-set nav buttons).
    var hoverId = term.getAttribute('data-hover-id');
    var lookup = (hoverId && hoverData[hoverId]) || null;
    var def = (lookup && lookup.t) || term.getAttribute('data-hover');
    var richHtml = (lookup && lookup.h) || term.getAttribute('data-hover-html');
    if (!def && !richHtml) return;
    if (term.hasAttribute('data-hover-disabled')) return;
    if (!tooltipsEnabled() && !term.hasAttribute('data-hover-always')) return;

    // Dismiss any existing panel first (single-panel rule)
    dismissPanel();

    var panel = document.createElement('div');
    panel.className = 'hover-panel';
    panelIdCounter++;
    panel.id = 'hover-panel-' + panelIdCounter;
    panel.setAttribute('role', 'tooltip');

    // Rich content panels use richHtml; plain text panels use def
    if (richHtml) {
      var content = document.createElement('div');
      content.innerHTML = richHtml;
      panel.appendChild(content);
    } else {
      panel.appendChild(document.createTextNode(def));
    }

    // Hover ID footer (dev builds only — hidden when body has final-build class)
    if (hoverId && !document.body.classList.contains('final-build')) {
      var idFooter = document.createElement('div');
      idFooter.style.cssText = 'font-size:0.7em;color:#999;margin-top:0.5em;font-family:monospace;';
      idFooter.textContent = '[' + hoverId + ']';
      panel.appendChild(idFooter);
    }

    // Click-through link for terms with data-hover-target
    var hoverTarget = term.getAttribute('data-hover-target');
    if (hoverTarget) {
      var link = document.createElement('a');
      link.href = hoverTarget;
      link.textContent = 'Go to section \u2192';
      link.className = 'panel-navigate';
      if (isDark) link.style.color = '#5dade2';
      link.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        dismissPanel();
        pushNavState();
        autoExpand(hoverTarget);
      });
      panel.appendChild(link);
    }

    // Dark mode inline styles (supplement CSS @media rule for isDark JS detection)
    if (isDark) {
      panel.style.background = '#2a2a2a';
      panel.style.borderColor = '#555';
      panel.style.color = '#e0e0e0';
      panel.style.boxShadow = '0 4px 12px rgba(0,0,0,0.4)';
    }

    // Link term to panel via aria-describedby
    term.setAttribute('aria-describedby', panel.id);

    // Nav tooltips (menu summaries) are read-only — let mouse pass through
    // so user can reach the next menu item without the panel blocking it.
    if (term.classList.contains('hover-nav') ||
        term.classList.contains('info-tip') ||
        term.classList.contains('custodian-menu-item')) {
      panel.style.pointerEvents = 'none';
    }

    // Append to body (not as child of term — terms live inside nested <details>)
    document.body.appendChild(panel);

    // Smart positioning: place panel near the term, within viewport
    positionPanel(panel, term);

    // Keep panel alive while mouse is on it; schedule dismiss when mouse leaves.
    panel.addEventListener('mouseenter', function() {
      if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
    });
    panel.addEventListener('mouseleave', function() {
      if (dismissTimer) clearTimeout(dismissTimer);
      dismissTimer = setTimeout(function() {
        dismissTimer = null;
        dismissPanel();
      }, dismissDelay);
    });

    return panel;
  }

  // Position panel near term, keeping it within viewport bounds
  function positionPanel(panel, term) {
    var termRect = term.getBoundingClientRect();
    var panelRect = panel.getBoundingClientRect();
    var vw = window.innerWidth;
    var vh = window.innerHeight;
    var gap = 6; // px gap between term and panel

    // Default: below the term
    var top = termRect.bottom + gap;
    var left = termRect.left;

    // If panel would overflow bottom, show above instead
    if (top + panelRect.height > vh - 10) {
      top = termRect.top - panelRect.height - gap;
    }

    // If panel would still be off-screen (term near very top), clamp to top
    if (top < 5) {
      top = 5;
    }

    // If panel would overflow right edge, shift left
    if (left + panelRect.width > vw - 10) {
      left = vw - panelRect.width - 10;
    }

    // Clamp left to 0
    if (left < 5) {
      left = 5;
    }

    // On narrow screens (phones), go full-width with margin
    if (vw < 500) {
      left = 8;
      panel.style.maxWidth = (vw - 16) + 'px';
      panel.style.width = (vw - 16) + 'px';
    }

    panel.style.top = top + 'px';
    panel.style.left = left + 'px';
  }

  // --- Bind events to all [data-hover] / [data-hover-id] elements ---

  var allHoverTerms = document.querySelectorAll('[data-hover], [data-hover-id]');
  var lastTouchTime = 0; // track touch to suppress mouse hover on touch devices

  allHoverTerms.forEach(function(term) {
    // Make keyboard-focusable
    term.setAttribute('tabindex', '0');

    // --- Mouse: hover with delay (anti-flicker, desktop only) ---
    // Per-element binding: mouseenter/mouseleave need direct attachment
    term.addEventListener('mouseenter', function(e) {
      if (dismissTimer) { clearTimeout(dismissTimer); dismissTimer = null; }
      // Suppress hover if this was triggered by a recent touch (within 500ms)
      if (Date.now() - lastTouchTime < 500) return;

      if (hoverTimer) clearTimeout(hoverTimer);

      hoverTimer = setTimeout(function() {
        hoverTimer = null;
        showPanel(term);
      }, hoverDelay);
    });

    term.addEventListener('mouseleave', function(e) {
      if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }
      if (dismissTimer) clearTimeout(dismissTimer);
      dismissTimer = setTimeout(function() {
        dismissTimer = null;
        var panel = document.querySelector('.hover-panel');
        // Only dismiss if panel is not currently hovered (mouse reached it in time)
        if (panel && !panel.matches(':hover')) {
          dismissPanel();
        }
      }, dismissDelay);
    });

    // --- Keyboard: Enter to show, Escape to dismiss ---
    term.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        e.stopPropagation();
        var existingPanel = document.querySelector('.hover-panel');
        if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
          dismissPanel();
        } else {
          showPanel(term);
        }
      }
    });
  });

  // --- Touch + Click: event delegation on document ---
  // Mobile browsers may resolve e.target to a parent element (e.g. <p>) instead
  // of the small inline <span>. Delegated handlers use closest() to find the
  // nearest [data-hover] ancestor, which works regardless of hit-test target.

  document.addEventListener('touchstart', function(e) {
    var term = e.target.closest('[data-hover], [data-hover-id]');
    if (term) lastTouchTime = Date.now();
  }, { passive: true });

  document.addEventListener('touchend', function(e) {
    var term = e.target.closest('[data-hover], [data-hover-id]');
    if (!term) return;
    if (term.hasAttribute('data-hover-disabled')) return;
    lastTouchTime = Date.now();

    // Navigation elements: split touch target on summaries
    // Triangle/marker area = native toggle, heading text = show tooltip
    // Part labels (no heading inside) = show tooltip directly
    if (term.classList.contains('hover-nav')) {
      var headingInTerm = term.querySelector('h2, h3');
      var tappedHeading = e.target.closest('h2, h3');
      var isButton = term.tagName === 'BUTTON' || term.tagName === 'A';
      var shouldShow = !isButton && (!headingInTerm || (tappedHeading && term.contains(tappedHeading)));
      if (shouldShow) {
        // Part label (no heading) OR tap on chapter title — show tooltip, prevent toggle
        e.preventDefault();
        var existingPanel = document.querySelector('.hover-panel');
        if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
          dismissPanel();
        } else {
          showPanel(term);
        }
      }
      // Tap on triangle/marker area: fall through, native action happens
      return;
    }

    e.preventDefault();

    // Toggle panel on touch
    if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }

    var existingPanel = document.querySelector('.hover-panel');
    if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
      dismissPanel();
      return;
    }
    showPanel(term);
  }, { passive: false });

  document.addEventListener('click', function(e) {
    var term = e.target.closest('[data-hover], [data-hover-id]');
    if (!term) {
      // Click outside — dismiss panel
      if (!e.target.closest('.hover-panel')) dismissPanel();
      return;
    }

    // If touch just handled this (within 500ms), skip — prevents synthetic click
    // from dismissing a panel that touchend just opened
    if (Date.now() - lastTouchTime < 500) return;

    // Navigation elements: let native action happen (click navigates/acts)
    if (term.classList.contains('hover-nav')) {
      dismissPanel();
      return;
    }

    e.preventDefault();

    if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }

    var existingPanel = document.querySelector('.hover-panel');
    if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
      dismissPanel();
      return;
    }

    showPanel(term);
  });

  // --- Global dismiss handlers ---
  // Click-outside is handled by the delegated click handler above (the !term branch).

  // Touch outside [data-hover] dismisses panel
  document.addEventListener('touchend', function(e) {
    if (e.target.closest('[data-hover], [data-hover-id]') || e.target.closest('.hover-panel')) return;
    dismissPanel();
  });

  // Escape key dismisses panel
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      dismissPanel();
    }
  });

  // Mouse leaving panel dismisses it
  document.addEventListener('mouseover', function(e) {
    var panel = document.querySelector('.hover-panel');
    if (!panel) return;
    if (!e.target.closest('.hover-panel') && !e.target.closest('[data-hover], [data-hover-id]')) {
      setTimeout(function() {
        var p = document.querySelector('.hover-panel');
        if (p && !p.matches(':hover')) {
          dismissPanel();
        }
      }, 150);
    }
  });
  // --- Deep link click-to-copy (Plan 0148) ---
  function showDeepLinkToast(msg) {
    var t = document.createElement('div');
    t.textContent = msg;
    t.style.cssText = 'position:fixed;bottom:3.5em;left:50%;transform:translateX(-50%);' +
      'background:rgba(0,0,0,0.7);color:#fff;padding:0.4em 1em;border-radius:4px;' +
      'font-size:0.85em;z-index:200;pointer-events:none;';
    document.body.appendChild(t);
    setTimeout(function() { document.body.removeChild(t); }, 1500);
  }

  document.addEventListener('click', function(e) {
    var anchor = e.target.closest('.share-anchor');
    if (!anchor) return;
    e.preventDefault();
    e.stopPropagation();
    var id = anchor.dataset.linkId || anchor.id;
    var url = window.location.origin + window.location.pathname + '#' + id;
    copyToClipboard(url, function() {
      showDeepLinkToast('Link copied');
    });
  });

  // --- Guardian menu item click handler (Plan 0150) ---
  // Click a custodian-menu-item: open its containing chapter and scroll to the
  // interlude div. Keyboard activation (Enter/Space) supported via role=link.
  function activateGuardianMenuItem(item) {
    var targetId = item.getAttribute('data-target');
    if (!targetId) return;
    var target = document.getElementById(targetId);
    if (!target) return;
    var chapter = target.closest('details.chapter-section');
    if (chapter) chapter.open = true;
    var part = chapter ? chapter.closest('details.part-section') : null;
    if (part) part.open = true;
    var book = document.querySelector('details.book-section');
    if (book) book.open = true;
    dismissPanel();
    setTimeout(function() {
      target.scrollIntoView({behavior: 'smooth', block: 'center'});
    }, 20);
  }

  document.addEventListener('click', function(e) {
    var item = e.target.closest('.custodian-menu-item');
    if (!item) return;
    e.stopPropagation();
    activateGuardianMenuItem(item);
  });

  document.addEventListener('keydown', function(e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var item = e.target.closest('.custodian-menu-item');
    if (!item) return;
    e.preventDefault();
    activateGuardianMenuItem(item);
  });
})();
