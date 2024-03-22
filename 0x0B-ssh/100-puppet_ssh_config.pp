#!/usr/bin/env bash

# Configuration automation using Puppet

file { '/etc/ssh/ssh_config':
  ensure => present,
content  => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
