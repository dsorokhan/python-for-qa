import re
import pprint

m = {}
ggg = []
s = set()
wp = []

conf = '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"'
regex = ''.join(
    '(?P<' + g + '>.*?)' if g else re.escape(c)
    for g, c in re.findall(r'\$(\w+)|(.)', conf))

with open('log.txt', 'r') as log_file:
    for line in log_file.readlines():
        m = re.match(regex, line)
        ggg.append(m.groupdict())

for i in ggg:
    s.add(i['status'])

for i in ggg:
    if i['status'] == '403':
        wp.append(i)


print (s)
pprint.pprint(wp)