from ovos_plugin_manager.templates.language import LanguageDetector
from langcodes import standardize_tag
from ovos_plugin_manager.templates.language import LanguageDetector


class FastTextLangDetectPlugin(LanguageDetector):
    """language detector that uses several other plugins and averages their predictions"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
        self.lid = fasttext.load_model(model_path)

    def detect(self, text):
        labels, _ = self.lid.predict(text)
        return standardize_tag(labels[0].split("__label__")[-1])

    def detect_probs(self, text):
        labels, probs = self.lid.predict(text, k=5)
        return {
            standardize_tag(l.split("__label__")[-1]): p
            for l, p in zip(labels, probs)}


if __name__ == "__main__":
    clf = FastTextLangDetectPlugin()
    print(clf.detect("olá mundo"))
    print(clf.detect_probs("olá mundo"))
