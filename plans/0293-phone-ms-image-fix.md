# Plan 0293: Phone MS Image — Remove isPhone Special-Casing

**Status:** READY
**Author:** Auditor (Argus S65)
**Origin:** Plan 0292 fixed tagline text and attempted phone image fix. Generator put image inline inside `<summary>` on phone — mobile browsers clipped it. Auditor moved image to nav with inline styling — shows in Puppeteer but not on real phone (image in nav flow, not positioned beside text). Root cause: three `isPhone` branches create phone-specific behavior that doesn't work. Fix: delete all three, let the existing responsive code handle all viewports uniformly.
**Risk:** LOW (3 edits in one file, all deletions of special-case branches)

---

## Problem

The MS cover image is invisible on real phones (Android Chrome, mobile Safari). Three `isPhone` branches in `build/reader.js` create phone-specific behavior that fails:

1. **Line 511-518:** Phone gets inline/block styling instead of absolute positioning → image sits in nav bar flow, not beside title text
2. **Line 768:** `paddingRight` only applied on desktop → phone text flows full-width, covering where image would appear
3. **Line 788:** Scroll-to-vanish only on desktop → if image did show on phone, it would persist while reading

## Fix

Delete all three `isPhone` branches. The existing responsive sizing (`navW > 700 ? 52% : 45%`) already handles phone dimensions. On a 390px phone: msWidth ≈ 175px, paddingRight ≈ 185px, text area ≈ 205px. Taglines wrap to 3-4 lines using the vertical space that's currently dead. Image vanishes on scroll (decorative only).

### Change 1: `build/reader.js` lines 507-518

Delete the `isPhone` variable and the `if/else` styling branch. Use the desktop (absolute positioning) style for all viewports.

**CURRENT:**
```javascript
    var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    var isPhone = navW <= 500;
    var wrapper = document.createElement('div');
    wrapper.id = 'cover-magnetosphere';
    wrapper.setAttribute('aria-hidden', 'true');
    if (isPhone) {
      wrapper.style.cssText = 'width:' + msWidth + 'px;' +
        'pointer-events:none;opacity:0.85;margin:0.5em auto;display:block;';
    } else {
      wrapper.style.cssText = 'position:absolute;bottom:calc(100% - 15px);right:0;' +
        'width:' + msWidth + 'px;' +
        'pointer-events:none;z-index:1;opacity:0.85;transition:opacity 0.3s;';
    }
```

**REPLACE WITH:**
```javascript
    var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    var wrapper = document.createElement('div');
    wrapper.id = 'cover-magnetosphere';
    wrapper.setAttribute('aria-hidden', 'true');
    wrapper.style.cssText = 'position:absolute;bottom:calc(100% - 15px);right:0;' +
      'width:' + msWidth + 'px;' +
      'pointer-events:none;z-index:1;opacity:0.85;transition:opacity 0.3s;';
```

### Change 2: `build/reader.js` line 768

Remove the `!isPhone` guard so `paddingRight` applies on all viewports.

**CURRENT:**
```javascript
    if (!isPhone && titleExtra) titleExtra.style.paddingRight = (msWidth + 10) + 'px';
```

**REPLACE WITH:**
```javascript
    if (titleExtra) titleExtra.style.paddingRight = (msWidth + 10) + 'px';
```

### Change 3: `build/reader.js` lines 788-803

Remove the `if (!isPhone)` wrapper so scroll-to-vanish works on all viewports. Keep the scroll listener code, just remove the guard.

**CURRENT:**
```javascript
    if (!isPhone) {
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
    }
```

**REPLACE WITH:**
```javascript
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
```

## Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

### Grep checks:
```bash
grep "isPhone" build/reader.js  # expect 0 results
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
  await p.screenshot({ path: '/tmp/0293-desktop.png' });

  // Phone
  p = await browser.newPage();
  await p.setViewport({ width: 390, height: 844 });
  await p.goto('file:///home/bruce/software/relinquishment/docs/downloads/Relinquishment.html', { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 3000));
  await p.screenshot({ path: '/tmp/0293-phone.png' });

  await browser.close();
  console.log('Screenshots: /tmp/0293-desktop.png, /tmp/0293-phone.png');
})();
"
```

Read BOTH screenshots to verify:
- [ ] Desktop: MS image beside text, no overlap, same as before
- [ ] Phone: MS image visible above-right of nav, text constrained by paddingRight
- [ ] Phone: text wraps within left ~55% of screen, no overlap with image

### Post-build:
```bash
cd ~/software/relinquishment
git add build/reader.js docs/downloads/
git commit -m "Plan 0293: phone MS image — remove isPhone branches, uniform behavior all viewports"
git push
```

## Fallback

If absolute positioning still fails on real mobile browsers (backdrop-filter + sticky clipping), fallback is approach A: hard `<br>` tags in taglines (preprocess.py:574-575) at phone-optimal break points, with CSS `@media (min-width:500px) { .tp-tagline br { display:none } }` to hide breaks on desktop. That's a separate plan.
