# All Russian mirrorlist USA distribution

import requests

from mirrorlist.all_url import all_arch_barch_url

def artix_usa_mirrors():
    url = all_arch_barch_url[1]

    response = requests.get(url)
    html = response.text

    lines = html.strip().split('\n')

    mirrors_country = None
    results = []

    for line in lines:
        line = line.strip()

        if line.startswith('#'):
            parts = line.replace('# United', '').strip().split()

            if parts:
                mirrors_country = parts[0]
            else:
                mirrors_country = None

        if mirrors_country == 'States' and line.startswith('Server ='):
            clear_line = line.replace('#', '').strip()
            print(clear_line)

            results.append(clear_line)

    return results

def artix_usa_start():
    # Использование
    found_lines = artix_usa_mirrors()
    for line in found_lines:
        print(line)
    return found_lines