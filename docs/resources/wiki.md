# Editing This Wiki

This website is built with [zensical]{target=_blank}, the successor of [mkdocs-material]{target=_blank}, and its content is based on markdown files.
This page presents an overview of the steps necessary to modify or add pages, and build the website.
It also contains examples for useful commands and can be used as a template for new pages.

## Making Changes Online

This method is adapted to making small changes, most likely to a single page.
Go to the [current version of the site][site_address]{target=_blank}, navigate to a page you wish to modify and click the page's modification link at the top right of the page's content.
You will be taken to the GitHub UI to make your changes, which you can commit directly.

Even new pages can be added directly online on GitHub, by navigating to the desired location and clicking  on the `Add File` button.
See [the section about adding pages](#adding-a-page) for more info about what is required for new pages to be accessible from the menu.
Please note: as a lot of fancy styling is added by [zensical]{target=_blank}, but only the basic markdown formatting is seen in the GitHub preview.

## Making Changes Locally

For bigger changes, local development is recommended.
Get a local copy of this repository, set up a `Python3` environment and install the dependencies:

```bash
git clone https://github.com/pylhc/pylhc.github.io  && cd pylhc.github.io
python -m pip install -r requirements.txt
```

Create a branch (from master) and make your changes.
You can run a local server by running, from the top-level directory:

```bash
zensical serve
```

!!! tip "Using uv"

    Considering only `zensical` is required to build the site, if using [uv]{target=_blank} one can simply add it as a tool (`uv tool install zensical`) and then run it through `uv` (`uvx zensical serve`). No need to manage environments!

The site will be rendered locally in your browser at `localhost:8000`, and the build will automatically re-trigger upon changes to any file located in the `docs` directory.
Commit your changes, push them to the repository, and open a pull request to get them approved once they are ready.

!!! info "Push Permissions"

    Currently only members of the `PyLHC` organisation on GitHub are allowed to push changes to our repositories.
    One can always fork the repo, clone their own fork and push to that, then open a PR.

## Adding a Page

<!-- TODO: Adapt this once transition to the zensical.toml config file is done -->

In order to add a page, a new `.md` file should be created in the appropriate location in the folder structure.
A link to the page then needs to be added in the `nav` section of the `mkdocs.yml` in the root directory, together with an ID.
The current navigation gives a clear example of how this works.

## Content Guidelines

Pages are written in Markdown, with file extension `.md`.
A general overview of the syntax as well as some best practices can be found on this [markdown guide][markdownsyntax]{target=_blank}.
Additionally, to allow for easier comparison between two versions of a file, it is recommended to keep it to one sentence per line.
Following this, it is also recommended to not put links in the text, instead creating an ID at the end of the document and linking to it.

Different blocks of either code or text should be separated by one blank line.
To create blocks of code, use `fenced code blocks`, which are created using triple backticks: `` ``` ``.
These blocks of code should be separated from the previous and following text by one blank line.
To allow for syntax highlighting, the language should be specified.
Below a basic example.

````markdown
```bash
something code that does something
```
````

!!! tip "Markdown best practices"

    If using and IDE, extensions such as the great [markdownlint]{target=_blank} extension will catch and fix mistakes for you.

## Markdown Elements We Use

The following displays markdown commands and tricks we use extensively in this website.
A more exhaustive list of markdown features is available on the [markdown guide][markdownsyntax]{target=_blank}.

### General Text Formatting

The following are used to format text in various ways:

- For **bold text**, surround the text with `**text**`.

- For *italic text*, surround the text with `*text*`.

- For an [internal link](#general-text-formatting), use `[link](../../resources/wiki.md#general-text-formatting)`.
  > Note that all links are relative to the current document. The `#`-labels, called "anchors", are automatically created by headers and can be omitted, for instance to link to the page itself.

- For an [external link][bestwiki]{target=_blank}, use `[link][bestwiki]{target=_blank}`.

    > Note that at the bottom of the file, an ID named `bestwiki` should be created at the bottom of the page, together with the hyperlink to the destination, like so:
    >
    ```markdown
    [bestwiki]: https://pylhc.github.io/
    ```
    >
    >The specifier `{target=_blank}` is added to ensure pages open in a new tab.
    In the specifier, additional information on the accessibility can be added.
    Links accessible only with a CERN login can be marked like `{target=_blank .cern_login}` or from the CERN network like `{target=_blank .cern_internal}`.

- For a quote such as the one just above:

    ```markdown
    > to markdown, or not to markdown
    ```

- For tooltips appearing when hovering content such as an acronym, which appear on mouse over, add at the bottom of the file:

    ```markdown
    *[acronym]: helpful explanation
    ```

- For an inline math environment, surround the equation with dollar signs: `$a^2 + b^2 = c^2$`.

- For a block math environment, use double dollar signs above and below the block's content:

    ```markdown
    $$
    a^2 + b^2 = c^2
    $$
    ```

- For a footnote[^1], use `[^1]` in the text and add at the bottom of the page `[^1]: Lorem ipsum`. The number can be replaced with a word (i.e. `[^name]`).

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

=== "Tabbed List"

    The code to create a tabbed list, like the one we are in right now:

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
![Image](../assets/images/tricks/placeholder.gif)
```

To include a centered image with a caption, use the following code.

```html
<figure>
    <img src="../../assets/images/something/image.png" width=90%>
  <figcaption>Figure: Something really amazing.</figcaption>
</figure>
```

Images should be saved in `assets/images`, in an appropriately named folder.

*[acronym]: helpful explanation

[^1]: Some additional content.
[^name]: fwefwef

[zensical]: https://zensical.org/
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material/
[site_address]: https://pylhc.github.io/
[uv]: https://docs.astral.sh/uv/
[markdownsyntax]: https://www.markdownguide.org/basic-syntax/
[markdownlint]: https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint
[bestwiki]: https://pylhc.github.io/
