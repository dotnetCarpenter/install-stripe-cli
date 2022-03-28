# install-stripe-cli

Since it has been [a full year] without an easy way to install and update [stripe-cli] on linux, I have created `install-stripe-cli` to make that easy.

I wrote [a presentation of `install-stripe-cli`](https://github.com/stripe/stripe-cli/issues/666#issuecomment-1079704202), that I will continue to link to as long as the presentation is still current with this code base.

- [Installation](#installation)
- [Usage](#usage)
- [Questions / Answers](#questions--answers)
- [Development](#development)


## Installation

Create a directory where you want to save `install-stripe-cli` and keep the `stripe-cli` installation.
Copy/Paste the snippet below into your terminal. That will save the latest release of `install-stripe-cli` and print usage if successfull. Requires that [curl], [wget], [jq], [xargs] and [b2sum] is installed.

```bash
curl -s https://api.github.com/repos/dotnetcarpenter/install-stripe-cli/tags \
| jq --raw-output 'sort_by(.name)|last|.commit.sha' \
| (read sha && echo "https://raw.githubusercontent.com/dotnetcarpenter/install-stripe-cli/$sha") \
| (read url && xargs sh -c "echo $url/install-stripe-cli-checksums.txt && echo $url/install-stripe-cli") \
| xargs -P 2 wget -qO;
b2sum --status -c install-stripe-cli-checksums.txt && chmod +x install-stripe-cli && ./install-stripe-cli --help
```

## Usage

```
Usage:
./install-stripe-cli [-h|--help] [-v|--version] [-lps] [-i usr|deb|rpm]

install-stripe-cli version: 1.0.2

Options:
  -h, --help			Print usage and exit. -h for short usage and --help for long.
  -v, --version			Print version and exit.
  -i, --install=deb|rpm|usr	Choose how to install. Negates --prompt.
  -l, --changelog		Display the changelog. Requires 'jq' to be installed.
  -p, --prompt			Ask which file to install.
  -s, --silent			Only print errors, when installing.

Examples:

	  ./install-stripe-cli

  will download stripe-cli to your current folder and automagically
  install either the .deb or .rpm file with your package manager.
  Or symlink it to /usr/local/bin if neither dpkg or rpm was found
  on your system.

	  ./install-stripe-cli -i usr

  will download stripe-cli to your current folder and symlink it from
  /usr/local/bin.  '--install usr'  option does not require 'sudo'.

	  ./install-stripe-cli -li deb

  will download stripe-cli to your current folder, install it with
  dpkg and print the changelog.

Exit Status:

  Returns success unless an invalid option is given or an error occurs.

  Error code 1:  Invalid option.
  Error code 2:  stripe-linux-checksums.txt failed to download.
  Error code 4:  Invalid --install option value.
  Error code 8:  Could not figure out which file to install.

 Coded with 💓 by @dotnetCarpenter - MIT LICENSE © 2022
```

## Questions / Answers

Q: _The wrong deb/rpm package is installed because stripe now has multiple deb and/or rpm files._

A: _Use `./install-stripe-cli --prompt` until a fix is made and please [create an issue](https://github.com/dotnetCarpenter/install-stripe-cli/issues), if one does not exist._


Q: _Will `install-stripe-cli` support installing [pacman]'s Arch Linux package?_

A: _Sure. If Stripe will build an Arch Linux package of [stripe-cli]._


## Development

Since keeping _install-stripe-cli-checksums.txt_ in sync with _install-stripe-cli_ is paramount, there is two helpful git hooks in the _scripts/_ folder.

+ _pre-push_ will only allow `git push` if _install-stripe-cli-checksums.txt_ is up to date.
+ _pre-commit_ will create a new BLAKE2 digest if there is a change to _install-stripe-cli_ and you forgot to run _scripts/create-digest.sh_. It will also add the newly generated _install-stripe-cli-checksums.txt_ to your commit, so they are in sync.

You need to copy the files into _.git/hooks/_ and make them executable, before they take effect.


[a full year]: https://github.com/stripe/stripe-cli/pull/673#issuecomment-1078892697
[stripe-cli]: https://stripe.com/docs/stripe-cli#install

[curl]: https://curl.se/
[wget]: https://www.gnu.org/software/wget/
[xargs]: https://www.gnu.org/software/findutils/xargs/
[b2sum]: https://www.gnu.org/software/coreutils/
[jq]: https://stedolan.github.io/jq/

[pacman]: https://archlinux.org/pacman/
