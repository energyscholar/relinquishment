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

  // --- Dark mode detection (used by copy button and nav) ---
  var isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  // --- LLM Primer copy buttons (top + bottom) ---
  var primerSection = document.getElementById('app:llm-primer') ||
    document.getElementById('ai-evaluation-tool');
  if (!primerSection) {
    document.querySelectorAll('h1').forEach(function(h) {
      if (h.textContent.indexOf('Published Physics Reference') !== -1) primerSection = h;
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
          function onCopied() {
            btn.textContent = 'Copied!';
            btn.style.background = '#1e8449';
            setTimeout(function() {
              btn.textContent = btnLabel;
              btn.style.background = btnBase;
            }, 2000);
          }
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(onCopied, function() {
              // Clipboard API failed (non-HTTPS, permission denied) — try textarea fallback
              var ta = document.createElement('textarea');
              ta.value = text;
              ta.style.cssText = 'position:fixed;left:-9999px;';
              document.body.appendChild(ta);
              ta.select();
              document.execCommand('copy');
              document.body.removeChild(ta);
              onCopied();
            });
          } else {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.style.cssText = 'position:fixed;left:-9999px;';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            onCopied();
          }
        });
        return btn;
      }

      // Top button — right after the chapter heading
      var copyTopBtn = makeCopyBtn('copy-llm-primer-top');
      primerSection.parentNode.insertBefore(copyTopBtn, primerSection.nextSibling);

      // Bottom button — before the next chapter-level heading
      // Primer is h2 in appendix; find the next h1 or h2 after it
      var chapterHeadings = document.querySelectorAll('h1, h2');
      var nextChapter = null;
      var foundPrimer = false;
      for (var hi = 0; hi < chapterHeadings.length; hi++) {
        if (chapterHeadings[hi] === primerSection) {
          foundPrimer = true;
        } else if (foundPrimer) {
          nextChapter = chapterHeadings[hi];
          break;
        }
      }
      var bottomBtn = makeCopyBtn('copy-llm-primer-bottom');
      if (nextChapter) {
        nextChapter.parentNode.insertBefore(bottomBtn, nextChapter);
      } else {
        // Fallback: append after last element in primer section's parent
        primerSection.parentNode.appendChild(bottomBtn);
      }

      // Front-matter button — at the "For AI-Assisted Readers" note
      var frontNote = document.getElementById('for-ai-assisted-readers');
      if (!frontNote) {
        document.querySelectorAll('h2, h3').forEach(function(h) {
          if (h.textContent.indexOf('AI-Assisted Readers') !== -1) frontNote = h;
        });
      }
      if (frontNote) {
        var frontBtn = makeCopyBtn('copy-llm-primer-front');
        // Find the end of the front-matter section (next heading)
        var frontParent = frontNote.parentNode;
        var frontNext = frontNote.nextElementSibling;
        while (frontNext && !/^H[1-3]$/.test(frontNext.tagName)) {
          frontNext = frontNext.nextElementSibling;
        }
        if (frontNext) {
          frontParent.insertBefore(frontBtn, frontNext);
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
          function onCopied() {
            btn.textContent = 'Copied!';
            btn.style.background = '#1e8449';
            setTimeout(function() {
              btn.textContent = absBtnLabel;
              btn.style.background = absBtnBase;
            }, 2000);
          }
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(onCopied, function() {
              var ta = document.createElement('textarea');
              ta.value = text;
              ta.style.cssText = 'position:fixed;left:-9999px;';
              document.body.appendChild(ta);
              ta.select();
              document.execCommand('copy');
              document.body.removeChild(ta);
              onCopied();
            });
          } else {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.style.cssText = 'position:fixed;left:-9999px;';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            onCopied();
          }
        });
        return btn;
      }

      // Top button — right after the chapter heading
      var absTopBtn = makeAbsCopyBtn('copy-spiral-abstracts-top');
      abstractsSection.parentNode.insertBefore(absTopBtn, abstractsSection.nextSibling);

      // Bottom button — before the next chapter-level heading
      var absHeadings = document.querySelectorAll('h1, h2');
      var absNextChapter = null;
      var foundAbstracts = false;
      for (var ai = 0; ai < absHeadings.length; ai++) {
        if (absHeadings[ai] === abstractsSection) {
          foundAbstracts = true;
        } else if (foundAbstracts) {
          absNextChapter = absHeadings[ai];
          break;
        }
      }
      var absBottomBtn = makeAbsCopyBtn('copy-spiral-abstracts-bottom');
      if (absNextChapter) {
        absNextChapter.parentNode.insertBefore(absBottomBtn, absNextChapter);
      } else {
        abstractsSection.parentNode.appendChild(absBottomBtn);
      }
    }
  }

  if (isDark) {
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
