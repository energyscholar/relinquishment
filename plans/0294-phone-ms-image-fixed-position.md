# Plan 0294: Phone MS Image — Move Outside Nav (Fixed Positioning)

**Status:** READY
**Author:** Auditor (Argus S65)
**Origin:** Plans 0292-0293 + two quick fixes failed to show the MS cover image on real phones. Root cause confirmed: `backdrop-filter:blur(4px)` on the `position:sticky` nav creates an implicit clipping boundary on mobile browsers (Android Chrome, mobile Safari). Absolute-positioned children extending above the nav are clipped. `overflow:visible` does not override this. The image must leave the nav.
**Risk:** LOW (4 changes in one file, positioning logic only)
**Annealed:** MED — toggle/scroll race condition verified safe, mobile URL bar stable, desktop position shift minor (top of title block vs bottom)

---

## Problem

The MS cover image is a child of the nav (`nav.appendChild(wrapper)`) with `position:absolute;bottom:calc(100% - 15px)` to extend above the nav. Mobile browsers clip this overflow due to `backdrop-filter` on the sticky nav. Works in Puppeteer and desktop browsers, invisible on real phones.

## Fix

Four changes in `build/reader.js`:

### Change 1: Wrapper styling (line 510-512)

Change from `position:absolute` (relative to nav) to `position:fixed` (relative to viewport). Compute position from the title-page-extra element's location.

**CURRENT:**
```javascript
    wrapper.style.cssText = 'position:absolute;bottom:calc(100% - 15px);right:0;' +
      'width:' + msWidth + 'px;' +
      'pointer-events:none;z-index:1;opacity:0.85;transition:opacity 0.3s;';
```

**REPLACE WITH:**
```javascript
    wrapper.style.cssText = 'position:fixed;right:0;' +
      'width:' + msWidth + 'px;' +
      'pointer-events:none;z-index:99;opacity:0.85;transition:opacity 0.3s;';
```

Note: `z-index:99` (just below nav's z-index:100) so image sits behind nav if they overlap.

### Change 2: Append to body + compute position (lines 760-762)

Change from appending to nav to appending to body. Compute vertical position from the title-page-extra element.

**CURRENT:**
```javascript
    wrapper.innerHTML = darkSvg + lightSvg;
    nav.appendChild(wrapper);
    var titleExtra = document.querySelector('.title-page-extra');
    if (titleExtra) titleExtra.style.paddingRight = (msWidth + 10) + 'px';
```

**REPLACE WITH:**
```javascript
    wrapper.innerHTML = darkSvg + lightSvg;
    var titleExtra = document.querySelector('.title-page-extra');
    if (titleExtra) {
      var rect = titleExtra.getBoundingClientRect();
      wrapper.style.top = rect.top + 'px';
      titleExtra.style.paddingRight = (msWidth + 10) + 'px';
    }
    document.body.appendChild(wrapper);
```

This positions the image's top edge at the same vertical position as `.title-page-extra` (authors/taglines). On initial load at scroll position 0, this is correct. The scroll-to-vanish handler (already in place) fades the image to opacity 0 when `scrollY > 20`, so position drift during scroll is irrelevant — the image is already invisible.

### Also revert: Remove `overflow:visible` from nav (line 69)

The failed fix from the previous attempt. Remove `overflow:visible;` from the nav's cssText.

**CURRENT:**
```
'align-items:center;font-size:0.8em;z-index:100;backdrop-filter:blur(4px);overflow:visible;';
```

**REPLACE WITH:**
```
'align-items:center;font-size:0.8em;z-index:100;backdrop-filter:blur(4px);';
```

### Change 4: Hide image when book expands (after scroll handler, ~line 795)

The `<details class="book-section">` toggle opens the book content. When it opens, the image should vanish — it's only for the plain title page. Add a toggle listener:

```javascript
    var bookSection = document.querySelector('details.book-section');
    if (bookSection) {
      bookSection.addEventListener('toggle', function() {
        if (bookSection.open) {
          wrapper.style.opacity = '0';
        }
      });
    }
```

Note: no need to restore opacity on close — the scroll handler already restores to 0.85 when `scrollY <= 20`, and closing the details returns the user to the title page at scroll 0.

## Why This Works

- `position:fixed` positions relative to the viewport, not any parent element
- No parent container can clip it (not affected by backdrop-filter, overflow, or stacking context)
- Appended to `document.body` — completely independent of nav DOM
- Vertical position computed once from title-page-extra's bounding rect at load time
- Scroll-to-vanish fades to opacity:0 at scrollY > 20 — handles all scroll states
- msToggle click handler still works (closure reference to wrapper, independent of DOM position)
- paddingRight on title-page-extra prevents text overlap (unchanged)
- Details toggle listener hides image when book opens — image is title-page-only decoration

## Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

### Puppeteer visual QC (both viewports):
```javascript
cd ~/software/relinquishment && node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-gpu'] });

  // Desktop
  var p = await browser.newPage();
  await p.setViewport({ width: 1400, height: 900 });
  await p.goto('file:///home/bruce/software/relinquishment/docs/downloads/Relinquishment.html', { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 3000));
  await p.screenshot({ path: '/tmp/0294-desktop.png' });

  // Phone
  p = await browser.newPage();
  await p.setViewport({ width: 390, height: 844 });
  await p.goto('file:///home/bruce/software/relinquishment/docs/downloads/Relinquishment.html', { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 3000));
  await p.screenshot({ path: '/tmp/0294-phone.png' });

  await browser.close();
  console.log('Screenshots: /tmp/0294-desktop.png, /tmp/0294-phone.png');
})();
"
```

Read BOTH screenshots to verify:
- [ ] Desktop: MS image beside title text (right side), no overlap with text
- [ ] Phone: MS image visible beside title text (right side), text constrained by paddingRight
- [ ] Both: image doesn't obscure readable text
- [ ] Both: click "Relinquishment ▾" to open book — image vanishes
- [ ] Both: close book, scroll to top — image reappears

### Post-build:
```bash
cd ~/software/relinquishment
git add build/reader.js docs/downloads/
git commit -m "Plan 0294: phone MS image — fixed positioning outside nav, bypass backdrop-filter clipping"
git push
```

## Fallback

If `position:fixed` has issues on mobile (URL bar show/hide causing jitter), alternative is: append wrapper before nav as sibling (`nav.parentNode.insertBefore(wrapper, nav)`), use `position:relative` with negative top margin. But fixed + scroll-to-vanish should handle this cleanly since the image is only visible at scroll position 0 where the viewport is stable.
