TEXT = "text"
INTENT = "intent"
RESPONSE = "response"
ACTION_TEXT = "action_text"

RESPONSE_KEY_ATTRIBUTE = "response_key"

MESSAGE_ACTION_NAME = "action_name"
MESSAGE_INTENT_NAME = "intent_name"

ENTITIES = "entities"
BILOU_ENTITIES = "bilou_entities"
BILOU_ENTITIES_ROLE = "bilou_entities_role"
BILOU_ENTITIES_GROUP = "bilou_entities_group"
NO_ENTITY_TAG = "O"

ENTITY_ATTRIBUTE_TYPE = "entity"
ENTITY_ATTRIBUTE_GROUP = "group"
ENTITY_ATTRIBUTE_ROLE = "role"
ENTITY_ATTRIBUTE_VALUE = "value"
ENTITY_ATTRIBUTE_TEXT = "text"
ENTITY_ATTRIBUTE_START = "start"
ENTITY_ATTRIBUTE_END = "end"
ENTITY_ATTRIBUTE_CONFIDENCE = "confidence"
ENTITY_ATTRIBUTE_CONFIDENCE_TYPE = (
    f"{ENTITY_ATTRIBUTE_CONFIDENCE}_{ENTITY_ATTRIBUTE_TYPE}"
)
ENTITY_ATTRIBUTE_CONFIDENCE_GROUP = (
    f"{ENTITY_ATTRIBUTE_CONFIDENCE}_{ENTITY_ATTRIBUTE_GROUP}"
)
ENTITY_ATTRIBUTE_CONFIDENCE_ROLE = (
    f"{ENTITY_ATTRIBUTE_CONFIDENCE}_{ENTITY_ATTRIBUTE_ROLE}"
)

EXTRACTOR = "extractor"

PRETRAINED_EXTRACTORS = {"DucklingHTTPExtractor", "SpacyEntityExtractor"}
TRAINABLE_EXTRACTORS = {"MitieEntityExtractor", "CRFEntityExtractor", "DIETClassifier"}

NUMBER_OF_SUB_TOKENS = "number_of_sub_tokens"

MESSAGE_ATTRIBUTES = [TEXT, INTENT, RESPONSE]
DENSE_FEATURIZABLE_ATTRIBUTES = [TEXT, RESPONSE]

LANGUAGE_MODEL_DOCS = {
    TEXT: "text_language_model_doc",
    RESPONSE: "response_language_model_doc",
}
SPACY_DOCS = {TEXT: "text_spacy_doc", RESPONSE: "response_spacy_doc"}

TOKENS_NAMES = {
    TEXT: "text_tokens",
    INTENT: "intent_tokens",
    RESPONSE: "response_tokens",
}

TOKENS = "tokens"
TOKEN_IDS = "token_ids"

SEQUENCE_FEATURES = "sequence_features"
SENTENCE_FEATURES = "sentence_features"

RESPONSE_SELECTOR_PROPERTY_NAME = "response_selector"
DEFAULT_OPEN_UTTERANCE_TYPE = "default"
OPEN_UTTERANCE_PREDICTION_KEY = "response"
OPEN_UTTERANCE_RANKING_KEY = "ranking"
RESPONSE_IDENTIFIER_DELIMITER = "/"

FEATURE_TYPE_SENTENCE = "sentence"
FEATURE_TYPE_SEQUENCE = "sequence"
VALID_FEATURE_TYPES = [FEATURE_TYPE_SEQUENCE, FEATURE_TYPE_SENTENCE]

FEATURIZER_CLASS_ALIAS = "alias"

MESSAGE_ACTION_NAME = "action_name"
MESSAGE_INTENT_NAME = "intent_name"
