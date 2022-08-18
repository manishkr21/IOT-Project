import pathlib

DATA_DIR = pathlib.Path("data")

MID_TO_NAME_PATH = DATA_DIR / "mid_to_display_name.tsv"
GOOGLE_AUDIO_DATASETS = [DATA_DIR / x for x in ("audioset_eval_strong.tsv", "audioset_train_strong.tsv")]

CHAINSAW_AUDIO_DIR = DATA_DIR / "chainsaw" / "strong"