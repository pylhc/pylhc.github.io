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