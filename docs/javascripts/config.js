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
var elements = document.getElementsByClassName("clickImg");
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", function() {
  window.open(this.getAttribute("src"), '_blank');
})
};


/* Change the abbr elements, which are used when creating the abbreviations (i.e. tooltips).
   This set's the aria-label attribute which is used by the hint-style tooltips
   and sets the class to use the correct css formatting (see hint.min.css)
*/
var elements = document.getElementsByTagName("abbr");
for (var i = 0; i < elements.length; i++) {
    elements[i].ariaLabel = elements[i].getAttribute("title");
    elements[i].removeAttribute("title");
    elements[i].setAttribute("class", "hint--top hint--large");

};


