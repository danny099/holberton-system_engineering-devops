#!/usr/bin/env bash
#kill procces with puppet
exec { 'pkill -f ./killmenow':
    command => 'pkill -f ./killmenow',
    path    => '/usr/bin',
}

