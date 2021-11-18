def _exec(context: dict, param: str):
    print('Túto hru, inšpirovanú slávnym Indiana Jonesom, vytvoril začínajúci vývojár Darius Lindvai.')
    print('Na začiatku hry sa ocitnete v roli Indiana Jonesa, ktorý sa snaží uniknúť z tmavej miestnosti.')
    print('Vašou úlohou je preskúmať miestnosť a nájsť všetky stopy a predmety, ktoré vám pri úniku pomôžu.')


cmd = {
    'name': 'o hre',
    'description': 'zobrazí informácie o hre',
    'aliases': ('o hre', 'about', 'info'),
    'exec': _exec
}
