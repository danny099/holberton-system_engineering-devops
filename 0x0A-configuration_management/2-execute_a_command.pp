#!/usr/bin/env bash
#kill procces with puppet
exec { 'killmenow':
    command => 'pkill -f ./killmenow',
    path    => '/usr/bin',
}
