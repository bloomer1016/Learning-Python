import ipinfo
access_token = 'api-key'
handler = ipinfo.getHandler(access_token)
ip_address = 'x.x.x.x'
details = handler.getDetails(ip_address)
details.all
