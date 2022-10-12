Gradually include here different pieces of useful information, possibly from questions answered in meetings or on Mattermost, which don't really fit anywhere else

# Common MAD-X Pitfalls

MAD-X can sometimes be a bit tricky to work with. This section is intended to
put together some of the common pitfalls encountered when creating a MAD-X
script.  
As a reminder, MAD-X ignores all the code that does not work, it does not raise
errors or crash like other languages.

* Check your `;`
    * A line needs to end with a semicolon. If not, the second line will be
      considered as part of it. The non-working line will then be ignored.
* When tracking for Beam 2, load the `lhcb4.seq` sequence file with `bv=1` flag
    * The `sequence` to use remains `lhcb2`
    * If analysing the tracking with BB.src or OMC3, a model made with the 
      regular `lhc_as_built.seq` file and `lhcb2` sequence with `bv=-1` is 
      required.
