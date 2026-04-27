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
  function copyToClipboard(text, onSuccess) {
    navigator.clipboard.writeText(text).then(onSuccess);
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

  // Magnetosphere toggle button (◐)
  var msToggle = document.createElement('a');
  msToggle.href = '#';
  msToggle.id = 'nav-ms-toggle';
  msToggle.textContent = '◐';
  msToggle.setAttribute('data-hover', 'Toggle cover illustration');
  msToggle.classList.add('hover-nav');
  msToggle.style.cssText = 'text-decoration:none;color:' +
    (isDark ? '#aaa' : '#888') + ';font-size:1.1em;cursor:pointer;' +
    'margin-left:0.5em;flex:0 0 auto;';
  msToggle.addEventListener('mouseenter', function() { msToggle.style.color = '#2471a3'; });
  msToggle.addEventListener('mouseleave', function() { msToggle.style.color = isDark ? '#aaa' : '#888'; });

  var toolsLink = document.createElement('a');
  toolsLink.href = 'https://relinquishment.ai/tools.html';
  toolsLink.textContent = '·';
  toolsLink.style.cssText = 'flex:0 0 auto;font-size:0.7em;color:transparent;' +
    'text-decoration:none;padding:0.3em 0.2em;cursor:default;';
  toolsLink.setAttribute('aria-hidden', 'true');

  // --- Nav bar: 5 items only (Back, breadcrumb, §, AI Eval, ▲ Top) ---
  nav.appendChild(backBtn);
  nav.appendChild(breadcrumb);
  nav.appendChild(shareBtn);
  nav.appendChild(evalBtn);
  nav.appendChild(topBtn);
  document.body.appendChild(nav);

  // --- Navigation Popup (Plan 0268) ---
  var currentChapterId = '';
  var popupOpen = false;

  var popupStyle = document.createElement('style');
  popupStyle.textContent =
    '#nav-backdrop{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.4);z-index:99;opacity:0;transition:opacity 0.2s;}' +
    '#nav-popup{display:none;position:fixed;left:0.5em;right:0.5em;max-height:70vh;background:#fff;border-radius:8px 8px 0 0;box-shadow:0 -4px 20px rgba(0,0,0,0.15);z-index:100;overflow-y:auto;-webkit-overflow-scrolling:touch;transform:translateY(100%);transition:transform 0.2s ease-out;font-size:0.9em;}' +
    '.nav-popup-close{position:sticky;top:0;text-align:right;padding:0.5em 0.8em;background:inherit;cursor:pointer;font-size:1.2em;color:#888;z-index:1;}' +
    '.nav-popup-list{padding:0 0.8em 0.5em;}' +
    '.nav-popup-part{font-weight:bold;font-size:1em;padding:0.6em 0 0.3em;cursor:pointer;border-top:1px solid #eee;}' +
    '.nav-popup-part:first-child{border-top:none;}' +
    '.nav-popup-chapter{padding:0.35em 0 0.35em 1.2em;cursor:pointer;color:#333;border-radius:4px;}' +
    '.nav-popup-chapter:hover{background:#f0f6fa;}' +
    '.nav-popup-current{background:#e8f0f8;font-weight:bold;color:#1a5276;}' +
    '.nav-popup-interlude{font-style:italic;color:#9b59b6;}' +
    '.nav-popup-dimmed{opacity:0.4;}' +
    '.nav-popup-footer{display:flex;gap:0.5em;justify-content:center;padding:0.6em;border-top:1px solid #eee;flex-wrap:wrap;position:sticky;bottom:0;background:inherit;}' +
    '.nav-popup-dot{font-size:0.8em;}' +
    '@media(prefers-color-scheme:dark){' +
      '#nav-backdrop{background:rgba(0,0,0,0.6);}' +
      '#nav-popup{background:#1e1e1e;box-shadow:0 -4px 20px rgba(0,0,0,0.4);}' +
      '.nav-popup-close{color:#888;}' +
      '.nav-popup-part{border-top-color:#333;color:#e0e0e0;}' +
      '.nav-popup-chapter{color:#ccc;}' +
      '.nav-popup-chapter:hover{background:#2a3a4a;}' +
      '.nav-popup-current{background:#1e3248;color:#6ba3f7;}' +
      '.nav-popup-interlude{color:#b77fdf;}' +
      '.nav-popup-footer{border-top-color:#333;}' +
    '}' +
    '@media print{#nav-popup,#nav-backdrop{display:none!important;}}';
  document.head.appendChild(popupStyle);

  var navBackdrop = document.createElement('div');
  navBackdrop.id = 'nav-backdrop';
  document.body.appendChild(navBackdrop);

  var navPopup = document.createElement('div');
  navPopup.id = 'nav-popup';

  var popupClose = document.createElement('div');
  popupClose.className = 'nav-popup-close';
  popupClose.textContent = '✕';
  popupClose.addEventListener('click', closePopup);
  navPopup.appendChild(popupClose);

  var popupList = document.createElement('div');
  popupList.className = 'nav-popup-list';
  navPopup.appendChild(popupList);

  var popupFooter = document.createElement('div');
  popupFooter.className = 'nav-popup-footer';
  popupFooter.appendChild(expandBtn);
  popupFooter.appendChild(gBtn);
  popupFooter.appendChild(msToggle);
  popupFooter.appendChild(pdfBtn);
  popupFooter.appendChild(tipsBtn);
  popupFooter.appendChild(toolsLink);
  navPopup.appendChild(popupFooter);

  document.body.appendChild(navPopup);

  function buildPopupContents() {
    popupList.innerHTML = '';
    document.querySelectorAll('details.part-section').forEach(function(part) {
      var summary = part.querySelector(':scope > summary');
      if (!summary) return;
      var h1 = summary.querySelector('h1[id]');
      var partName = h1 ? h1.textContent.trim() : summary.textContent.trim();
      var partId = h1 ? h1.id : '';

      var firstCh = part.querySelector('details.chapter-section');
      var fg = firstCh ? (firstCh.getAttribute('data-filter-group') || 'M') : 'M';
      var dotColor = fg === 'A' ? '#d4a847' : (fg === 'C' ? '#9b7db8' : '#6a9fb5');

      var partEl = document.createElement('div');
      partEl.className = 'nav-popup-part';
      var dot = document.createElement('span');
      dot.className = 'nav-popup-dot';
      dot.style.color = dotColor;
      dot.textContent = '● ';
      partEl.appendChild(dot);
      partEl.appendChild(document.createTextNode(partName));
      partEl.addEventListener('click', function() { navigateTo(partId); });
      popupList.appendChild(partEl);

      part.querySelectorAll(':scope > details.chapter-section').forEach(function(ch) {
        var chSummary = ch.querySelector(':scope > summary');
        if (!chSummary) return;
        var h2 = chSummary.querySelector('h2[id], h3[id]');
        var chName = h2 ? h2.textContent.trim() : chSummary.textContent.trim();
        var chId = h2 ? h2.id : '';
        var isInterlude = ch.getAttribute('data-filter-group') === 'G';
        var isCurrent = chId && chId === currentChapterId;
        var isHidden = ch.style.display === 'none';

        var chEl = document.createElement('div');
        chEl.className = 'nav-popup-chapter';
        if (isCurrent) chEl.className += ' nav-popup-current';
        if (isInterlude) chEl.className += ' nav-popup-interlude';
        if (isHidden) chEl.className += ' nav-popup-dimmed';
        chEl.textContent = chName;
        chEl.setAttribute('data-chapter-id', chId);
        chEl.addEventListener('click', function() {
          if (isHidden && document.body.classList.contains('custodian-only')) {
            document.body.classList.remove('custodian-only');
            showGuardianOnly = false;
            gBtn.style.cssText = gInactive;
          }
          navigateTo(chId);
        });
        popupList.appendChild(chEl);
      });
    });
  }

  function navigateTo(id) {
    closePopup();
    if (!id) return;
    pushNavState();
    autoExpand('#' + id);
  }

  function openPopup() {
    updateBreadcrumb();
    buildPopupContents();
    popupOpen = true;
    navBackdrop.style.display = 'block';
    navPopup.style.display = 'block';
    navPopup.style.bottom = nav.offsetHeight + 'px';
    requestAnimationFrame(function() {
      requestAnimationFrame(function() {
        navBackdrop.style.opacity = '1';
        navPopup.style.transform = 'translateY(0)';
      });
    });
    var cur = navPopup.querySelector('.nav-popup-current');
    if (cur) setTimeout(function() { cur.scrollIntoView({block: 'center', behavior: 'smooth'}); }, 50);
  }

  function closePopup() {
    if (!popupOpen) return;
    popupOpen = false;
    navBackdrop.style.opacity = '0';
    navPopup.style.transform = 'translateY(100%)';
    setTimeout(function() {
      navBackdrop.style.display = 'none';
      navPopup.style.display = 'none';
    }, 200);
  }

  navBackdrop.addEventListener('click', closePopup);

  breadcrumb.removeAttribute('data-hover');
  breadcrumb.classList.remove('hover-nav');
  breadcrumb.style.cursor = 'pointer';
  breadcrumb.setAttribute('role', 'button');
  breadcrumb.setAttribute('tabindex', '0');
  breadcrumb.setAttribute('aria-label', 'Open chapter navigation');
  breadcrumb.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    if (popupOpen) closePopup();
    else openPopup();
  });

  var dropHint = document.createElement('span');
  dropHint.textContent = ' ▾';
  dropHint.style.cssText = 'color:#888;font-size:0.85em;';

  // Body padding for sticky nav
  document.body.style.paddingBottom = '3em';

  // --- Cover magnetosphere SVG injection ---
  (function() {
    var styleEl = document.createElement('style');
    styleEl.textContent =
      '@media (prefers-color-scheme: dark) { #cover-ms-light { display: none !important; } #cover-ms-dark { display: block; } }' +
      '@media (prefers-color-scheme: light), (prefers-color-scheme: no-preference) { #cover-ms-dark { display: none !important; } #cover-ms-light { display: block; } }' +
      '@media print { #cover-magnetosphere { display: none !important; } }';
    document.head.appendChild(styleEl);

    var navW = nav.offsetWidth;
    var msWidth;
    if (navW > 700) {
      msWidth = Math.min(Math.floor(navW * 0.52), 500);
    } else {
      msWidth = Math.floor(navW * 0.45);
    }
    if (msWidth < 40) return;
    var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    var wrapper = document.createElement('div');
    wrapper.id = 'cover-magnetosphere';
    wrapper.setAttribute('aria-hidden', 'true');
    wrapper.style.cssText = 'position:absolute;bottom:100%;right:0;' +
      'width:' + msWidth + 'px;' +
      'pointer-events:none;z-index:1;opacity:0.85;transition:opacity 0.3s;';

    var darkSvg =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" id="cover-ms-dark" width="100%">' +
      '<title>Stylized magnetosphere. Earth at left-center with dipole field lines sweeping into the magnetotail. The plasma sheet — the Flat — glows copper-gold through the tail center. Deep space, stars, bow shock, solar wind.</title>' +
      '<defs>' +
      '<radialGradient id="cv-earth" cx="38%" cy="32%">' +
      '<stop offset="0%" stop-color="#85c1e9"/>' +
      '<stop offset="45%" stop-color="#2e86c1"/>' +
      '<stop offset="100%" stop-color="#1a5276"/>' +
      '</radialGradient>' +
      '<radialGradient id="cv-atmo" cx="50%" cy="50%" r="50%">' +
      '<stop offset="50%" stop-color="#5dade2" stop-opacity="0.12"/>' +
      '<stop offset="80%" stop-color="#5dade2" stop-opacity="0.05"/>' +
      '<stop offset="100%" stop-color="#5dade2" stop-opacity="0"/>' +
      '</radialGradient>' +
      '<radialGradient id="cv-atmo-outer" cx="50%" cy="50%" r="50%">' +
      '<stop offset="40%" stop-color="#1a6b6a" stop-opacity="0.06"/>' +
      '<stop offset="100%" stop-color="#1a6b6a" stop-opacity="0"/>' +
      '</radialGradient>' +
      '<linearGradient id="cv-flat" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#C4913B" stop-opacity="0.9"/>' +
      '<stop offset="25%" stop-color="#C4913B" stop-opacity="0.7"/>' +
      '<stop offset="60%" stop-color="#C4913B" stop-opacity="0.35"/>' +
      '<stop offset="100%" stop-color="#C4913B" stop-opacity="0.04"/>' +
      '</linearGradient>' +
      '<linearGradient id="cv-flat-glow" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#C4913B" stop-opacity="0.3"/>' +
      '<stop offset="30%" stop-color="#C4913B" stop-opacity="0.15"/>' +
      '<stop offset="100%" stop-color="#C4913B" stop-opacity="0"/>' +
      '</linearGradient>' +
      '<linearGradient id="cv-tail-fill" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#1a5276" stop-opacity="0.12"/>' +
      '<stop offset="100%" stop-color="#1a5276" stop-opacity="0.02"/>' +
      '</linearGradient>' +
      '<linearGradient id="cv-bow" x1="100%" y1="0%" x2="0%" y2="0%">' +
      '<stop offset="0%" stop-color="#5dade2" stop-opacity="0.5"/>' +
      '<stop offset="100%" stop-color="#5dade2" stop-opacity="0.08"/>' +
      '</linearGradient>' +
      '<filter id="cv-glow"><feGaussianBlur stdDeviation="2.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
      '<filter id="cv-soft"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
      '<filter id="cv-wide-glow"><feGaussianBlur stdDeviation="8"/></filter>' +
      '<filter id="cv-star-glow"><feGaussianBlur stdDeviation="1.2"/></filter>' +
      '</defs>' +
      '<g opacity="0.7">' +
      '<circle cx="45" cy="22" r="0.8" fill="#fff" opacity="0.6">' + (motionOk ? '<animate attributeName="opacity" values="0.6;0.2;0.6" dur="5.0s" begin="0.3s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="112" cy="14" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="78" cy="48" r="0.6" fill="#fff" opacity="0.5"/>' +
      '<circle cx="205" cy="20" r="0.7" fill="#fff" opacity="0.3"/>' +
      '<circle cx="340" cy="12" r="0.9" fill="#fff" opacity="0.5"/>' +
      '<circle cx="430" cy="30" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="540" cy="18" r="0.7" fill="#fff" opacity="0.6">' + (motionOk ? '<animate attributeName="opacity" values="0.6;0.2;0.6" dur="4.8s" begin="1.0s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="650" cy="35" r="0.6" fill="#fff" opacity="0.3"/>' +
      '<circle cx="700" cy="70" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="25" cy="95" r="0.5" fill="#fff" opacity="0.3"/>' +
      '<circle cx="58" cy="130" r="0.7" fill="#fff" opacity="0.5"/>' +
      '<circle cx="30" cy="200" r="0.6" fill="#fff" opacity="0.4"/>' +
      '<circle cx="22" cy="280" r="0.8" fill="#fff" opacity="0.5"/>' +
      '<circle cx="95" cy="295" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="220" cy="305" r="0.6" fill="#fff" opacity="0.3"/>' +
      '<circle cx="350" cy="302" r="0.7" fill="#fff" opacity="0.5"/>' +
      '<circle cx="480" cy="298" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="580" cy="305" r="0.6" fill="#fff" opacity="0.3"/>' +
      '<circle cx="670" cy="290" r="0.8" fill="#fff" opacity="0.5"/>' +
      '<circle cx="690" cy="160" r="0.5" fill="#fff" opacity="0.4"/>' +
      '<circle cx="660" cy="220" r="0.7" fill="#fff" opacity="0.3"/>' +
      '<circle cx="710" cy="250" r="0.6" fill="#fff" opacity="0.5"/>' +
      '<circle cx="300" cy="38" r="1.0" fill="#fff" opacity="0.7" filter="url(#cv-star-glow)">' + (motionOk ? '<animate attributeName="opacity" values="0.7;0.25;0.7" dur="3.2s" begin="0s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="520" cy="60" r="0.9" fill="#fff" opacity="0.6" filter="url(#cv-star-glow)">' + (motionOk ? '<animate attributeName="opacity" values="0.6;0.2;0.6" dur="4.1s" begin="1.5s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="55" cy="265" r="1.0" fill="#fff" opacity="0.6" filter="url(#cv-star-glow)">' + (motionOk ? '<animate attributeName="opacity" values="0.6;0.2;0.6" dur="3.7s" begin="0.8s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="610" cy="280" r="0.8" fill="#fff" opacity="0.5" filter="url(#cv-star-glow)">' + (motionOk ? '<animate attributeName="opacity" values="0.5;0.15;0.5" dur="4.5s" begin="2.2s" repeatCount="indefinite"/>' : '') + '</circle>' +
      '<circle cx="440" cy="48" r="0.4" fill="#dde" opacity="0.3"/>' +
      '<circle cx="180" cy="295" r="0.4" fill="#dde" opacity="0.3"/>' +
      '<circle cx="550" cy="260" r="0.4" fill="#eef" opacity="0.25"/>' +
      '<circle cx="40" cy="160" r="0.4" fill="#eef" opacity="0.25"/>' +
      '<circle cx="625" cy="140" r="0.5" fill="#fff" opacity="0.3"/>' +
      '<circle cx="155" cy="45" r="0.4" fill="#fff" opacity="0.35"/>' +
      '</g>' +
      '<g opacity="0.35">' +
      '<line x1="0" y1="128" x2="72" y2="140" stroke="#C4913B" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="148" x2="78" y2="153" stroke="#C4913B" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="160" x2="80" y2="160" stroke="#C4913B" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="172" x2="78" y2="167" stroke="#C4913B" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="192" x2="72" y2="180" stroke="#C4913B" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '</g>' +
      '<g opacity="0.15">' +
      '<line x1="0" y1="110" x2="55" y2="125" stroke="#C4913B" stroke-width="0.5" stroke-linecap="round" stroke-dasharray="3,6">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="9" to="0" dur="2.2s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="210" x2="55" y2="195" stroke="#C4913B" stroke-width="0.5" stroke-linecap="round" stroke-dasharray="3,6">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="9" to="0" dur="2.2s" repeatCount="indefinite"/>' : '') + '</line>' +
      '</g>' +
      '<path d="M 100,45 C 72,90 68,130 72,160 C 68,190 72,230 100,275" fill="none" stroke="url(#cv-bow)" stroke-width="1.8" stroke-linecap="round">' + (motionOk ? '<animate attributeName="stroke-width" values="1.8;2.3;1.8" dur="4s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 100,45 C 72,90 68,130 72,160 C 68,190 72,230 100,275" fill="none" stroke="#5dade2" stroke-width="0.6" stroke-linecap="round" opacity="0.15" filter="url(#cv-soft)"/>' +
      '<path d="M 200,128 C 280,108 420,95 720,88 L 720,232 C 420,225 280,212 200,192 Z" fill="url(#cv-tail-fill)"/>' +
      '<path d="M 200,128 C 280,108 420,97 720,88" fill="none" stroke="#1a5276" stroke-width="0.8" opacity="0.4"/>' +
      '<path d="M 200,192 C 280,212 420,223 720,232" fill="none" stroke="#1a5276" stroke-width="0.8" opacity="0.4"/>' +
      '<g fill="none" stroke-linecap="round">' +
      '<path d="M 157,140 C 140,125 130,132 125,152 C 130,172 140,185 157,178" stroke="#5dade2" stroke-width="1.0" opacity="0.55">' + (motionOk ? '<animate attributeName="opacity" values="0.55;0.40;0.55" dur="5s" begin="0s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 153,132 C 125,105 108,122 100,160 C 108,198 125,215 153,188" stroke="#5dade2" stroke-width="0.9" opacity="0.45">' + (motionOk ? '<animate attributeName="opacity" values="0.45;0.30;0.45" dur="5.5s" begin="1s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 148,122 C 112,82 90,115 84,160 C 90,205 112,238 148,198" stroke="#5dade2" stroke-width="0.7" opacity="0.3">' + (motionOk ? '<animate attributeName="opacity" values="0.30;0.18;0.30" dur="6s" begin="2s" repeatCount="indefinite"/>' : '') + '</path>' +
      '</g>' +
      '<g fill="none" stroke-linecap="round">' +
      '<path d="M 182,140 C 215,115 260,120 300,132" stroke="#5dade2" stroke-width="1.0" opacity="0.5"/>' +
      '<path d="M 182,180 C 215,205 260,200 300,188" stroke="#5dade2" stroke-width="1.0" opacity="0.5"/>' +
      '<path d="M 185,135 C 240,95 340,100 440,115" stroke="#5dade2" stroke-width="0.8" opacity="0.35"/>' +
      '<path d="M 185,185 C 240,225 340,220 440,205" stroke="#5dade2" stroke-width="0.8" opacity="0.35"/>' +
      '<path d="M 188,130 C 250,70 380,80 560,95" stroke="#5dade2" stroke-width="0.6" opacity="0.2" stroke-dasharray="4,3"/>' +
      '<path d="M 188,190 C 250,250 380,240 560,225" stroke="#5dade2" stroke-width="0.6" opacity="0.2" stroke-dasharray="4,3"/>' +
      '</g>' +
      '<path d="M 150,118 C 132,80 118,55 108,35" fill="none" stroke="#5dade2" stroke-width="0.5" opacity="0.2" stroke-dasharray="3,3"/>' +
      '<path d="M 150,202 C 132,240 118,265 108,285" fill="none" stroke="#5dade2" stroke-width="0.5" opacity="0.2" stroke-dasharray="3,3"/>' +
      '<ellipse cx="170" cy="160" rx="38" ry="16" fill="none" stroke="#5dade2" stroke-width="0.6" opacity="0.18"/>' +
      '<ellipse cx="170" cy="160" rx="52" ry="24" fill="none" stroke="#5dade2" stroke-width="0.5" opacity="0.12"/>' +
      '<rect x="195" y="153" width="525" height="14" rx="7" fill="url(#cv-flat-glow)" filter="url(#cv-wide-glow)"/>' +
      '<rect x="195" y="156" width="525" height="8" rx="4" fill="url(#cv-flat-glow)" filter="url(#cv-soft)"/>' +
      '<line x1="197" y1="160" x2="715" y2="160" stroke="url(#cv-flat)" stroke-width="2" stroke-linecap="round" filter="url(#cv-glow)"/>' +
      '<line x1="197" y1="160" x2="450" y2="160" stroke="#C4913B" stroke-width="1" stroke-linecap="round" opacity="0.7"/>' +
      '<g opacity="0.6">' +
      '<circle cx="215" cy="160" r="1.2" fill="#C4913B"/>' +
      '<circle cx="250" cy="159" r="0.9" fill="#C4913B" opacity="0.8"/>' +
      '<circle cx="290" cy="161" r="1.0" fill="#C4913B" opacity="0.6"/>' +
      '<circle cx="335" cy="160" r="0.8" fill="#C4913B" opacity="0.5"/>' +
      '<circle cx="385" cy="159" r="0.7" fill="#C4913B" opacity="0.4"/>' +
      '<circle cx="440" cy="161" r="0.6" fill="#C4913B" opacity="0.3"/>' +
      '<circle cx="500" cy="160" r="0.5" fill="#C4913B" opacity="0.2"/>' +
      '<circle cx="565" cy="160" r="0.4" fill="#C4913B" opacity="0.15"/>' +
      '<circle cx="630" cy="160" r="0.3" fill="#C4913B" opacity="0.1"/>' +
      '</g>' +
      '<circle cx="170" cy="160" r="48" fill="url(#cv-atmo-outer)"/>' +
      '<circle cx="170" cy="160" r="34" fill="url(#cv-atmo)"/>' +
      '<circle cx="170" cy="160" r="18" fill="url(#cv-earth)"/>' +
      '<path d="M 164,149 C 167,147 170,148 172,150 C 174,153 172,155 169,155 C 166,155 163,152 164,149" fill="#27ae60" opacity="0.30"/>' +
      '<path d="M 166,155 C 168,154 170,156 169,159 C 167,163 163,164 162,161 C 161,158 164,156 166,155" fill="#27ae60" opacity="0.28"/>' +
      '<path d="M 175,152 C 177,150 180,152 179,155 C 178,158 175,158 174,155 C 173,153 174,152 175,152" fill="#27ae60" opacity="0.22"/>' +
      '<path d="M 161,147 C 163,145 167,145 168,147 C 168,148 166,149 163,148 C 161,148 160,147 161,147" fill="#27ae60" opacity="0.22"/>' +
      '<ellipse cx="168" cy="143" rx="5" ry="2" fill="#fff" opacity="0.12"/>' +
      '<ellipse cx="170" cy="177" rx="4" ry="1.5" fill="#fff" opacity="0.08"/>' +
      '<circle cx="163" cy="152" r="6" fill="#fff" opacity="0.10"/>' +
      '<text x="380" y="178" fill="#C4913B" font-size="12" font-family="Georgia, serif" font-style="italic" text-anchor="middle" opacity="0.7" letter-spacing="1.5">the Flat</text>' +
      '<text x="712" y="312" fill="#fff" font-size="6" font-family="sans-serif" text-anchor="end" opacity="0.15">Argus / S63</text>' +
      '</svg>';

    var lightSvg =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" id="cover-ms-light" width="100%">' +
      '<title>Stylized magnetosphere (light mode). Earth, dipole field lines, magnetotail, plasma sheet — the Flat — rendered for light backgrounds. The dayside.</title>' +
      '<defs>' +
      '<radialGradient id="lm-earth" cx="38%" cy="32%">' +
      '<stop offset="0%" stop-color="#85c1e9"/>' +
      '<stop offset="45%" stop-color="#2e86c1"/>' +
      '<stop offset="100%" stop-color="#1a5276"/>' +
      '</radialGradient>' +
      '<radialGradient id="lm-atmo" cx="50%" cy="50%" r="50%">' +
      '<stop offset="50%" stop-color="#2e86c1" stop-opacity="0.10"/>' +
      '<stop offset="80%" stop-color="#2e86c1" stop-opacity="0.04"/>' +
      '<stop offset="100%" stop-color="#2e86c1" stop-opacity="0"/>' +
      '</radialGradient>' +
      '<radialGradient id="lm-atmo-outer" cx="50%" cy="50%" r="50%">' +
      '<stop offset="40%" stop-color="#1a6b6a" stop-opacity="0.05"/>' +
      '<stop offset="100%" stop-color="#1a6b6a" stop-opacity="0"/>' +
      '</radialGradient>' +
      '<linearGradient id="lm-flat" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#C4913B" stop-opacity="0.9"/>' +
      '<stop offset="25%" stop-color="#C4913B" stop-opacity="0.7"/>' +
      '<stop offset="60%" stop-color="#C4913B" stop-opacity="0.35"/>' +
      '<stop offset="100%" stop-color="#C4913B" stop-opacity="0.06"/>' +
      '</linearGradient>' +
      '<linearGradient id="lm-flat-glow" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#C4913B" stop-opacity="0.25"/>' +
      '<stop offset="30%" stop-color="#C4913B" stop-opacity="0.12"/>' +
      '<stop offset="100%" stop-color="#C4913B" stop-opacity="0"/>' +
      '</linearGradient>' +
      '<linearGradient id="lm-tail-fill" x1="0%" y1="0%" x2="100%" y2="0%">' +
      '<stop offset="0%" stop-color="#1a5276" stop-opacity="0.07"/>' +
      '<stop offset="100%" stop-color="#1a5276" stop-opacity="0.01"/>' +
      '</linearGradient>' +
      '<linearGradient id="lm-bow" x1="100%" y1="0%" x2="0%" y2="0%">' +
      '<stop offset="0%" stop-color="#1a5276" stop-opacity="0.4"/>' +
      '<stop offset="100%" stop-color="#1a5276" stop-opacity="0.06"/>' +
      '</linearGradient>' +
      '<filter id="lm-glow"><feGaussianBlur stdDeviation="2.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
      '<filter id="lm-soft"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
      '<filter id="lm-wide-glow"><feGaussianBlur stdDeviation="8"/></filter>' +
      '</defs>' +
      '<g opacity="0.30">' +
      '<line x1="0" y1="128" x2="72" y2="140" stroke="#C4913B" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="148" x2="78" y2="153" stroke="#C4913B" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="160" x2="80" y2="160" stroke="#C4913B" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="172" x2="78" y2="167" stroke="#C4913B" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="192" x2="72" y2="180" stroke="#C4913B" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="4,7">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>' : '') + '</line>' +
      '</g>' +
      '<g opacity="0.12">' +
      '<line x1="0" y1="110" x2="55" y2="125" stroke="#C4913B" stroke-width="0.5" stroke-linecap="round" stroke-dasharray="3,6">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="9" to="0" dur="2.2s" repeatCount="indefinite"/>' : '') + '</line>' +
      '<line x1="0" y1="210" x2="55" y2="195" stroke="#C4913B" stroke-width="0.5" stroke-linecap="round" stroke-dasharray="3,6">' + (motionOk ? '<animate attributeName="stroke-dashoffset" from="9" to="0" dur="2.2s" repeatCount="indefinite"/>' : '') + '</line>' +
      '</g>' +
      '<path d="M 100,45 C 72,90 68,130 72,160 C 68,190 72,230 100,275" fill="none" stroke="url(#lm-bow)" stroke-width="1.8" stroke-linecap="round">' + (motionOk ? '<animate attributeName="stroke-width" values="1.8;2.3;1.8" dur="4s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 100,45 C 72,90 68,130 72,160 C 68,190 72,230 100,275" fill="none" stroke="#1a5276" stroke-width="0.6" stroke-linecap="round" opacity="0.10" filter="url(#lm-soft)"/>' +
      '<path d="M 200,128 C 280,108 420,95 720,88 L 720,232 C 420,225 280,212 200,192 Z" fill="url(#lm-tail-fill)"/>' +
      '<path d="M 200,128 C 280,108 420,97 720,88" fill="none" stroke="#1a5276" stroke-width="0.8" opacity="0.25"/>' +
      '<path d="M 200,192 C 280,212 420,223 720,232" fill="none" stroke="#1a5276" stroke-width="0.8" opacity="0.25"/>' +
      '<g fill="none" stroke-linecap="round">' +
      '<path d="M 157,140 C 140,125 130,132 125,152 C 130,172 140,185 157,178" stroke="#1a5276" stroke-width="1.0" opacity="0.40">' + (motionOk ? '<animate attributeName="opacity" values="0.40;0.28;0.40" dur="5s" begin="0s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 153,132 C 125,105 108,122 100,160 C 108,198 125,215 153,188" stroke="#1a5276" stroke-width="0.9" opacity="0.30">' + (motionOk ? '<animate attributeName="opacity" values="0.30;0.18;0.30" dur="5.5s" begin="1s" repeatCount="indefinite"/>' : '') + '</path>' +
      '<path d="M 148,122 C 112,82 90,115 84,160 C 90,205 112,238 148,198" stroke="#1a5276" stroke-width="0.7" opacity="0.20">' + (motionOk ? '<animate attributeName="opacity" values="0.20;0.12;0.20" dur="6s" begin="2s" repeatCount="indefinite"/>' : '') + '</path>' +
      '</g>' +
      '<g fill="none" stroke-linecap="round">' +
      '<path d="M 182,140 C 215,115 260,120 300,132" stroke="#1a5276" stroke-width="1.0" opacity="0.35"/>' +
      '<path d="M 182,180 C 215,205 260,200 300,188" stroke="#1a5276" stroke-width="1.0" opacity="0.35"/>' +
      '<path d="M 185,135 C 240,95 340,100 440,115" stroke="#1a5276" stroke-width="0.8" opacity="0.22"/>' +
      '<path d="M 185,185 C 240,225 340,220 440,205" stroke="#1a5276" stroke-width="0.8" opacity="0.22"/>' +
      '<path d="M 188,130 C 250,70 380,80 560,95" stroke="#1a5276" stroke-width="0.6" opacity="0.12" stroke-dasharray="4,3"/>' +
      '<path d="M 188,190 C 250,250 380,240 560,225" stroke="#1a5276" stroke-width="0.6" opacity="0.12" stroke-dasharray="4,3"/>' +
      '</g>' +
      '<path d="M 150,118 C 132,80 118,55 108,35" fill="none" stroke="#1a5276" stroke-width="0.5" opacity="0.12" stroke-dasharray="3,3"/>' +
      '<path d="M 150,202 C 132,240 118,265 108,285" fill="none" stroke="#1a5276" stroke-width="0.5" opacity="0.12" stroke-dasharray="3,3"/>' +
      '<ellipse cx="170" cy="160" rx="38" ry="16" fill="none" stroke="#1a5276" stroke-width="0.6" opacity="0.12"/>' +
      '<ellipse cx="170" cy="160" rx="52" ry="24" fill="none" stroke="#1a5276" stroke-width="0.5" opacity="0.08"/>' +
      '<rect x="195" y="153" width="525" height="14" rx="7" fill="url(#lm-flat-glow)" filter="url(#lm-wide-glow)"/>' +
      '<rect x="195" y="156" width="525" height="8" rx="4" fill="url(#lm-flat-glow)" filter="url(#lm-soft)"/>' +
      '<line x1="197" y1="160" x2="715" y2="160" stroke="url(#lm-flat)" stroke-width="2" stroke-linecap="round" filter="url(#lm-glow)"/>' +
      '<line x1="197" y1="160" x2="450" y2="160" stroke="#C4913B" stroke-width="1" stroke-linecap="round" opacity="0.6"/>' +
      '<g opacity="0.5">' +
      '<circle cx="215" cy="160" r="1.2" fill="#C4913B"/>' +
      '<circle cx="250" cy="159" r="0.9" fill="#C4913B" opacity="0.8"/>' +
      '<circle cx="290" cy="161" r="1.0" fill="#C4913B" opacity="0.6"/>' +
      '<circle cx="335" cy="160" r="0.8" fill="#C4913B" opacity="0.5"/>' +
      '<circle cx="385" cy="159" r="0.7" fill="#C4913B" opacity="0.4"/>' +
      '<circle cx="440" cy="161" r="0.6" fill="#C4913B" opacity="0.3"/>' +
      '<circle cx="500" cy="160" r="0.5" fill="#C4913B" opacity="0.2"/>' +
      '<circle cx="565" cy="160" r="0.4" fill="#C4913B" opacity="0.15"/>' +
      '<circle cx="630" cy="160" r="0.3" fill="#C4913B" opacity="0.1"/>' +
      '</g>' +
      '<circle cx="170" cy="160" r="48" fill="url(#lm-atmo-outer)"/>' +
      '<circle cx="170" cy="160" r="34" fill="url(#lm-atmo)"/>' +
      '<circle cx="170" cy="160" r="18" fill="url(#lm-earth)"/>' +
      '<path d="M 164,149 C 167,147 170,148 172,150 C 174,153 172,155 169,155 C 166,155 163,152 164,149" fill="#27ae60" opacity="0.35"/>' +
      '<path d="M 166,155 C 168,154 170,156 169,159 C 167,163 163,164 162,161 C 161,158 164,156 166,155" fill="#27ae60" opacity="0.32"/>' +
      '<path d="M 175,152 C 177,150 180,152 179,155 C 178,158 175,158 174,155 C 173,153 174,152 175,152" fill="#27ae60" opacity="0.25"/>' +
      '<path d="M 161,147 C 163,145 167,145 168,147 C 168,148 166,149 163,148 C 161,148 160,147 161,147" fill="#27ae60" opacity="0.25"/>' +
      '<ellipse cx="168" cy="143" rx="5" ry="2" fill="#fff" opacity="0.18"/>' +
      '<ellipse cx="170" cy="177" rx="4" ry="1.5" fill="#fff" opacity="0.12"/>' +
      '<circle cx="163" cy="152" r="6" fill="#fff" opacity="0.14"/>' +
      '<text x="380" y="178" fill="#996B2F" font-size="12" font-family="Georgia, serif" font-style="italic" text-anchor="middle" opacity="0.6" letter-spacing="1.5">the Flat</text>' +
      '<text x="712" y="312" fill="#1a5276" font-size="6" font-family="sans-serif" text-anchor="end" opacity="0.12">Argus / S63</text>' +
      '</svg>';

    wrapper.innerHTML = darkSvg + lightSvg;
    nav.appendChild(wrapper);

    msToggle.addEventListener('click', function(e) {
      e.preventDefault();
      var hidden = wrapper.style.display === 'none';
      wrapper.style.display = hidden ? '' : 'none';
      msToggle.style.opacity = hidden ? '1' : '0.4';
      try {
        if (hidden) localStorage.removeItem('cover-ms-hidden');
        else localStorage.setItem('cover-ms-hidden', 'true');
      } catch(e) {}
    });

    try {
      if (localStorage.getItem('cover-ms-hidden') === 'true') {
        wrapper.style.display = 'none';
        msToggle.style.opacity = '0.4';
      }
    } catch(e) {}

    var scrollHidden = false;
    window.addEventListener('scroll', function() {
      var manuallyHidden = false;
      try { manuallyHidden = localStorage.getItem('cover-ms-hidden') === 'true'; } catch(e) {}
      if (manuallyHidden) return;

      if (window.scrollY > 20 && !scrollHidden) {
        wrapper.style.opacity = '0';
        scrollHidden = true;
      } else if (window.scrollY <= 20 && scrollHidden) {
        wrapper.style.opacity = '0.85';
        scrollHidden = false;
      }
    });
  })();

  // --- Breadcrumb update on scroll ---

  function updateBreadcrumb() {
    var partName = '';
    var partId = '';
    var chapterName = '';
    var chapterId = '';

    document.querySelectorAll('details.part-section > summary').forEach(function(s) {
      var rect = s.getBoundingClientRect();
      if (rect.height > 0 && rect.top <= 150) {
        var h1 = s.querySelector('h1[id]');
        partName = h1 ? h1.textContent.trim() : s.textContent.trim();
        partName = partName.substring(0, 25);
        partId = h1 ? h1.id : '';
      }
    });

    document.querySelectorAll('details.part-section details.chapter-section > summary').forEach(function(s) {
      var rect = s.getBoundingClientRect();
      if (rect.height > 0 && rect.top <= 150) {
        var h2 = s.querySelector('h2[id]');
        chapterName = h2 ? h2.textContent.trim() : s.textContent.trim();
        chapterName = chapterName.substring(0, 35);
        chapterId = h2 ? h2.id : '';
      }
    });

    currentChapterId = chapterId;

    breadcrumb.innerHTML = '';
    var bcText = 'Relinquishment';
    if (partName && chapterName) {
      bcText = partName + ' \u203A ' + chapterName;
    } else if (partName) {
      bcText = partName;
    }
    var span = document.createElement('span');
    span.textContent = bcText;
    span.style.cssText = 'color:' + (isDark ? '#aaa' : '#777') + ';';
    breadcrumb.appendChild(span);
    breadcrumb.appendChild(dropHint);

    shareBtn.href = '#' + (chapterId || partId || '');

    var newHash = chapterId ? '#' + chapterId : (partId ? '#' + partId : '');
    if (newHash && newHash !== location.hash) {
      var curId = location.hash.slice(1);
      var curEl = curId ? document.getElementById(curId) : null;
      var chapterEl = chapterId ? document.getElementById(chapterId) : null;
      var insideChapter = curEl && chapterEl && chapterEl.contains(curEl);
      if (!insideChapter) {
        history.replaceState(null, '', newHash);
      }
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
    var parentCh = target.closest('details.chapter-section');
    if (parentCh && parentCh.style.display === 'none' && document.body.classList.contains('custodian-only')) {
      document.body.classList.remove('custodian-only');
      showGuardianOnly = false;
      gBtn.style.cssText = gInactive;
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


  if (initialHash) {
    autoExpand(initialHash);
  }
  window.addEventListener('hashchange', function() {
    if (popupOpen) closePopup();
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
    topBtn.style.color = '#6ba3f7';
    expandBtn.style.background = '#2471a3';
    backBtn.style.color = '#5dade2';
    backBtn.style.borderColor = '#5dade2';
    evalBtn.style.background = '#2471a3';

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
    if (popupOpen) { closePopup(); return; }
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

  // Escape key dismisses panel and nav popup
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      if (popupOpen) { closePopup(); return; }
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
