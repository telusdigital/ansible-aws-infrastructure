# ansible-aws-infrastructure


aws-infrastructure builds out things according to seemingly arbitrary conventions. They probably make sense, in the appropriate context.

[![Licence](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://tldrlegal.com/license/mit-license)
[![Platforms](http://img.shields.io/badge/platforms-ubuntu-lightgrey.svg?style=flat)](#)

Tunables
--------
 * `autodeploy_passthrough_enabled` (boolean) - should ports in security groups be opened to support autodeploy passthrough
 * `autoscale` (boolean) - should this playbook autoscale
 * `elb_ssl_offload` (boolean) - terminate SSL in the ELB
 * `elb_ssl_certificate_name` (string) - name of the certificate to use
 * `load_balance_prototypes` (boolean) - are the prototypes load balanced
 * `load_balancers_enabled` (boolean) - are load balancers used
 * `dns_points_to_load_balancer` (boolean) - should the dns record point to the load balancer
 * `dns_load_balancing_enabled` (boolean) - load balance with Route53
 * `dns_load_balanced_roles` (list of strings) - list of what roles should be load balanced
 * `root_volume_size` (integer) - the size of the root volume in GB
 * `subnet_prefix` (string) - the first 2 octaves of the ip in the format '10.0'
 * `using_rds` (boolean) - use AWS RDS
 * `rds_engine` (enumeration | postgres, MySQL) - the type of RDS engine to use
 * `rds_database_name` (string) - the database name
 * `rds_database_username` (string) - the database username
 * `rds_database_password` (string) - the database password
 * `rds_database_size` (integer) - the size of the database in GB
 * `rds_database_backup_retention` (integer) - how long to keep data in days
 * `using_elasticache` (boolean) - use AWS Elastic Cache
 * `elasticache_engine` (enumeration | memcached, redis) - the engine to use in the elasti cache
 * `fallback_server_type` (boolean) - to use fallback server type or not
 * `forge_region` (string) - valid aws region to build in
 * `forge_bucket` (string) - s3 bucket name to find the playbooks for forge in
 * `forge_userdata` (64bit encoded string) - aws bootstrap code
 * `virtualization_type` (enumeration | hvm, paravirtual) - the type of virtualization
 * `health_check_response_timeout` (integer) - how long to wait till check times out in seconds
 * `health_check_interval` (integer) - how long to wait between checks in seconds
 * `health_check_unhealthy_threshold` (integer) - The number of consecutive failed health checks that must occur before declaring an EC2 instance unhealthy in seconds
 * `health_check_healthy_threshold` (integer) - The number of consecutive successful health checks that must occur before declaring an EC2 instance healthy in seconds
 * `health_check_ping_port` (integer) - The port health checks test on the EC2 instance
 * `health_check_protocol` (string) - The protocal to use with the health checks tests
 * `health_check_ping_path` (string) - The path to test with the health checks
 * `always_use_spot_instance_for_roles` (list of strings) - list of what roles will be build on spot instances
 * `autoscale_roles` (list of strings) - list of what roles will be autoscaled
 * `default_instance_type` (list of key/vaules) - list of what roles should use as an instance type
 * `fallback_instance_type` (list of key/vaules) - list of what instance type should be used if we are falling back (ie spot prices are spiked)
 * `use_spot_instances_in_environments` (list of strings) - list of environment tiers that should use spot instances
 * `default_instance_bid` (list of key/vaules) - list of instance sizes and what the max bid should be for it
 * `override_instance_type` (list of key/vaules) - list of roles and instance types to use
 * `override_instance_bid` (list of key/vaules) - list of instance types to use and their max bids
 * `override_root_volume_size` (list of key/vaules) - list of roles and the max root volume size
 * `override_region` (string) - allows you to build a box in a region other than that specified in the configs
 * `default_server_types` (list of enumeration | webserver, securewebserver, mysql, postgresql, mongodb, alternativewebserver, alternativesecurewebserver) - defines each type of role and what its default role is (for opening security groups)
 * `override_server_types` (list of key/vaules) - list of server role what instances that should be
 * `roles_needing_public_ip` (list of string) - list of roles needing public ip
 * `vpc_peering_enabled` (boolean) - if VPC peering is enabled
 * `vpc_peering_from` (string) - what to peer from (usually this project)
 * `vpc_peering_to` (list of string) - list of vpcs to connect too
 * `ec2_ami_id` (string) - id of the ami you want to use

Dependencies
------------
- Ansible >2.0

Example Playbook
----------------
    - hosts: servers
      roles:
         - role: telusdigital.aws-infrastructure
           required_systems:
             - application
             - database
           autodeploy_passthrough_enabled: yes
           using_load_balancers: yes
           elb_ssl_offload: yes
           elb_ssl_certificate_name: application.foo-production

Contributors
------------
* [Chris Olstrom](https://colstrom.github.io/) | [e-mail](mailto:chris@olstrom.com) | [Twitter](https://twitter.com/ChrisOlstrom)
* Steven Harradine
* Justin Scott
* Aaron Pederson
* Ben Visser
* Kinnan Kwok
* Royston Tong
* Alex Podobnik
