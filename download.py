import sys
from app.parser import parse
from app.downloader import Downloader
from app.extractor import extract


args = parse(sys.argv[1:])

dl = Downloader(output=args['output'], login=args['login'], password=args['password'])

result = dl.get(args['url'])

if result:
    items = extract(result)
    for url in items:
        dl.save(url)
