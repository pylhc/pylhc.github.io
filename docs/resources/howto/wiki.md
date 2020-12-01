# Editing Wiki pages

This page presents an overview of the steps necessary to modify the wiki and add new pages.
It also contains examples for useful commands and can be used as a template for new pages.

More detailed information can be found here:

- [markdown guide][markdownsyntax]
- [mkdocs homepage][mkdocs]
- [mkdocs material help][mkdocs_material]

## Setup

### To Make Changes Online

This is a method adapted to making small changes, most likely to a single page.
Go to the current version of the site [here][site_address], navigate to a page you wish to modify and click the page's modification link :fontawesome-solid-pen:{style="height:0.95em"}.
You will be taken to the Github GUI to make your changes, which you can later commit.

Even new pages can be added directly online on github, by navigating to the desired location and clicking  on the `Add File` button.
See [the section about adding pages](#adding-a-page) for more info about what is required for new pages to be accessible from the menu.

!!! note
    As a lot of fancy styling is added by the [material theme][mkdocs_material] used, only the basic markdown formatting is seen in the preview.

### To Make Changes Locally

For bigger changes, local development is recommended.
Get a local copy of this repository, set up a `Python3.6+` environment and install the dependencies:

```bash
git clone https://github.com/pylhc/pylhc.github.io
pip install mkdocs mkdocs-material mkdocs-minify-plugin
```

Create a branch (from master) and make your changes.
You can run a local server by running 

```bash
python -m mkdocs serve
``` 

from the top-level directory, and see the site rendered locally in your browser at `localhost:8000`.
The rendered website will automatically reload upon changes to any file located in the `docs` directory.

Commit your changes to this repository, and open a pull request to get them approved once they are ready.

### Adding a page

In order to add a new page, a new `.md` should be created in the appropriate location in the folder structure.
A link to the page then needs to be added in the `nav` section of the `mkdocs.yml` in the root directory, together with an ID.

## Guidelines

Pages are written in Markdown (file extension `.md`).
A general overview of the syntax a well as some best practices can be found [here][markdownsyntax]{target=_blank}.
Additionally, to allow for easier comparison between two versions of a file, it is recommended to keep it to one sentence per line.
Ideally, the line length is kept below 100 characters.
Following this, it is also recommended to not put links in the text, instead creating an ID at the end of the document and linking to this.

Different blocks of either code or text should be separated by one blank line.

To create blocks of code, use `fenced code blocks`, which are created using `` ``` ``.
These blocks of code should be separated from the previous and following text by one blank line.
To allow for syntax highlighting, the language should be specified.
Below a basic example.

````markdown
```bash
something code that does something
```
````

## Environments

### General text formatting

These are basic markdown commands, repeated here for convenience.
A more exhaustive list is available [here][markdownsyntax].

- To create a **bold** text, surround the text with `**text**`.

- To create an __italic__ text, surround the text with `__text__`.

- To create a [link][bestwiki]{target=_blank}, use `[link][bestwiki]{target=_blank}`.
Note that at the bottom of the file, an ID named `bestwiki` should be created, together with the hyperlink to the webpage, like so `[bestwiki]: https://pylhc.github.io/`.
The specifier `{target=_blank}` is added to ensure pages open in a new tab.
In the specifier, additional information on the accessibility can be added.
Links accessable only with a CERN login can be marked like `{target=_blank .cern_login}` or from the CERN network like `{target=_blank .cern_internal}`.

- To add small hints to a difficult word, which appear on mouse over, add `*[difficult word]: helpful explanation` at the bottom of the file.

### Code listing

To highlight `code` inline, surround the text to highlight with `` ` ``.

For creating a code block, surround the code with `` ``` ``.
Please make sure that the code block is separated from the text by one blank line.
Additionally, please specify the language.

````markdown
```python
for i in range(3):
    print(i)
```
````

### Lists

=== "Unordered list"
    An unordered list looks like this.

    - First
    - Second
    - Third

    It can be created using

    ```markdown
    - First
    - Second
    - Third
    ```

=== "Ordered list"
    An ordered list looks like this.

    1. First
    2. Second
    3. Third

    It can be created using

    ```markdown
    1. First
    2. Second
    3. Third
    ```

=== "Task list"
    A task list looks like this.

    - [ ] First
    - [x] Second
    - [ ] Third

    It can be created using

    ```markdown
    - [ ] First
    - [x] Second
    - [ ] Third
    ```

=== "Procedure Task List"
    Below, a task list with hints, as is used in the procedures, is displayed.

    - [ ] <details class="nodeco"><summary>Task 1 Summary</summary>
        <p> Hints for task 1.
        </p></details>

    - [ ] <details class="nodeco"><summary>Task 2 Summary</summary>
        <p> Hints for task 2.
        </p></details>

    - [ ] <details class="nodeco"><summary>Task 3 Summary</summary>
        <p> Hints for task 3.
        </p></details>

    It can be created using the following code.
    ```html
    - [ ] <details class="nodeco"><summary>Task 1 Summary</summary>
        <p> Hints for task 1.
            </p></details>

    - [ ] <details class="nodeco"><summary>Task 2 Summary</summary>
        <p> Hints for task 2.
            </p></details>

    - [ ] <details class="nodeco"><summary>Task 3 Summary</summary>
        <p> Hints for task 3.
            </p></details>
    ```

    Note that ticks set by a user are not permanent and will be reset upon reloading the page.

#### Tabbed list

A tabbed list looks like this.

=== "Entry 1"
    Text 1
=== "Entry 2"
    Text 2
=== "Entry 3"
    Text 3

It can be created using

```markdown
=== "Entry 1"
    Text 1
=== "Entry 2"
    Text 2
=== "Entry 3"
    Text 3
```

### Text Boxes

??? abstract "Paper Box"
    Textbox for adding papers.
    Code:

    ```markdown
    ??? abstract "Paper Box"
        Textbox for adding papers.
    ```

??? info "Info Box"
    Textbox for adding useful information.
    Code:

    ```markdown
    ??? info "Info Box"
        Textbox for adding useful information.
    ```

??? question "Question Box"
    Textbox for answering commonly asked questions.
    Code:

    ```markdown
    ??? question "Question Box"
        Textbox for answering commonly asked questions.
    ```

??? tip "Tip Box"
    Textbox for adding useful tips to novice users.
    Code:

    ```markdown
    ??? tip "Tip Box"
        Textbox for adding useful tips to novice users.
    ```

Note that appending a `+` to `???` will result in an expanded box by default.

!!! note "Note Box"
    Textbox for adding small notes.
    Code:

    ```markdown
    !!! note "Note Box"
        Textbox for adding small notes.
    ```

!!! warning "Warning Box"
    Textbox for warning users of common pitfalls.
    Code:

    ```markdown
    !!! warning "Warning Box"
        Textbox for warning users of common pitfalls.
    ```

!!! danger "Danger Box"
    Textbox for warning users of potential serious consequences if not executed properly.
    Code:

    ```markdown
    !!! danger "Danger Box"
        Textbox for warning users of potential serious consequences if not executed properly.
    ```

!!! todo "Todo Box"
    Textbox for warning users that this webpage is still work in progress.
    Code:

    ```markdown
    !!! todo "Todo Box"
        Textbox for warning users that this webpage is still work in progress.
    ```

### Various other commands

#### Tables

Tables in markdown look like this.

| Column 1      | Column 2    |
| -----------   | ----------- |
| Entry 11      | Entry 21    |
| Entry 12      | Entry 22    |

It can be created using

```markdown
| Column 1      | Column 2    |
| -----------   | ----------- |
| Entry 11      | Entry 21    |
| Entry 12      | Entry 22    |
```

When creating a table, please ensure that column width is constant and that pipes (`|`) are aligned.

#### Images

To paste an image, use the following code.

```markdown
![Image](../../assets/images/tricks/placeholder.gif)
```

To include a centered image with a caption, use the following code.

```html
<figure>
    <img src="../../../assets/images/something/image.png" width=90%>
  <figcaption>Figure: Something really amazing.</figcaption>
</figure>
```

Images should be saved in `assets/images`, in an appropriately named folder.

*[difficult word]: helpful explanation

[mkdocs]: https://www.mkdocs.org/
[mkdocs_material]: https://squidfunk.github.io/mkdocs-material/
[site_address]: https://pylhc.github.io/
[markdownsyntax]: https://www.markdownguide.org/basic-syntax/
[bestwiki]: https://pylhc.github.io/
