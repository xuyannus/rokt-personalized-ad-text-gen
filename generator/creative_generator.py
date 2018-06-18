from keyword_extract.extractor_helper import get_user_keywords, get_advertiser_keywords, get_publisher_keywords
import itertools

from utils.data_loader import get_db_connection

MAX_KEYWORD_LEN = 10


def generate_personalized_creatives(user_id, creative_id, memberid):
    db_client = get_db_connection()
    db_client.connect()

    customer_keywords = get_user_keywords(user_id)
    creative_keywords = get_advertiser_keywords(db_client.get_conn(), creative_id)
    publisher_keywords = get_publisher_keywords(memberid)

    keywords = customer_keywords
    keywords.extend(publisher_keywords)

    combinations = []
    solutions = []

    for L in range(1, MAX_KEYWORD_LEN + 1):
        for subset in itertools.combinations(keywords, L):
            combinations.append(subset)

    for keywords in combinations:
        solutions.append(",".join(keywords) + ",".join(creative_keywords))

    return {
        "customer_keywords": customer_keywords,
        "creative_keywords": creative_keywords,
        "publisher_keywords": publisher_keywords,
        "solutions": solutions
    }


def generate_personalized_creative(user_id, creative_id, memberid):
    response = generate_personalized_creatives(user_id, creative_id, memberid)
    return {
        "customer_keywords": response["customer_keywords"],
        "creative_keywords": response["creative_keywords"],
        "publisher_keywords": response["publisher_keywords"],
        "solutions": response["solutions"][0]
    }