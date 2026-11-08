/* Principles of Information Security: visit counting with Google Tag Manager. MIT licence.

   Loaded asynchronously by every page, play and demo through one tag that carries its settings:
     <script async src=".../assets/js/analytics.js" data-gtm="GTM-..." data-site="https://.../" data-store="hndne-pis:" data-privacy=".../privacy.html">

   Rules:
   - Nothing happens unless the page is served from the live portal address (data-site). A copy opened from a
     clone, a local server or a test run never asks, never counts and never contacts Google.
   - Nothing is requested from Google until the visitor presses Allow. Not allowing, or a browser that sends
     Global Privacy Control, means Tag Manager is never loaded.
   - The choice is kept in this browser only, under the portal's storage prefix, and can be changed at any time
     on the privacy page, which this script fills in where the page holds an element with id "analytics-choice".
   - Every element is built with DOM calls and textContent: no HTML string is ever written into the page. */
(function () {
  "use strict";
  var me = document.currentScript;
  if (!me) { return; }
  var ID = me.getAttribute("data-gtm") || "";
  var SITE = me.getAttribute("data-site") || "";
  var KEY = (me.getAttribute("data-store") || "") + "analytics";
  var PRIVACY = me.getAttribute("data-privacy") || "";
  var live = /^GTM-[A-Z0-9]+$/.test(ID) && SITE !== "" && KEY !== "analytics" && location.href.indexOf(SITE) === 0;
  var gpc = navigator.globalPrivacyControl === true;
  var started = false;
  var banner = null;

  function read() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function write(v) {
    try { if (v === null) { localStorage.removeItem(KEY); } else { localStorage.setItem(KEY, v); } } catch (e) { /* storage blocked: the choice lasts for this page only */ }
  }

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }

  function start() {
    if (started || !live || gpc) { return; }
    started = true;
    gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "granted" });
    window.dataLayer.push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtm.js?id=" + encodeURIComponent(ID);
    document.head.appendChild(s);
  }

  function stop() {
    if (started) { gtag("consent", "update", { analytics_storage: "denied" }); }
    /* remove the analytics cookies this site may have set, on this host and its parent domain */
    var host = location.hostname, parent = host.split(".").slice(-2).join(".");
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (/^_ga/.test(name)) {
        ["", "; domain=" + host, "; domain=." + parent].forEach(function (dom) {
          document.cookie = name + "=; max-age=0; path=/" + dom;
        });
      }
    });
  }

  function el(tag, attrs, text) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (text) { n.textContent = text; }
    return n;
  }
  function button(label, primary, on) {
    var b = el("button", { type: "button" }, label);
    var st = b.style;
    st.font = "inherit"; st.fontWeight = "600"; st.minHeight = "44px"; st.padding = ".45rem 1.1rem";
    st.borderRadius = "999px"; st.cursor = "pointer"; st.border = "2px solid var(--rose)";
    st.background = primary ? "var(--rose)" : "transparent";
    st.color = primary ? "var(--ink)" : "var(--linen)";
    b.addEventListener("click", on);
    return b;
  }

  function choose(v) {
    write(v);
    if (v === "granted") { start(); } else { stop(); }
    if (banner) { document.body.style.paddingBottom = ""; banner.remove(); banner = null; }
    fillPanel();
  }

  function showBanner() {
    if (banner || !live || gpc) { return; }
    banner = el("section", { role: "region", "aria-label": "Visit counting" });
    var st = banner.style;
    st.position = "fixed"; st.left = "0"; st.right = "0"; st.bottom = "0"; st.zIndex = "1000";
    st.background = "var(--ink)"; st.color = "var(--linen)"; st.fontFamily = "var(--font-body)";
    st.fontSize = "0.95rem"; st.lineHeight = "1.5"; st.padding = "0.9rem 1rem";
    st.borderTop = "4px solid var(--rose)";
    var inner = el("div");
    inner.style.maxWidth = "64rem"; inner.style.margin = "0 auto";
    inner.style.display = "flex"; inner.style.flexWrap = "wrap"; inner.style.gap = ".7rem 1.2rem"; inner.style.alignItems = "center";
    var p = el("p");
    p.style.margin = "0"; p.style.flex = "1 1 22rem";
    p.appendChild(document.createTextNode("May this site count your visit with Google Analytics? It records which pages are opened, never your answers or your progress. "));
    if (PRIVACY) {
      var a = el("a", { href: PRIVACY }, "How visits are counted");
      a.style.color = "var(--rose)"; a.style.fontWeight = "600";
      p.appendChild(a);
    }
    var row = el("div");
    row.style.display = "flex"; row.style.gap = ".6rem"; row.style.flexWrap = "wrap";
    row.appendChild(button("Allow", true, function () { choose("granted"); }));
    row.appendChild(button("Do not allow", false, function () { choose("denied"); }));
    inner.appendChild(p);
    inner.appendChild(row);
    banner.appendChild(inner);
    document.body.appendChild(banner);
    document.body.style.paddingBottom = banner.offsetHeight + "px";
  }

  /* the privacy page's own panel: the current choice and a way to change it */
  function fillPanel() {
    var box = document.getElementById("analytics-choice");
    if (!box) { return; }
    while (box.firstChild) { box.removeChild(box.firstChild); }
    var v = read();
    var state = !live ? "Visit counting is off on this copy of the site, so there is nothing to choose here."
      : gpc ? "Your browser asks sites not to track you (Global Privacy Control), so this site never counts your visits."
      : v === "granted" ? "You allowed this site to count your visits in this browser."
      : v === "denied" ? "You chose not to have your visits counted in this browser."
      : "You have not chosen yet, so your visits are not counted.";
    var p = el("p", {}, state);
    p.setAttribute("role", "status");
    box.appendChild(p);
    if (live && !gpc) {
      var row = el("p");
      var allow = el("button", { type: "button", "class": "btn" }, "Allow counting");
      allow.addEventListener("click", function () { choose("granted"); });
      var deny = el("button", { type: "button", "class": "btn" }, "Do not allow counting");
      deny.addEventListener("click", function () { choose("denied"); });
      row.appendChild(allow);
      row.appendChild(document.createTextNode(" "));
      row.appendChild(deny);
      box.appendChild(row);
    }
  }

  function ready() {
    var v = read();
    if (v === "granted") { start(); } else if (v !== "denied" && !document.getElementById("analytics-choice")) { showBanner(); }
    fillPanel();
  }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", ready); } else { ready(); }
}());
