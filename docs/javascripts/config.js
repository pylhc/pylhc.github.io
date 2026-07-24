window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

/* Make all "clickImg" images a hyperref to themselves.
   Do not use too many (i.e. hundreds) of them, as each of them gets a listener, which might slow down the page. */
document$.subscribe(function () {
    var elements = document.getElementsByClassName("clickImg");
    for (var i = 0; i < elements.length; i++) {
        elements[i].addEventListener("click", function() {
    window.open(this.getAttribute("src"), '_blank');
    })
    };
})


/* Change the abbr elements, which are used when creating the abbreviations (i.e. tooltips).
   This set's the aria-label attribute which is used by the hint-style tooltips
   and sets the class to use the correct css formatting (see hint.min.css)
*/
document$.subscribe(function () {
    var abbr_elements = document.getElementsByTagName("abbr");
    for (var i = 0; i < abbr_elements.length; i++) {
        abbr_elements[i].setAttribute("aria-label", abbr_elements[i].getAttribute("title"));
        abbr_elements[i].removeAttribute("title");
        abbr_elements[i].setAttribute("class", "hint--top hint--limited");
    };
})

/* Create logbook links from date, logbook and event_id as list: [Link](logbook://date,logbook,event_id). */
document$.subscribe(function () {
  document.querySelectorAll('a[href^="logbook://"]').forEach(function (a) {
    const [date, logbook, event_id] = a.getAttribute("href").slice("logbook://".length).split(",").map(s => s.trim());
    const main = `https://be-op-logbook.web.cern.ch/elogbook-server/#/logbook?logbookId=${logbook}&dateFrom=${date}T00%3A00%3A00&dateTo=${date}T23%3A59%3A59&eventToHighlight=${event_id}`;
    const alt  = `https://logbook.cern.ch/elogbook-server/#/logbook?logbookId=${logbook}&dateFrom=${date}T00%3A00%3A00&dateTo=${date}T23%3A59%3A59&eventToHighlight=${event_id}`;
    a.href = main;
    a.target = "_blank";
    a.classList.add("cern_login");
    a.setAttribute("alt_href", alt);
    a.addEventListener("click", function(e) {
        // Check if the alt key is pressed
        if (e.altKey){
            e.preventDefault(); // Prevent default link behavior
            var altDestination = this.getAttribute("alt_href");
            if (altDestination) {
                window.open(altDestination, '_blank'); // Open link in a new tab
            }
        }
    });
  });
});
