import asyncio
import logging
from argparse import ArgumentParser
from asyncio import exceptions
from copy import deepcopy
from itertools import chain
from typing import Iterable

from async_dns import Address
from async_dns.core import types
from async_dns.resolver import DNSClient

from fishing_hosts_generator import FishingDomainsGenerator
from mutators.delete_char_mutator import DeleteCharMutator
from mutators.homoglyph_mutator import HomoglyphMutator
from mutators.last_char_mutator import LastCharMutator
from mutators.third_level_domain_mutator import ThirdLevelDomainMutator


DEFAULT_DOMAIN_ZONES = [
    'com', 'ru', 'net', 'org', 'info', 'cn', 'es',
    'top', 'au', 'pl', 'it', 'uk', 'tk', 'ml', 'ga',
    'cf', 'us', 'xyz', 'top', 'site', 'win', 'bid'
]

logger = logging.getLogger('fishing_domains_checker')
logging.basicConfig(level=logging.INFO)


async def check_domain(domain):
    result = {'domain': domain}
    client = DNSClient()
    try:
        response = await client.query(domain, types.A, Address.parse('8.8.8.8'))
        result['IP'] = [record.data.data for record in response.an]
    except exceptions.TimeoutError:
        result['IP'] = None
    return result


def bulk_check_domains(domains: Iterable[str]):
    logger.info('Total domains: %s', len(list(deepcopy(domains))))
    logger.info('Resolving domains')
    # асинхронная проверка всех созданных доменных имён
    loop = asyncio.get_event_loop()
    coros = [check_domain(host) for host in domains]
    tasks = asyncio.gather(*coros)
    results = loop.run_until_complete(tasks)

    valid_domains = [result for result in results if result['IP']]
    logger.info('Valid domains: %s', len(valid_domains))
    return valid_domains


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-kw", "--keywords", required=True,
                        dest="keywords", nargs='+', metavar="KEYWORD",
                        help="keywords separated by spaces")
    parser.add_argument("-dz", "--domainzones",
                        dest="domain_zones", nargs='+', metavar="DOMAIN-ZONE",
                        default=DEFAULT_DOMAIN_ZONES, help="domain zones separated by spaces")
    args = parser.parse_args()

    keywords = args.keywords
    domain_zones = args.domain_zones
    mutators = [LastCharMutator, HomoglyphMutator, ThirdLevelDomainMutator, DeleteCharMutator]
    logger.info('Generating fishing domains')

    # собираем все фишинговы домены для всех ключевых слов в один генератор
    domains = chain.from_iterable(
        [FishingDomainsGenerator(keyword, mutators, domain_zones) for keyword in keywords]
    )
    # валидируем домены
    valid_domains = bulk_check_domains(domains)

    print(
        *[f"{record['domain']} {' '.join(record['IP'])}" for record in valid_domains],
        sep='\n'
    )
