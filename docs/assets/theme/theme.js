/* SeventyOneTen theme switch. A classic script (not a module): load it in <head> without defer so the theme is on <html>
   before first paint. The choice is "system", "dark" or "light", kept under localStorage key s71.theme. "system" removes
   data-theme and lets prefers-color-scheme decide (tokens.css: night when the system states no preference).

     s71Theme.get()            -> "system" | "dark" | "light"
     s71Theme.set("light")     -> applies and remembers it
     s71Theme.effective()      -> "dark" | "light", what is on screen now
     s71Theme.subscribe(fn)    -> fn(choice, effective) on every change, also from another tab; returns an unsubscribe function
*/
(function () {
  var KEY = "s71.theme";
  var CHOICES = { system: 1, dark: 1, light: 1 };
  var listeners = [];
  var memory = "system";
  var mq = null;
  try { mq = window.matchMedia("(prefers-color-scheme: light)"); } catch (e) { mq = null; }

  function read() {
    try {
      var v = window.localStorage.getItem(KEY);
      if (CHOICES[v] === 1) { return v; }
    } catch (e) { /* storage blocked: fall through */ }
    return memory;
  }
  function write(v) {
    memory = v;
    try { window.localStorage.setItem(KEY, v); } catch (e) { /* the choice lasts for this page only */ }
  }
  function apply(choice) {
    var root = document.documentElement;
    if (choice === "dark" || choice === "light") { root.setAttribute("data-theme", choice); }
    else { root.removeAttribute("data-theme"); }
  }
  function effective(choice) {
    if (choice === "dark" || choice === "light") { return choice; }
    return mq && mq.matches ? "light" : "dark";
  }
  function notify() {
    var choice = read();
    var eff = effective(choice);
    for (var i = 0; i < listeners.length; i++) {
      try { listeners[i](choice, eff); } catch (e) { /* one listener must not stop the rest */ }
    }
  }

  apply(read());

  var api = {
    get: read,
    set: function (choice) {
      if (CHOICES[choice] !== 1) { throw new Error("s71Theme: unknown choice " + choice); }
      write(choice);
      apply(choice);
      notify();
    },
    effective: function () { return effective(read()); },
    subscribe: function (fn) {
      listeners.push(fn);
      return function () {
        var i = listeners.indexOf(fn);
        if (i >= 0) { listeners.splice(i, 1); }
      };
    }
  };
  window.s71Theme = api;

  if (mq) {
    var onSystem = function () { if (read() === "system") { notify(); } };
    if (mq.addEventListener) { mq.addEventListener("change", onSystem); }
    else if (mq.addListener) { mq.addListener(onSystem); }
  }
  window.addEventListener("storage", function (ev) {
    if (ev.key === KEY) { apply(read()); notify(); }
  });
})();
