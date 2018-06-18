import re
import html

from keyword_extract.extractor_method import KeywordExtract
from utils.data_loader import get_creative_text


def get_user_keywords(user_id):
    if user_id == 1:
        return ["sydney", "programmer", "soccer", "music", "cats", "rokt"]
    return {}


def get_advertiser_keywords(conn, creative_id):
    text = get_creative_text(conn, creative_id)
    text = html.unescape(clean_html(text))
    print(text)

    text_service = KeywordExtract()
    text_service.extract_keywords_from_text(text)
    return text_service.get_ranked_phrases()


def get_publisher_keywords(memberid):
    return []


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
