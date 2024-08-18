# Introduction to Linux: On Ubuntu.

## Table of Content
- [Author](#author)
- [Description](#about-bash-projects)
___

- [API](0x15-api/README.md)
- [API: Advanced](0x16-api_advanced/README.md)
- [Application Server](0x1A-application_server/README.md)
- [Attack Is The Best Defense](attack_is_the_best_defense/README.md)
- [Command Line For The Win](command_line_for_the_win/README.md)
- [Configuration Management](0x0A-configuration_management/README.md)
- [Firewall](0x13-firewall/README.md)
- [HTTPS and SSL](0x10-https_ssl/README.md)
- [Load Balancer](0x0F-load_balancer/README.md)
- [Loops, Conditions And Parsing](0x04-loops_conditions_and_parsing/README.md)
- [MySQL](0x14-mysql/README.md)
- [Networking Basics: I](0x07-networking_basics/README.md)
- [Networking Basics: II](0x08-networking_basics_2/README.md)
- [Processes And Signals](0x05-processes_and_signals/README.md)
- [Postmortem](0x19-postmortem/README.md)
- [Regular Expressions](0x06-regular_expressions/README.md)
- [SSH](0x0B-ssh/README.md)
- [Shell: Basics](0x00-shell_basics/README.md)
- [Shell: Permissions](0x01-shell_permissions/README.md)
- [Shell: Redirections](0x02-shell_redirections/README.md)
- [Shell: Variables and Expansion](0x03-shell_variables_expansions/README.md)
- [Web Infrastructure Design](0x09-web_infrastructure_design/README.md)
- [Web Server](0x0C-web_server/README.md)
- [Web Stack Debugging](0x0D-web_stack_debugging_0/README.md)
- [Web Stack Debugging: I](0x0E-web_stack_debugging_1/README.md)
- [Web Stack Debugging: II](0x12-web_stack_debugging_2/README.md)
- [Web Stack Debugging: III](0x17-web_stack_debugging_3/README.md)
- [Web Stack Debugging: IV](0x1B-web_stack_debugging_4/README.md)
- [Web Stack Monitoring](0x18-webstack_monitoring/README.md)
- [What Happens When You Type `google.com` In Your Browser and Press `Enter`](0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter/README.md)
___

# About Bash projects

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

### Concepts

*For this project, we expect you to look at this concept:*

- [Struggling with the sandbox? Try this: Using Docker & WSL on your local host](https://intranet.alxswe.com/concepts/100039)

![RTFM](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)

# Resources

**Read or watch:**
- [What Is “The Shell”?](https://linuxcommand.org/lc3_lts0010.php)
- [Navigation](https://linuxcommand.org/lc3_lts0020.php)
- [Looking Around](https://linuxcommand.org/lc3_lts0030.php)
- [A Guided Tour](https://linuxcommand.org/lc3_lts0040.php)
- [Manipulating Files](https://linuxcommand.org/lc3_lts0050.php)
- [Working With Commands](https://linuxcommand.org/lc3_lts0060.php)
- [Reading Man pages](https://linuxcommand.org/lc3_man_pages/man1.html)
- [Keyboard shortcuts for Bash](https://www.howtogeek.com/181/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
- [LTS](https://wiki.ubuntu.com/LTS)
- [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

## man or help:
- `cd`
- `ls`
- `pwd`
- `less`
- `file`
- `ln`
- `cp`
- `mv`
- `rm`
- `mkdir`
- `type`
- `which`
- `help`
- `man`

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

## General
- What does RTFM mean?
- What is a Shebang

## What is the Shell
- What is the shell
- What is the difference between a terminal and a shell
- What is the shell prompt
- How to use the history (the basics)

## Navigation
- What do the commands or built-ins `cd`, `pwd`, `ls` do
- How to navigate the filesystem
- What are the . and .. directories
- What is the working directory, how to print it and how to change it
- What is the root directory
- What is the home directory, and how to go there
- What is the difference between the root directory and the home directory of the user root
- What are the characteristics of hidden files and how to list them
- What does the command `cd -` do

## Looking Around
- What do the commands `ls`, `less`, `file` do
- How do you use options and arguments with commands
- Understand the ls long format and how to display it
- [A Guided Tour](https://linuxcommand.org/lc3_lts0040.php)
- What does the `ln` command do
- What do you find in the most common/important directories
- What is a symbolic link
- What is a hard link
- What is the difference between a hard link and a symbolic link

## Manipulating Files
- What do the commands `cp`, `mv`, `rm`, `mkdir` do
- What are wildcards and how do they work
- How to use wildcards

## Working with Commands
- What do `type`, `which`, `help`, `man` commands do
- What are the different kinds of commands
- What is an alias
- When do you use the command help instead of man

## Reading Man Pages
- How to read a man page
- What are man page sections
- What are the section numbers for User commands, System calls and Library functions

## Keyboard Shortcuts for Bash
- Common shortcuts for Bash

## LTS
- What does `LTS` mean?

# Requirements

## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we’ll learn more about how to utilize this command.

# More Info

*Example of line count and first line*

```bash
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$
```

In order to test your scripts, you will need to use this command: `chmod u+x file`. We will see later what does `chmod` mean and do, but you can have a look at `man chmod` if you are curious.

*Example*

```bash
julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$
```

## Author

**Tafara Nyamhunga - [Github](https://github.com/tafara-n) / [Twitter](https://twitter.com/tafaranyamhunga)**
