"""Times of India News Headlines Dataset"""
import csv
import datasets

_CITATION = '''\\n@inproceedings{Casanueva2020,
    author      = Mulin,
    title       = Holiday Dataset,
    year        = {2022},
    month       = {Mar},
    note        = {},
    url         = {},
    booktitle   = {}
}'''

_DESCRIPTION = """\
This news dataset is a holiday information of singapore from 2017 to 2022.
"""

_DATE = "Date"
_DAY = "Day"
_HOLIDAY = "Holiday"

_HOMEPAGE = ""
_LICENSE = "MIT"

_TRAIN_DOWNLOAD_URL = 'https://raw.githubusercontent.com/ZhangLe59151/sg-dataset/main/holiday/holiday.csv'
_TEST_DOWNLOAD_URL = 'https://raw.githubusercontent.com/ZhangLe59151/sg-dataset/main/holiday/holiday.csv'


class TimesOfHoliday(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.1.0")

    def _info(self):
        features = datasets.Features({_DATE: datasets.Value('string'), _DAY: datasets.Value('string'), _HOLIDAY: datasets.Value('string')})
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        train_path = dl_manager.download_and_extract(_TRAIN_DOWNLOAD_URL)
        test_path = dl_manager.download_and_extract(_TEST_DOWNLOAD_URL)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": train_path}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": test_path})
            ]

    def _generate_examples(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            csv_reader = csv.reader(f, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            next(csv_reader)
            for id_, row in enumerate(csv_reader):
                Date, Day, Holiday = row
                yield id_, {
                    _DATE: str(Date),
                    _DAY: Day,
                    _HOLIDAY: Holiday,
                }

