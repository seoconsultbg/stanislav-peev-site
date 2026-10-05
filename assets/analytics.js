// Cookie consent banner + contact events for GA4 (G-SNM7XHD6X3).
// Consent defaults (everything denied) are set inline in <head> before gtag config;
// this file only shows the banner, stores the choice and sends the contact events.
// Loaded from the inline gtag block, so pages built from it carry it automatically.
(function () {
  var CONSENT_KEY = 'sp-consent';
  var LEAD_KEY = 'sp-lead-pending';
  var LEAD_TTL = 30 * 60 * 1000;

  function gtag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }

  function readChoice() {
    try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
  }

  function saveChoice(value) {
    try { localStorage.setItem(CONSENT_KEY, value); } catch (e) {}
  }

  // ---------- banner ----------
  var CSS =
    '.consent{position:fixed;left:22px;bottom:22px;z-index:70;max-width:380px;' +
    'background:var(--surface,#18231e);color:var(--ink,#e9efeb);border:1px solid var(--line,#263329);' +
    'border-radius:14px;padding:18px 20px;box-shadow:0 12px 32px -10px rgba(0,0,0,.6);' +
    'font-size:.92rem;line-height:1.5}' +
    '.consent p{margin:0 0 14px}' +
    '.consent p a{color:var(--green,#45d6a0)}' +
    '.consent-actions{display:flex;gap:10px}' +
    '.consent-btn{flex:1;font:inherit;font-weight:700;padding:10px 16px;border-radius:999px;cursor:pointer;' +
    'background:transparent;color:var(--ink,#e9efeb);border:1.5px solid var(--ink-soft,#a2b3ab)}' +
    '.consent-btn:hover{border-color:var(--green,#45d6a0);color:var(--green,#45d6a0)}' +
    '.consent-link{background:none;border:0;padding:0;font:inherit;color:var(--ink-soft,#a2b3ab);cursor:pointer}' +
    '.consent-link:hover{color:var(--green,#45d6a0)}' +
    '@media (max-width:600px){.consent{left:12px;right:12px;bottom:12px;max-width:none}}';

  var banner = null;

  function closeBanner() {
    if (banner) { banner.remove(); banner = null; }
  }

  // GA stops using its cookies once consent is denied, but does not delete them
  function dropGaCookies() {
    document.cookie.split(';').forEach(function (c) {
      var name = c.trim().split('=')[0];
      if (name.indexOf('_ga') !== 0) return;
      document.cookie = name + '=; Max-Age=0; path=/';
      document.cookie = name + '=; Max-Age=0; path=/; domain=.' + location.hostname;
    });
  }

  function choose(value) {
    var was = readChoice();
    saveChoice(value);
    gtag('consent', 'update', { analytics_storage: value });
    if (value === 'denied') dropGaCookies();
    // The landing page view went out cookieless; resend it once with cookies so the
    // session keeps its landing page and source.
    if (value === 'granted' && was !== 'granted') {
      gtag('event', 'page_view', { page_location: location.href, page_referrer: document.referrer });
    }
    closeBanner();
  }

  function openBanner() {
    if (banner) return;
    banner = document.createElement('div');
    banner.className = 'consent';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML =
      '<p>I use Google Analytics cookies to count visits and see which pages are useful. ' +
      'Nothing is used for ads. <a href="/privacy/">Privacy</a></p>' +
      '<div class="consent-actions">' +
      '<button type="button" class="consent-btn" data-consent="granted">Accept</button>' +
      '<button type="button" class="consent-btn" data-consent="denied">Decline</button>' +
      '</div>';
    banner.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-consent]');
      if (btn) choose(btn.getAttribute('data-consent'));
    });
    document.body.appendChild(banner);
  }

  // lets visitors change their mind later
  function addFooterLink() {
    var nav = document.querySelector('.site-footer .footer-nav');
    if (!nav) return;
    var link = document.createElement('button');
    link.type = 'button';
    link.className = 'consent-link';
    link.textContent = 'Cookie settings';
    link.addEventListener('click', openBanner);
    nav.appendChild(link);
  }

  // ---------- contact events ----------
  function where(el) {
    if (el.closest('.site-footer')) return 'footer';
    if (el.closest('.site-header')) return 'header';
    var box = el.closest('section, aside, article');
    if (!box) return 'body';
    return box.id || box.className.split(' ')[0] || box.tagName.toLowerCase();
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (href.indexOf('mailto:') === 0) {
      gtag('event', 'contact_email', { link_location: where(a) });
    } else if (/^https:\/\/wa\.me\//.test(href)) {
      gtag('event', 'contact_whatsapp', { link_location: where(a) });
    }
  }, true);

  // The form posts to FormSubmit, which redirects to /thanks/. The flag set here
  // turns that redirect into one generate_lead (a reload of /thanks/ does not count).
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form.action || form.action.indexOf('formsubmit.co') === -1) return;
    try {
      sessionStorage.setItem(LEAD_KEY, JSON.stringify({ page: location.pathname, t: Date.now() }));
    } catch (err) {}
  }, true);

  function sendLeadOnThanksPage() {
    if (location.pathname.indexOf('/thanks') !== 0) return;
    var pending = null;
    try {
      pending = JSON.parse(sessionStorage.getItem(LEAD_KEY) || 'null');
      sessionStorage.removeItem(LEAD_KEY);
    } catch (e) {}
    if (pending && Date.now() - pending.t < LEAD_TTL) {
      gtag('event', 'generate_lead', { lead_source: 'contact_form', form_page: pending.page });
    }
  }

  function init() {
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);
    addFooterLink();
    sendLeadOnThanksPage();
    if (!readChoice()) openBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
