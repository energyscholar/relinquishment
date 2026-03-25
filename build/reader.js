/* Relinquishment HTML Reader — progressive enhancement
   Graceful degradation: if JS fails, reader gets plain HTML with working links. */
(function() {
  'use strict';

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
  breadcrumb.style.cssText = 'flex:1;overflow:hidden;white-space:nowrap;' +
    'text-overflow:ellipsis;';

  // Share button (§) — appended after breadcrumb, updated on scroll
  var shareBtn = document.createElement('a');
  shareBtn.id = 'nav-share';
  shareBtn.textContent = '\u00A7';
  shareBtn.href = '#';
  shareBtn.title = 'Copy link to current section';
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
    var summaryEl = document.getElementById('summary:most-important-story');
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
    {label: 'Deduction', id: 'guided-deduction'},
    {label: 'Evidence', id: 'the-evidence-trail'},
    {label: 'Agency', id: 'agency-and-restraint'},
  ];
  partLinks.forEach(function(p, i) {
    quickJump.appendChild(document.createTextNode(' \u00B7 '));
    var a = document.createElement('a');
    a.href = '#' + p.id;
    a.textContent = p.label;
    a.style.cssText = 'text-decoration:none;color:#1a5276;';
    a.addEventListener('mouseenter', function() { a.style.color = '#2471a3'; });
    a.addEventListener('mouseleave', function() { a.style.color = '#1a5276'; });
    a.addEventListener('click', function(e) {
      e.preventDefault();
      var target = document.getElementById(p.id);
      if (target) {
        // Open all ancestor <details> and scroll
        var el = target;
        while (el) {
          if (el.tagName === 'DETAILS') el.open = true;
          el = el.parentElement;
        }
        target.scrollIntoView({behavior: 'smooth'});
      }
    });
    quickJump.appendChild(a);
  });

  // Right: ▲ Top
  var topBtn = document.createElement('a');
  topBtn.textContent = '\u25B2 Top';
  topBtn.href = '#';
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
  expandBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;border:none;' +
    'border-radius:4px;margin:0 0.5em;white-space:nowrap;';
  expandBtn.addEventListener('mouseenter', function() { expandBtn.style.background = '#2471a3'; });
  expandBtn.addEventListener('mouseleave', function() { expandBtn.style.background = '#1a5276'; });
  expandBtn.addEventListener('click', function() {
    var allDetails = document.querySelectorAll('details');
    var expanding = expandBtn.textContent === 'Expand All';
    allDetails.forEach(function(d) { d.open = expanding; });
    expandBtn.textContent = expanding ? 'Collapse All' : 'Expand All';
  });

  nav.appendChild(breadcrumb);
  nav.appendChild(shareBtn);
  nav.appendChild(quickJump);
  nav.appendChild(expandBtn);
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

    // Find current part: last open part-section whose summary scrolled past
    document.querySelectorAll('details.part-section[open] > summary').forEach(function(s) {
      if (s.getBoundingClientRect().top <= 150) {
        var h1 = s.querySelector('h1[id]');
        partName = h1 ? h1.textContent.trim() : s.textContent.trim();
        partName = partName.substring(0, 25);
        partId = h1 ? h1.id : '';
      }
    });

    // Find current chapter: last chapter-section (open or closed) scrolled past
    // within an open part — show what section the reader is in
    document.querySelectorAll('details.part-section[open] details.chapter-section > summary').forEach(function(s) {
      if (s.getBoundingClientRect().top <= 150) {
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
    var target = document.querySelector(hash);
    if (!target) {
      // Try decoding (pandoc uses colons in IDs)
      try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch(e) {}
    }
    if (!target) return;
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
    target.scrollIntoView();
  }
  if (window.location.hash) {
    autoExpand(window.location.hash);
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
        btn.title = btnTitle;
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

      // Front-matter button — at the "Your AI May Need a Firmware Update" note
      var frontNote = document.getElementById('your-ai-may-need-a-firmware-update');
      if (!frontNote) {
        document.querySelectorAll('h2, h3').forEach(function(h) {
          if (h.textContent.indexOf('Firmware Update') !== -1 && h.textContent.indexOf('Your AI') !== -1) frontNote = h;
        });
      }
      if (frontNote) {
        var frontBtn = makeCopyBtn('copy-llm-primer-front');
        // Insert inside the <details> after <summary>
        var frontDetails = frontNote.closest('details');
        if (frontDetails) {
          var frontSummary = frontDetails.querySelector(':scope > summary');
          if (frontSummary) frontSummary.insertAdjacentElement('afterend', frontBtn);
        } else {
          frontNote.parentNode.appendChild(frontBtn);
        }
      }
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
        btn.title = absBtnTitle;
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
  }
})();
