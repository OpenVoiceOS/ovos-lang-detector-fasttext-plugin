import os
from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        if 'MYCROFT_LOOSE_REQUIREMENTS' in os.environ:
            print('USING LOOSE REQUIREMENTS!')
            requirements = [r.replace('==', '>=').replace('~=', '>=') for r in requirements]
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]



PLUGIN_ENTRY_POINT = (
    'ovos-lang-detector-fasttext-plugin=ovos_lang_detector_fasttext_plugin:FastTextLangDetectPlugin'
)

setup(
    name='ovos-lang-detector-fasttext-plugin',
    version='0.0.0a2',
    packages=['ovos_lang_detector_fasttext_plugin'],
    url='https://github.com/OpenVoiceOS/ovos-lang-detector-fasttext-plugin',
    license='apache-2',
    author='JarbasAI',
    include_package_data=True,
    install_requires=required("requirements.txt"),
    author_email='jarbasai@mailfence.com',
    description='average plugin classifications for language detection',
    entry_points={'neon.plugin.lang.detect': PLUGIN_ENTRY_POINT}
)
