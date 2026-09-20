// WebMCP - tools for AI agents in the browser (navigator/document.modelContext).
// Does nothing in a browser without that API. The contact form is NEVER submitted from here.
(function () {
  var PREFILL_KEY = 'webmcp-contact-prefill';
  var FIELDS = ['name', 'email', 'website', 'message'];

  function fillContactForm(values) {
    var form = document.querySelector('form.contact-form');
    if (!form) return false;
    FIELDS.forEach(function (key) {
      var el = form.querySelector('[name="' + key + '"]');
      if (el && typeof values[key] === 'string') el.value = values[key];
    });
    form.scrollIntoView({ block: 'center' });
    return true;
  }

  // finishes a prefill that was started on a page without a form
  try {
    var pending = sessionStorage.getItem(PREFILL_KEY);
    if (pending && document.querySelector('form.contact-form')) {
      sessionStorage.removeItem(PREFILL_KEY);
      fillContactForm(JSON.parse(pending));
    }
  } catch (e) {}

  var contexts = [];
  [navigator.modelContext, document.modelContext].forEach(function (mc) {
    if (mc && typeof mc.registerTool === 'function' && contexts.indexOf(mc) === -1) contexts.push(mc);
  });
  if (!contexts.length) return;

  function text(value) {
    return { content: [{ type: 'text', text: typeof value === 'string' ? value : JSON.stringify(value) }] };
  }

  function sameOrigin(path) {
    var url = new URL(path, location.origin);
    if (url.origin !== location.origin) throw new Error('Only stanislav-peev.com paths are allowed');
    return url;
  }

  function fetchText(path, accept, signal) {
    var url;
    try { url = sameOrigin(path); } catch (e) { return Promise.reject(e); }
    return fetch(url.href, { headers: { Accept: accept }, signal: signal }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status + ' for ' + url.pathname);
      return res.text();
    });
  }

  var tools = [
    {
      name: 'get_profile',
      title: 'Stanislav Peev - profile',
      description: 'Short profile of Stanislav Peev, independent SEO consultant and AI search (GEO) specialist based in Bratislava: focus areas, research, credentials, selected clients and written contact channels. Returns markdown.',
      inputSchema: { type: 'object', properties: {} },
      annotations: { readOnlyHint: true },
      execute: function (input, options) {
        return fetchText('/', 'text/markdown', options && options.signal).then(text);
      }
    },
    {
      name: 'list_research',
      title: 'Stanislav Peev - published research',
      description: 'Lists the published research studies and data reports (title, URL, date, summary), newest first. Pass a URL path to get_page_markdown to read a study. Three studies publish raw data under CC BY 4.0.',
      inputSchema: { type: 'object', properties: {} },
      annotations: { readOnlyHint: true },
      execute: function (input, options) {
        return fetchText('/rss.xml', 'application/rss+xml', options && options.signal).then(function (xml) {
          var doc = new DOMParser().parseFromString(xml, 'application/xml');
          var items = [];
          doc.querySelectorAll('item').forEach(function (item) {
            var pick = function (tag) {
              var el = item.querySelector(tag);
              return el ? el.textContent.trim() : '';
            };
            items.push({ title: pick('title'), url: pick('link'), published: pick('pubDate'), summary: pick('description') });
          });
          return text(items);
        });
      }
    },
    {
      name: 'get_page_markdown',
      title: 'Read a stanislav-peev.com page as markdown',
      description: 'Returns any page of stanislav-peev.com as clean markdown. Use /services/ for services, /research/ for the research index and /sitemap.xml for all URLs.',
      inputSchema: {
        type: 'object',
        properties: {
          path: { type: 'string', description: 'Site-relative path ending with a slash, e.g. /services/seo-audit/' }
        },
        required: ['path']
      },
      annotations: { readOnlyHint: true },
      execute: function (input, options) {
        return fetchText(String((input && input.path) || '/'), 'text/markdown', options && options.signal).then(text);
      }
    },
    {
      name: 'prefill_contact_form',
      title: 'Prefill the contact form',
      description: 'Opens the contact form of Stanislav Peev and fills it with the given details. It does NOT submit: the user reviews the text and presses the button themselves. Contact is in writing only - he does not take calls. He replies personally, usually within one business day.',
      inputSchema: {
        type: 'object',
        properties: {
          name: { type: 'string', description: 'Name of the person' },
          email: { type: 'string', description: 'Email address for the reply' },
          website: { type: 'string', description: 'The website the request is about, optional' },
          message: { type: 'string', description: 'The business, the biggest search frustration, the target market' }
        }
      },
      execute: function (input) {
        var values = input || {};
        if (fillContactForm(values)) {
          return Promise.resolve(text('Form filled. The user must review it and submit it themselves.'));
        }
        try { sessionStorage.setItem(PREFILL_KEY, JSON.stringify(values)); } catch (e) {}
        location.assign('/#contact');
        return Promise.resolve(text('Opening https://stanislav-peev.com/#contact with the form prefilled. The user submits it themselves.'));
      }
    }
  ];

  var controller = new AbortController();
  window.addEventListener('pagehide', function (event) {
    if (!event.persisted) controller.abort();
  });
  contexts.forEach(function (mc) {
    tools.forEach(function (tool) {
      try {
        var registered = mc.registerTool(tool, { signal: controller.signal });
        if (registered && typeof registered.catch === 'function') registered.catch(function () {});
      } catch (e) {}
    });
  });
})();
