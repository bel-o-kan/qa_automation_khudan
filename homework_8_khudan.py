def get_domain_names(file_name):
    with open(file_name, 'r') as f:
        domains = f.read().splitlines()

    domain_names = [domain.split('.')[1] for domain in domains]

    return domain_names
domain_names = get_domain_names('domains.txt')
print(domain_names)


def get_last_names(file_name):
    last_names = []
    with open(file_name, 'r') as f:
        for line in f:
            last_name = line.split()[1]
            last_names.append(last_name)
    return last_names

last_name = get_last_names("Last_Name.txt")
print(last_name)


import re

def get_authors_dates(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line and not line.isnumeric() :
            match = re.search(r'(\d{1,2}(st|nd|rd|th) \w+ \d{4})', line)
            if match:
                results.append({"date": match.group(1)})

    return results

authors_dates = get_authors_dates('authors.txt')
print(authors_dates)

