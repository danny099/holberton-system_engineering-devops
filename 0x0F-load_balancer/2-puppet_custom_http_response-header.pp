# same task #0 but with puppet

exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure => installed,
}

file_line { 'header' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By "$HOSTNAME";",
  after  => 'server_name _;',
}

file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}

service { 'nginx':
  ensure => running,
}
