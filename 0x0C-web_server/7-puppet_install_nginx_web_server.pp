# install and configure nginx web server with puppet
package { 'nginx':
  ensure => installed,
}

# Ensure index file is present and contains 'Hello World!'
file { 'Website index file':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
  require => Package['nginx'],
}

# Ensure nginx to redirect /redirect_me to another page
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    server_name _;
    root /var/www/html;

    location / {
      return 200 'Hello World!';
    }

    location = /redirect_me {
      return 301 https://github.com/Tashydaije;
    }
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}


# Ensure nginx is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
