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
    // add equation numbering:
    tags: 'ams',
    tagSide: 'right',
    tagIndent: '1.2em',
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  }
};

/* Redraws the page with mathjax equations.
Otherwise a manual reload is needed.
But creates weird boxes/scrollbars -> fixed with css.*/
document$.subscribe(() => {
  MathJax.typesetPromise()
})