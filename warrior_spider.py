import sys
import urllib.parse

BANNER = """\u001b[36m
 __    __   ____  ____   ____    ___   ____       ____    ____  ____    ____  ___ ___       ____  ____     ___  ____  
|  T__T  T /    T|    \ |    \  /   \ |    \     |    \  /    T|    \  /    T|   T   T     /    T|    \   /  _]|    \ 
|  |  |  |Y  o  ||  D  )|  D  )Y     Y|  D  )    |  o  )Y  o  ||  D  )Y  o  || _   _ |    Y   __j|  D  ) /  [_ |  o  )
|  |  |  ||     ||    / |    / |  O  ||    /     |   _/ |     ||    / |     ||  \_/  |    |  T  ||    / Y    _]|   _/ 
l  `  '  !|  _  ||    \ |    \ |     ||    \     |  |   |  _  ||    \ |  _  ||   |   |    |  l_ ||    \ |   [_ |  |   
 \      / |  |  ||  .  Y|  .  Yl     !|  .  Y    |  |   |  |  ||  .  Y|  |  ||   |   |    |     ||  .  Y|     T|  |   
  \_/\_/  l__j__jl__j\_jl__j\_j \___/ l__j\_j    l__j   l__j__jl__j\_jl__j__jl___j___j    l___,_jl__j\_jl_____jl__j   
                                                                                                                      created by Jeetu Rajput\u001b[0m"""

USAGE = "Usage: python3 spider.py [-h | --help] urls.txt"

def print_help():
    print(USAGE)
    print("Options:")
    print("-h, --help\tshow this help message and exit")

if len(sys.argv) != 2:
    print_help()
    sys.exit(1)
elif sys.argv[1] in ['-h', '--help']:
    print_help()
    sys.exit(0)

urls_file = sys.argv[1]
peram_file = 'peram.txt'
non_peram_file = 'non_peram.txt'

with open(urls_file, 'r') as urls, open(peram_file, 'w') as pf, open(non_peram_file, 'w') as npf:
    print(BANNER)
    for url in urls:
        try:
            parsed_url = urllib.parse.urlparse(url.strip())
            params = urllib.parse.parse_qs(parsed_url.query)
            if params:
                params_str = '&'.join([f"{key}={value[0]}" for key, value in params.items()])
                pf.write(f"{url.strip()}?{params_str}\n")
            else:
                npf.write(f"{url.strip()}\n")
        except Exception as e:
            print(f"Error in URL: {url.strip()} - {str(e)}")
