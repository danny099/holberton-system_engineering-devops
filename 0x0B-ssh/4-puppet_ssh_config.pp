#!/usr/bin/env bash
# connect with puppet
file_line { 'Declare identity file':
  ensure => 'present',
  line   => ' IdentityFile ~/.ssh/holberton',
  path   => '/etc/ssh/ssh_config'
}

file_line { 'Turn off passwd auth':
  ensure => 'present',
  line   => ' PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
  match  => 'PasswordAuthentication yes'
}
