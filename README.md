# install-stripe-cli

Since it has been [a full year] without an easy way to install and update [stripe-cli] on linux, I have created `install-stripe-cli` to make that easy.

I wrote [a presentation of `install-stripe-cli`](https://github.com/stripe/stripe-cli/issues/666#issuecomment-1079704202), that I will continue to link to as long as the presentation is still current with this code base.


## Usage

```
Usage:
./install-stripe-cli [-h|--help] [-lps] [-i usr|deb|rpm]

Options:
  -h, --help			Print usage and exit. -h for short usage and --help for long.
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

[a full year]: https://github.com/stripe/stripe-cli/pull/673#issuecomment-1078892697
[stripe-cli]: https://stripe.com/docs/stripe-cli#install