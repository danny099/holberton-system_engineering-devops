#!/usr/bin/env bash
#puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School for the win!',
}

file_line { 'fffff':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'rewrite ^/redirect_me https://www.linkedin.com/in/danny-alejandro-martinez-rivera-72b470192 permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
