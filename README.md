# Python + Poetry GitHub Action Template

## Getting started from the template
1. Rename the `src/action_python_poetry` package.
1. Globally replace instances of `action-python-poetry` and `action_python_poetry` with your project and package name.
1. If your repo is private, set it up on [CodeCov](https://app.codecov.io/) and add a codecov token to your repo under the `CODECOV_TOKEN` secret.
1. Create and test your action. `__main__.py` in your package will be executed when the action is run.
1. Update `action.yml`, `README.md`, and `.github/workflows/test-action.yml` to reflect your action's specification.
1. Update the copyright notice and permissions stuff in `LICENSE`, making sure to retain the original text of both in your distribution according to the MIT license that this template is distributed under.
1. Remove this section from `README.md`.
1. Happy hacking!

### Like this template?
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png)](https://www.buymeacoffee.com/k2bd)

## Quickstart

```yml
name: Run Action
on:
  workflow_dispatch:

jobs:
  action-python-poetry:
    runs-on: ubuntu-latest
    steps:
      - uses: k2bd/action-python-poetry@v1
        with:
          helloName: k2bd
          repeats: 3
```

## Action Specification

### `helloName`

**Required**

The name of the person to say hello to

### `repeats`

*Optional* - default 1

Number of times to say hello to this person

## Developing

Install [Poetry](https://python-poetry.org/) and `poetry install` the project

### Useful Commands

Note: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`

- `poe autoformat` - Autoformat code
- `poe lint` - Linting
- `poe test` - Run Tests

### Testing the action

The action can be tested locally by building the Dockerfile, e.g.

```sh
docker run -e INPUT_HELLONAME=k2bd -e INPUT_REPEATS=2 $(docker build -q .)
```

Additionally, there is a manual invocation action on the repo called "Test Action" that can be used to invoke the repo's version of the action from the Actions tab of the repo.

### Releasing

Release a new version by creating a new annotated semver tag e.g. `git tag -a v1.2.3 -m "Release version 1.2.3"` and pushing it (`git push --tags`). Then create a new release from that tag in GitHub.

There is an autoversioning action that keeps major version tags (`v1`, `v2`, ...) and `latest` up-to-date when a new release is published.
