# spf-check
Recursively check DNS lookups in SPF record since there is a limit of allowed 10 DNS lookups in SPF record.

# Usage
    usage: spf-check.py [-h] [-v] [domain]
    
    Recursively check DNS lookups in SPF record
    
    positional arguments:
      domain         Domain name to query SPF record from
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Enable verbose mode

# Example:
Simple output:

    ./spf-check.py google.com
    4
Verbose output:

     ./spf-check.py -v google.com
    SPF records: ['v=spf1 include:_spf.google.com ~all']
    Included domains: ['_spf.google.com']
    SPF records: ['v=spf1 include:_netblocks.google.com include:_netblocks2.google.com include:_netblocks3.google.com ~all']
    Included domains: ['_netblocks.google.com', '_netblocks2.google.com', '_netblocks3.google.com']
    SPF records: ['v=spf1 ip4:35.190.247.0/24 ip4:64.233.160.0/19 ip4:66.102.0.0/20 ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:74.125.0.0/16 ip4:108.177.8.0/21 ip4:173.194.0.0/16 ip4:209.85.128.0/17 ip4:216.58.192.0/19 ip4:216.239.32.0/19 ~all']
    Included domains: []
    SPF records: ['v=spf1 ip6:2001:4860:4000::/36 ip6:2404:6800:4000::/36 ip6:2607:f8b0:4000::/36 ip6:2800:3f0:4000::/36 ip6:2a00:1450:4000::/36 ip6:2c0f:fb50:4000::/36 ~all']
    Included domains: []
    SPF records: ['v=spf1 ip4:172.217.0.0/19 ip4:172.217.32.0/20 ip4:172.217.128.0/19 ip4:172.217.160.0/20 ip4:172.217.192.0/19 ip4:172.253.56.0/21 ip4:172.253.112.0/20 ip4:108.177.96.0/19 ip4:35.191.0.0/16 ip4:130.211.0.0/22 ~all']
    Included domains: []
    All domains: ['google.com', '_spf.google.com', '_netblocks.google.com', '_netblocks2.google.com', '_netblocks3.google.com']
    The domains in the SPF records of google.com are:
    _spf.google.com
    _netblocks.google.com
    _netblocks2.google.com
    _netblocks3.google.com
    The total number of lookups: 4
