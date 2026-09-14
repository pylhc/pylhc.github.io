# OMC Team Website

This is the source repository for the website of the optics measurements and corrections team (OMC) at CERN.
The pages are [deployed here][site_address].

## Contributing to the Website

### To Make Changes Online

This is a method adapted to making small changes, most likely to a single page.
Go to the [current version of the site][site_address], navigate to a page you wish to modify and click the page's modification link (the little pen at the top right).
You will be taken to the Github GUI to make your changes, which you can later commit.

### To Make Changes Locally

For bigger changes, local development is recommended.
Get a local copy of this repository, set up a `Python 3` environment and install the dependencies:

```bash
git clone https://github.com/pylhc/pylhc.github.io
python -m pip install zensical
```

Create a branch (from master) and make your changes.
You can run a local server by running `zensical serve` from the top-level directory, and see the site rendered locally in your browser at `localhost:8000`.
The rendered website will automatically reload upon changes to any file located in the `docs` directory.

Commit your changes to this repository, and open a pull request to get them approved once they are ready.

---

The static pages are built with `Zensical`, see [its documentation][zensical] for details.
A page is provided on the website with advice on editing it.

[site_address]: https://pylhc.github.io/
[zensical]: https://zensical.org/
