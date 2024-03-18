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
   Do not use too many (i.e. hundreds) of them, as each of them get's a listener, which might slow down the page. */
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

// /* Create logbook links from logbook, date and id as . */
// document$.subscribe(function createLogbookLinks() {
//     var elements = document.getElementsByClassName('logbook-link');
//     for (var i = 0; i < elements.length; i++) {
//         var element = elements[i];
//         // alternative method: key value pairs directly in attributes: [Link](#){logbook='xxx' date='yyy' event_id='zzz' .logbook-link}
//         // var logbook = element.getAttribute('logbook');
//         // var date = element.getAttribute('date');
//         // var event_id = element.getAttribute('event_id');
//         // element.href = 'https://be-op-logbook.web.cern.ch/elogbook-server/#/logbook?logbookId=' + logbook + '&dateFrom=' + date + 'T00%3A00%3A00&dateTo=' + date + 'T23%3A59%3A59&eventToHighlight=' + event_id;
//         
//         // key value pairs as single string: [Link](logbook=xxx,date=yyy,event_id=zzz)  (works also with [LINK][linkname]{.logbook-link} -> [linkname]: logbook=xxx,date=yyy,event_id=zzz)
//         var keyValuePairs = element.href.split(","); 
//         var result = {};
//         for (var i = 0; i < keyValuePairs.length; i++) {
//             var pair = keyValuePairs[i].split('=');
//             var aux_key = pair[0].split('/');
//             var key = aux_key[aux_key.length - 1].trim();
//             var value = pair[1].trim();
//             result[key] = value;
//         };
//        // console.log(result)
//         element.href = 'https://be-op-logbook.web.cern.ch/elogbook-server/#/logbook?logbookId=' + result["logbook"] + '&dateFrom=' + result["date"] + 'T00%3A00%3A00&dateTo=' + result["date"] + 'T23%3A59%3A59&eventToHighlight=' + result["event_id"];

//         element.target = "_blank";
//         element.classList.add('cern_login');
//     };
// })


/* Create logbook links from date, logbook and event_id as list: [Link](date,logbook,event_id){.logbook-link}. */
document$.subscribe(function createLogbookLinks() {
    var elements = document.getElementsByClassName('logbook-link');
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];

        var parts = element.href.split(",");
        var trimmed = parts.map(function(part) {
            // console.log(part);
            var aux = part.split('/');
            return aux[aux.length - 1].trim().replace('%20', '');
        })

        var date = trimmed[0];
        var logbook = trimmed[1];
        var event_id = trimmed[2];
        element.href = 'https://be-op-logbook.web.cern.ch/elogbook-server/#/logbook?logbookId=' + logbook + '&dateFrom=' + date + 'T00%3A00%3A00&dateTo=' + date + 'T23%3A59%3A59&eventToHighlight=' + event_id;
        element.setAttribute("alt_href", 'https://logbook.cern.ch/elogbook-server/#/logbook?logbookId=' + logbook + '&dateFrom=' + date + 'T00%3A00%3A00&dateTo=' + date + 'T23%3A59%3A59&eventToHighlight=' + event_id);

        element.target = "_blank";
        element.classList.add('cern_login');
        element.addEventListener("click", function(event) {
            // Check if the alt key is pressed
            if (event.altKey) {
                event.preventDefault(); // Prevent default link behavior
                var altDestination = this.getAttribute("alt_href");
                if (altDestination) {
                    window.open(altDestination, '_blank'); // Open link in a new tab
                }
            }
        });
    };
})



