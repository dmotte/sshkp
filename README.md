# sshkp

[![GitHub release workflow](https://img.shields.io/github/workflow/status/dmotte/sshkp/release?logo=github&label=release&style=flat-square)](https://github.com/dmotte/sshkp/actions)
[![PyPI](https://img.shields.io/pypi/v/sshkp?logo=python&style=flat-square)](https://pypi.org/project/sshkp/)

:snake: Script to execute an **SSH command** using a password from a **KeePass database**.

This project uses the [pykeepass](https://pypi.org/project/pykeepass/) library and the `sshpass` command line utility.

Note that, for this to work, the title of your KeePass database entry should be written in a form that can be used with the `ssh` command, e.g. `user@hostname`.

## Installation

This utility is available as a Python package on **PyPI**:

```bash
pip3 install sshkp
```

## Usage

```bash
export KP_FILENAME="/path/to/my/keepass/database.kdbx"
read -p "Password: " -s KP_PASSWORD && export KP_PASSWORD
sshkp user@hostname ls -la  # executes a command
sshkp user@hostname .print  # just prints the SSH password
```

If you don't set the `KP_PASSWORD` environment variable before calling the script, the password will be asked at runtime.

:information_source: For more details on how to use this command, you can also refer to the help message (`sshkp --help`).

## Development

If you want to contribute to this project, the first thing you have to do is to **clone this repository** on your local machine:

```bash
git clone https://github.com/dmotte/sshkp.git
```

Then you can install the package in **editable** mode:

```bash
pip3 install -e . --user
```

This will just link the package to the original location, basically meaning any changes to the original package would reflect directly in your environment ([source](https://stackoverflow.com/a/35064498)).
