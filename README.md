# FastText Language Identification

This plugin identifies the language of a text with the [fasttext-language-identification](https://huggingface.co/facebook/fasttext-language-identification) model. Facebook AI Research trained this model as a companion to [NLLB](https://github.com/facebookresearch/fairseq/blob/nllb/README.md#lid-model). The plugin downloads the model from the Hugging Face Hub on first use.

## Install

```bash
pip install ovos-lang-detector-fasttext-plugin
```

## Usage

Set this plugin as the language detection module in `mycroft.conf`:

```javascript
  "language": {
    "detection_module": "ovos-lang-detector-fasttext-plugin"
  },
```

You can also call the plugin directly:

```python
from ovos_lang_detector_fasttext_plugin import FastTextLangDetectPlugin

clf = FastTextLangDetectPlugin()
print(clf.detect("olá mundo"))
print(clf.detect_probs("olá mundo"))
```

`detect` returns the most likely language code. `detect_probs` returns the top 5 language codes with their probabilities.

## Related projects

- [OpenVoiceOS/ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): defines the `LanguageDetector` template this plugin implements.
- [facebookresearch/fairseq](https://github.com/facebookresearch/fairseq/blob/nllb/README.md#lid-model): the NLLB project, source of the underlying language identification model.

## License

Apache-2.0
