# Task 1
file { 'login':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#This file has been wiped hahaha'
}
