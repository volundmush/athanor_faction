INSTALLED_APPS = ["athanor_faction"]

GLOBAL_SCRIPTS = dict()

GLOBAL_SCRIPTS['faction'] = {
    'typeclass': 'athanor_faction.controllers.AthanorFactionController',
    'repeats': -1, 'interval': 60, 'desc': 'Faction Manager for Faction System'
}