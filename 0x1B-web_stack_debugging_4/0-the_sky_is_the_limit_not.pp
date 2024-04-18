class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    hasrestart => true,
  }
}

$nginx_ulimit = 'ULIMIT="-n 65535"'
class { 'nginx': }

file { '/etc/default/nginx':
  ensure  => present,
  content => $nginx_ulimit,
  notify  => Service['nginx'],
}
