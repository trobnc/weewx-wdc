from weecfg.extension import ExtensionInstaller

# Copyright 2022 David Bätge
# Distributed under the terms of the GNU Public License (GPLv3)


def loader():
    return BasicInstaller()


class BasicInstaller(ExtensionInstaller):
    def __init__(self):
        super(BasicInstaller, self).__init__(
            version="1.2.0",
            name='weewx-wdc',
            description='Weather Data Center skin for weewx.',
            author="David Baetge",
            author_email="david.baetge@gmail.com",
            config={
                'StdReport': {
                    'WdcReport': {
                        'skin': 'weewx-wdc',
                        'enable': 'true',
                        'lang': 'en',
                        # 'unit_system': 'US'
                    }
                }
            },
            files=[
                ('bin/user', [
                    'bin/user/diagram_util.py',
                    'bin/user/stats_util.py',
                    'bin/user/general_util.py',
                    'bin/user/celestial_util.py',
                    'bin/user/archive_util.py',
                    'bin/user/table_util.py'
                ]),
                ('skins/weewx-wdc',
                 ['skins/weewx-wdc/index.html.tmpl',
                  'skins/weewx-wdc/week.html.tmpl',
                  'skins/weewx-wdc/month.html.tmpl',
                  'skins/weewx-wdc/month-%Y-%m.html.tmpl',
                  'skins/weewx-wdc/NOAA/NOAA-%Y-%m.txt.tmpl',
                  'skins/weewx-wdc/year.html.tmpl',
                  'skins/weewx-wdc/NOAA/NOAA-%Y.txt.tmpl',
                  'skins/weewx-wdc/year-%Y.html.tmpl',
                  'skins/weewx-wdc/statistics.html.tmpl',
                  'skins/weewx-wdc/celestial.html.tmpl',
                  'skins/weewx-wdc/offline.html.tmpl',
                  'skins/weewx-wdc/manifest.json',
                  'skins/weewx-wdc/icon-192x192.png',
                  'skins/weewx-wdc/icon-256x256.png',
                  'skins/weewx-wdc/icon-384x384.png',
                  'skins/weewx-wdc/icon-512x512.png',
                  'skins/weewx-wdc/skin.conf',
                  'skins/weewx-wdc/lang/de.conf',
                  'skins/weewx-wdc/lang/en.conf',
                  'skins/weewx-wdc/service-worker.js',
                  'skins/weewx-wdc/dist/scss/index.css',
                  'skins/weewx-wdc/dist/js/index.js',
                  'skins/weewx-wdc/favicon.ico',
                  'skins/weewx-wdc/includes/html-head.inc',
                  'skins/weewx-wdc/includes/almanac-tile.inc',
                  'skins/weewx-wdc/includes/almanac-tile-simple.inc',
                  'skins/weewx-wdc/includes/almanac-moon-detail-tile.inc',
                  'skins/weewx-wdc/includes/almanac-sun-detail-tile.inc',
                  'skins/weewx-wdc/includes/combined-diagram-tile.inc',
                  'skins/weewx-wdc/includes/data-table-tile.inc',
                  'skins/weewx-wdc/includes/diagram-tile.inc',
                  'skins/weewx-wdc/includes/stat-tile.inc',
                  'skins/weewx-wdc/includes/climatological-days.inc',
                  'skins/weewx-wdc/includes/ui-shell.inc',
                  'skins/weewx-wdc/includes/footer.inc',
                  'skins/weewx-wdc/includes/forecast.inc',
                  'skins/weewx-wdc/includes/forecast-table.inc',
                  'skins/weewx-wdc/includes/icons/barometer.svg',
                  'skins/weewx-wdc/includes/pictograms/sun.svg',
                  'skins/weewx-wdc/includes/pictograms/moon.svg',
                  'skins/weewx-wdc/includes/icons/cloud-base.svg',
                  'skins/weewx-wdc/includes/icons/dew-point.svg',
                  'skins/weewx-wdc/includes/icons/ev.svg',
                  'skins/weewx-wdc/includes/icons/feel-temp.svg',
                  'skins/weewx-wdc/includes/icons/heat.svg',
                  'skins/weewx-wdc/includes/icons/humidity.svg',
                  'skins/weewx-wdc/includes/icons/rain-rate.svg',
                  'skins/weewx-wdc/includes/icons/rain.svg',
                  'skins/weewx-wdc/includes/icons/solar.svg',
                  'skins/weewx-wdc/includes/icons/temp.svg',
                  'skins/weewx-wdc/includes/icons/uv.svg',
                  'skins/weewx-wdc/includes/icons/wind-chill.svg',
                  'skins/weewx-wdc/includes/icons/wind-direction.svg',
                  'skins/weewx-wdc/includes/icons/wind-gust.svg',
                  'skins/weewx-wdc/includes/icons/wind-speed.svg',
                  'skins/weewx-wdc/includes/icons/sunrise.svg',
                  'skins/weewx-wdc/includes/icons/sunset.svg',
                  'skins/weewx-wdc/includes/icons/moon.svg',
                  'skins/weewx-wdc/includes/icons/moonrise.svg',
                  'skins/weewx-wdc/includes/icons/moonset.svg',
                  'skins/weewx-wdc/includes/icons/github.svg',
                  'skins/weewx-wdc/includes/icons/wdc.svg',
                  'skins/weewx-wdc/includes/icons/forecast/B1.svg',
                  'skins/weewx-wdc/includes/icons/forecast/B2.svg',
                  'skins/weewx-wdc/includes/icons/forecast/BK.svg',
                  'skins/weewx-wdc/includes/icons/forecast/CL.svg',
                  'skins/weewx-wdc/includes/icons/forecast/FW.svg',
                  'skins/weewx-wdc/includes/icons/forecast/OV.svg',
                  'skins/weewx-wdc/includes/icons/forecast/SC.svg',
                  'skins/weewx-wdc/includes/icons/forecast/rain.svg',
                  'skins/weewx-wdc/includes/icons/forecast/snow.svg',
                  ]),
            ]
        )

    # def configure(self, engine):
    #    """Customized configuration that sets a language code"""
    #    # TODO: Set a units code as well
    #    code = engine.get_lang_code('wdc', 'en')
    #    self['config']['StdReport']['WdcReport']['lang'] = code
    #    return True
