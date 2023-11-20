#!/usr/bin/env python3

import dns.resolver
import argparse
import sys

parser = argparse.ArgumentParser(description='Recursively check DNS lookups in SPF record')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('domain', nargs='?', help='Domain name to query SPF record from')
    
args = parser.parse_args()

if len(sys.argv) == 1:
  parser.print_help()

verbose = args.verbose


def get_spf_records(domain):
    spf_records = []
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for answer in answers:
            answer = answer.to_text()
            if answer.startswith('"v=spf1'):
                spf_records.append(answer.strip('"'))
    except Exception as e:
        print(f'Error: {e}')
    if verbose:
        print(f"SPF records: {spf_records}")
    return spf_records

def get_included_domains(domain):
    included_domains = []
    spf_records = get_spf_records(domain)
    for spf_record in spf_records:
        spf_parts = spf_record.split()
        for spf_part in spf_parts:
            if spf_part.startswith('include:'):
                included_domain = spf_part.replace('include:', '')
                included_domains.append(included_domain)
    if verbose:
        print(f"Included domains: {included_domains}")
    return included_domains

def get_all_domains(domain):
    all_domains = []
    queue = [domain]
    while queue:
        current_domain = queue.pop(0)
        all_domains.append(current_domain)
        included_domains = get_included_domains(current_domain)
        for included_domain in included_domains:
            if included_domain not in all_domains and included_domain not in queue:
                queue.append(included_domain)
    if verbose:
        print(f"All domains: {all_domains}")
    return all_domains

def check_spf(domain):
    all_domains = get_all_domains(domain)
    # remove original domain
    all_domains.remove(domain)
    if verbose:
        print(f'The domains in the SPF records of {domain} are:')
        for domain in all_domains:
            print(domain)
        print(f'The total number of lookups: {len(all_domains)}')
    else:
        print(len(all_domains))

def main():
    if len(sys.argv) > 1:
        domain = args.domain
        check_spf(domain)

if __name__ == "__main__":
    main()