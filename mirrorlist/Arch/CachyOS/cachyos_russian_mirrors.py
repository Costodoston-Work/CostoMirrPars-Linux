# All Russian mirrorlist СachyOS distribution

import requests

from mirrorlist.all_url import all_arch_barch_url

def cachyos_russian_mirrors():
    url = all_arch_barch_url[2]

    response = requests.get(url)
    html = response.text

    lines = html.strip().split('\n')

    mirrors_country = None
    results = []

    for line in lines:
        line = line.strip()

        if line.startswith('##'):
            parts = line.replace('##', '').strip().split()

            if parts:
                mirrors_country = parts[0]
            else:
                mirrors_country = None

        if mirrors_country == 'Russia'and line.startswith('Server =') or line.startswith('# Server ='):
                clear_line = line.replace('#', '').strip()
                results.append(clear_line)

    return results

def cachyos_russia_start():
    # Использование
    found_lines = cachyos_russian_mirrors()
    for line in found_lines:
        print(line)
    return found_lines