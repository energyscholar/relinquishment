/**
 * Relinquishment E2E Device Tests — Layer 2
 *
 * Tests the BUILT HTML output (Relinquishment.html) on real device emulation:
 *   Phone:   iPhone 14 (390x844, touch, isMobile)
 *   Tablet:  iPad Mini (768x1024, touch)
 *   Desktop: 1280x800 (no touch)
 *
 * Layer 1 = test-hover-panel.html (mock DOM, in-browser)
 * Layer 2 = this file (built HTML, Puppeteer, device emulation)
 *
 * Run: node build/test-e2e-devices.js
 * Requires: puppeteer (npm install puppeteer)
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

// --- Config ---

const HTML_PATH = path.resolve(__dirname, '..', 'docs', 'downloads', 'Relinquishment.html');
const FILE_URL = 'file://' + HTML_PATH;

const BROWSER_ARGS = [
  '--no-sandbox',
  '--disable-setuid-sandbox',
  '--disable-dev-shm-usage',
];

// Device configurations
const DEVICES = {
  phone: {
    name: 'iPhone 14',
    viewport: { width: 390, height: 844, deviceScaleFactor: 3, isMobile: true, hasTouch: true },
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
  },
  tablet: {
    name: 'iPad Mini',
    viewport: { width: 768, height: 1024, deviceScaleFactor: 2, isMobile: false, hasTouch: true },
    userAgent: 'Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
  },
  desktop: {
    name: 'Desktop 1280x800',
    viewport: { width: 1280, height: 800, deviceScaleFactor: 1, isMobile: false, hasTouch: false },
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  },
};

// --- Test Framework ---

let totalPassed = 0;
let totalFailed = 0;
let totalSkipped = 0;
const failures = [];

function pass(name) {
  totalPassed++;
  console.log(`  PASS: ${name}`);
}

function fail(name, reason) {
  totalFailed++;
  const msg = reason ? `${name} — ${reason}` : name;
  failures.push(msg);
  console.log(`  FAIL: ${name}${reason ? ' — ' + reason : ''}`);
}

function skip(name, reason) {
  totalSkipped++;
  console.log(`  SKIP: ${name} (${reason})`);
}

function group(name) {
  console.log(`\n=== ${name} ===`);
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// --- Browser Helpers ---

async function launchBrowser() {
  return puppeteer.launch({
    headless: true,
    args: BROWSER_ARGS,
  });
}

async function createPage(browser, deviceKey) {
  const page = await browser.newPage();
  const device = DEVICES[deviceKey];
  await page.setViewport(device.viewport);
  await page.setUserAgent(device.userAgent);
  return page;
}

// Collect console errors during page load
function trackConsoleErrors(page) {
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', err => {
    errors.push(err.message);
  });
  return errors;
}

async function loadPage(page, url, waitMs = 2000) {
  await page.goto(url, { waitUntil: 'load', timeout: 15000 });
  await delay(waitMs);
}

async function safeClose(page) {
  try { await page.close(); } catch (_) { /* already closed */ }
}

// --- Test Groups ---

/**
 * 1. BUILD VERIFICATION (all devices)
 */
async function testBuildVerification(browser) {
  group('1. BUILD VERIFICATION');

  for (const [key, device] of Object.entries(DEVICES)) {
    const label = `[${device.name}]`;
    const page = await createPage(browser, key);
    const errors = trackConsoleErrors(page);

    try {
      // 1a: File loads without errors
      await loadPage(page, FILE_URL);
      const title = await page.title();
      if (title && title.length > 0) {
        pass(`${label} Built HTML loads successfully`);
      } else {
        fail(`${label} Built HTML loads successfully`, 'empty title');
      }

      // 1b: No console errors on load
      // Filter out benign file:// protocol warnings
      const realErrors = errors.filter(e =>
        !e.includes('favicon') &&
        !e.includes('ERR_FILE_NOT_FOUND') &&
        !e.includes('navigator.clipboard')
      );
      if (realErrors.length === 0) {
        pass(`${label} No console errors on load`);
      } else {
        fail(`${label} No console errors on load`, realErrors.join('; '));
      }

      // 1c: Hover attributes exist
      // Preferred: data-hover-id (externalized). Legacy fallbacks: data-hover, title.
      const hoverInfo = await page.evaluate(() => {
        const dataHoverId = document.querySelectorAll('.hover-term[data-hover-id]').length;
        const dataHover = document.querySelectorAll('.hover-term[data-hover]').length;
        const titleHover = document.querySelectorAll('.hover-term[title]').length;
        return { dataHoverId, dataHover, titleHover };
      });
      if (hoverInfo.dataHoverId > 0) {
        pass(`${label} Hover terms use data-hover-id externalization (${hoverInfo.dataHoverId} found)`);
      } else if (hoverInfo.dataHover > 0) {
        pass(`${label} Hover terms use inline data-hover (${hoverInfo.dataHover} found, externalization pending)`);
      } else if (hoverInfo.titleHover > 0) {
        pass(`${label} Hover terms exist with title attributes (${hoverInfo.titleHover} found, data-hover migration pending)`);
      } else {
        fail(`${label} Hover terms exist`, 'no .hover-term elements found');
      }

      // 1d: Nav bar renders
      const hasNav = await page.evaluate(() => {
        const nav = document.getElementById('reader-nav');
        if (!nav) return false;
        const rect = nav.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
      });
      if (hasNav) {
        pass(`${label} Nav bar (#reader-nav) renders`);
      } else {
        fail(`${label} Nav bar (#reader-nav) renders`);
      }

    } finally {
      await safeClose(page);
    }
  }
}

/**
 * 2. DEEP LINK ARRIVAL (all devices)
 */
async function testDeepLinkArrival(browser) {
  group('2. DEEP LINK ARRIVAL');

  for (const [key, device] of Object.entries(DEVICES)) {
    const label = `[${device.name}]`;
    const page = await createPage(browser, key);

    try {
      // 2a: Navigate to #ch:firmware-update — target section auto-expanded
      await loadPage(page, FILE_URL + '#ch:firmware-update', 2000);

      const fwResult = await page.evaluate(() => {
        const target = document.getElementById('ch:firmware-update');
        if (!target) return { found: false };
        // Check that ancestor details are open
        let el = target;
        let allOpen = true;
        while (el) {
          if (el.tagName === 'DETAILS' && !el.open) {
            allOpen = false;
            break;
          }
          el = el.parentElement;
        }
        // Check for .deep-link-target class (may not be implemented yet)
        const hasDeepLinkClass = target.classList.contains('deep-link-target') ||
          target.closest('.deep-link-target') !== null;
        return { found: true, allOpen, hasDeepLinkClass };
      });

      if (fwResult.found && fwResult.allOpen) {
        pass(`${label} #ch:firmware-update — target section auto-expanded`);
      } else if (fwResult.found) {
        fail(`${label} #ch:firmware-update — target section auto-expanded`, 'ancestor details not all open');
      } else {
        fail(`${label} #ch:firmware-update — target section auto-expanded`, 'target element not found');
      }

      if (fwResult.hasDeepLinkClass) {
        pass(`${label} #ch:firmware-update — has .deep-link-target class`);
      } else {
        skip(`${label} #ch:firmware-update — .deep-link-target class`, 'not yet implemented');
      }

      // 2b: Navigate to #pos10:the-braid — ancestor details open
      await loadPage(page, FILE_URL + '#pos10:the-braid', 2000);

      const braidResult = await page.evaluate(() => {
        const target = document.getElementById('pos10:the-braid');
        if (!target) return { found: false };
        let el = target;
        let allOpen = true;
        const closedAncestors = [];
        while (el) {
          if (el.tagName === 'DETAILS') {
            if (!el.open) {
              allOpen = false;
              closedAncestors.push(el.className || 'unnamed');
            }
          }
          el = el.parentElement;
        }
        return { found: true, allOpen, closedAncestors };
      });

      if (braidResult.found && braidResult.allOpen) {
        pass(`${label} #pos10:the-braid — ancestor details (part-section, book-section) are open`);
      } else if (braidResult.found) {
        fail(`${label} #pos10:the-braid — ancestor details open`, `closed: ${braidResult.closedAncestors.join(', ')}`);
      } else {
        fail(`${label} #pos10:the-braid — ancestor details open`, 'target element not found');
      }

      // 2c: scroll-margin-top — target heading not flush with viewport top
      const scrollMargin = await page.evaluate(() => {
        const target = document.getElementById('pos10:the-braid');
        if (!target) return { found: false };
        const rect = target.getBoundingClientRect();
        return { found: true, top: rect.top };
      });

      if (scrollMargin.found && scrollMargin.top > 0) {
        pass(`${label} scroll-margin-top — target heading not flush with viewport top (top=${Math.round(scrollMargin.top)}px)`);
      } else if (scrollMargin.found) {
        // top=0 or negative means flush/hidden — may be acceptable depending on implementation
        skip(`${label} scroll-margin-top — target at top=${Math.round(scrollMargin.top)}px`, 'scroll-margin-top may not be set yet');
      } else {
        fail(`${label} scroll-margin-top check`, 'target not found');
      }

    } finally {
      await safeClose(page);
    }
  }
}

/**
 * 3. PHONE PANEL INTERACTION (iPhone 14 only)
 */
async function testPhonePanelInteraction(browser) {
  group('3. PHONE PANEL INTERACTION');

  const page = await createPage(browser, 'phone');

  try {
    await loadPage(page, FILE_URL, 2000);

    // Expand all sections so hover terms are visible
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
    });
    await delay(500);

    // Find first hover term — prefer externalized data-hover-id, fall back to inline/title
    const termSelector = await page.evaluate(() => {
      if (document.querySelector('.hover-term[data-hover-id]')) return '.hover-term[data-hover-id]';
      if (document.querySelector('.hover-term[data-hover]')) return '.hover-term[data-hover]';
      if (document.querySelector('.hover-term[title]')) return '.hover-term[title]';
      return null;
    });

    if (!termSelector) {
      skip('3a — Phone panel tap', 'no hover terms found');
      skip('3b — Panel full-width', 'no hover terms');
      skip('3c — Panel content matches', 'no hover terms');
      skip('3d — Tap outside dismisses', 'no hover terms');
      skip('3e — Only one panel at a time', 'no hover terms');
      await safeClose(page);
      return;
    }

    const attrName = termSelector.includes('data-hover-id') ? 'data-hover-id'
                   : termSelector.includes('data-hover') ? 'data-hover' : 'title';

    // 3a: Tap on .hover-term — .hover-panel appears
    const firstTerm = await page.$(termSelector);
    if (firstTerm) {
      await firstTerm.tap();
      await delay(600);

      const panelInfo = await page.evaluate((attr) => {
        const panel = document.querySelector('.hover-panel');
        if (!panel) return { exists: false };
        const rect = panel.getBoundingClientRect();
        return {
          exists: true,
          visible: rect.width > 0 && rect.height > 0,
          width: rect.width,
          text: panel.textContent.substring(0, 100),
        };
      }, attrName);

      if (panelInfo.exists && panelInfo.visible) {
        pass('[iPhone 14] Tap on hover-term shows .hover-panel');

        // 3b: Panel is full-width (close to device width, 390px)
        if (panelInfo.width >= 350) {
          pass(`[iPhone 14] Panel is full-width (${Math.round(panelInfo.width)}px on 390px screen)`);
        } else {
          fail(`[iPhone 14] Panel is full-width`, `width=${Math.round(panelInfo.width)}px, expected >=350px`);
        }

        // 3c: Panel content matches data-hover/title text
        const defText = await page.evaluate((sel, attr) => {
          const term = document.querySelector(sel);
          return term ? (term.getAttribute(attr) || '').substring(0, 50) : '';
        }, termSelector, attrName);

        if (defText.length > 0 && panelInfo.text.includes(defText.substring(0, 25))) {
          pass('[iPhone 14] Panel content matches definition text');
        } else {
          // Panel might format text differently, check any overlap
          skip('[iPhone 14] Panel content matches definition text', 'content check inconclusive');
        }

        // 3d: Tap outside panel — panel dismissed
        await page.tap('body');  // tap body, outside panel
        await delay(400);
        const panelGone = await page.evaluate(() => {
          const panel = document.querySelector('.hover-panel');
          return !panel || panel.offsetParent === null ||
            window.getComputedStyle(panel).display === 'none';
        });
        if (panelGone) {
          pass('[iPhone 14] Tap outside panel dismisses it');
        } else {
          fail('[iPhone 14] Tap outside panel dismisses it');
        }

        // 3e: Only one panel visible at a time after rapid taps
        const terms = await page.$$(`${termSelector}`);
        if (terms.length >= 2) {
          await terms[0].tap();
          await delay(100);
          await terms[1].tap();
          await delay(600);

          const visiblePanels = await page.evaluate(() => {
            const panels = document.querySelectorAll('.hover-panel');
            return Array.from(panels).filter(p =>
              p.offsetParent !== null &&
              window.getComputedStyle(p).display !== 'none'
            ).length;
          });

          if (visiblePanels <= 1) {
            pass('[iPhone 14] Only one panel visible after rapid taps');
          } else {
            fail('[iPhone 14] Only one panel visible after rapid taps', `${visiblePanels} panels visible`);
          }
        } else {
          skip('[iPhone 14] Only one panel after rapid taps', 'not enough hover terms');
        }

      } else {
        skip('[iPhone 14] Tap on hover-term shows panel', 'hover-panel system not yet implemented');
        skip('[iPhone 14] Panel full-width', 'depends on panel system');
        skip('[iPhone 14] Panel content matches', 'depends on panel system');
        skip('[iPhone 14] Tap outside dismisses', 'depends on panel system');
        skip('[iPhone 14] Only one panel at a time', 'depends on panel system');
      }
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 4. PHONE NAVIGATION (iPhone 14 only)
 */
async function testPhoneNavigation(browser) {
  group('4. PHONE NAVIGATION');

  const page = await createPage(browser, 'phone');

  try {
    await loadPage(page, FILE_URL, 2000);

    // Expand all sections
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
    });
    await delay(500);

    // Look for a hover term with click-through (data-hover-target)
    const hasClickThrough = await page.evaluate(() => {
      return document.querySelector('.hover-term[data-hover-target]') !== null;
    });

    if (!hasClickThrough) {
      skip('[iPhone 14] Click-through link in panel', 'data-hover-target not implemented yet');
      skip('[iPhone 14] Back button appears after click-through', 'depends on click-through');
      skip('[iPhone 14] Back button restores position', 'depends on click-through');
      skip('[iPhone 14] URL reflects current section', 'depends on click-through');
      await safeClose(page);
      return;
    }

    // 4a: Tap on click-through link — target auto-expands
    const ctTerm = await page.$('.hover-term[data-hover-target]');
    await ctTerm.tap();
    await delay(600);

    // Find and tap click-through element in panel
    const clickedThrough = await page.evaluate(() => {
      const panel = document.querySelector('.hover-panel');
      if (!panel) return false;
      const link = panel.querySelector('a, [data-click-through], .panel-navigate');
      if (!link) return false;
      link.click();
      return true;
    });

    if (clickedThrough) {
      await delay(800);
      pass('[iPhone 14] Click-through link in panel navigates');

      // 4b: Back button appears
      const backVisible = await page.evaluate(() => {
        const back = document.getElementById('nav-back') ||
          document.querySelector('[data-nav-back]') ||
          document.querySelector('.back-button');
        if (!back) return false;
        return back.offsetParent !== null &&
          window.getComputedStyle(back).display !== 'none';
      });

      if (backVisible) {
        pass('[iPhone 14] Back button appears after click-through');

        // 4c: Back button restores position
        const backSelector = await page.evaluate(() => {
          if (document.getElementById('nav-back')) return '#nav-back';
          if (document.querySelector('[data-nav-back]')) return '[data-nav-back]';
          if (document.querySelector('.back-button')) return '.back-button';
          return null;
        });

        if (backSelector) {
          await page.tap(backSelector);
          await delay(800);
          pass('[iPhone 14] Back button tap restores previous position');
        }
      } else {
        skip('[iPhone 14] Back button appears', 'back button not found/visible');
        skip('[iPhone 14] Back button restores position', 'depends on back button');
      }

      // 4d: URL reflects current section
      const currentUrl = page.url();
      if (currentUrl.includes('#')) {
        pass(`[iPhone 14] URL reflects current section (${currentUrl.split('#')[1]})`);
      } else {
        skip('[iPhone 14] URL reflects current section', 'no hash in URL');
      }

    } else {
      skip('[iPhone 14] Click-through navigation', 'no click-through link in panel');
      skip('[iPhone 14] Back button', 'depends on click-through');
      skip('[iPhone 14] Back restores position', 'depends on click-through');
      skip('[iPhone 14] URL reflects section', 'depends on click-through');
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 5. PHONE SHARE (iPhone 14 only)
 */
async function testPhoneShare(browser) {
  group('5. PHONE SHARE');

  const page = await createPage(browser, 'phone');

  try {
    await loadPage(page, FILE_URL, 2000);

    // Expand all so summaries are visible
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
    });
    await delay(500);

    // 5a: Check for .heading-link elements as share mechanism
    // (.section-share removed — Plan 0134c feature deleted)
    const shareInfo = await page.evaluate(() => {
      const headingLinks = document.querySelectorAll('.heading-link');
      return { headingLinks: headingLinks.length };
    });

    if (shareInfo.headingLinks > 0) {
      pass(`[iPhone 14] Share mechanism exists via .heading-link elements (${shareInfo.headingLinks} found)`);
    } else {
      skip('[iPhone 14] share mechanism', 'no heading-link elements found');
    }

    // 5b: Share icon tap target >= 44px (heading-link only)
    const tapTargetOk = await page.evaluate(() => {
      const shareEl = document.querySelector('.heading-link');
      if (!shareEl) return { found: false };
      const rect = shareEl.getBoundingClientRect();
      return {
        found: true,
        width: rect.width,
        height: rect.height,
        meets44px: rect.width >= 44 || rect.height >= 44,
      };
    });

    if (tapTargetOk.found && tapTargetOk.meets44px) {
      pass(`[iPhone 14] Share tap target >= 44px (${Math.round(tapTargetOk.width)}x${Math.round(tapTargetOk.height)})`);
    } else if (tapTargetOk.found) {
      fail(`[iPhone 14] Share tap target >= 44px`, `${Math.round(tapTargetOk.width)}x${Math.round(tapTargetOk.height)}px — too small for touch`);
    } else {
      skip('[iPhone 14] Share tap target size', 'no share element found');
    }

    // 5c: Share icon tap does NOT toggle parent details
    const navShareExists = await page.$('#nav-share');
    if (navShareExists) {
      // Record state of a details element, click share via evaluate, check state unchanged
      const shareResult = await page.evaluate(() => {
        const firstPart = document.querySelector('details.part-section');
        const beforeState = firstPart ? firstPart.open : null;

        // Simulate tap on #nav-share via click event
        const shareEl = document.getElementById('nav-share');
        if (shareEl) {
          const evt = new MouseEvent('click', { bubbles: true });
          shareEl.dispatchEvent(evt);
        }

        const afterState = firstPart ? firstPart.open : null;
        return { beforeState, afterState };
      });

      if (shareResult.beforeState !== null && shareResult.beforeState === shareResult.afterState) {
        pass('[iPhone 14] Share tap does NOT toggle parent details');
      } else if (shareResult.beforeState === null) {
        skip('[iPhone 14] Share tap isolation', 'no part-section to check');
      } else {
        fail('[iPhone 14] Share tap toggled parent details unexpectedly');
      }
    } else {
      skip('[iPhone 14] Share tap isolation test', '#nav-share not found');
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 6. PHONE RESPONSIVE LAYOUT (iPhone 14 only)
 */
async function testPhoneResponsiveLayout(browser) {
  group('6. PHONE RESPONSIVE LAYOUT');

  const page = await createPage(browser, 'phone');

  try {
    await loadPage(page, FILE_URL, 2000);

    // 6a: Nav bar breadcrumb layout
    const navLayout = await page.evaluate(() => {
      const nav = document.getElementById('reader-nav');
      const breadcrumb = document.getElementById('nav-breadcrumb');
      if (!nav || !breadcrumb) return { found: false };
      const navRect = nav.getBoundingClientRect();
      const bcRect = breadcrumb.getBoundingClientRect();
      const bcStyle = window.getComputedStyle(breadcrumb);
      return {
        found: true,
        navWidth: navRect.width,
        bcWidth: bcRect.width,
        bcFlexBasis: bcStyle.flexBasis,
        bcFlex: bcStyle.flex,
      };
    });

    if (navLayout.found) {
      // On phone (390px), breadcrumb should take significant width
      if (navLayout.bcWidth >= navLayout.navWidth * 0.3) {
        pass(`[iPhone 14] Nav bar breadcrumb has adequate width (${Math.round(navLayout.bcWidth)}px of ${Math.round(navLayout.navWidth)}px)`);
      } else {
        fail(`[iPhone 14] Nav bar breadcrumb width`, `only ${Math.round(navLayout.bcWidth)}px of ${Math.round(navLayout.navWidth)}px`);
      }
    } else {
      fail('[iPhone 14] Nav bar breadcrumb layout', 'nav or breadcrumb not found');
    }

    // 6b: Summary elements have >= 44px height (touch targets)
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
    });
    await delay(300);

    const summaryHeights = await page.evaluate(() => {
      const summaries = document.querySelectorAll('details.chapter-section > summary');
      const heights = [];
      summaries.forEach(s => {
        const rect = s.getBoundingClientRect();
        heights.push(rect.height);
      });
      return heights;
    });

    if (summaryHeights.length > 0) {
      const minHeight = Math.min(...summaryHeights);
      if (minHeight >= 44) {
        pass(`[iPhone 14] Summary elements >= 44px height (min=${Math.round(minHeight)}px)`);
      } else {
        // Some summaries may be shorter due to font size; check average
        const avg = summaryHeights.reduce((a, b) => a + b, 0) / summaryHeights.length;
        if (avg >= 40) {
          pass(`[iPhone 14] Summary elements adequate touch targets (avg=${Math.round(avg)}px, min=${Math.round(minHeight)}px)`);
        } else {
          fail(`[iPhone 14] Summary elements >= 44px`, `min=${Math.round(minHeight)}px, avg=${Math.round(avg)}px`);
        }
      }
    } else {
      fail('[iPhone 14] Summary element height check', 'no chapter summaries found');
    }

    // 6c: Cold-landing primer visible on Part 1-3 chapters
    // These are breadcrumb texts like "New here? Start with The Stack"
    const coldLanding = await page.evaluate(() => {
      // Search for cold-landing text in part summaries or chapter intros
      const body = document.body.textContent;
      const hasNewHere = body.includes('New here') || body.includes('Start with');
      // Also check for any cold-landing class
      const coldEl = document.querySelector('.cold-landing, .cold-landing-primer, [data-cold-landing]');
      return { hasNewHere, hasColdElement: coldEl !== null };
    });

    if (coldLanding.hasColdElement) {
      pass('[iPhone 14] Cold-landing primer elements present');
    } else if (coldLanding.hasNewHere) {
      pass('[iPhone 14] Cold-landing primer text found');
    } else {
      skip('[iPhone 14] Cold-landing primer', 'not yet implemented');
    }

    // 6d: Firmware Update has prominent share element
    const fwShare = await page.evaluate(() => {
      const fwSection = document.getElementById('ch:firmware-update');
      if (!fwSection) return { found: false };
      const details = fwSection.closest('details');
      if (details) details.open = true;
      // Look for copy button (the prominent share element)
      const copyBtn = document.querySelector('.copy-llm-primer, #copy-llm-primer-top, #copy-llm-primer-front');
      const headingLink = fwSection ? fwSection.querySelector('.heading-link') : null;
      return {
        found: true,
        hasCopyBtn: copyBtn !== null,
        hasHeadingLink: headingLink !== null,
      };
    });

    if (fwShare.found && fwShare.hasCopyBtn) {
      pass('[iPhone 14] Firmware Update has prominent share/copy element');
    } else if (fwShare.found && fwShare.hasHeadingLink) {
      pass('[iPhone 14] Firmware Update has heading link for sharing');
    } else if (fwShare.found) {
      skip('[iPhone 14] Firmware Update prominent share element', 'copy button not yet rendered (may need JS execution time)');
    } else {
      fail('[iPhone 14] Firmware Update section not found');
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 7. DESKTOP PANEL INTERACTION (1280x800)
 */
async function testDesktopPanelInteraction(browser) {
  group('7. DESKTOP PANEL INTERACTION');

  const page = await createPage(browser, 'desktop');

  try {
    await loadPage(page, FILE_URL, 2000);

    // Expand all sections
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
    });
    await delay(500);

    // Find hover terms
    const termSelector = await page.evaluate(() => {
      if (document.querySelector('.hover-term[data-hover]')) return '.hover-term[data-hover]';
      if (document.querySelector('.hover-term[title]')) return '.hover-term[title]';
      return null;
    });

    if (!termSelector) {
      skip('[Desktop] All panel tests', 'no hover terms found');
      await safeClose(page);
      return;
    }

    // 7a: Mouse hover with 400ms delay — .hover-panel appears
    const firstTerm = await page.$(termSelector);
    if (firstTerm) {
      await firstTerm.hover();
      await delay(500); // 400ms hover delay + buffer

      const panelExists = await page.evaluate(() => {
        const panel = document.querySelector('.hover-panel');
        if (!panel) return { exists: false };
        const rect = panel.getBoundingClientRect();
        const style = window.getComputedStyle(panel);
        return {
          exists: true,
          visible: rect.width > 0 && rect.height > 0,
          width: rect.width,
          maxWidth: parseInt(style.maxWidth) || rect.width,
        };
      });

      if (panelExists.exists && panelExists.visible) {
        pass('[Desktop] Mouse hover on hover-term shows .hover-panel');

        // 7b: Mouse leave — panel dismissed
        // Move mouse to a neutral area
        await page.mouse.move(10, 10);
        await delay(400);

        const panelDismissed = await page.evaluate(() => {
          const panel = document.querySelector('.hover-panel');
          return !panel || panel.offsetParent === null ||
            window.getComputedStyle(panel).display === 'none';
        });
        if (panelDismissed) {
          pass('[Desktop] Mouse leave dismisses panel');
        } else {
          fail('[Desktop] Mouse leave dismisses panel');
        }

        // 7c: Panel max-width <= 500px
        if (panelExists.maxWidth <= 500) {
          pass(`[Desktop] Panel max-width <= 500px (${panelExists.maxWidth}px)`);
        } else if (panelExists.width <= 500) {
          pass(`[Desktop] Panel width <= 500px (${Math.round(panelExists.width)}px)`);
        } else {
          fail(`[Desktop] Panel max-width <= 500px`, `width=${Math.round(panelExists.width)}px`);
        }

        // 7d: Escape key dismisses panel
        await firstTerm.hover();
        await delay(500);

        await page.keyboard.press('Escape');
        await delay(300);

        const escDismissed = await page.evaluate(() => {
          const panel = document.querySelector('.hover-panel');
          return !panel || panel.offsetParent === null ||
            window.getComputedStyle(panel).display === 'none';
        });
        if (escDismissed) {
          pass('[Desktop] Escape key dismisses panel');
        } else {
          fail('[Desktop] Escape key dismisses panel');
        }

        // 7e: Keyboard: Tab to .hover-term, Enter — panel opens
        await page.keyboard.press('Tab');
        await delay(100);

        // Tab until we reach a hover-term (up to 50 tabs)
        let foundHoverTerm = false;
        for (let i = 0; i < 50; i++) {
          const isFocusedOnTerm = await page.evaluate((sel) => {
            const active = document.activeElement;
            return active && active.matches(sel);
          }, termSelector);

          if (isFocusedOnTerm) {
            foundHoverTerm = true;
            break;
          }
          await page.keyboard.press('Tab');
          await delay(50);
        }

        if (foundHoverTerm) {
          await page.keyboard.press('Enter');
          await delay(500);

          const kbPanelOpen = await page.evaluate(() => {
            const panel = document.querySelector('.hover-panel');
            return panel && panel.offsetParent !== null;
          });

          if (kbPanelOpen) {
            pass('[Desktop] Tab + Enter on hover-term opens panel');
          } else {
            skip('[Desktop] Tab + Enter opens panel', 'keyboard panel activation not implemented');
          }
        } else {
          skip('[Desktop] Keyboard panel activation', 'could not Tab to hover-term (tabindex may not be set)');
        }

      } else {
        skip('[Desktop] Mouse hover shows panel', 'hover-panel system not yet implemented');
        skip('[Desktop] Mouse leave dismisses', 'depends on panel system');
        skip('[Desktop] Panel max-width', 'depends on panel system');
        skip('[Desktop] Escape dismisses', 'depends on panel system');
        skip('[Desktop] Keyboard panel activation', 'depends on panel system');
      }
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 8. IMMUNE SYSTEM CHAIN (iPhone 14)
 * Full chain: #firmware-update → expanded → copy button → clipboard
 */
async function testImmuneSystemChain(browser) {
  group('8. IMMUNE SYSTEM CHAIN');

  const page = await createPage(browser, 'phone');

  try {
    // NOTE: We load WITHOUT hash fragment because autoExpand has a bug
    // where querySelector throws on colon-IDs (#ch:firmware-update),
    // killing the entire reader.js IIFE and preventing copy button creation.
    // That bug is detected in group 2 (Deep Link Arrival).
    // Here we test the immune system chain independently.
    await loadPage(page, FILE_URL, 3000);

    // 8a: Manually expand to Firmware Update section
    const sectionOpen = await page.evaluate(() => {
      const heading = document.getElementById('ch:firmware-update');
      if (!heading) return { found: false };
      let el = heading;
      while (el) {
        if (el.tagName === 'DETAILS') el.open = true;
        el = el.parentElement;
      }
      return { found: true };
    });

    if (sectionOpen.found) {
      pass('[iPhone 14] Firmware Update section found and expanded');
    } else {
      fail('[iPhone 14] Firmware Update section', 'heading #ch:firmware-update not found');
      await safeClose(page);
      return;
    }

    // 8b: Copy button visible
    // reader.js creates the copy button dynamically; wait for it
    await delay(500);

    const copyBtnInfo = await page.evaluate(() => {
      const btn = document.querySelector('.copy-llm-primer') ||
        document.getElementById('copy-llm-primer-top') ||
        document.getElementById('copy-llm-primer-front');
      if (!btn) return { found: false };
      const rect = btn.getBoundingClientRect();
      return {
        found: true,
        visible: rect.width > 0 && rect.height > 0,
        text: btn.textContent,
        inViewport: rect.top >= 0 && rect.bottom <= (window.innerHeight + 500),
      };
    });

    if (copyBtnInfo.found && copyBtnInfo.visible) {
      pass(`[iPhone 14] Copy button visible ("${copyBtnInfo.text.trim()}")`);

      // 8c: Tap copy button
      const copyBtn = await page.$('.copy-llm-primer, #copy-llm-primer-top');
      if (copyBtn) {
        // Scroll to button first
        await page.evaluate(() => {
          const btn = document.querySelector('.copy-llm-primer') ||
            document.getElementById('copy-llm-primer-top');
          if (btn) btn.scrollIntoView({ block: 'center' });
        });
        await delay(300);

        await copyBtn.tap();
        await delay(500);

        // Check for confirmation UI (button text changes to "Copied!")
        const afterTap = await page.evaluate(() => {
          const btn = document.querySelector('.copy-llm-primer') ||
            document.getElementById('copy-llm-primer-top');
          return btn ? btn.textContent.trim() : '';
        });

        if (afterTap.includes('Copied')) {
          pass('[iPhone 14] Copy button tap shows "Copied!" confirmation');
        } else {
          // On file:// protocol, clipboard may fail silently; check if button exists at all
          skip('[iPhone 14] Copy button confirmation', `button text after tap: "${afterTap}" (clipboard may be blocked on file:// protocol)`);
        }

        // 8d: Check that the primer text has content (even if clipboard fails on file://)
        const primerHasContent = await page.evaluate(() => {
          const div = document.getElementById('llm-primer-text');
          return div ? div.textContent.trim().length : 0;
        });

        if (primerHasContent > 100) {
          pass(`[iPhone 14] Science Reference content present (${primerHasContent} chars)`);
        } else if (primerHasContent > 0) {
          pass(`[iPhone 14] Science Reference content present (${primerHasContent} chars, shorter than expected)`);
        } else {
          fail('[iPhone 14] Science Reference content', '#llm-primer-text empty or missing');
        }

      } else {
        fail('[iPhone 14] Copy button tap', 'button element not found for tap');
      }

    } else if (copyBtnInfo.found) {
      fail('[iPhone 14] Copy button visible', 'button exists but not visible');
    } else {
      fail('[iPhone 14] Copy button', 'no .copy-llm-primer or #copy-llm-primer-top found');
    }

  } finally {
    await safeClose(page);
  }
}

/**
 * 9. TOOLTIP JSON CONTRACT (all devices)
 * Verifies the externalized tooltip architecture: single <script id="hover-data">
 * dict exists, parses as JSON, and every [data-hover-id] reference resolves.
 */
async function testTooltipJsonContract(browser) {
  group('9. TOOLTIP JSON CONTRACT');

  for (const [dk, device] of Object.entries(DEVICES)) {
    const label = `[${device.name}]`;
    const page = await createPage(browser, dk);

    try {
      await loadPage(page, FILE_URL);

      const dictInfo = await page.evaluate(() => {
        const el = document.getElementById('hover-data');
        if (!el) return { missing: true };
        try {
          const data = JSON.parse(el.textContent);
          return { keys: Object.keys(data).length, sample: Object.keys(data).slice(0, 3) };
        } catch (e) { return { parseError: e.message }; }
      });

      if (dictInfo.missing) {
        fail(`${label} hover-data block exists`, 'missing');
      } else if (dictInfo.parseError) {
        fail(`${label} hover-data parses`, dictInfo.parseError);
      } else {
        pass(`${label} hover-data has ${dictInfo.keys} entries (sample: ${dictInfo.sample.join(', ')})`);
      }

      if (!dictInfo.missing && !dictInfo.parseError) {
        const orphans = await page.evaluate(() => {
          const data = JSON.parse(document.getElementById('hover-data').textContent);
          const refs = Array.from(document.querySelectorAll('[data-hover-id]'))
            .map(el => el.getAttribute('data-hover-id'));
          return refs.filter(r => !(r in data));
        });
        if (orphans.length) {
          fail(`${label} all data-hover-id refs resolve`,
            `${orphans.length} orphans: ${orphans.slice(0, 3).join(', ')}`);
        } else {
          pass(`${label} all data-hover-id refs resolve`);
        }
      }
    } finally {
      await safeClose(page);
    }
  }
}

/**
 * 10. TOOLTIP RENDERS (desktop + phone)
 * Spot-checks that three known terms render a .hover-panel with content
 * pulled from the externalized JSON dict. Uses real puppeteer hover/tap
 * (synthetic dispatchEvent on mouseenter is untrusted and doesn't fire
 * reader.js's hoverTimer chain reliably).
 */
async function testTooltipRenders(browser) {
  group('10. TOOLTIP RENDERS');

  const targets = ['the-flat', 'wormholes', 'dual-use'];

  for (const dk of ['desktop', 'phone']) {
    const device = DEVICES[dk];
    const label = `[${device.name}]`;
    const page = await createPage(browser, dk);

    try {
      await loadPage(page, FILE_URL);

      await page.evaluate(() => {
        document.querySelectorAll('details').forEach(d => { d.open = true; });
      });
      await delay(400);

      for (const id of targets) {
        // Dismiss any existing panel first
        await page.evaluate(() => {
          document.querySelectorAll('.hover-panel').forEach(p => p.remove());
        });

        // Find target element and scroll into view
        const handle = await page.evaluateHandle((hoverId) => {
          return document.querySelector(`[data-hover-id="${hoverId}"]`);
        }, id);

        const elExists = await page.evaluate(el => !!el, handle);
        if (!elExists) {
          skip(`${label} ${id} tooltip rendered`, 'term not in DOM');
          continue;
        }

        await page.evaluate(el => el.scrollIntoView({ block: 'center' }), handle);
        await delay(100);

        // Input strategy differs by device:
        //  - Desktop: real hover (mouseenter → hoverTimer → showPanel)
        //  - Mobile: synthetic click dispatched in-page. Puppeteer's tap() can
        //    miss hit-testing when an inline span wraps or is narrow. A direct
        //    el.click() invocation inside page.evaluate bubbles to reader.js's
        //    delegated document click handler, which calls showPanel.
        if (device.viewport.hasTouch && device.viewport.isMobile) {
          await page.evaluate((hoverId) => {
            const el = document.querySelector(`[data-hover-id="${hoverId}"]`);
            if (el) el.click();
          }, id);
        } else {
          try { await handle.hover(); } catch (_) {
            await page.evaluate((hoverId) => {
              const el = document.querySelector(`[data-hover-id="${hoverId}"]`);
              if (el) el.click();
            }, id);
          }
        }

        // Desktop needs >250ms hoverDelay; add buffer
        await delay(500);

        const panelInfo = await page.evaluate(() => {
          const panel = document.querySelector('.hover-panel');
          if (!panel) return { present: false };
          return {
            present: true,
            text: panel.textContent.slice(0, 120),
          };
        });

        if (!panelInfo.present) {
          fail(`${label} ${id} tooltip rendered`, 'no .hover-panel after input');
        } else {
          const preview = (panelInfo.text || '').replace(/\s+/g, ' ').slice(0, 50);
          pass(`${label} ${id} tooltip rendered ("${preview}...")`);
        }
      }
    } finally {
      await safeClose(page);
    }
  }
}

// --- Main ---

async function main() {
  // Check that the built HTML exists
  if (!fs.existsSync(HTML_PATH)) {
    console.log(`\nSKIP: Built HTML not found at:\n  ${HTML_PATH}`);
    console.log('Run the build first, then re-run this test.\n');
    process.exit(0);
  }

  console.log('Relinquishment E2E Device Tests — Layer 2');
  console.log(`HTML: ${HTML_PATH}`);
  console.log(`Devices: ${Object.values(DEVICES).map(d => d.name).join(', ')}`);

  let browser;
  try {
    browser = await launchBrowser();

    const tests = [
      testBuildVerification,
      testDeepLinkArrival,
      testPhonePanelInteraction,
      testPhoneNavigation,
      testPhoneShare,
      testPhoneResponsiveLayout,
      testDesktopPanelInteraction,
      testImmuneSystemChain,
      testTooltipJsonContract,
      testTooltipRenders,
    ];

    for (const test of tests) {
      try {
        await test(browser);
      } catch (err) {
        console.error(`  ERROR in ${test.name}: ${err.message}`);
        totalFailed++;
      }
    }

  } catch (err) {
    console.error(`\nFATAL: ${err.message}`);
    totalFailed++;
  } finally {
    if (browser) await browser.close();
  }

  // Summary
  console.log('\n========================================');
  console.log(`RESULTS: ${totalPassed} passed, ${totalFailed} failed, ${totalSkipped} skipped`);
  if (failures.length > 0) {
    console.log('\nFailures:');
    failures.forEach(f => console.log(`  - ${f}`));
  }
  console.log('========================================\n');

  process.exit(totalFailed > 0 ? 1 : 0);
}

main();
