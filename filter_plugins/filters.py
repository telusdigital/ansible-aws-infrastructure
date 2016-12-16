def make_rules(rules, role_name='', open_to_internal_traffic_roles=[], to_port=0, from_port=0, cidr='', group_id='', protocol=''):
  if( role_name in open_to_internal_traffic_roles):
    rules.append({
      "proto": protocol,
      "from_port": from_port,
      "to_port" : to_port,
      "cidr_ip": cidr
      })
  return rules

class FilterModule(object):
  def filters(self):
    return {'make_rules': make_rules}
