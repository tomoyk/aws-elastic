import re
from datetime import datetime as dt

def parser(line):
    json_body = {}

    '''
    Pickup enclosed "item" in double quotes
    '''
    pattern_quote = re.compile(r'(\"[^\"]+\")')
    quote_items = pattern_quote.findall(line)

    # remove blank item in list and double-quote in string
    quote_items = [tmp.replace('"', '') for tmp in quote_items]
    if len(quote_items) < 1:
        raise ValueError

    try:
        request_line = quote_items[0].split()
        json_body['method'] = request_line[0].upper()
        json_body['request_uri'] = request_line[1]
        json_body['http_version'] = request_line[2].upper()
        json_body['referer'] = quote_items[1]
        json_body['user_agent'] = quote_items[2]
    except Exception as e:
        print(e)
        print("\t", line)
        return {}

    # remove matched item in list
    line = re.sub(pattern_quote, '', line)

    '''
    Pickup item splited by space
    '''
    request_items = [l for l in line.split() if l]

    try:
        json_body['source_ip'] = str(request_items[0])
        json_body['remote_user'] = request_items[2]
        date_str = request_items[3].replace('[', '')
        date = dt.strptime(date_str, '%d/%b/%Y:%H:%M:%S')
        json_body['time_stamp'] = date.strftime('%Y-%m-%d %H:%M:%S')
        json_body['time_zone'] = request_items[4].replace(']', '')
        json_body['status_code'] = request_items[5]
        json_body['body_bytes'] = request_items[6]
    except Exception as e:
        print(e)
        print("\t", line)
        return {}

    '''
    for p,q in json_body.items():
        print(p,q)
    '''

    return json_body


if __name__ == '__main__':
    '''
    res = parser('192.168.0.182 - - [07/Apr/2019:17:35:45 +0900] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.40 Safari/537.36" "-"')
    print(res)
    res = parser('192.168.0.182 - - [07/Apr/2019:17:35:50 +0900] "GET /robots.txt HTTP/1.1" 404 208 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.40 Safari/537.36"')
    print(res)
    '''
    import sys
    with open(sys.argv[1]) as f:
        #print(f.read())
        for l in f.read().splitlines():
            r = parser(l)
            for k,v in r.items():
                # print(k, ":", v)
                pass
            
