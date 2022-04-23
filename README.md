# sshkp

:snake: Script to execute an **SSH command** using a password from a **KeePass database**.

This project uses the [pykeepass](https://pypi.org/project/pykeepass/) library and the `sshpass` command line utility.

Note that, for this to work, the title of your KeePass database entry should be written in a form that can be used with the `ssh` command, e.g. `user@hostname`.

## Usage

```bash
export KP_FILENAME="/path/to/my/keepass/database.kdbx"
read -p "Password: " -s KP_PASSWORD && export KP_PASSWORD
sshkp user@hostname ls -la  # executes a command
sshkp user@hostname .print  # just prints the SSH password
```

If you don't set the `KP_PASSWORD` environment variable before calling the script, the password will be asked at runtime.

See `sshkp --help` for more information.

It is advised to install the script in a directory under your `$PATH` (see [below](#installation)).

## Installation

To install _sshkp_ you need to execute the following commands as root:

```bash
apt update && apt install sshpass python3-pip
pip3 install -r requirements.txt

curl -Lo "/usr/local/bin/sshkp" \
    https://github.com/dmotte/sshkp/releases/latest/download/sshkp
chmod +x "/usr/local/bin/sshkp"
```

:information_source: For **user installation** (no root needed, will only work for current user) we recommend `~/.local/bin` instead of `/usr/local/bin`. If it's not in your `$PATH`, you can add the following to your `.bashrc` or `.zshrc`:

```bash
export PATH="~/.local/bin:$PATH"
```
