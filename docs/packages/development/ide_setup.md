# IDE Setup for Python

While a proper IDE is not strictly needed to develop python code,
its usage will make the development process easier and more efficient, allowing the programmer to interact with the code in ways not possible with a text editor.


## VSCode

We recommend the usage of [VSCode][vscode_webpage]{target=_blank} for Python development, while other excellent IDEs exist,
the following VSCode features are of great value:

- [Remote SSH connection][vscode_remote_ssh]{target=_blank}:<br>
  Use any machine with VSCode installed to connect to a remote machine and continue developing on it,
  e.g. you can store your files on `afs` and connect to them through `lxplus`, working on them  as if they were present locally.
  Check the [CERN Knowledge Base][vscode_lxplus]{target=_blank} for more information.
- [Python support][vscode_python]{target=_blank}:<br>
  Make use of static type checking and auto-completion. Interact with the code via an easy-to-use debugger.
- [Interactive Python][vscode_interactive_python]{target=_blank}:<br>
  Use any script as if it were a jupyter notebook, allowing you to run code snippets in real time and inspect variables.
- [Integrated Testing][vscode_testing]{target=_blank}:<br>
  Use the `pytest` framework to easily write and run tests, which can be individually run or all at once directly from the editor.
- [Great Extendibility][vscode_marketplace]{target=_blank}:<br>
  Many extensions are available, making VSCode a great tool for many different use cases and programming languages (e.g. [LaTeX][vscode_latex]{target=_blank}, [Java](../../guis/usage/ide_install.md#vscode),
  which means you do not have to learn a new environment for your different projects.
- Widespread use among the team:<br>
  Most developers of the OMC-Team use VSCode and are happy to help you with setting up and using it.

### Recommended Extensions

Main:

- [Python][vscode_python_extension]{target=_blank}: [Documentation][vscode_python]{target=_blank}
- [Jupyter][vscode_jupyter]{target=_blank}: [Documentation][vscode_interactive_python]{target=_blank}
- [Remote SSH][vscode_remote_ssh_extension]{target=_blank}: [Documentation][vscode_remote_ssh]{target=_blank} and [lxplus SSH configuration][vscode_lxplus]{target=_blank .cern_login}.

Additional:

- [Ruff][vscode_ruff]{target=_blank}: A fast Python linter.
- [Github Pullrequests][vscode_github]{target=_blank}: Interact with Github Pullrequests directly from VSCode.
- [Markdown Table Formatter][vscode_markdown_tables]{target=_blank}: Format tables in markdown files.

[vscode_lxplus]: https://cern.service-now.com/service-portal?id=kb_article&n=KB0008901
[vscode_webpage]: https://code.visualstudio.com/
[vscode_python]: https://code.visualstudio.com/docs/python/python-quick-start
[vscode_interactive_python]: https://code.visualstudio.com/docs/python/jupyter-support-py
[vscode_remote_ssh]: https://code.visualstudio.com/docs/remote/ssh-tutorial
[vscode_testing]: https://code.visualstudio.com/docs/python/testing
[vscode_marketplace]: https://marketplace.visualstudio.com/vscode
[vscode_latex]: https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop
[vscode_jupyter]: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
[vscode_python_extension]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vscode_ruff]: https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff
[vscode_github]: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
[vscode_markdown_tables]: https://marketplace.visualstudio.com/items?itemName=fcrespo82.markdown-table-formatter
[vscode_remote_ssh_extension]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh