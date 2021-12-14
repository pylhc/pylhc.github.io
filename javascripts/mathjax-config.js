/* mathjax-config.js  file
refs: 
https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#arithmatex
https://docs.mathjax.org/en/latest/input/tex/eqnumbers.html
 https://docs.mathjax.org/en/latest/options/index.html
*/

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams',
    tagSide: 'right',
    tagIndent: '1.2em',
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  }
};

/* Given in markdown example, but creates weird boxes */
// document$.subscribe(() => {
//   MathJax.typesetPromise()
// })