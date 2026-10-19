#!/usr/bin/env python3
"""Preview locally and rebuild content whenever data or photos change."""
import argparse, functools, http.server, threading, time
from build import ROOT, build

def signature():
    return tuple(sorted((str(p),p.stat().st_mtime_ns,p.stat().st_size)
                 for parent in (ROOT/'data',ROOT/'assets/photos')
                 for p in parent.rglob('*') if p.is_file()))

def watch(stop):
    previous=signature()
    while not stop.wait(1):
        current=signature()
        if current!=previous:
            try:
                build(); print('Content/photos updated. Refresh the browser.',flush=True)
            except Exception as exc:
                print(f'Could not rebuild: {exc}',flush=True)
            previous=current

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=4174)
    args=parser.parse_args()
    build()
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
    stop=threading.Event()
    with http.server.ThreadingHTTPServer(('127.0.0.1',args.port),handler) as server:
        threading.Thread(target=watch,args=(stop,),daemon=True).start()
        print(f'ARFANDIQA preview: http://localhost:{args.port}/',flush=True)
        print('Drop photos into assets/photos, then refresh the browser. Ctrl+C to stop.',flush=True)
        try: server.serve_forever()
        except KeyboardInterrupt: stop.set()
