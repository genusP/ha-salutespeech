DOMAIN = "salute_stt"
API_AUTH_ENDPOINT = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'

LANGUAGES=[
    'ru-RU',
    'en-US'
]

MAP_VOICES = {
    'ru-RU': {
        'Nec': 'Наталья',
        'Bys': 'Борис',
        'May': 'Марфа',
        'Tur': 'Тарас',
        'Ost': 'Александра',
        'Pon': 'Сергей',
    },
    'en-US': {
        'Kin': 'Kira',
    }
}

CONF_VOICE='voice'
CONF_RATE='rate'

DEFAULT_LANG=LANGUAGES[0]
DEFAULT_VOICE=list(MAP_VOICES[DEFAULT_LANG].keys())[0]
