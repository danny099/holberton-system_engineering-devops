#!/usr/bin/env bash
#kill procces with puppet
exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f ./killmenow',
}
