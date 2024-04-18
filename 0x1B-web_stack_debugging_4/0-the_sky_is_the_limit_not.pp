$nginx_ulimit = 'ULIMIT="-n 70000"'
# Define Nginx class
class { 'nginx':
  ensure  => 'installed',
  service => 'running'
}

file { '/etc/default/nginx':
  ensure  => present,
  content => $nginx_ulimit
  notify  => Service['nginx']
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
