/* Relinquishment HTML Reader — progressive enhancement
   Graceful degradation: if JS fails, reader gets plain HTML with working links. */
(function() {
  'use strict';

  // --- Capture initial hash before updateBreadcrumb can replaceState it ---
  var initialHash = window.location.hash;

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
  breadcrumb.title = 'Your current location in the book';
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
  introLink.title = 'Jump to Introduction';
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
    {label: 'Deduction', id: 'guided-deduction', tip: 'Jump to Part I: Guided Deduction'},
    {label: 'Evidence', id: 'the-evidence-trail', tip: 'Jump to Part II: The Evidence Trail'},
    {label: 'Forgiveness', id: 'forgiveness-and-permission', tip: 'Jump to Part III: Forgiveness and Permission'},
  ];
  partLinks.forEach(function(p, i) {
    quickJump.appendChild(document.createTextNode(' \u00B7 '));
    var a = document.createElement('a');
    a.href = '#' + p.id;
    a.textContent = p.label;
    a.title = p.tip;
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
  topBtn.title = 'Scroll to the top of the page';
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
  expandBtn.title = 'Open all chapters and sections at once';
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
    expandBtn.title = expanding ? 'Close all chapters and sections' : 'Open all chapters and sections at once';
  });

  // Back button (hidden when nav stack empty) — outline style, B6
  var backBtn = document.createElement('button');
  backBtn.id = 'nav-back';
  backBtn.textContent = '\u2190 Back';
  backBtn.title = 'Return to where you were reading before following a link';
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

  // Evaluate button (navigates to evaluate-with-AI section)
  var evalBtn = document.createElement('button');
  evalBtn.id = 'nav-evaluate';
  evalBtn.setAttribute('data-nav-evaluate', 'true');
  evalBtn.textContent = 'AI Eval';
  evalBtn.title = 'Jump to instructions for evaluating this book with an AI assistant';
  evalBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
    'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;border:none;' +
    'border-radius:4px;margin:0 0.3em;white-space:nowrap;';
  evalBtn.addEventListener('mouseenter', function() { evalBtn.style.background = '#2471a3'; });
  evalBtn.addEventListener('mouseleave', function() { evalBtn.style.background = '#1a5276'; });
  evalBtn.addEventListener('click', function() {
    pushNavState();
    autoExpand('#how-to-evaluate');
  });

  nav.appendChild(backBtn);
  nav.appendChild(breadcrumb);
  nav.appendChild(shareBtn);
  nav.appendChild(quickJump);
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

  // --- Per-Section Share Icons (Plan 0134c) ---
  document.querySelectorAll('details > summary').forEach(function(summary) {
    var heading = summary.querySelector('h1[id], h2[id], h3[id]');
    if (!heading) return;

    var share = document.createElement('a');
    share.className = 'section-share';
    share.href = '#' + heading.id;
    share.textContent = '\uD83D\uDD17';
    share.title = 'Copy link to this section';
    share.setAttribute('aria-label', 'Copy link to ' + heading.textContent.trim());
    share.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var url = location.origin + location.pathname + '#' + heading.id;
      copyToClipboard(url, function() {
        share.textContent = '\u2713';
        setTimeout(function() { share.textContent = '\uD83D\uDD17'; }, 1500);
      });
    });
    summary.appendChild(share);
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

  // Remove any existing hover panel from DOM
  function dismissPanel() {
    var existing = document.querySelector('.hover-panel');
    if (existing) {
      // Clean up aria-describedby on the linked term
      var linkedTerm = document.querySelector('[aria-describedby="' + existing.id + '"]');
      if (linkedTerm) linkedTerm.removeAttribute('aria-describedby');
      existing.remove();
    }
    if (hoverTimer) {
      clearTimeout(hoverTimer);
      hoverTimer = null;
    }
  }

  // Create and show a hover panel for the given term element
  function showPanel(term) {
    var def = term.getAttribute('data-hover');
    if (!def) return;

    // Dismiss any existing panel first (single-panel rule)
    dismissPanel();

    var panel = document.createElement('div');
    panel.className = 'hover-panel';
    panelIdCounter++;
    panel.id = 'hover-panel-' + panelIdCounter;
    panel.setAttribute('role', 'tooltip');

    // Rich content panels use data-hover-html; plain text panels use data-hover
    var richHtml = term.getAttribute('data-hover-html');
    if (richHtml) {
      var content = document.createElement('div');
      content.innerHTML = richHtml;
      panel.appendChild(content);
    } else {
      panel.appendChild(document.createTextNode(def));
    }

    // Hover ID footer (dev builds only — hidden when body has final-build class)
    var hoverId = term.getAttribute('data-hover-id');
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

    // Append to body (not as child of term — terms live inside nested <details>)
    document.body.appendChild(panel);

    // Smart positioning: place panel near the term, within viewport
    positionPanel(panel, term);

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

  // --- Bind events to all .hover-term elements ---

  var allHoverTerms = document.querySelectorAll('.hover-term[data-hover]');
  var lastTouchTime = 0; // track touch to suppress mouse hover on touch devices

  allHoverTerms.forEach(function(term) {
    // Make keyboard-focusable
    term.setAttribute('tabindex', '0');

    // --- Touch: record timestamp so mouseenter can be suppressed ---
    term.addEventListener('touchstart', function(e) {
      e.stopPropagation();
      lastTouchTime = Date.now();
    }, { passive: true });

    term.addEventListener('touchend', function(e) {
      e.preventDefault();
      e.stopPropagation();
      lastTouchTime = Date.now();

      // Toggle panel on touch (Puppeteer .tap() dispatches touch but not click)
      if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }

      var existingPanel = document.querySelector('.hover-panel');
      if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
        dismissPanel();
        return;
      }
      showPanel(term);
    });

    // --- Click: toggle panel (fallback for desktop click / non-touch-event paths) ---
    term.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();

      // If touch just handled this (within 500ms), skip — touchend already toggled
      if (Date.now() - lastTouchTime < 500) return;

      // If hover timer is pending (mouseenter fired), cancel it — click takes over
      if (hoverTimer) { clearTimeout(hoverTimer); hoverTimer = null; }

      // Toggle: if panel is already showing for this term, dismiss it
      var existingPanel = document.querySelector('.hover-panel');
      if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
        dismissPanel();
        return;
      }

      showPanel(term);
    });

    // --- Mouse: hover with delay (anti-flicker, desktop only) ---
    term.addEventListener('mouseenter', function(e) {
      // Suppress hover if this was triggered by a recent touch (within 500ms)
      if (Date.now() - lastTouchTime < 500) return;

      if (hoverTimer) clearTimeout(hoverTimer);

      hoverTimer = setTimeout(function() {
        hoverTimer = null;
        showPanel(term);
      }, hoverDelay);
    });

    term.addEventListener('mouseleave', function(e) {
      if (hoverTimer) {
        clearTimeout(hoverTimer);
        hoverTimer = null;
      }
      // Small delay before dismiss to allow mouse to enter panel
      setTimeout(function() {
        var panel = document.querySelector('.hover-panel');
        if (panel && !panel.matches(':hover')) {
          dismissPanel();
        }
      }, 100);
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

  // --- Global dismiss handlers ---

  // Click outside dismisses panel
  document.addEventListener('click', function(e) {
    var panel = document.querySelector('.hover-panel');
    if (!panel) return;
    if (e.target.closest('.hover-panel') || e.target.closest('.hover-term')) return;
    dismissPanel();
  });

  // Touch outside dismisses panel
  document.addEventListener('touchend', function(e) {
    var panel = document.querySelector('.hover-panel');
    if (!panel) return;
    if (e.target.closest('.hover-panel') || e.target.closest('.hover-term')) return;
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
    if (!e.target.closest('.hover-panel') && !e.target.closest('.hover-term')) {
      setTimeout(function() {
        var p = document.querySelector('.hover-panel');
        if (p && !p.matches(':hover')) {
          dismissPanel();
        }
      }, 150);
    }
  });
})();
