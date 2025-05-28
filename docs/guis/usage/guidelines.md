# GUI development Guidelines

## General Guidelines

Usually the testing of GUI codes is quite relaxed and there is no review process.
This is for three reasons:

1. Automated testing a GUI is more complicated than testing individual modules.
1. The GUIs are just "sugar" on top of the actual analysis codes, which if everything fails, can usually still be run via the command line.
1. "Testing" is assumed to be done "during development", meaning the coder should run at least the normal stages of their GUI once before releasing it.

### Model-View-Controller Architecture

While not strictly enforced, our GUIs follow the [Model-View-Controller][mvc_wiki]{:target="_blank"} architecture,
as it is a very useful and therefore also very common GUI pattern.
[A better explanation can be found here][mvc_geeks]{:target="_blank"}, but this section summarizes a few key points relevant to our usecase.

The main philosophy of the MVC architecture is to separate the actual GUI elments, the _View_, from the underlying data, stored in the _Model_,
and let the _Controller_ handle the communication between the two and with the user.

In our code this is not always possible or strictly enforced and sometimes it is even hard to distinguish whether something should be part of the
_Controller_ or the _View_, but it is a good idea to at least think about if it can be done for the specific part you are working on.

Main advatages of the MVC architecture are:

- The _Model_ components are usually easier to test.
- It automatically reduces complexity and coupling in the GUI code, by its build-in separation of functionality and modularization.
- This makes it easier to reutilize code between different parts of the GUI (e.g. re-use of the same data) or even between different GUIs (e.g use the same plotting components).
- It is easier to find the part in the code that you want to change (i.e. do you want to make a cosmetic change? - _View_; or a workflow change? - _Controller_; or a change in how to store data? - _Model_).

## Java Guidelines

While the `java` development is not as strictly regulated as the `python` repositories,
this code has been used for many years and probably will be continued to be used for many years to come.

**Try to keep it clean!**

Because GUI testing is hard and because we have easy access to old versions via [CAS][cas_cern]{:target="_blank" .cern_internal},
there is no tests suite and no review process for the `java` development and changes can be simply pushed to the `master` branch.

Some "best practices" have been established through the years:

- Follow the [MVC architecture](#model-view-controller-architecture).
- **Do not re-invent the wheel**, reuse or at least orient yourself to existing code whenever possible.
- If you see horribly written code (yes, it exists /s), do not hesitate to fix it.
- Use `camelCase` for variable names and `PascalCase` for class names.
- Put all external paths as constants into the `src/java/cern/lhc/betabeating/external/ExternalPathsCollection.java`.
- As in `python`, use constants (`static final String`) for strings.
- If you are introducing new "properties", which can be set via the `bbgui_user.properties` file, use the prefix `PROPERTY_`  (and `static final String`) to make them easily searchable in the code.
- Follow the note about [adding new settings](../betabeat/settings.md#adding-new-settings).
- Do not use `Strings` for file paths, for now we mostly use `File` objects (but see also the [Issue #239][issue_239]).

!!! tip "Factory Pattern"
    One pattern that you will find in different places of `java` code is the [factory design-pattern][factory_pattern_wiki]{:target="_blank"}.
    While useful in some scenarios, I personally (jdilly) find it too verbose and annoying to implement,
    in the past there were even [scripts to automatically write the factory-code][internal_program_writer]{:target="_blank"} because it needs so many lines of repeating code.

    In particular, this pattern was used for the [creation of the `ExternalProgram` classes][factory_pattern_doc]{:target="_blank"} to allow the setting of
    multiple attributes before even creating the class, without having to write multiple constructors
    (which in turn is a limitation of the `java` language, as you cannot set "default" values as in `python`).
    The newer implementations of the `ExternalPrograms` follow a different approach:
    One constructor with all **required** parameters, which means _"this programm can run"_ and the optional
    attibutes can be set later on via the setter-methods.

[cas_cern]: https://cas.cern.ch
[issue_239]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/issues/239
[mvc_wiki]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
[mvc_geeks]: https://www.geeksforgeeks.org/mvc-framework-introduction/
[factory_pattern_wiki]: https://en.wikipedia.org/wiki/Factory_method_pattern
[internal_program_writer]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/BetaBeatSrc/src/java/cern/lhc/betabeating/external/helper/InternalProgramWriter.java
[factory_pattern_doc]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/BetaBeatSrc/src/java/cern/lhc/betabeating/external/documentation
