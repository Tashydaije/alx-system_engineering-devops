# Web server

## Learning Objectives
* What is the main role of a web server -  to store, process, and deliver web pages and other web content to clients (typically web browsers) over the internet or a local network thereby facilitating the interaction between clients and web applications.

* What is a child process - A child process is a process that is created by another process, known as its parent process. In computing, processes are instances of executing programs, and the creation of child processes allows for parallel execution and delegation of tasks.

* Why web servers usually have a parent process and child processes - Web servers typically utilize a parent-child process model to handle incoming client requests efficiently. The parent process manages essential tasks such as accepting incoming connections and creating child processes to handle client requests. Each child process is responsible for handling a specific client request, processing it, and returning a response. This allows the web server to handle multiple reqs simultaneously, improving performance and scalability. Child processes can be managed and terminated independently, ensuring robustness and fault tolerance.

* What are the main HTTP requests - GET, POST, PUT, DELETE, HEAD, PATCH, TRACE, OPTIONS.

## DNS
* What DNS stands for - Domain Name System.
* What is DNS main role -  to translate human-readable domain names (like example.com) into machine-readable IP addresses (like 192.0.2.1).

## DNS Record Types
* A(Address) Record:
  - A records map a domain name to the IPv4 address (32-bit) of the server hosting the domain. 
* CNAME(Canonical Name) Record:
  - CNAME records alias one domain name to another. They are used when you want one domain name to resolve to another domain name instead of an IP address.
* TXT(Text) Record:
  - TXT records store arbitrary text data. They are commonly used for various purposes such as domain ownership verification, SPF (Sender Policy Framework) records for email authentication, DKIM (DomainKeys Identified Mail) records, and general information like descriptive text or instructions.

* MX(Mail Exchange) Record:
  - Specifies the mail servers responsible for receiving email on behalf of the domain
