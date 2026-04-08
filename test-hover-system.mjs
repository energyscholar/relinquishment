/**
 * Relinquishment HTML Reader — Comprehensive Test Harness
 * Tests all key JS functionality on both desktop and mobile viewports.
 *
 * Usage: node test-hover-system.mjs
 * Requires: puppeteer (npm install puppeteer)
 */
import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = resolve(__dirname, 'docs/downloads/Relinquishment.html');

let passed = 0, failed = 0, skipped = 0;

function ok(test, msg) {
  if (test) { passed++; console.log('  \x1b[32m✓\x1b[0m ' + msg); }
  else { failed++; console.log('  \x1b[31m✗\x1b[0m ' + msg); }
}
function skip(msg) { skipped++; console.log('  \x1b[33m-\x1b[0m ' + msg + ' (skipped)'); }

async function openPage(browser, mobile) {
  const page = await browser.newPage();
  if (mobile) {
    await page.emulate({
      viewport: { width: 390, height: 844, isMobile: true, hasTouch: true },
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'
    });
  } else {
    await page.setViewport({ width: 1280, height: 900 });
  }
  await page.goto('file://' + htmlPath, { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  // Open all details so content is accessible
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => d.open = true);
  });
  await new Promise(r => setTimeout(r, 500));
  return page;
}

async function getPanel(page) {
  return page.evaluate(() => {
    const p = document.querySelector('.hover-panel');
    return p ? { text: p.textContent.substring(0, 120), visible: p.offsetParent !== null } : null;
  });
}

async function clearPanel(page) {
  await page.evaluate(() => {
    document.querySelectorAll('.hover-panel').forEach(p => p.remove());
    document.querySelectorAll('[aria-describedby]').forEach(el => el.removeAttribute('aria-describedby'));
  });
  await new Promise(r => setTimeout(r, 200));
}

// Scroll to element, wait, then get fresh bounding rect
async function scrollToAndGetPos(page, selector) {
  return page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    el.scrollIntoView({ block: 'center' });
    const rect = el.getBoundingClientRect();
    return { x: rect.x + rect.width / 2, y: rect.y + rect.height / 2, text: el.textContent.trim().substring(0, 40) };
  }, selector);
}

// Find Nth hover-term not in summary, scroll to it
async function findFreeHoverTerm(page, n = 0) {
  return page.evaluate((n) => {
    const terms = Array.from(document.querySelectorAll('.hover-term[data-hover]'))
      .filter(t => !t.closest('summary') && !t.closest('a'));
    const t = terms[n];
    if (!t) return null;
    t.scrollIntoView({ block: 'center' });
    const rect = t.getBoundingClientRect();
    return { x: rect.x + rect.width / 2, y: rect.y + rect.height / 2, text: t.textContent.trim().substring(0, 40) };
  }, n);
}

// Dispatch synthetic touch events on an element found by selector
async function syntheticTap(page, selector) {
  return page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (!el) return false;
    el.scrollIntoView({ block: 'center' });
    const rect = el.getBoundingClientRect();
    const touch = new Touch({
      identifier: Date.now(), target: el,
      clientX: rect.x + rect.width / 2, clientY: rect.y + rect.height / 2
    });
    el.dispatchEvent(new TouchEvent('touchstart', {
      touches: [touch], changedTouches: [touch], bubbles: true
    }));
    el.dispatchEvent(new TouchEvent('touchend', {
      touches: [], changedTouches: [touch], bubbles: true
    }));
    return true;
  }, selector);
}

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox']
  });

  // ============================================================
  console.log('\n═══ DESKTOP (mouse) ═══\n');
  // ============================================================

  const desktop = await openPage(browser, false);

  // --- Hover popups ---
  console.log('Hover popups:');
  {
    await clearPanel(desktop);
    const pos = await findFreeHoverTerm(desktop, 0);
    await new Promise(r => setTimeout(r, 200));
    const freshPos = await findFreeHoverTerm(desktop, 0);
    await desktop.mouse.move(freshPos.x, freshPos.y);
    await new Promise(r => setTimeout(r, 400));
    ok((await getPanel(desktop)) !== null, 'D1: Hover on body hover-term ("' + freshPos.text + '") shows popup');
    await desktop.mouse.move(0, 0);
    await new Promise(r => setTimeout(r, 300));
  }

  {
    await clearPanel(desktop);
    // Use a bottom-nav button (always visible, good hit-test target)
    const pos = await scrollToAndGetPos(desktop, '#expand-toggle[data-hover]');
    if (pos) {
      await new Promise(r => setTimeout(r, 200));
      const fresh = await scrollToAndGetPos(desktop, '#expand-toggle[data-hover]');
      await desktop.mouse.move(fresh.x, fresh.y);
      await new Promise(r => setTimeout(r, 400));
      ok((await getPanel(desktop)) !== null, 'D2: Hover on hover-nav button ("' + fresh.text + '") shows popup');
      await desktop.mouse.move(0, 0);
      await new Promise(r => setTimeout(r, 300));
    }
  }

  // --- Click popups ---
  console.log('Click popups:');
  {
    await clearPanel(desktop);
    const pos = await findFreeHoverTerm(desktop, 1);
    await new Promise(r => setTimeout(r, 200));
    const fresh = await findFreeHoverTerm(desktop, 1);
    await desktop.mouse.click(fresh.x, fresh.y);
    await new Promise(r => setTimeout(r, 400));
    ok((await getPanel(desktop)) !== null, 'D3: Click on hover-term shows popup');

    // Click again to dismiss
    const fresh2 = await findFreeHoverTerm(desktop, 1);
    await desktop.mouse.click(fresh2.x, fresh2.y);
    await new Promise(r => setTimeout(r, 400));
    ok((await getPanel(desktop)) === null, 'D4: Second click dismisses popup');
  }

  {
    await clearPanel(desktop);
    const pos = await findFreeHoverTerm(desktop, 2);
    await new Promise(r => setTimeout(r, 200));
    const fresh = await findFreeHoverTerm(desktop, 2);
    await desktop.mouse.click(fresh.x, fresh.y);
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(desktop)) !== null, 'D5a: Popup shown for click-outside test');
    await desktop.mouse.click(10, 10);
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(desktop)) === null, 'D5b: Click outside dismisses popup');
  }

  // --- Navigation ---
  console.log('Navigation:');
  {
    const navWorks = await desktop.evaluate(() => {
      const link = document.querySelector('a.hover-nav[data-hover][href]');
      return link ? { href: link.getAttribute('href'), text: link.textContent.trim().substring(0, 30) } : null;
    });
    ok(navWorks !== null, 'D6: hover-nav links have href ("' + (navWorks?.text || '') + '" → ' + (navWorks?.href || '') + ')');
  }

  // --- Menu (TOC) ---
  console.log('TOC menu:');
  {
    const tocInfo = await desktop.evaluate(() => {
      const toc = document.getElementById('TOC');
      if (!toc) return null;
      const links = toc.querySelectorAll('a[data-hover]');
      const partLabels = toc.querySelectorAll('.toc-part-label[data-hover]');
      return { linkCount: links.length, partLabelCount: partLabels.length };
    });
    ok(tocInfo && tocInfo.linkCount >= 40, 'D7: TOC links with data-hover (' + tocInfo?.linkCount + ' >= 40)');
    ok(tocInfo && tocInfo.partLabelCount >= 4, 'D8: Part labels with data-hover (' + tocInfo?.partLabelCount + ' >= 4)');
  }

  // --- Accordion expand/collapse ---
  console.log('Accordion:');
  {
    const accordionWorks = await desktop.evaluate(() => {
      const details = document.querySelector('details.chapter-section');
      if (!details) return null;
      details.open = false;
      const summary = details.querySelector('summary');
      summary.click();
      const opened = details.open;
      summary.click();
      const closed = !details.open;
      return { opened, closed };
    });
    ok(accordionWorks?.opened, 'D9: Accordion opens on click');
    ok(accordionWorks?.closed, 'D10: Accordion closes on click');
  }

  // --- Expand/Collapse All ---
  console.log('Expand/Collapse All:');
  {
    const expandWorks = await desktop.evaluate(() => {
      const btn = document.getElementById('expand-toggle');
      if (!btn) return null;
      // Close all first
      document.querySelectorAll('details').forEach(d => d.open = false);
      btn.textContent = 'Expand All';
      btn.click();
      const allOpen = Array.from(document.querySelectorAll('details')).every(d => d.open);
      btn.click();
      const allClosed = Array.from(document.querySelectorAll('details')).every(d => !d.open);
      // Re-open for further tests
      document.querySelectorAll('details').forEach(d => d.open = true);
      return { allOpen, allClosed };
    });
    ok(expandWorks?.allOpen, 'D11: Expand All opens all sections');
    ok(expandWorks?.allClosed, 'D12: Collapse All closes all sections');
  }

  // --- Back button ---
  console.log('Back button:');
  {
    const backWorks = await desktop.evaluate(() => {
      const backBtn = document.getElementById('nav-back');
      return backBtn ? { exists: true, hidden: backBtn.style.display === 'none' } : null;
    });
    ok(backWorks?.exists, 'D13: Back button exists');
    ok(backWorks?.hidden, 'D14: Back button hidden when nav stack empty');
  }

  // --- Copy buttons (Science Firmware Upgrade) ---
  console.log('Copy buttons:');
  {
    const copyBtns = await desktop.evaluate(() => {
      const btns = document.querySelectorAll('.copy-llm-primer');
      return { count: btns.length, texts: Array.from(btns).map(b => b.textContent.trim().substring(0, 40)) };
    });
    ok(copyBtns.count >= 1, 'D15: Copy Prompt button(s) present (' + copyBtns.count + ')');

    const primerDiv = await desktop.evaluate(() => {
      const div = document.getElementById('llm-primer-text');
      return div ? { exists: true, length: div.textContent.length } : null;
    });
    ok(primerDiv?.exists && primerDiv.length > 1000, 'D16: LLM primer content injected (' + (primerDiv?.length || 0) + ' chars)');
  }

  // --- Breadcrumb ---
  console.log('Breadcrumb:');
  {
    const breadcrumb = await desktop.evaluate(() => {
      const bc = document.getElementById('nav-breadcrumb');
      return bc ? { text: bc.textContent.trim(), hasHover: bc.hasAttribute('data-hover') } : null;
    });
    ok(breadcrumb?.hasHover, 'D17: Breadcrumb has data-hover popup');
  }

  // --- Stack chart ---
  console.log('Stack chart:');
  {
    await clearPanel(desktop);
    const stackPos = await scrollToAndGetPos(desktop, '[data-hover-id="stack-fire"]');
    if (stackPos) {
      await new Promise(r => setTimeout(r, 200));
      const fresh = await scrollToAndGetPos(desktop, '[data-hover-id="stack-fire"]');
      await desktop.mouse.move(fresh.x, fresh.y);
      await new Promise(r => setTimeout(r, 400));
      const panel = await getPanel(desktop);
      ok(panel !== null, 'D18: Hover on Stack chart "Fire" cell shows popup');
      await desktop.mouse.move(0, 0);
      await new Promise(r => setTimeout(r, 200));
    }

    const stackWidth = await desktop.evaluate(() => {
      const chart = document.getElementById('stack-chart');
      if (!chart) return null;
      const table = chart.parentElement?.querySelector('table') ||
                     chart.nextElementSibling;
      if (!table || table.tagName !== 'TABLE') return null;
      const parent = table.parentElement;
      return { tableWidth: table.offsetWidth, parentWidth: parent.offsetWidth };
    });
    if (stackWidth) {
      const ratio = stackWidth.tableWidth / stackWidth.parentWidth;
      ok(ratio > 0.8, 'D19: Stack chart width (' + Math.round(ratio * 100) + '% of container, > 80%)');
    } else {
      skip('D19: Stack chart table not found');
    }
  }

  // --- Hover ID footers (dev build) ---
  console.log('Hover IDs:');
  {
    const hasHoverIds = await desktop.evaluate(() => {
      const terms = document.querySelectorAll('[data-hover-id]');
      return { count: terms.length, sample: terms[0]?.getAttribute('data-hover-id') };
    });
    ok(hasHoverIds.count > 60, 'D20: data-hover-id attributes present (' + hasHoverIds.count + ', sample: ' + hasHoverIds.sample + ')');
  }

  await desktop.close();

  // ============================================================
  console.log('\n═══ MOBILE (touch) ═══\n');
  // ============================================================

  const mobile = await openPage(browser, true);

  // --- Touch on body hover-term ---
  console.log('Hover popups (touch):');
  {
    await clearPanel(mobile);
    await syntheticTap(mobile, '.hover-term[data-hover]:not(summary .hover-term)');
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(mobile)) !== null, 'M1: Touch on body hover-term shows popup');
  }

  // --- Touch on title-line hover-term (inside summary) ---
  {
    await clearPanel(mobile);
    const result = await mobile.evaluate(() => {
      const terms = Array.from(document.querySelectorAll('.hover-term[data-hover]'))
        .filter(t => t.closest('summary') && !t.classList.contains('hover-nav'));
      const t = terms[0];
      if (!t) return null;
      t.scrollIntoView({ block: 'center' });
      const rect = t.getBoundingClientRect();
      const touch = new Touch({
        identifier: Date.now(), target: t,
        clientX: rect.x + rect.width / 2, clientY: rect.y + rect.height / 2
      });
      t.dispatchEvent(new TouchEvent('touchstart', {
        touches: [touch], changedTouches: [touch], bubbles: true
      }));
      t.dispatchEvent(new TouchEvent('touchend', {
        touches: [], changedTouches: [touch], bubbles: true
      }));
      return t.textContent.trim().substring(0, 20);
    });
    await new Promise(r => setTimeout(r, 300));
    ok(result && (await getPanel(mobile)) !== null, 'M2: Touch on title-line ("' + result + '") shows popup');
  }

  // --- Touch on hover-nav does NOT show popup ---
  {
    await clearPanel(mobile);
    await syntheticTap(mobile, '.hover-nav[data-hover]');
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(mobile)) === null, 'M3: Touch on hover-nav does NOT show popup (native action)');
  }

  // --- Touch outside dismisses ---
  {
    await clearPanel(mobile);
    await syntheticTap(mobile, '.hover-term[data-hover]:not(summary .hover-term)');
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(mobile)) !== null, 'M4a: Popup shown');

    await mobile.evaluate(() => {
      const body = document.body;
      const touch = new Touch({
        identifier: Date.now(), target: body, clientX: 10, clientY: 10
      });
      body.dispatchEvent(new TouchEvent('touchend', {
        touches: [], changedTouches: [touch], bubbles: true
      }));
    });
    await new Promise(r => setTimeout(r, 300));
    ok((await getPanel(mobile)) === null, 'M4b: Touch outside dismisses popup');
  }

  // --- Stack chart cell touch ---
  console.log('Stack chart (touch):');
  {
    await clearPanel(mobile);
    await new Promise(r => setTimeout(r, 600)); // Wait for lastTouchTime to expire
    // Direct dispatch on the exact element (selector-based syntheticTap may miss it)
    const m5result = await mobile.evaluate(() => {
      const el = document.querySelector('[data-hover-id="stack-question-mark"]');
      if (!el) return 'NOT FOUND';
      el.scrollIntoView({ block: 'center' });
      const rect = el.getBoundingClientRect();
      const touch = new Touch({
        identifier: Date.now(), target: el,
        clientX: rect.x + rect.width / 2, clientY: rect.y + rect.height / 2
      });
      el.dispatchEvent(new TouchEvent('touchstart', {
        touches: [touch], changedTouches: [touch], bubbles: true
      }));
      el.dispatchEvent(new TouchEvent('touchend', {
        touches: [], changedTouches: [touch], bubbles: true
      }));
      return 'OK';
    });
    await new Promise(r => setTimeout(r, 500));
    const panel = await getPanel(mobile);
    if (!panel) {
      // Debug: check what panel state we're in
      const debug = await mobile.evaluate(() => {
        return {
          panels: document.querySelectorAll('.hover-panel').length,
          el: (() => {
            const el = document.querySelector('[data-hover-id="stack-question-mark"]');
            return el ? { tag: el.tagName, cls: el.className, parent: el.parentElement.tagName } : null;
          })()
        };
      });
      console.log('    M5 DEBUG:', JSON.stringify(debug));
    }
    // Check full panel text (getPanel truncates to 120 chars, "Flat" may be beyond that)
    const m5full = await mobile.evaluate(() => {
      const p = document.querySelector('.hover-panel');
      return p ? p.textContent : '';
    });
    ok(m5result === 'OK' && panel !== null && m5full.includes('Flat'), 'M5: Touch on "?" shows popup mentioning Flat');
  }

  // --- Accordion works on mobile ---
  console.log('Accordion (mobile):');
  {
    const accordionWorks = await mobile.evaluate(() => {
      const details = document.querySelector('details.chapter-section');
      if (!details) return null;
      details.open = false;
      const summary = details.querySelector('summary');
      summary.click();
      return { opened: details.open };
    });
    ok(accordionWorks?.opened, 'M6: Accordion opens on tap');
  }

  // --- TOC navigation works on mobile ---
  console.log('TOC navigation (mobile):');
  {
    const tocNavWorks = await mobile.evaluate(() => {
      const link = document.querySelector('#TOC a[href]');
      if (!link) return null;
      return { href: link.getAttribute('href'), hasDataHover: link.hasAttribute('data-hover'), isHoverNav: link.classList.contains('hover-nav') };
    });
    ok(tocNavWorks?.isHoverNav, 'M7: TOC links are hover-nav class (touch passes through to navigate)');
  }

  // --- Lower nav bar items ---
  console.log('Lower nav bar (mobile):');
  {
    const navItems = await mobile.evaluate(() => {
      const items = {};
      const bc = document.getElementById('nav-breadcrumb');
      items.breadcrumb = bc ? bc.classList.contains('hover-nav') : false;
      const share = document.getElementById('nav-share');
      items.share = share ? share.classList.contains('hover-nav') : false;
      const expand = document.getElementById('expand-toggle');
      items.expand = expand ? expand.classList.contains('hover-nav') : false;
      const back = document.getElementById('nav-back');
      items.back = back ? back.classList.contains('hover-nav') : false;
      const evalBtn = document.getElementById('nav-evaluate');
      items.eval = evalBtn ? evalBtn.classList.contains('hover-nav') : false;
      return items;
    });
    ok(navItems.breadcrumb, 'M8a: Breadcrumb is hover-nav');
    ok(navItems.share, 'M8b: Share button is hover-nav');
    ok(navItems.expand, 'M8c: Expand button is hover-nav');
    ok(navItems.back, 'M8d: Back button is hover-nav');
    ok(navItems.eval, 'M8e: AI Eval button is hover-nav');
  }

  await mobile.close();

  // ============================================================
  console.log('\n═══ STRUCTURAL CHECKS ═══\n');
  // ============================================================

  const struct = await openPage(browser, false);

  const counts = await struct.evaluate(() => {
    return {
      dataHover: document.querySelectorAll('[data-hover]').length,
      hoverTerm: document.querySelectorAll('.hover-term[data-hover]').length,
      hoverNav: document.querySelectorAll('.hover-nav[data-hover]').length,
      titleAttrs: document.querySelectorAll('[title]').length,
      hoverTermInSummary: Array.from(document.querySelectorAll('.hover-term[data-hover]')).filter(t => t.closest('summary')).length,
      duplicateIds: (() => {
        const ids = {};
        document.querySelectorAll('[data-hover-id]').forEach(el => {
          const id = el.getAttribute('data-hover-id');
          ids[id] = (ids[id] || 0) + 1;
        });
        return Object.entries(ids).filter(([_, c]) => c > 1).map(([id, c]) => id + ':' + c);
      })(),
      emptyHover: document.querySelectorAll('[data-hover=""]').length,
      stackCells: document.querySelectorAll('[data-hover-id^="stack-"]').length,
      hoveridCount: document.querySelectorAll('[data-hover-id]').length,
      unresolved: (document.body.innerHTML.match(/HOVERSTART/g) || []).length,
      primerDiv: !!document.getElementById('llm-primer-text'),
      abstractsDiv: !!document.getElementById('spiral-abstracts-text')
    };
  });

  ok(counts.dataHover >= 200, 'S1: Total data-hover elements (' + counts.dataHover + ' >= 200)');
  ok(counts.hoverTerm >= 60, 'S2: hover-term elements (' + counts.hoverTerm + ' >= 60)');
  ok(counts.hoverNav >= 100, 'S3: hover-nav elements (' + counts.hoverNav + ' >= 100)');
  ok(counts.titleAttrs <= 5, 'S4: Remaining title= attrs (' + counts.titleAttrs + ' <= 5)');
  ok(counts.hoverTermInSummary === 3, 'S5: hover-terms in summary = 3 (title line only, got ' + counts.hoverTermInSummary + ')');
  ok(counts.duplicateIds.length === 0, 'S6: No duplicate hover-ids' + (counts.duplicateIds.length ? ' DUPS: ' + counts.duplicateIds.join(', ') : ''));
  ok(counts.emptyHover === 0, 'S7: No empty data-hover (' + counts.emptyHover + ')');
  ok(counts.stackCells === 14, 'S8: Stack chart cells = 14 (got ' + counts.stackCells + ')');
  ok(counts.unresolved === 0, 'S9: No unresolved HOVERSTART markers (' + counts.unresolved + ')');
  ok(counts.primerDiv, 'S10: LLM primer div present');
  ok(counts.abstractsDiv, 'S11: Spiral abstracts div present');

  await struct.close();
  await browser.close();

  // ============================================================
  console.log('\n' + '═'.repeat(50));
  console.log('PASSED: ' + passed + '  FAILED: ' + failed + (skipped ? '  SKIPPED: ' + skipped : ''));
  if (failed > 0) {
    console.log('\x1b[31mSOME TESTS FAILED\x1b[0m');
    process.exit(1);
  } else {
    console.log('\x1b[32mALL TESTS PASSED\x1b[0m');
  }
})();
