# define ers service
namespace php ERS
namespace py ers

/**
 * Const
 */
const i16 DEFAULT_LIST_SIZE = 100
const i16 MAX_LIST_SIZE = 1000
const i16 SORT_TYPE_DESC = 1
const i16 SORT_TYPE_ASC = 2
const i16 FOOD_DEFAULT_STOCK = 1000
const string FOOD_STOCK_CACHE_PREFIX = "food:stock"
const i32 TIYANDIAN_RESTAURANT_ID = 59
const i16 AREA_ALL = -1
const i16 REGION_TYPE_ALL = -1
const i16 AREA_UNGROUPED = -2
const i16 SAAS_TRIAL_DAYS_LIMIT = 15
const string SAAS_LOCK_PREFIX = "lock:saas:"

const i16 USER_ID_SYSTEM = -1
const i16 REGION_CHANGE_TATUS_GEOS_FINISHED = 1
const i16 REGION_CHANGE_TATUS_EOS_FINISHED = 2

const list<i32> EXCLUDE_TEST_RESTAURANT = [59, 11811, 11813, 11814, 25381, 28817, 28820]
const list<i32> INNER_TEST_RESTAURANT = [11811, 11813, 11814, 25381, 28817, 28820]
const list<string> STATUS_NEED_NOTICE = ['is_valid', 'busy_level', 'order_mode']

const string RESTAURANT_ATTR_HALF_PRICE = "half_price"
const string RESTAURANT_ATTR_HALF_PRICE_BACKUP = "half_price_backup"
const string RESTAURANT_ATTR_FREE_ORDER = "free_order"
const string RESTAURANT_ATTR_HUANBAO = "huanbao"
const string RESTAURANT_ATTR_HUANBAO_DOUBLE_POINT = "huanbao_double_point"
const string RESTAURANT_ATTR_COCA = "coca"
const string RESTAURANT_ATTR_DOUBLE_POINT = "double_point"
const string RESTAURANT_ATTR_FAPIAO = "fapiao"
const string RESTAURANT_ATTR_QUAN = "quan"
const string RESTAURANT_ATTR_DISCOUNT8 = "discount8"
const string RESTAURANT_ATTR_ZHUKAO_HALF_PRICE = "zhukao_half_price"
const string RESTAURANT_ATTR_NEW_USER_DISCOUNT = "new_user_discount"
/* TODO may remove new_user_discount_amount */
const string RESTAURANT_ATTR_NEW_USER_DISCOUNT_AMOUNT = "new_user_discount_amount"
const string RESTAURANT_ATTR_NEW_USER_DISCOUNT_RESTAURANT_PAY = "new_user_discount_restaurant_pay"
const string RESTAURANT_ATTR_COUPON_DISCOUNT_RESTAURANT_PAY = "coupon_discount_restaurant_pay"
const string RESTAURANT_ATTR_DISCOUNT_88 = "discount_88"
const string RESTAURANT_ATTR_GUANGZHOU_COCA = "guangzhou_coca"
const string RESTAURANT_ATTR_EXTRA_DISCOUNT = "extra_discount"
const string RESTAURANT_ATTR_SETUP_STEP = "setup_step"
const string RESTAURANT_ATTR_DP_NEW_USER_DISCOUNT = "dp_new_user_discount"
const string RESTAURANT_ATTR_ELEME_BUY_DISCOUNT = "eleme_buy_discount"
const string RESTAURANT_ATTR_MUST_PAY_ONLINE = "must_pay_online"


/**
 * Enums
 */
enum RestaurantConst {
    BUSY_LEVEL_FREE = 0,
    BUSY_LEVEL_CLOSED = 2,
    BUSY_LEVEL_NETWORK_UNSTABLE = 3,
    BUSY_LEVEL_HOLIDAY = 4,

    TOTAL_STATUS_OPEN = 1,
    TOTAL_STATUS_CLOSED = 2,
    TOTAL_STATUS_NETWORK_UNSTABLE = 3,
    TOTAL_STATUS_RESTING = 4,
    TOTAL_STATUS_BOOKONLY = 5,
    TOTAL_STATUS_ORDER_BY_PHONE = 6,
    TOTAL_STATUS_HOLIDAY = 7,

    ORDER_MODE_PHONE = 1,
    ORDER_MODE_ELEME = 2,
    ORDER_MODE_NETWORK = 3,
    ORDER_MODE_NAPOS_WEB = 3,
    ORDER_MODE_WIRELESS_PRINTER = 4,
    ORDER_MODE_TPD = 5,
    ORDER_MODE_OPENAPI = 6,
    ORDER_MODE_TPD_ELEME = 7,
    ORDER_MODE_TPD_NAPOS = 8,
    ORDER_MODE_NAPOS_MOBILE = 9, # deprecated
    ORDER_MODE_NAPOS_MOBILE_ANDROID = 9,
    ORDER_MODE_NAPOS_MOBILE_IOS = 10,

    METHOD_OF_PAYMENT_CASH = 1
    METHOD_OF_PAYMENT_ONLINE = 2

    COME_FROM_OFFLINE = 0,
    COME_FROM_ONLINE = 1,

    SERVICE_CATEGORY_A = 1,
    SERVICE_CATEGORY_B = 2,
    SERVICE_CATEGORY_C = 3,

    DOCK_CORP_ELEME_DELIVERY = 7,

    CERTIFICATION_TYPE_PERSONAL = 1,
    CERTIFICATION_TYPE_CORP = 2,
}

enum RestaurantMessageConst {
    TYPE_OTHER = 0,
    TYPE_BINDCARD_APPROVE = 1,
    TYPE_BINDCARD_REJECT = 2,
    TYPE_WITHDRAW_FAIL = 3,
}

enum ActivityConst {
    MIDDLE = 0,
    BANNER = 1,

    NO_INFO = 0,
    WITH_LINK = 1,
    WITH_PAGE = 2,
}

enum DeviceRestaurantConst {
    DEVICE_TYPE_IOS = 1
    DEVICE_TYPE_ANDROID = 2
}

enum RestaurantActivityConst {
    TYPE_COUPON = 3,
    TYPE_NEW_USER_DISCOUNT = 7,
    TYPE_EXTRA_DISCOUNT = 100,
    TYPE_OLPAYMENT_REDUCE = 101,
    TYPE_ADVANCED_DISCOUNT = 102,
    TYPE_NEW_USER_DISCOUNT_EXCLUSIVE = 103,
    TYPE_ORDER_HONGBAO = 104,
    TYPE_JINBAO = 105,

    STATUS_TYPE_NO_CONTRACT = 1,
    STATUS_TYPE_CONTRACT_PROCESSING = 2,
    STATUS_TYPE_CONTRACT_NOTSET = 3,
    STATUS_TYPE_PARTICIPATED = 4,
}

enum SubsidyConst {
    CATEGORY_RESTAURANT_ACTIVITY = 12,
    CATEGORY_FOOD_ACTIVITY = 11,

    ACTIVITY_COUPON = 3,
    ACTIVITY_NEW_USER_DISCOUNT = 7,
    ACTIVITY_EXTRA_DISCOUNT = 100,
    ACTIVITY_OLPAYMENT_REDUCE = 101,
    ACTIVITY_ADVANCED_DISCOUNT = 102,
    ACTIVITY_NEW_USER_DISCOUNT_EXCLUSIVE= 103,
}

enum SubsidyContractStatus {
    UNCENSORED = 0,
    APPROVED = 1,
    REJECTED = 2,
    SUBSTITUTED = 3,
    REFUSED = 4,
    SIGNED = 5,
}

enum AppVersionConst {
    ANDROID_ELEME = 1,
    IOS_ELEME = 2,
    ANDROID_NAPOS = 3,
}

enum TGarnishCategoryKind {
    REQUIRED = 0,
    OPTIONAL = 1,
}

enum TFoodUgcImageReportConst {
    STATUS_UNPROCESSED = 1,
    STATUS_PROCESSED = 2,
}

enum TOrderMode {
    PHONE = 1,
    ELEME = 2,
    NETWORK = 3,
    WIRELESS = 4,
}

enum FreeGiftActivityCategory {
    FREE_GIFT = 1,
    PACKAGE_GIFT = 2,
    NO_GIFT = 3,
}

enum SaasConst {
    TRIAL_ORDER_AMOUNT = 300,
    TRIAL_ORDER_COUNT = 10,

    TRIAL_DAYS = 15,

    STATUS_SUSPEND = 0,
    STATUS_FREE = 1,
    STATUS_TRIAL = 2,
    STATUS_PAY = 3,
    STATUS_TEMP_FREE = 4,

    CHANGE_ATTR_REMAINS = 1,
    CHANGE_ATTR_RANKING = 2,

    CHANGE_TYPE_LOGIN = 1,
    CHANGE_TYPE_ORDER = 2,
    CHANGE_TYPE_CUSTOM = 11,
    CHANGE_TYPE_TRIAL = 12,
    CHANGE_TYPE_CONTRACT_RECHARGE = 13,
    CHANGE_TYPE_CONTRACT_ABANDON = 14,
}

enum SaasContractRecordConst {
    STATUS_ABANDON = 0,
    STATUS_NEW = 1,
    STATUS_NORMAL = 2,
    STATUS_ARCHIVED = -1,

    CONTRACT_TYPE_NEW = 1,
    CONTRACT_TYPE_UPGRADE = 2,
    CONTRACT_TYPE_RENEW = 3,

    PLAN_TYPE_NORMAL = 1,
    PLAN_TYPE_RANKING = 2,

    PAYMENT_TYPE_CASH = 1,
    PAYMENT_TYPE_ELEME_ONLINE = 3,

    INCOME_STATUS_UNREC = 0,
    INCOME_STATUS_REC = 1,

    PLAN_SELECT_LEVEL_ALL = 0,
    PLAN_SELECT_LEVEL_INTERNAL = 1,
}

enum SaasContractComboConst {
    STATUS_STOP = 0,
    STATUS_NEW = 1,
    STATUS_IN_PROGRESS = 2,
    STATUS_ACOMPLISHED = 3,
    STATUS_ABANDON = -1,

    INCOME_STATUS_NEW = 0,
    INCOME_STATUS_STEP_1 = 1,
    INCOME_STATUS_STEP_2 = 2,
    INCOME_STATUS_STEP_3 = 3,

    INCOME_PERCENTAGE_1 = 30,
    INCOME_PERCENTAGE_2 = 30,
    INCOME_PERCENTAGE_3 = 40,

    COMBO_TYPE_A = 1,
    COMBO_TYPE_B = 2,
    COMBO_TYPE_C = 3,

    COMBO_BASIC_SAAS_DURATION = 720,
    COMBO_BASIC_SAAS_PRICE = 9640,
    COMBO_C_SAAS_PRICE = 8194,

    COMBO_A_RANKING_DURATION = 270,
    COMBO_B_RANKING_DURATION = 0,
    COMBO_C_RANKING_DURATION = 0,
}

enum OperationRemindConst {
    STATUS_UNPROCESSED = 0
    STATUS_PROCESSED = 1
}

enum RestaurantOpenApplyConst {
    STATUS_UNPROCESSED = 1
    STATUS_PASSED = 2
    STATUS_REJECT = 3
    STATUS_PROCESSING = 4
}

enum OnlinePaymentApplyConst {
    STATUS_INVALID = -1
    STATUS_UNPROCESSED = 0
    STATUS_APPROVE = 1
}

enum RestaurantSetupStepConst {
    NEW_RST = 0,
    START_INFO = 1,
    BIND_PHONE = 2,
    MENU = 3,
    ORDER_MODE = 4,
    FINISHED = 5
}


/**
 * Types and Structs
 */
typedef i64 Geohash
typedef i64 Timestamp
typedef string Mobile
typedef string Json
typedef map<i32, i32> FoodStockMap

enum CertificationType {
    TYPE_PERSONAL = 1,
    TYPE_CORP = 2,
}

enum CertificationConst {
    STATUS_PENDING = 0,
    STATUS_PASSED = 1,
    STATUS_FAILED = -1,
}

struct TCRegionMap {
    1: required i32 city_id,
    2: required i32 region_group_id,
    3: required i32 region_id,
}

struct TRestaurantCertification {
    1: required i32 restaurant_id,
    2: optional string person_name,
    3: optional string identity_card_no,
    4: optional string identity_card_image_front,
    5: optional string identity_card_image_front_wm,
    6: optional string identity_card_image_back,
    7: optional string identity_card_image_back_wm,
    8: optional string health_card_image_front,
    9: optional string health_card_image_front_wm,
    10: optional string health_card_image_back,
    11: optional string health_card_image_back_wm,

    12: optional string corp_name,
    13: optional string license_no,
    14: optional string license_location,
    15: optional string license_expire_date,
    16: optional string license_image,
    17: optional string license_image_wm,
    18: optional string restaurant_service_license_copy,
    19: optional string restaurant_service_license_copy_wm,

    20: required i16 type,
    21: optional i16 status,
    22: optional string comment,
    23: optional Timestamp created_at,
    24: optional Timestamp updated_at,
}

struct TRestaurantCertificationQuery {
    1: required list<i32> restaurant_ids,
    2: required i16 type,
    3: optional i16 status,
    4: optional i32 offset,
    5: optional i32 limit,
    6: optional i32 from_timestamp,
    7: optional i32 to_timestamp
}

struct TAmendedPoi {
    1: required i32 id,
    2: required string name,
    3: required string address,
    4: required string extra_tag,
    5: required i32 city_id,
    6: required double latitude,
    7: required double longitude,
    8: optional Timestamp created_at,
    9: optional string pguid,
}

struct TAppCampaign {
    1: required i32 id,
    2: required string sn,
    3: required string description,
    4: required string iphone_link,
    5: required string android_link,
    6: optional Timestamp created_at,
}

struct TChangelogRestaurant {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string field_name,
    4: optional string from_value,
    5: optional string to_value,
    6: required i32 by_user_id,
    7: optional Timestamp created_at,
}

struct TChangelogRegion {
    1: required i32 id,
    2: required i32 region_id,
    3: required string field_name,
    4: optional string from_value,
    5: optional string to_value,
    6: required i32 by_user_id,
    7: optional Timestamp created_at,
    8: optional i16 status,
}

struct TDeletelogRegion {
    1: required i32 id,
    2: required i32 region_id,
    3: required i32 by_user_id,
    4: optional Timestamp created_at,
    5: optional i16 status,
}

struct TDeviceRestaurant {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional string device_id,
    4: optional i16 device_type,
    5: optional string eleme_guid,
    6: optional string version,
    7: optional Timestamp created_at,
}

struct TDeviceRestaurantQuery {
    1: optional string device_id,
    2: optional i32 restaurant_id,
    3: optional i16 device_type,
    4: optional i32 offset,
    5: optional i32 limit,
    6: optional list<i32> restaurant_ids,
    7: optional map<i32, string> device_from_version,
}

struct TZone {
    1: optional i32 id,
    2: optional string name,
    3: optional i32 district_id,
    4: optional i32 city_id,
    5: optional i32 sort,
    6: optional i16 is_valid,
    7: optional Timestamp created_at,
    8: optional i16 need_az_group,
}

struct TRestaurant {
    1: required i32 id,
    2: required i16 is_valid,
    3: required i16 agent_fee,
    4: required i16 busy_level,
    5: required string name,
    6: optional double latitude,
    7: optional double longitude,
    8: required string description,
    9: optional string address_text,

    # deliver_amount is the max of
    # (entry_restaurant.deliver_amount, restaurant.min_deliver_amount)
    # if query by entry_id else restaurant.min_deliver_amount
    10: optional i16 deliver_amount,
    # TODO deprecated
    11: optional i16 total_status,
    # db new columns
    12: required string wireless_printer_esn,
    13: required bool support_online,
    14: required string open_time_bitmap,
    15: required string book_time_bitmap,

    16: required string deliver_description,
    17: required i16 num_rating_1,
    18: required i16 num_rating_2,
    19: required i16 num_rating_3,
    20: required i16 num_rating_4,
    21: required i16 num_rating_5,
    22: required Timestamp created_at,
    23: optional string image_url,
    24: required string image_hash,
    25: optional string phone,
    26: required Mobile mobile,
    27: required i16 order_mode,
    28: optional string promotion_info,
    29: required i16 one_delivery,
    30: optional string pinyin_name,
    31: required string name_for_url,
    32: required i16 min_deliver_amount,
    33: optional string close_description,
    34: required i16 is_saas,
    35: optional string header_image_url,
    36: required i16 waimai_num_print_copies,
    37: required i16 tangchi_num_print_copies,
    38: required string printer_version,
    39: optional i16 sn,
    40: required i16 deliver_radius,
    41: optional double min_lng,
    42: optional double max_lng,
    43: optional double min_lat,
    44: optional double max_lat,
    45: required i16 is_bookable,
    46: required string flavors,
    47: required i16 dine_enabled,
    48: optional i16 deliver_spent,
    49: required i16 is_time_ensure,
    50: optional string time_ensure_description,
    # TODO deprecated
    51: optional Timestamp time_ensure_at,
    52: optional i16 time_ensure_spent,
    53: optional string time_ensure_discount,
    54: required i16 city_id,
    55: required i16 is_phone_hidden,
    # TODO deprecated
    56: required i16 coupon_enabled,
    # TODO deprecated
    57: optional Timestamp coupon_start_at,
    # TODO deprecated
    58: optional Timestamp coupon_end_at,
    # TODO deprecated
    59: optional i32 coupon_number,
    60: optional i16 coupon_discount,
    61: required string paper_width,
    62: required i16 auto_print_tangchi,
    63: required double speed_coef1,
    64: required double speed_coef2,
    65: required double speed_coef3,
    66: required double avg_comment_time,
    68: required string activities,
    69: required i16 has_food_img,
    70: required i16 online_payment,
    71: required i16 invoice,
    72: required double invoice_min_amount,
    73: required string attribute,
    # TODO deprecated
    74: required string deliver_area,
    75: optional string open_date,
    76: required double original_order_quantity,
    77: required string keeper_name,
    78: required string keeper_phone,
    79: required string remark,
    80: required string corporation,
    81: required i32 geohash_ranking_weight,

    # serving_time like [('08:00:00', '23:00:00')]
    82: optional list<list<string>> serving_time,

    # num_ratings represents num_rating 1-5
    # [num_rating_1, num_rating2, ...]
    83: optional list<i16> num_ratings,

    84: required i32 recent_food_popularity,
    85: required i16 is_premium,

    # TODO deprecated, use book_time_bitmap instead
    86: optional list<string> deliver_times,

    # napos client settings [json]
    87: required string napos_client_settings,
    88: required string keeper_identity_card,

    89: optional bool support_coupon,
    90: optional string time_ensure_full_description,
    91: required i32 come_from,
    92: required i32 no_agent_fee_total,
    93: required i32 service_category,
    94: required i32 dock_corp_id,
    95: optional string deliver_geojson,

    96: required double service_rating,
    97: required i32 recent_order_num,
    98: required i32 has_activity,
    99: optional i16 certification_type,
    100: required i32 oid,
    101: optional i16 method_of_payment,
}

struct TRestaurantRate {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required i32 num_service_rating_1,
    4: required i32 num_service_rating_2,
    5: required i32 num_service_rating_3,
    6: required i32 num_service_rating_4,
    7: required i32 num_service_rating_5,
}

struct TRestaurantEvaluation {
    1: optional i32 id,
    2: optional double recent_daily_sales,
    3: optional double recent_daily_order_num,
    4: optional double recent_daily_sales_trend,
    5: optional double recent_daily_order_num_trend,
}

struct TRestaurantSearchQuery {
    1: required string keyword,
    2: optional list<i32> restaurant_ids,
    3: optional list<i32> city_ids,
    4: optional i32 offset,
    5: optional i32 size
}

struct TRestaurantAreaSearchQuery {
    1: required double latitude,
    2: required double longitude,
    4: required string keyword,
    5: optional i32 offset,
    6: optional i32 size
}

struct TRestaurantAreaSearchCountQuery {
    1: required double latitude,
    2: required double longitude,
    3: required string keyword,
    4: required bool is_inside,
}

struct TRestaurantCertificationSearchQuery {
    1: required i32 status,
    2: optional i32 offset,
    3: optional i32 size
}

struct TRestaurantSearchFilterQuery {
    1: required string keyword,
    2: optional list<i32> restaurant_ids,
    3: optional list<i32> city_ids,
    4: optional i32 is_valid,
    5: optional i32 is_premium,
    6: optional i32 has_image,
    7: optional i32 certification_status,
    8: optional i32 online_payment,
    9: optional i32 order_mode,
    10: optional i32 busy_level,
    11: optional i32 region_type,
    12: optional list<i32> region_group_ids,
    13: optional list<i32> region_ids,
    14: optional i32 has_activity,
    15: optional list<i32> saas_statuses,
    16: optional bool has_dianping_id,
    17: optional string order_by_id,
    18: optional i32 offset,
    19: optional i32 size,
    20: optional string address_text,
    21: optional i32 eat_in_restaurant,
    22: optional i32 license_image,
    23: optional i32 identity_card_image_front,
    24: optional i32 restaurant_service_license_copy,
    25: optional i32 dist_edu_enabled,
}

# lean restaurant struct for performance concern
struct TLeanRestaurant {
    1: required i32 id,
    2: required i16 is_valid,
    3: required i16 agent_fee,
    4: required i16 busy_level,
    5: required string name,
    6: required string description,
    7: optional string address_text,

    # deliver_amount is the max of
    # (entry_restaurant.deliver_amount, restaurant.min_deliver_amount)
    # if query by entry_id else restaurant.min_deliver_amount
    8: optional i16 deliver_amount,
    # TODO deprecated
    9: optional i16 total_status,
    # db new columns
    10: required bool support_online,
    11: required string open_time_bitmap,
    12: required string book_time_bitmap,

    13: required string deliver_description,
    14: required string image_hash,
    15: optional string phone,
    16: required Mobile mobile,
    17: required i16 order_mode,
    18: optional string promotion_info,
    19: optional string pinyin_name,
    20: required string name_for_url,
    21: optional string close_description,
    22: required i16 is_bookable,
    23: required string flavors,
    24: optional i16 deliver_spent,
    25: required i16 is_time_ensure,
    26: optional string time_ensure_full_description,
    27: required i16 city_id,
    28: required i16 is_phone_hidden,
    29: optional bool support_coupon,
    30: optional i16 coupon_discount,
    31: required double speed_coef1,
    32: required double speed_coef2,
    33: required double speed_coef3,
    34: required i16 online_payment,
    35: required i16 invoice,
    36: required double invoice_min_amount,
    37: required string attribute,

    # num_ratings represents num_rating 1-5
    # [num_rating_1, num_rating2, ...]
    38: optional list<i16> num_ratings,

    39: required i16 is_premium,

    40: optional double latitude,
    41: optional double longitude,
    42: optional i32 recent_food_popularity,
    43: required Timestamp created_at,
}

struct TRestaurantBankcard {
    1: required i32 restaurant_id,
    2: required string card_id,
    3: required i16 bank_id,
    4: required string branch_name,
    5: required string cardholder_name,
}

struct TCBankcard {
    1: required string card_id,
    2: required i16 bank_id,
    3: required string cardholder_name,
}

struct TFavoredRestaurant {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required Timestamp created_at,
    4: required i32 user_id,
    5: required i32 weight,
}

struct TFood {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string name,
    4: required double original_price,
    5: required double price,
    6: required i16 is_valid,
    7: optional string image_url,
    8: required string image_hash,
    9: optional string description,
    10: required i16 num_rating_1,
    11: required i16 num_rating_2,
    12: required i16 num_rating_3,
    13: required i16 num_rating_4,
    14: required i16 num_rating_5,
    16: required string attribute,
    17: optional Timestamp created_at,
    18: optional i32 category_id,
    19: optional Timestamp updated_at,
    20: optional string pinyin_name,
    21: required i16 is_new,
    22: required i16 is_featured,
    23: required i16 is_gum,
    24: required i16 is_spicy,
    25: required string sn,
    26: required i32 recent_popularity,
    27: required double recent_rating,
    29: required i32 stock,
    30: required i32 max_stock,
    31: required bool daily_reset,
    32: optional Timestamp price_changed_at,
    33: required i16 has_activity,
    34: optional double packing_fee,
    35: optional i32 sort_order,
    36: optional Timestamp removed_at
}

struct TFoodSearchQuery {
    1: required string keyword,
    2: optional list<i32> restaurant_ids,
    3: optional list<i32> city_ids,
    4: optional i32 offset,
    5: optional i32 size
}

struct TFoodCategory {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string name,
    4: required i32 weight,
    5: required i16 is_valid,
    # TODO deprecated, use attribute_list instead
    6: required string attributes,
    7: required Timestamp created_at,
    8: optional list<string> attribute_list,
    9: required string description,
    10: optional Timestamp removed_at
}

struct TFoodFlavor {
    1: required i32 id,
    2: required i32 food_id,
    3: required i32 food_category_id,
    4: required i32 restaurant_id,
    5: required string flavor_name,
    6: required i32 flavor_id,
}

struct TRestaurantFlavor {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string flavor_name,
    4: required i32 flavor_id,
    5: required i16 is_manually,
}

struct TFoodUgcImage {
    1: required i32 id,
    2: required i32 food_id,
    3: required string food_name,
    4: required i32 restaurant_id,
    5: required string image_hash,
    6: required i32 user_id,
    7: required string user_name,
    8: required string avatar_hash,
    9: required i32 order_item_id,
    10: required i16 status,
    11: required Timestamp created_at,
    12: required string sn,
    13: required i16 come_from,
    14: required i32 like_count,
}

struct TFoodUgcImageQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string keyword,
    4: optional list<i32> food_ids,
    5: optional list<i32> restaurant_ids,
    6: optional list<i32> user_ids,
    7: optional list<i32> statuses,
    8: optional list<i32> order_item_ids,
    9: optional Timestamp created_at_from,
    10: optional Timestamp created_at_to,
    11: optional i16 come_from,
}

struct TFoodUgcImageCover {
    1: required i32 id,
    2: required i32 food_id,
    3: required i32 restaurant_id,
    4: required i32 count,
    5: required Timestamp cover_update,
    6: required string cover_image_hash,
    7: required i32 cover_user_id,
    8: required string cover_user_name,
    9: required string cover_avatar_hash,
    10: required i16 is_valid,
    11: optional i32 food_ugc_image_id,
    12: optional i32 order_item_id,
}

struct TFoodUgcImageCoverQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string keyword,
    4: optional list<i32> food_ids,
    5: optional list<i32> restaurant_ids,
}

struct TFoodUgcImagePr {
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 food_ugc_image_id,
    4: required i16 from_status,
    5: required i16 to_status,
    6: required string remark,
    7: required Timestamp created_at,
}

struct TFriendLinkQuery {
    1: optional string name,
    2: optional i16 is_valid,
    3: optional i32 offset,
    4: optional i32 limit,
}

struct TFriendLink {
    1: optional i32 id,
    2: optional i32 weight,
    3: optional string link,
    4: optional string name,
    5: optional i16 is_valid,
}

struct TQuickMessageQuery {
    1: optional string title,
    2: optional string content,
    3: optional string search,
    4: optional i32 offset,
    5: optional i32 limit,
}

struct TQuickMessage {
    1: optional i32 id,
    2: optional string title,
    3: optional string content,
}

struct TCFoodCategoryWithFoods {
    1:required TFoodCategory food_category,
    2:required list<TFood> foods,
}

struct TGarnishCategory {
    1: required i32 id,
    2: required string name,
    3: required TGarnishCategoryKind kind,
    4: required i32 rst_id,
    5: required bool is_valid,
}

struct TGarnish {
    1: required i32 id,
    2: required i32 category_id,
    3: required string name,
    4: required double price,
    5: required i16 weight,
    6: required bool is_valid,
}

struct TFoodGarnishCategory {
    1: required i32 id,
    2: required i32 food_id,
    3: required i32 garnish_category_id,
    4: required i32 weight,
}


struct TEntry {
    1: required i32 id,
    2: required string sn,
    3: required string name,
    4: required string pinyin,
    5: required string address,
    6: required double latitude,
    7: required double longitude,
    9: required i16 mobile_reserved,
    10: required i32 city_id,
    11: required i16 is_rsts_cached,
    12: optional Timestamp created_at,
    13: required i32 district_id,
    14: required i32 zone_id,
    15: required i32 sort,
    16: required i16 is_valid,
    17: required string search,
    18: required string extra_tag,
    19: required i16 online_payment,
    20: required Geohash to_geohash,
    21: required i16 migrate_status,
    22: required string psn,
}

struct TRegion {
    1: required i32 id,
    2: required string name,
    3: required i32 type_code,
    4: required i32 has_geohash,
    5: required string color,
    6: required string area,
    7: required i32 city_id,
    8: required Timestamp created_at,
}

struct TArea {
    1: required i32 id,
    2: required string name,
    3: required i32 type_code,
    4: required string boundary,
    5: required double latitude,
    6: required double longitude,
    7: required i32 city_id,
    8: required Timestamp created_at,
}

struct TRegionGroup {
    1: required i32 id,
    2: required string name,
    3: i32 city_id,
}

struct TCity {
    1: required i32 id,
    2: required string name,
    3: required string abbr,
    4: required string hint,
    5: required string area_code,
    6: required string company_name,
    7: required string company_address,
    8: required i32 sort,
    9: required string notice_emails,
    10: required i16 is_valid,
    11: required i32 district_code,
    12: required string boundary,
    13: required double latitude,
    14: required double longitude,
    15: required string company_abbr,
    16: required i32 country_region_id,
    17: required i16 is_map,
    18: required string pinyin,
}

struct TCountryRegion {
    1: required i32 id,
    2: required string name,
    3: required i32 sort,
    4: required i32 is_valid,
}

struct TCountryRegionQuery {
    1: optional i32 is_valid,
    2: optional i32 offset,
    3: optional i32 limit,
}

struct TDistrict {
    1: optional i32 id,
    2: optional string name,
    3: optional i32 city_id,
    4: optional i32 sort,
    5: optional i16 is_valid,
    6: optional Timestamp created_at,
    7: optional string attributes,
    8: optional i16 need_az_group,
}

struct TDirectStruct {
    1: optional list<i32> city_ids,
    2: optional list<i32> region_group_ids,
    3: optional list<i32> region_ids,
}

struct TFreeGiftActivity {
    1: required i32 id,
    2: required string name,
    3: required string desc,
    4: required string attribute_name,
    5: required string image_hash,
    6: required string icon_hash,
    7: required string gift_name,
    8: required string unit_name,
    9: required i16 category_id,
    10: required i32 entity_category_id,
    11: required i32 entity_id,
    12: required i16 is_valid,
    13: required bool show_in_filter,
    14: required bool has_gift,
    15: required string icon_name,
}

struct TActivity {
    1: required i32 id,
    2: required string sn,
    3: required string description,
    4: required string image,
    5: required string image_hash,
    6: required string link,
    7: required i32 sort,
    8: required Timestamp created_at,
    9: required string start_date,
    10: required string end_date,
    11: required bool is_valid,
    12: required string selected_cities,
    13: required string selected_regions,
    14: required string selected_region_groups,
    16: required i16 type,
    17: required string weekday,
    18: required string act_intro,
    19: required string act_how,
    20: required string act_scope,
    21: required string act_time,
    22: required string act_notice,
    23: required string act_image,
    24: required string act_image_hash,
    25: required i32 has_info,
    26: required bool is_default,
    27: required string mobile_image_hash,
    28: required string mobile_intro,
    29: required string mobile_link,
}

struct TLogo {
    1: required i32 id,
    2: required string name,
    3: required string start_date,
    4: required string end_date,
    5: required string small_logo,
    6: required string small_logo_hash,
    7: required string big_logo,
    8: required string big_logo_hash,
    9: required bool is_valid,
}

struct TRestaurantComment {
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 restaurant_id,
    4: required string username,
    5: required Timestamp created_at,
    6: required string content,
    7: required i16 is_valid,
    8: required i32 feedback_id,
    9: required string avatar,
}

struct TRestaurantCommentReply {
    1: required i32 id,
    2: required i32 comment_id,
    3: required i32 user_id,
    4: required Timestamp created_at,
    5: required string content,
    6: required i32 type,
    7: required i16 is_valid,
}

struct TWalleCommentReplyQuery {
    1: optional i16 is_valid,
    2: optional string search,
    3: optional i32 offset,
    4: optional i32 limit,
}

struct TCWalleCommentReply {
    1: required i32 id,
    2: required i32 comment_id,
    3: required i32 user_id,
    4: required Timestamp created_at,
    5: required string content,
    6: required i32 type,
    7: required i16 is_valid,
    8: required string username,
    9: required string comment_content,
}

struct TCWalleRestaurantChangeRecord {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string restaurant_name,
    4: required string status_name,
    5: required i32 from_status,
    6: required i32 to_status,
    7: required string remark,
    8: required i32 user_id,
    9: required Timestamp created_at,

    10: required string description,
    11: required string username,
}

struct TDockCorp {
    1: required i32 id,
    2: required i32 app_id,
    3: required string name,
    4: required string phone,
    5: required string description,
    6: required i16 corp_type,
}

struct TDockCorpRestaurant {
    1: required i32 id,
    2: required i32 corp_id,
    3: required i32 restaurant_id,
}

struct TDockCorpQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string keyword,
    4: optional i16 corp_type,
}

struct TRestaurantActivityQuery {
    1: optional list<i32> city_ids,
    2: optional string begin_date,
    3: optional string end_date,
    4: optional i16 offset,
    5: optional i16 limit,
}

struct TRestaurantActivity {
    1: optional i32 id,
    2: optional i32 city_id,
    3: optional i16 type,
    4: optional string attribute,
    5: optional string begin_date,
    6: optional string end_date,
    7: optional double default_subsidy,
    8: optional Timestamp created_at,
    9: optional string description,
    10: optional string default_complex_subsidy
}

struct TFoodActivity {
    1: required i32 id,
    2: required string name,
    3: required string icon_name,
    4: required i16 is_valid,
    5: required string icon_hash,
    6: required string image_hash,
    7: required string description,
    8: required string begin_date,
    9: required string end_date,
    10: required string city_id,
    11: required i16 can_always_buy,
    12: optional string weekday,
    13: optional string begin_time,
    14: optional string end_time,
    15: required i16 quantity_condition,
    16: required i16 sum_condition,
    17: required double discount,
    18: required double nth_discount,
    19: required double reduce_amount,
    20: optional string gift_name,
    21: required Timestamp created_at,
    22: required i16 max_quantity,
    23: required i16 must_pay_online,
    24: required i16 invalid_food_after_expiration,
    25: required i16 compatible_with_coupon,
    26: required i16 max_sum,
    27: required double default_subsidy,
    28: optional string image_text,
    29: optional string image_text_color,
    30: required double fixed_price,
    31: required i16 must_new_user,
}

struct TFoodActivityQuery {
    1: optional list<i32> restaurant_ids,
    2: optional list<i32> city_ids,
    3: optional string begin_date,
    4: optional string end_date,
    5: optional bool is_valid,
    6: optional string keyword,
    7: optional list<i32> weekday,
    8: optional i32 limit,
    9: optional i32 offset,
}


struct TActivitySubsidyContractQuery {
    1: optional list<i32> city_ids,
    2: optional list<i32> restaurant_ids,
    3: optional i32 activity_id,
    4: optional i32 activity_category_id,
    5: optional list<i16> statuses,
    6: optional Timestamp created_at_from,
    7: optional i32 offset,
    8: optional i32 limit
}

struct TActivitySubsidyContract {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional i32 activity_id,
    4: optional i32 activity_category_id,
    5: optional i16 city_id,
    6: optional double amount,
    7: optional i32 submit_user_id,
    8: optional i16 status,
    9: optional Timestamp created_at,
    10: optional Timestamp signed_at,
    11: optional Timestamp expired_at,
    12: optional string complex_subsidy,
}


struct TRestaurantOpenApply {
    1: required i32 id,
    2: required i32 user_id,
    3: required string applicant,
    4: required string telephone,
    5: required string mobilephone,
    6: required string qq,
    7: required i16 city_id,
    8: required i64 geohash,
    9: required i32 entry_id,
    10: required string restaurant_name,
    11: required string restaurant_address,
    12: required string restaurant_description,
    13: required string restaurant_url,
    14: required i16 status,
    15: required Timestamp created_at,
}

struct TRestaurantPromotion {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string content,
    4: required i16 is_valid,
    5: required Timestamp created_at,
    6: required Timestamp deadline,
}

struct TSeoSmCityIndex {
    1: optional i32 id,
    2: optional i32 city_id,
    3: optional i32 category_id,
    4: optional string all_indexes,
}

struct TSeoSmIndex {
    1: optional i32 id,
    2: optional string name,
    3: optional i32 sort_weight,
}

struct TRestaurantOpenApplyQuery {
    1: optional i32 user_id,
    2: optional list<i16> city_ids,
    3: optional i16 status,
    4: optional Timestamp created_at_start,
    5: optional Timestamp created_at_end,
    6: optional string applicant,
    7: optional string telephone,
    8: optional string mobilephone,
    9: optional string restaurant_name,
    10:optional i32 offset,
    11:optional i32 limit,
}

struct TSeoSmPlace {
    1: optional i32 id,
    2: optional i32 index_id,
    3: optional i32 city_id,
    4: optional string name,
    5: optional string address,
    6: optional i64 place_id,
    7: optional string sn,
}

struct TSeoSmRestaurant {
    1: optional i32 id,
    2: optional i32 index_id,
    3: optional i32 city_id,
    4: optional string name,
    5: optional string address,
    6: optional string name_for_url,
}

struct TRestaurantCommentQuery {
    1: optional Timestamp from_datetime,
    2: optional Timestamp to_datetime,
    3: optional list<i32> exc_restaurant_ids,
    4: optional list<i32> restaurant_ids,
    5: optional i32 offset,
    6: optional i32 limit,
    7: optional i32 comment_id,
    8: optional i16 is_valid,
    9: optional i32 user_id,
}

struct TCWalleRestaurantComment {
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 restaurant_id,
    4: required string username,
    5: required Timestamp created_at,
    6: required string content,
    7: required i16 is_valid,
    8: required i16 is_replied,
    9: required string restaurant_name,
}

struct TWalleRestaurantCommentQuery {
    1: optional i16 is_valid,
    2: optional i16 is_replied,
    3: optional string search,

    4: optional i32 offset,
    5: optional i32 limit,
}

struct TFreeGiftActivityQuery {
    1: optional i32 category_id,
    2: optional bool is_valid,
    3: optional i32 offset,
    4: optional i32 limit,
}

struct TActivityQuery {
    1: optional bool is_valid,
    2: optional bool is_default,
    3: optional string type,
    4: optional string sort,
    5: optional string start_date,
    6: optional string end_date,
    7: optional i32 offset,
    8: optional i32 limit,
    9: optional string keyword,

    10: optional i32 has_info,
    11: optional string weekday,
    12: optional Geohash geohash,
}

struct TCityQuery {
    1: optional bool is_valid,
    2: optional i32 offset,
    3: optional i32 limit,
}

struct TLogoQuery {
    1: optional bool is_valid,
    2: optional i32 offset,
    3: optional i32 limit,
    4: optional string keyword,
}

struct TSeoSmCityIndexQuery {
    1: optional i32 city_id,
    2: optional i32 category_id,
}

struct TSeoSmQuery {
    1: optional i32 index_id,
    2: optional i32 city_id,
    3: optional i32 offset,
    4: optional i32 limit,
}

typedef list<string> QueryFields
typedef list<TRestaurant> TRestaurantList

struct TFoodQuery {
    1: optional i32 restaurant_id,
    2: optional i32 category_id,
    3: optional bool is_valid,
    4: optional i32 limit,
    5: optional i32 offset,
    6: optional string keyword,
}

# deprecated, use mset_food_stock_by_category instead
struct TFoodStock {
    1: optional i32 restaurant_id,
    2: optional i32 category_id,
    3: optional bool is_max,
}

struct TFoodCategoryQuery {
    1: optional i32 restaurant_id,
    2: optional bool is_valid,
    3: optional i32 limit,
    4: optional i32 offset,
}

struct TFoodGarnishCategoryQuery {
    1: optional i32 food_id,
    2: optional i32 garnish_category_id,
    3: optional i32 limit,
    4: optional i32 offset,
}

struct TGarnishQuery {
    1: optional i32 category_id,
    2: optional bool is_valid,
    3: optional i32 limit,
    4: optional i32 offset,
}

struct TGarnishCategoryQuery {
    1: optional i32 restaurant_id,
    2: optional TGarnishCategoryKind kind,
    3: optional bool is_valid,
    4: optional i32 limit,
    5: optional i32 offset,
}

struct TRestaurantQuery {
    1: optional string address,
    2: optional string mobile,
    3: optional string name,
    4: optional string phone,
    5: optional i16 busy_level,
    6: optional i16 order_mode,
    7: optional bool allow_ol_payment,
    8: optional bool has_deliver_area,
    9: optional bool has_food_img,
    10: optional bool has_image_hash,
    11: optional bool is_coupon,
    12: optional bool is_recommend,
    13: optional bool is_premium,
    14: optional bool is_valid,
    15: list<i32> city_ids,
    16: list<i32> region_ids,
    17: list<i32> managed_city_ids,
    18: list<i32> managed_region_ids,
    19: optional i32 offset,
    20: optional i32 limit,
    21: optional string keyword,
    22: optional i32 come_from,
    23: optional i32 service_category,
    24: optional bool desc,
    25: optional i16 certification_type,
}

struct TEntryQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i16 is_valid
    4: optional i32 zone_id,
    5: optional i32 district_id,
    6: optional i32 city_id,
}

struct TWalleEntryQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i16 is_valid
    4: optional i32 zone_id,
    5: optional string search,
    6: optional string name,
    7: optional string address,
}

struct TDistrictQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i16 is_valid
    4: optional i32 city_id,
}

struct TZoneQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i16 is_valid
    4: optional i32 district_id,
    5: optional i32 city_id,
}

struct TWalleFilter {
    1: optional list<i32> region_ids,
    2: optional list<i32> region_group_ids,
    3: optional list<i32> city_ids,
    4: optional string date_end,
}

struct TWalleKPIFilter {
    1: optional list<i32> region_ids,
    2: optional list<i32> region_group_ids,
    3: optional list<i32> city_ids,
    5: optional i16 year,
    6: optional i16 month,
}

struct TSaasStatus {
    1: optional i32 restaurant_id,
    2: optional i32 status,
    3: optional i32 remains,
    4: optional string ranking_end,
    5: optional string last_minus,
    6: optional bool is_pay,
    7: optional i32 rank_remains,
    8: optional string temp_free_end,
}

struct TCSaasStatus {
    1: optional i32 restaurant_id,
    2: optional i32 status,
    3: optional i32 remains,
    4: optional string ranking_end,
    5: optional string last_minus,
    6: optional bool is_pay,
    7: optional i32 rank_remains,
    8: optional string temp_free_end,
    9: optional string restaurant_name,
}

struct TSaasStatusQuery {
    1: optional list<i32> restaurant_ids,
    2: optional list<i32> statuses,
    3: optional i32 from_remains,
    4: optional i32 to_remains,
    5: optional i32 from_rank_remains,
    6: optional i32 to_rank_remains,
    7: optional string from_last_minus,
    8: optional string to_last_minus,
    9: optional bool is_pay,
    10: optional string from_temp_free_end,
    11: optional string to_temp_free_end,
    12: optional list<i32> city_ids,
    13: optional list<i32> region_ids,
    14: optional bool is_valid,
    15: optional i32 offset,
    16: optional i32 limit,
    17: optional string from_ranking_end,
    18: optional string to_ranking_end,
}

struct TSaasStatusChange {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional i32 change_attr,
    4: optional i32 change_type,
    5: optional i32 change_amount,
    6: optional string remark,
    7: optional string contract_record_sn,
    8: optional i32 user_id,
    9: optional Timestamp created_at,
}

struct TSaasStatusChangeQuery {
    1: optional i32 restaurant_id,
    2: optional i32 change_attr,
    3: optional i32 change_type,
    4: optional Timestamp created_at_start,
    5: optional Timestamp created_at_end,
    6: optional i32 offset,
    7: optional i32 limit,
}

struct TSaasContractPlanQuery {
    1: optional bool is_valid,
    2: optional bool client,
    3: optional i16 plan_type,
    4: optional i16 select_level,
    5: optional i32 offset,
    6: optional i32 limit,
}

struct TSaasContractPlan {
    1: optional i32 id,
    2: optional bool is_valid,
    3: optional i16 plan_type,
    4: optional string name,
    5: optional i32 duration,
    6: optional bool client,
    7: optional i32 price,
    8: optional string bonus,
    9: optional i16 select_level,
    10: optional bool is_bonus_forced,
}

struct TSaasContractRecordQuery {
    1: optional i32 restaurant_id,
    2: optional list<i16> statuses,
    3: optional list<i16> plan_types,
    4: optional list<i16> contract_types,
    5: optional i16 income_status,
    6: optional bool is_bonus_sent,
    7: optional string from_signed_date,
    8: optional string to_signed_date,
    9: optional string from_income_rec_date,
    10: optional string to_income_rec_date,
    11: optional Timestamp from_created_at,
    12: optional Timestamp to_created_at,
    13: optional i32 offset,
    14: optional i32 limit,
    15: optional list<i32> region_ids,
    16: optional list<i32> city_ids,
    17: optional i32 processor_id,
    18: optional string search,
    19: optional list<i16> payment_types,
    20: optional string plan_name,
    21: optional i32 rrc_region_id,
    22: optional i32 position,
}

struct TCRankingInfo{
    1: optional i32 rrc_region_id,
    2: optional i32 position,
    3: optional string ranking_start_date,
    4: optional string rrc_region_name,
}

struct TSaasContractRecord {
    1: optional i32 id,
    2: optional string sn,
    3: optional string relevant_sn,
    4: optional i32 status,
    5: optional string remark,
    6: optional string modification,
    7: optional i32 restaurant_id,
    8: optional string restaurant_name,
    9: optional i16 contract_type,
    10: optional i16 payment_type,
    11: optional i16 plan_type,
    12: optional string plan_name,
    13: optional i32 plan_duration,
    14: optional i32 plan_duration_real,
    15: optional i16 plan_client,
    16: optional double plan_price,
    17: optional double plan_price_real,
    18: optional string plan_bonus,
    19: optional bool is_bonus_sent,
    20: optional string plan_remark,
    21: optional string a_name,
    22: optional string a_address,
    23: optional string a_phone,
    24: optional string a_contact_person,
    25: optional string a_contact_phone,
    26: optional string a_code,
    27: optional string b_name,
    28: optional string b_address,
    29: optional string b_phone,
    30: optional string b_contact_person,
    31: optional string b_contact_phone,
    32: optional string b_approver,
    33: optional string b_signed_date,
    34: optional i32 processor_id,
    35: optional i32 income_rec_user_id,
    36: optional string income_rec_date,
    37: optional string income_rec_remark,
    38: optional i16 income_status,
    39: optional string reference_date,
    40: optional Timestamp created_at,
    41: optional bool is_upgraded,
    42: optional bool is_bonus_forced,
    # deprecated
    43: optional i32 rrc_region_id,
    44: optional string rrc_region_name,
    45: optional i32 position,
    46: optional string ranking_start_date,
    47: optional list<TCRankingInfo> ranking_infos,
}

struct TSaasContractComboQuery {
    1: optional i32 restaurant_id,
    2: optional list<i16> statuses,
    3: optional list<i16> combo_types,
    4: optional list<i16> income_statuses,
    5: optional string from_signed_date,
    6: optional string to_signed_date,
    7: optional Timestamp from_created_at,
    8: optional Timestamp to_created_at,
    9: optional list<i32> region_ids,
    10: optional list<i32> city_ids,
    11: optional i32 processor_id,
    12: optional string search,
    13: optional i32 offset,
    14: optional i32 limit,
}

struct TSaasContractCombo {
    1: optional i32 id,
    2: optional string sn,
    3: optional i32 status,
    4: optional string modification,
    5: optional i32 restaurant_id,
    6: optional string restaurant_name,
    7: optional i16 combo_type,
    8: optional i16 saas_duration,
    9: optional double saas_price,
    10: optional string ranking_description,
    11: optional double ranking_price,
    12: optional i16 ranking_duration,
    13: optional string signed_date,
    14: optional i16 income_status,
    15: optional string income_date_1,
    16: optional string income_date_2,
    17: optional string income_date_3,
    18: optional string saas_subcontract_1,
    19: optional string saas_subcontract_2,
    20: optional string saas_subcontract_3,
    21: optional string ranking_subcontract_1,
    22: optional string ranking_subcontract_2,
    23: optional string ranking_subcontract_3,
    24: optional i32 processor_id,
    25: optional Timestamp created_at,
    26: optional string a_name,
    27: optional string a_address,
    28: optional string a_phone,
    29: optional string a_contact_person,
    30: optional string b_name,
    31: optional string b_address,
    32: optional string b_phone,
    33: optional string b_contact_person,
    34: optional string b_approver,
    35: optional string relevant_sn,
    36: optional double saas_price_real,
    37: optional double saas_paid,
    38: optional double ranking_price_real,
    39: optional double ranking_paid,
    40: optional i16 saas_recharged,
    41: optional i16 ranking_recharged,
}

struct TRegionQuery {
    1: required list<i32> region_ids,
    2: required string search,
    3: required list<i16> type_codes,
    4: required list<i32> city_ids,
    5: required bool show_all,
}

struct TRegionGroupQuery {
    1: optional list<i32> region_group_ids,
    2: optional string search,
    3: optional list<i32> city_ids,
    4: optional i32 offset,
    5: optional i32 limit,
    6: required bool show_all,
}

struct TRestaurantInRegionQuery{
    1: required list<i32> region_ids,
    2: required bool is_valid,
    3: required string search,
    4: required i32 offset,
    5: required i32 limit,
}

struct TCRestaurantSaasStats {
    1: optional i16 group,
    2: optional i32 napos_num,
    3: optional double napos_rate,
    4: optional i32 trial_num,
    5: optional double trial_rate,
    6: optional i32 pay_num,
    7: optional double pay_rate,
    8: optional i32 temp_free_num,
    9: optional double temp_free_rate,
    10: optional i32 napos_mobile_num,
    11: optional double napos_mobile_rate,
    12: optional i32 has_food_img_num,
    13: optional double has_food_img_rate,
    14: optional i32 online_payment_num,
    15: optional double online_payment_rate,
    16: optional i32 has_food_activity_num,
    17: optional double has_food_activity_rate,
    18: optional i32 total_num,
}

struct TCCommentWithReplies {
    1: required TRestaurantComment comment,
    2: required list<TRestaurantCommentReply> comment_replies,
}

struct TCFoodActivityWithRestaurantIds{
    1: required TFoodActivity food_activity,
    2: required list<i32> restaurant_ids,
}

struct TCRestaurantActivityWithRestaurantIds{
    1: required TRestaurantActivity restaurant_activity,
    2: required list<i32> restaurant_ids,
}

struct TOperationRemindQuery {
    1: optional i16 status,
    2: optional bool remind_time_out,
    3: optional i32 by_user_id,
    4: optional string restaurant_name,
    5: optional i32 offset,
    6: optional i32 limit,
}

struct TCOperationRemind {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required string restaurant_name,
    4: required string description,
    5: required i32 by_user_id,
    6: required i16 status,
    7: required Timestamp remind_time,
    8: required Timestamp created_at,
}

struct TCFavoredUser {
    1: optional i32 id,
    2: optional string username,
    3: optional Timestamp favored_time,
}

struct TNaposCommentQuery {
    1: optional i32 restaurant_id,
    2: optional string type,
    3: optional i32 offset,
    4: optional i32 limit,
}

struct TRestaurantMessage {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional string content,
    4: optional bool is_read,
    5: optional string link,
    6: optional string link_text,
    7: optional Timestamp created_at,
    8: optional i32 type_code,
}


struct TCWalleKPIStats {
    1: optional i32 num,
    2: optional i32 pay_num,
    3: optional i32 trial_num,
    4: optional i32 new_num,
    5: optional i32 client_num,
    6: optional i32 food_img_num,
    7: optional i32 time_ensure_num,
    8: optional i32 coupon_enabled_num,
}

struct TOnlinePaymentApplyQuery{
    1:optional i16 status,
    2:optional string search,
    3:optional list<i32> region_ids,

    4:optional i32 offset,
    5:optional i32 limit,
}

struct TCWalleOnlinePaymentApply {
    1:required i32 id,
    2:required i16 status,
    3:required i32 restaurant_id,
    4:required string restaurant_name,
    5:required Timestamp created_at,

    6:required i32 user_id,
    7:required string username,
    8:required string card_id,
    9:required string cardholder_name,
    10:required i32 bank_id,
    11:required string bank_name,
}

struct TWhitelist {
    1: optional list<i32> city_ids,
    2: optional list<i32> region_group_ids,
    3: optional list<i32> region_ids,
    4: optional list<i32> restaurant_ids,
}

struct TCRestaurantManageTree{
    1: optional i32 region_id,
    2: optional string region_name,
    3: optional i32 region_group_id,
    4: optional string region_group_name,
    5: optional i32 city_id,
    6: optional string city_name,
}

struct TPerformanceAssessmentBlock {
    1: optional i32 id,
    2: optional string name,
    3: optional i32 type_code,
    4: optional i32 city_id,
    5: optional list<i32> region_group_ids,
    6: optional list<i32> region_ids,
}

struct TNaposEnv {
    1:optional i32 restaurant_id,
    2:optional bool food_safe_agreed,
    3:optional bool dist_edu_enabled,
}

struct TRestaurantDirector {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional i32 director_id,
    4: optional i16 notice_enabled,
    5: optional i16 in_charge,
    6: optional Timestamp updated_at,
}

struct TRestaurantDirectorQuery {
    1: optional list<i32> restaurant_ids,
    2: optional list<i32> director_ids,
    3: optional i16 notice_enabled,
    4: optional i16 in_charge,
    5: optional i32 offset,
    6: optional i32 limit,
}

struct TRestaurantDistSwitch {
    1: required i32 id,
    2: required i32 restaurant_id,
    3: required Mobile mobile,
}


/**
 * Exceptions
 */
enum ERSErrorCode {
    UNKNOWN_ERROR = 0,
    ACTIVITY_NOT_FOUND = 1,
    ANONYMOUS_USER_PERMISSION_DENIED = 2,
    APP_URL_NOT_FOUND = 3,
    AREA_NOT_FOUND = 4,
    BANKCARD_NOT_FOUND = 5,
    BANKCARD_NOT_MATCH_CORPORATION = 6,
    BANKCARD_WITH_NO_SUBSIDY = 7,
    CITY_NOT_FOUND = 8,
    COMMENT_NOT_FOUND = 9,
    COMMENT_REPLY_NOT_FOUND = 10,
    COUPON_ALREADY_USED = 11,
    COUPON_NOT_FOUND = 12,
    COUPON_OUT_OF_DATE = 13,
    DEVICE_RESTAURANT_NOT_FOUND = 14,
    DIRECTOR_NOT_FOUND = 15,
    DISTRICT_NOT_FOUND = 16,
    DOCK_CORP_NOT_FOUND = 17,
    DOCK_CORP_RESTAURANT_NOT_FOUND = 18,
    DUPLICATED_DEVICE_RESTAURANT = 19,
    ENTRY_NOT_FOUND = 20,
    ENTRY_RESTAURANT_NOT_FOUND = 21,
    FOOD_ALREADY_HAS_FOOD_ACTIVITY = 22,
    FOOD_ACTIVITY_NOT_FOUND = 23,
    FOOD_ACTIVITY_CANT_CHANGE_CITY = 24,
    FOOD_ACTIVITY_CANT_CHANGE_DISCOUNT = 25,
    FOOD_ACTIVITY_HAS_NO_LIMIT = 26,
    FOOD_ACTIVITY_SUBSIDY_CANT_PROCESS = 27,
    FOOD_ACTIVITY_SUBSIDY_NOT_FOUND = 28,
    FOOD_ACTIVITY_FIELD_INVALID = 29,
    FOOD_ACTIVITY_EFFECT_INVALID = 30,
    FOOD_CATEGORY_POSITION_INVALID = 31,
    FOOD_CATEGORY_NOT_COMPLETE = 32,
    FOOD_GROUP_RESTAURANT_DIVERSED = 33,
    FOOD_NOT_FOUND = 34,
    FOOD_HAS_NO_CATEGORY_ID = 35,
    FOOD_NAME_CANNOT_CHANGE = 36,
    FOOD_PRICE_CHANGED_TOO_OFTEN = 37,
    FOOD_PRICE_CHANGED_TOO_MUCH = 38,
    FOOD_CATEGORY_NOT_FOUND = 39,
    FOOD_CATEGORY_NOT_BELONGS_TO_RESTAURANT = 40,
    FOOD_REQUIRED_GARNISH_CONFLICT = 41,
    FOOD_UGC_IMAGE_LIKE_TOO_FREQUENTLY = 42,
    FOOD_UGC_IMAGE_NOT_FOUND = 43,
    FOOD_UGC_IMAGE_PR_NOT_FOUND = 44,
    FOOD_POSITION_INVALID = 45,
    FOOD_NOT_COMPLETE = 46,
    FRIEND_LINK_NOT_FOUND = 47,
    GARNISH_NOT_FOUND = 48,
    GARNISH_CATEGORY_NOT_FOUND = 49,
    GEOHASH_NAME_NOT_FOUND = 50,
    GEOHASH_RESTAURANT_NOT_FOUND = 51,
    INVALID_DATE_RANGE = 52,
    INVALID_ENTRY = 53,
    INVALID_RESTAURANT = 54,
    INVALID_RESTAURANT_AREA = 55,
    INVALID_SUBSIDY = 56,
    INVALID_TIME_RANGE = 57,
    LOGO_NOT_FOUND = 58,
    MISSING_DEVICE_RESTAURANT_ATTRIBUTE = 59,
    MODE_ELEME_INVALID_OPEN_TIME = 60,
    PERMISSION_DENIED = 61,
    QUICK_MESSAGE_NOT_FOUND = 62,
    REGION_AREA_TOO_LARGE = 63,
    REGION_NOT_FOUND = 64,
    REGION_GROUP_NOT_FOUND = 65,
    RESTAURANT_ADMIN_NOT_FOUND = 66,
    RESTAURANT_AREA_TOO_LARGE = 67,
    RESTAURANT_CHANGE_RECORD_NOT_FOUND = 68,
    RESTAURANT_EVALUATION_NOT_FOUND = 69,
    RESTAURANT_HAS_NO_ACTIVITY_SUBSIDY = 70,
    RESTAURANT_MESSAGE_NOT_FOUND = 71,
    RESTAURANT_NOT_FOUND = 72,
    RESTAURANT_OPEN_APPLY_NOT_FOUND = 73,
    RESTAURANT_RATE_NOT_FOUND = 74,
    RESTAURANT_OPEN_APPLY_STATUS_INVALID = 75,
    RESTAURANT_PROMOTION_NOT_FOUND = 76,
    SAAS_CHANGE_RECORD_NOT_FOUND = 77,
    SAAS_CONTRACT_RECORD_NOT_FOUND = 78,
    SAAS_CONTRACT_PLAN_TYPE_ERROR = 79,
    SAAS_CONTRACT_RANKING_INFO_MISSING = 80,
    SAAS_CONTRACT_RANKING_INFO_ALREADY_SET = 81,
    SAAS_CONTRACT_RECORD_STATUS_ERROR = 82,
    SAAS_STATUS_ERROR = 83,
    SAAS_STATUS_NOT_FOUND = 84,
    SAAS_PAY_CANT_TO_FREE = 85,
    SAAS_TRIAL_DAYS_OVER_LIMIT = 86,
    SAAS_SUSPENDED_RESTAURANT_CLOSED_ONLY = 87,
    SAAS_CONTRACT_PLAN_NOT_FOUND = 88,
    SAAS_CONTRACT_UPGRADE_OVERDUE = 89,
    SAAS_CONTRACT_RELEVANT_RECORD_NOT_FOUND = 90,
    SAAS_CONTRACT_RELEVANT_RECORD_ALREADY_UPGRADED = 91,
    SAAS_CONTRACT_RELEVANT_RECORD_NOT_NORMAL = 92,
    SAAS_CONTRACT_UPGRADE_PLAN_ERROR = 93,
    SAAS_CONTRACT_UPGRADE_RESTAURANT_ERROR = 94,
    SAAS_CONTRACT_RECORD_ABANDONED = 95,
    SAAS_CONTRACT_ONLY_ONE_NEW = 96,
    SAAS_CONTRACT_COMBO_NOT_FOUND = 97,
    SAAS_CONTRACT_COMBO_ONE_FOR_RESTAURNT = 98,
    SAAS_CONTRACT_COMBO_NOT_PAYABLE = 99,
    SAAS_CONTRACT_COMBO_USER_LACK_OF_BALANCE = 100,
    SAAS_CONTRACT_COMBO_CONFIRM_OVERLOAD = 101,
    SEO_SM_INDEX_NOT_FOUND = 102,
    STOCK_NOT_ENOUGH = 103,
    TOO_MANY_FOOD_UGC_IMAGES = 104,
    USER_AUTH_FAIL = 105,
    CL_NOT_FOUND = 106,
    DL_NOT_FOUND = 107,
    AREA_OUT_OF_CITY = 108,
    ZONE_NOT_FOUND = 109,
    INVALID_NAME_FOR_URL = 110,
    FOOD_CATEGORY_ONE_ATRR_ONLY = 111,
    ONLINE_PAYMENT_APPLY_NOT_FOUND = 112,
    ONLINE_PAYMENT_APPLY_ALREADY_PROCESSED = 113,
    DELIVER_AREA_MUST_IN_UPDATE = 114,
    INVALID_RESTAURANT_DELIVER_PRICE = 115,
    INVALID_MOBILE = 116,
    DUPLICATED_FOOD_UGC_IMAGE = 117,
    APP_CAMPAIGN_NOT_FOUND = 118,
    TOO_MANY_POLYGON_IN_DELIVER_AREA = 119,
    DUPLICATED_POLYGON_IN_DELIVER_AREA = 120,
    ORDER_IN_PENDING = 121,
    TOO_MANY_POLYGON_IN_DELIVER_GEOJSON = 122,
    RESTAURANT_POLYGON_AREA_TOO_LARGE = 123,
    INVALID_RESTAURANT_GEOMETRY = 124,
    MISS_PROPERTY_IN_DELIVER_GEOJSON = 125,
    DUPLICATED_POLYGON_IN_DELIVER_GEOJSON = 126,
    RESTAURANT_COMMENT_NOT_FOUND = 127,
    INVALID_STOCK = 128,
    FOOD_GARNISH_CATEGORY_NOT_FOUND = 129,
    ACTIVITY_ICON_NOT_FOUND = 130,
    FREE_GIFT_ACTIVITY_NOT_FOUND = 131,
    ORDER_MODE_CORP_TYPE_NOT_MATCH = 132,
    RESTAURANT_ACTIVITY_NOT_FOUND = 133,
    RESTAURANT_ACTIVITY_FIELD_ERROR = 134,
    CERTIFICATION_NOT_FOUND = 135,
    CERTIFICATION_HAS_EXISTED = 136,
    CERTIFICATION_UPDATE_DENIED = 137,
    CERTIFICATION_PROCESS_ILLEGAL = 138,
    INVALID_REGION_AREA = 139,
    INVALID_RESTAURANT_ATTRIBUTE = 140,
    DELIVERY_PRICE_MUST_BE_FIGURE = 141,
    INVALUD_FOOD_DISCOUNT = 142,
    ACTIVITY_CONTRACT_NOT_SIGNED = 143,
    AMENDED_POI_NOT_FOUND = 144,
    RESTAURANT_HAS_TOO_MANY_FOODS = 145,
    VALIDATION_ERROR = 146,
    VALIDATION_NONEXIST_ERROR = 147,
    EOS_CLIENT_ERROR = 148,
    EUS_CLIENT_ERROR = 149,
    GEOS_CLIENT_ERROR = 150,
    EES_CLIENT_ERROR = 151,
    DMS_CLIENT_ERROR = 152,
    SMS_CLIENT_ERROR = 153,
    OAS_CLIENT_ERROR = 154,
    TDS_CLIENT_ERROR = 155,
    DATABASE_ERROR = 156,
    INVALID_FIELD_VALUE = 157,
    INVALID_OPEN_TIME = 158,
    TOO_BUSY_ERROR = 159,
    EPS_CLIENT_ERROR = 160,
    ERS_CLIENT_ERROR = 161,
    RESTAURANT_DIST_SWITCH_NOT_FOUND = 162,
    NON_BOD_CANNOT_UPDATE_METHOD_OF_PAYMENT_DIRECTLY = 163,
    // Append New Error Code Here..
}

exception ERSUserException {
    1: required ERSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception ERSSystemException {
    1: required ERSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception ERSUnknownException {
    1: required ERSErrorCode error_code,
    2: required string error_name,
    3: required string message,
}


/**
 * Services
 */
service ElemeRestaurantService {
    /**
     * Base APIs
     */

    bool ping()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_restaurant(1: TRestaurantSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_area_restaurant(1: TRestaurantAreaSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> search_area_restaurant_struct(1: TRestaurantAreaSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> search_area_restaurant_outside(1: TRestaurantAreaSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 search_area_restaurant_count(1: TRestaurantAreaSearchCountQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_certification_restaurant(1: TRestaurantCertificationSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_filter_restaurant(1: TRestaurantSearchFilterQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_area_food(1: TRestaurantAreaSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    Json search_food(1: TFoodSearchQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void clear_cache(1:string api_name,
                     2:list<string> params)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool check_favored(1: i32 user_id,
                       2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_favored(1: i32 user_id,
                     2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_favored(1: i32 user_id,
                        2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_favored(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, i32> mcount_restaurant_by_entry_id(1: list<i32> entry_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool check_favor_food(1: i32 user_id,
                          2: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_favor_food(1: i32 user_id,
                        2: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_favor_food(1: i32 user_id,
                           2: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_comment(1: i32 user_id,
                     2: string username,
                     3: i32 restaurant_id,
                     4: string content)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_comment(1: TRestaurantCommentQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_comment_reply(1: i32 comment_id,
                           2: i32 user_id,
                           3: string content,
                           4: i32 type)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i16 get_deliver_amount_by_entry(1: i32 restaurant_id,
                                    2: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    FoodStockMap get_foods_stock(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void incr_foods_stock(1: FoodStockMap food_stock_map)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void decr_foods_stock(1: FoodStockMap food_stock_map)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_food_stock(1: i32 food_id,
                        2: i32 stock)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_restaurant_food_eleme_buy_discount(1: i32 restaurant_id,
                                                2: double discount)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void refresh_food_stock(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 get_region_id(1:i32 entry_id,
                      2:Geohash geohash,
                      3:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, i32> get_region_region_group_map(1:list<i32> region_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, i32> get_restaurant_region_map(1:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_restaurant_message(1:i32 restaurant_id,
                                2:i16 message_type,
                                3:map<string, string> info)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_activity_valid(1:list<i32> activity_ids,
                             2:bool is_valid)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_activity_default(1:list<i32> activity_ids,
                               2:bool is_default)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_direct_struct(1:i32 user_id,
                           2:TDirectStruct update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_regions(1:i32 user_id,
                     2:list<i32> region_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_region_groups(1:i32 user_id,
                           2:list<i32> region_group_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_activity(1:i32 activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated, use save_activity instead
    i32 update_activity(1:TActivity update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_activity(1: i32 activity_id,
                      2: TActivity save_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_dock_corp(1: i32 dock_corp_id,
                       2: TDockCorp save_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 set_restaurant_dock_corp(1: i32 restaurant_id,
                                 2: i32 corp_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void delete_dock_corp_restaurant_by_restaurant_id(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated, use mset_food_stock_by_category instead
    void mset_food_stock(1:TFoodStock mset_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_food_stock_by_category(1:i32 category_id, 2:bool is_max)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_food_stock_by_food_ids(1:list<i32> food_ids, 2:bool is_max)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated, use save_food / napos_save_food instead
    i32 update_food(1:TFood update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_food(1: i32 food_id,
                  2: TFood t_food)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 napos_save_food(1: i32 food_id,
                        2: TFood t_food)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_food(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_food_position(1:i32 food_id,
                           2:i32 position)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool mset_food_position(1:list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated use save_food_category instead
    i32 update_food_category(1:TFoodCategory update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_food_category(1: i32 category_id,
                           2: TFoodCategory t_category)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_food_category(1:i32 food_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_food_category_position(1:i32 category_id,
                                    2:i32 position)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool mset_food_category_position(1:list<i32> category_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_food_category_attr(1:i32 category_id,
                                2:string attr)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_food_category_attr(1:i32 category_id,
                                   2:string attr)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_food_garnish_category(1:i32 food_garnish_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 update_food_garnish_category(1:TFoodGarnishCategory update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<string> food_ugc_image_upload(1: i32 order_item_id,
                                       2: list<string> image_hash_list,
                                       3: i32 come_from)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void process_food_ugc_image(1: i32 food_ugc_image_id,
                                2: i16 to_status,
                                3: i32 user_id,
                                4: string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_garnish(1:i32 garnish_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 update_garnish(1:TGarnish update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_garnish_category(1:i32 garnish_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 update_garnish_category(1:TGarnishCategory update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 update_logo(1:TLogo update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 new_restaurant(1:TRestaurant new_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant_geohash(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant_region(1:i32 restaurant_id,
                                  2:i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void reset_restaurant_region(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_restaurant_status(1:i32 restaurant_id,
                               2:string status,
                               3:i32 value,
                               4:i32 user_id,
                               5:string remark,
                               6:Timestamp remind_time,
                               7:i32 corp_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_restaurant_status_direct(1:list<i32> restaurant_ids,
                                       2:string status,
                                       3:i32 value,
                                       4:i32 user_id,
                                       5:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void send_restaurant_change_notice(1:i32 record_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void send_saas_change_notice(1:i32 record_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_free_gift_icon_by_category(1:i32 entity_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_restaurant_open_apply(1: i32 user_id,
                                   2: string applicant,
                                   3: string telephone,
                                   4: string mobilephone,
                                   5: string qq,
                                   6: i16 city_id,
                                   7: i32 entry_id,
                                   8: i64 geohash,
                                   9: string restaurant_name,
                                   10: string restaurant_address,
                                   11: string restaurant_description,
                                   12: string restaurant_url)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool is_reserved_restaurant_url(1: string restaurant_url)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_city_entry_json(1: i32 city_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_restaurant_ugc_image_json(1: i32 restaurant_id
                                         2: i16 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_restaurant_ugc_image_json_new(1: i32 restaurant_id
                                             2: i16 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_restaurant_menu_json(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_restaurant_menu_json_new(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_food_activity(1: i32 food_activity_id, 2: list<i32> food_ids, 3: list<i32> weekdays)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void clear_food_activity(1: list<i32> food_ids, 2: list<i32> weekdays)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void sync_food_activity_with_category(1: i32 food_id, 2: i32 food_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void dismiss_food_activity(1: i32 food_activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_seo_sm_place(1: TSeoSmQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant(1: i32 restaurant_id,
                           2: i32 user_id,
                           3: TRestaurant t_rst)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void overload_close_restaurant(1: list<i16> order_modes,
                                   2: list<i16> saas_statuses,
                                   3: list<i32> sms_services,
                                   4: list<i32> exculde_city_ids,
                                   5: list<i32> exculde_region_group_ids,
                                   6: list<i32> exculde_region_ids,
                                   7: list<i32> exculde_restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 get_restaurant_deliver_time(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCRestaurantManageTree get_restaurant_manage_tree(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void all_restaurant_back_alive(1: Timestamp from_datetime
                                   2: list<i16> order_modes,
                                   3: list<i16> saas_statuses,
                                   4: list<i32> sms_services,
                                   5: list<i32> city_ids,
                                   6: list<i32> region_group_ids,
                                   7: list<i32> region_ids,
                                   8: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool check_restaurant_permission(1: i32 user_id,
                                     2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> mget_restaurant_in_region(1: list<i32> region_ids, 2: bool is_valid)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    /**
     * Apps APIs
     */
    void archive_restaurant_status()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void do_archive_restaurant_status(1:list<i32> restaurant_ids,
                                        2:Timestamp record_time)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_area_structure(1:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_stats_area_structure(1:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string filter_area(1:i32 user_id,
                       2:string struct_json)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string filter_stats_area(1:i32 user_id,
                             2:string struct_json)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool saas_status_touch(1:i32 restaurant_id,
                           2:i16 change_type,
                           3:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_recharge_custom(1:i32 restaurant_id,
                              2:i16 change_attr,
                              3:i16 change_amount,
                              4:i32 user_id,
                              5:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_set_status_custom(1:i32 restaurant_id,
                                2:i16 status_new,
                                3:string remark,
                                4:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_set_trial(1:i32 restaurant_id,
                        2:i16 bonus,
                        3:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_set_temp_free(1:i32 restaurant_id,
                            2:string end_date,
                            3:string remark,
                            4:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_abandon_contract(1:string sn,
                               2:i32 user_id,
                               3:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_archive_contract(1:string sn,
                               2:i32 user_id,
                               3:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_set_contract_bonus_sent(1:string sn,
                                      2:i32 user_id,
                                      3:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_confirm_income(1:string sn,
                             2:i16 payment_type,
                             3:i32 user_id,
                             4:Timestamp rec_date,
                             5:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_check_trials(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_check_remains()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_check_temp_frees()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_check_abandons()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_daily_report()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_saas_contract_plan(1:i32 plan_id,
                                2:TSaasContractPlan t_saas_contract_plan)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_saas_contract_plan(1:TSaasContractPlanQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasContractPlan> query_saas_contract_plan(
        1:TSaasContractPlanQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TSaasContractPlan get_saas_contract_plan(1:i32 plan_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string new_saas_contract_record(1:TSaasContractRecord t_record)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_saas_contract_record(1:TSaasContractRecordQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasContractRecord> query_saas_contract_record(
        1:TSaasContractRecordQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCSaasStatus> query_saas_status(
        1:TSaasStatusQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_saas_status(
        1:TSaasStatusQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasStatusChange> query_saas_status_change(
        1: TSaasStatusChangeQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_saas_status_change(
        1: TSaasStatusChangeQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TSaasContractRecord get_saas_contract_record(1:string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasContractRecord> mget_saas_contract_record(1:list<string> sns)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void saas_update_contract_ranking_info(1: string sn,
                                           2: list<TCRankingInfo> ranking_infos,
                                           3: i32 user_id,
                                           4: string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TSaasContractCombo get_saas_contract_combo(1:string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasContractCombo> mget_saas_contract_combo(1:list<string> sns)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSaasContractCombo> query_saas_contract_combo(
        1:TSaasContractComboQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_saas_contract_combo(
        1:TSaasContractComboQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string new_saas_contract_combo(1:TSaasContractCombo t_combo)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void confirm_saas_combo_income(1:string sn,
                             2:i16 payment_type,
                             3:i32 user_id,
                             4:Timestamp rec_date,
                             5:string remark,
                             6:i32 saas_duration,
                             7:double saas_price,
                             8:i32 ranking_duration,
                             9:double ranking_price)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void stop_saas_contract_combo(1:string sn,
                                  2:i32 user_id,
                                  3:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void abandon_saas_contract_combo(1:string sn,
                                     2:i32 user_id,
                                     3:string remark)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void op_quit(1:i32 restaurant_id,
                 2:i32 admin_user_id,
                 3:string password)

    i32 new_food_activity(1:TFoodActivity new_activity)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_food_activity(1:i32 food_activity_id, 2:TFoodActivity activity_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_restaurant_appliable_activity_ids(1:i32 restaurant_id, 2:i32 activity_category_id, 3:i16 activity_type)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i16 get_restaurant_activity_status(1:i32 restaurant_id, 2:i16 activity_type)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, i16> get_food_activity_status(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, list<i32>> get_participatable_food_activity_ids(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void apply_for_activity_subsidy_contract(1:i32 restaurant_id,
                                             2:i32 activity_id,
                                             3:i32 activity_category_id,
                                             4:double subsidy,
                                             5:i32 submit_user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void apply_for_complex_activity_subsidy_contract(1:i32 restaurant_id,
                                                     2:i32 activity_id,
                                                     3:i32 activity_category_id,
                                                     4:string subsidy_json,
                                                     5:i32 submit_user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void approve_activity_subsidy_contract(1:list<i32> contract_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void reject_activity_subsidy_contract(1:list<i32> contract_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void sign_activity_subsidy_contract(1:i32 subsidy_contract_id, 2:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void refuse_activity_subsidy_contract(1:i32 subsidy_contract_id, 2:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    double get_restaurant_activity_subsidy(1:i32 restaurant_id,
                                           2:i32 activity_id,
                                           3:i32 activity_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_restaurant_activity_complex_subsidy(1:i32 restaurant_id,
                                                   2:i32 activity_id,
                                                   3:i32 activity_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    TActivitySubsidyContract get_activity_subsidy_contract(1:i32 subsidy_contract_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TActivitySubsidyContract> query_activity_subsidy_contract(1:TActivitySubsidyContractQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_activity_subsidy_contract(1:TActivitySubsidyContractQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_city(1:i32 city_id, 2:TCity t_city)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_area(1:i32 area_id, 2:TArea t_area)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void delete_area(1:i32 area_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_region(1:i32 region_id, 2:TRegion t_region)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 create_region(1:TRegion t_region, 2: i32 group_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_region_and_its_group(1:i32 region_id,
                                     2:TRegion t_region,
                                     3:i32 group_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_region(1:i32 region_id,
                       2:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRegion> query_region(1:TRegionQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> user_get_region_ids(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> user_get_region_group_ids(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_restaurant_in_region(1:TRestaurantInRegionQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_entry(1:i32 entry_id,
                   2: TEntry t_entry)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_entry(1:TWalleEntryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TEntry> walle_query_entry(1: TWalleEntryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCWalleKPIStats walle_get_kpi_stats(1: TWalleKPIFilter filter_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_online_payment_apply(
        1: TOnlinePaymentApplyQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCWalleOnlinePaymentApply> walle_query_online_payment_apply(
        1: TOnlinePaymentApplyQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_new_online_payment_apply(1: i32 user_bankcard_id,
                                       2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_online_payment_approve(1: i32 record_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_online_payment_overrule(1: i32 record_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void fast_online_payment_approve(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_district(1:i32 district_id,
                      2: TDistrict t_district)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_zone(1:i32 zone_id,
                  2: TZone t_zone)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_restaurant_in_region(1:TRestaurantInRegionQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDeviceRestaurant> query_device_restaurant(1: TDeviceRestaurantQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void send_contract_notification(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 new_device_restaurant(1: i32 restaurant_id,
                              2: string device_id,
                              3: i16 device_type,
                              4: string eleme_guid,
                              5: string version)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_device_restaurant(1: i32 id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    i32 walle_get_saas_stats_count(1: TWalleFilter filter_struct,
                                   2: string group_by)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TLeanRestaurant> walle_query_restaurant(1: TRestaurantQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCRestaurantSaasStats> walle_get_saas_stats(1: TWalleFilter filter_struct,
                                                     2: string group_by,
                                                     3: string sort_key,
                                                     4: i16 sort_type,
                                                     5: i32 offset,
                                                     6: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string walle_get_activity_list(1: TActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string walle_get_activity_list_by_ids(1: list<i32> activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string walle_get_logo_list(1: TLogoQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string walle_get_restaurant_list(1: TRestaurantQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCWalleRestaurantChangeRecord> walle_get_restaurant_change_records(1:i32 restaurant_id,
                                                                            2:i16 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    /**
     * op is short for online_payment,
     * this api is only for eus.walle_query_online_payment_apply
     * return map<restaurant_id, restaurant_name>
     */
    map<i32, string> walle_get_op_apply_restaurants(1: list<i32> restaurant_ids,
                                                    2: list<i32> regions_ids,
                                                    3: string keyword)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string walle_get_restaurant_list_by_ids(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_save_friend_link(1:i32 friend_link_id, 2:TFriendLink t_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_remove_friend_link(1:i32 friend_link_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_friend_link(1:TFriendLinkQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFriendLink> walle_query_friend_link(1:TFriendLinkQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_save_quick_message(1:i32 quick_message_id, 2:TQuickMessage t_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_remove_quick_message(1:i32 quick_message_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_quick_message(1:TQuickMessageQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TQuickMessage> walle_query_quick_message(1:TQuickMessageQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_comment_reply(
        1:TWalleCommentReplyQuery query_struct
    )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCWalleCommentReply> walle_query_comment_reply(
        1:TWalleCommentReplyQuery query_struct
    )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_set_comment_reply_valid(1:i32 reply_id,
                                       2:i16 is_valid)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 walle_count_restaurant_comment(
        1:TWalleRestaurantCommentQuery query_struct
    )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCWalleRestaurantComment> walle_query_restaurant_comment(
        1:TWalleRestaurantCommentQuery query_struct
    )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_set_restaurant_comment_valid(1:i32 comment_id,
                                            2:i16 is_valid)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void walle_reply_restaurant_comment(1:i32 comment_id,
                                        2:i32 user_id,
                                        3:string content)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_restaurant_open_apply_status(1: list<i32> ids, 2: i16 status)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void napos_restaurant_promotion_save(1: i32 promotion_id,
                                         2: TRestaurantPromotion t_promotion)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 napos_count_comments(1: TNaposCommentQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCCommentWithReplies> napos_query_comments(
        1: TNaposCommentQuery query_struct
        )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantMessage napos_get_message(1: i32 message_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantMessage> napos_mget_message(1: i32 restaurant_id,
                                                2: i32 offset,
                                                3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 napos_count_unread_message(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantMessage> napos_mget_unread_message(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void napos_read_message(1: i32 message_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_operation_remind_status(1: list<i32> or_ids, 2: i16 status)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    /*
     * openapi
     */
    list<i32> openapi_get_new_restaurant_ids(
            1: i32 city_id
            2: Timestamp start_time,
            3: Timestamp end_time)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    /**
     * Inner APIs
     */
    void revert_decr_foods_stock(1: i64 order_id,
                                 2: FoodStockMap food_stock_map)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void process_saas_status_touch(1: i64 order_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    void process_post_bankcard_bind_approve(1: i32 restaurant_id,
                                            2: Timestamp timestamp)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void mset_tuesday_half_price_food_stock(1: bool is_max)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void reset_half_price_food_stock_by_category(1: string unique_week,
                                                 2: i32 category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void process_remove_market_staff(1:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void refresh_flavors_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_delete_region_task_status(1: i64 dl_region_id,
                                       2: i16 status)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_update_region_task_status(1: i64 cl_region_id,
                                       2: i16 status)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void send_update_restaurant_evaluation_task()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void daily_clear_restaurant_menu_cache()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void semi_send_update_restaurant_evaluation_task(1: i32 offset,
                                                     2: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant_evaluation(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void notify_napos_mobile_to_sync(1: i32 restaurant_id,
                                     2: bool is_new_order)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void notify_napos_mobile_to_sync2(1: i32 restaurant_id,
                                      2: bool is_new_order,
                                      3: i64 timestamp)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_food_ugc_image_cover(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void refresh_food_has_activity(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void refresh_restaurant_food_activity(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void post_participate_restaurant_activity(1: i32 restaurant_id,
                                              2: TRestaurantActivity activity)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void post_quit_restaurant_activity(1: i32 restaurant_id,
                                       2: bool has_activity,
                                       3: i32 activity_type)
    throws (1: ERSUserException user_exception,
            2: ERSSystemException system_exception,
            3: ERSUnknownException unknown_exception),

    /**
     * Query APIs
     */
    TRestaurant get(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant get_by_oid(1: i32 restaurant_oid)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 get_oid_by_restaurant_id(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # TODO change to map
    list<TRestaurant> mget(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant master_get(1: i32 id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant get_by_wireless_printer_esn(1: string esn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant get_by_name_for_url(1: string name_for_url)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant get_by_mobile(1: string mobile)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurant get_by_admin(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TAppCampaign get_app_campaign_by_sn(1: string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantBankcard get_bankcard(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCBankcard get_bankcard_new(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated, use mget_restaurant_bankcard instead
    list<TRestaurantBankcard> mget_bankcard(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, TRestaurantBankcard> mget_restaurant_bankcard(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 update_bankcard(1: TRestaurantBankcard update_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_bankcard(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_by_dock_corp(1: i32 dock_corp_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated, use query_open_apply instead
    TRestaurantOpenApply get_open_apply_by_admin(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantOpenApply get_open_apply(1: i32 id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantOpenApply> query_restaurant_open_apply(1: TRestaurantOpenApplyQuery t_open_apply)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_restaurant_open_apply(1: TRestaurantOpenApplyQuery t_open_apply)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TEntry get_entry(1: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TEntry> mget_entry(1: list<i32> ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TEntry get_entry_by_sn(1: string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TEntry> query_entry(1: TEntryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDistrict get_district(1: i32 district_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDistrict> query_district(1: TDistrictQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TZone get_zone(1: i32 zone_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TZone> query_zone(1: TZoneQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDirectStruct get_direct_struct(1:i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegion get_region(1: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegion master_get_region(1: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, TRegion> mget_region(1: list<i32> region_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegion get_region_by_entry(1: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegion get_region_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegionGroup get_region_group(1: i32 region_group_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, TRegionGroup> mget_region_group(1: list<i32> region_group_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRegionGroup get_region_group_by_region(1: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_region_group(1: TRegionGroupQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRegionGroup> query_region_group(1: TRegionGroupQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 save_region_group(1: i32 region_group_id,
                          2: TRegionGroup region_group)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_region_group(1: i32 region_group_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_region_group_region(1: i32 region_group_id,
                                    2: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRegion> get_regions_by_region_group_ids(1: list<i32> region_group_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TActivity get_activity(1: i32 activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TActivity> mget_activity(1: list<i32> activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city(1: i32 city_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city_by_name(1: string city_name)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, TCity> mget_city(1: list<i32> city_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city_by_region(1: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city_by_region_group(1: i32 region_group_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city_by_code(1: i32 district_code)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCity get_city_by_area_code(1: string area_code)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCountryRegion> query_country_region(1: TCountryRegionQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCity> query_city(1: TCityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFood get_food(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> mget_food(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> mget_valid_food(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 get_other_most_stable_food_in_category(1: i32 food_id,
                                               2: i32 food_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFood master_get_food(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFood get_food_by_sn(1: string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodCategory get_food_category(1: i32 food_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodCategory> mget_food_category(1: list<i32> food_category_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodCategory master_get_food_category(1: i32 food_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodUgcImage get_food_ugc_image(1: i32 food_ugc_image_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodUgcImagePr> get_food_ugc_image_pr(1: i32 food_ugc_image_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodUgcImage> mget_food_ugc_image(1: list<i32> food_ugc_image_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodUgcImage get_food_ugc_image_by_sn(1: string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodUgcImage get_food_ugc_image_by_order_item_id(1: i32 order_item_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # date: %Y-%m-%d
    list<TFoodUgcImage> query_food_ugc_image_by_user_id(1: i32 user_id,
                                                        2: string date,
                                                        3: i32 max_day)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_food_ugc_image(1: TFoodUgcImageQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodUgcImage> query_food_ugc_image(1: TFoodUgcImageQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_food_ugc_image_cover(1: TFoodUgcImageCoverQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodUgcImageCover> query_food_ugc_image_cover(1: TFoodUgcImageCoverQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 like_food_ugc_image(1: i32 user_id, 2:i32 food_ugc_image_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 dislike_food_ugc_image(1: i32 user_id, 2:i32 food_ugc_image_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> filter_liked_food_ugc_image_ids(1: i32 user_id, 2: list<i32> food_ugc_image_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_liked_food_ugc_image_cover_ids_by_user(1: i32 restaurant_id, 2: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void report_food_ugc_image(1: i32 user_id, 2: i32 food_ugc_image_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    list<TGarnish> mget_garnish(1: list<i32> garnish_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TGarnish> mget_garnish_by_food(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodFlavor> mget_food_flavor_by_food_ids(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TGarnishCategory get_garnish_category(1: i32 garnish_category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TGarnishCategory> mget_garnish_category(1: list<i32> garnish_category_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TGarnishCategory> mget_garnish_category_by_food(1: i32 food_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TActivity> query_activity(1: TActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TActivity get_activity_by_sn(1: string sn)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_activity_ids_by_geohash(1: Geohash geohash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TCRegionMap get_region_map_by_geohash(1: Geohash geohash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDockCorp get_dock_corp(1: i32 id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDockCorp get_dock_corp_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDockCorp get_dock_corp_by_app(1: i32 app_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDockCorp> mget_dock_corp(1: list<i32> ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_dock_corp(1: TDockCorpQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDockCorp> query_dock_corp(1: TDockCorpQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDockCorpRestaurant get_dock_corp_restaurant(1: i32 id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDockCorpRestaurant> mget_dock_corp_restaurant(1: i32 ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TDockCorpRestaurant> query_dock_corp_restaurant(
        1: list<i32> corp_ids,
        2: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TLogo get_logo(1: i32 logo_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TLogo> mget_logo(1: list<i32> logo_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TLogo> get_current_logo()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_location_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_location_by_region(1: i32 region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFreeGiftActivity get_free_gift_activity(1: i32 free_gift_activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFreeGiftActivity> mget_free_gift_activity(1: list<i32> free_gift_activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFreeGiftActivity> mget_free_gift_activity_list()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFreeGiftActivity> mget_free_gift_activity_by_attributes(1:list<string> attrs)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_by_entry(1: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_premium_by_entry(1: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated
    list<TLeanRestaurant> query_premium_by_geohash2(1: Geohash geohash, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_premium_by_geohash(1: Geohash geohash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_bookable_by_entry(1: i32 entry_id,
                                              2: string deliver_time)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_favor_by_geohash(1: i32 user_id,
                                             2: Geohash geohash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_favor_by_entry(1: i32 user_id,
                                           2: i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> query_favor_ids(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_favor(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # deprecated
    list<TRestaurant> query_by_geohash(1: Geohash geohash, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_by_area(1: i32 is_valid, 2: i32 is_premium, 3: Json area)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_by_psn(1: string psn, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_premium_by_geohash(1: Geohash geohash, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_premium_by_psn(1: string psn, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TLeanRestaurant> query_by_geohash2(1: Geohash geohash, 2: i32 offset, 3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_bookable_by_geohash2(1: Geohash geohash,
                                                2: string deliver_time)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> query_favor_food_ids_by_restaurant(1: i32 user_id,
                                                 2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> query_favor_food_ids_by_user(1: i32 user_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_favor_food_by_user(1: i32 user_id,
                                         2: i32 offset,
                                         3: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_food(1: TFoodQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_food_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodCategory> query_food_category(1: TFoodCategoryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodGarnishCategory> query_food_garnish_category(
        1: TFoodGarnishCategoryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodCategory> query_food_category_by_restaurant(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TGarnish> query_garnish(1: TGarnishQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TGarnishCategory> query_garnish_category(1: TGarnishCategoryQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantComment get_comment(1: i32 comment_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TEntry> query_entry_by_restaurant(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_hot_food_by_entry(1:i32 entry_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_hot_food_by_geohash(1:Geohash geohash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_hot_food_by_restaurant(1: i32 restaurant_id, 2: i32 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCCommentWithReplies> query_comment_with_replies(
        1:TRestaurantCommentQuery query_struct
        )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantComment> query_all_comment(
        1:TRestaurantCommentQuery query_struct
        )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 get_director_id(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_director_ids_by_area(1: list<i32> region_ids,
                                       2: list<i32> region_group_ids,
                                       3: list<i32> city_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurant> query_restaurant_by_dock_corp(1: i32 dock_corp_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantFlavor> query_restaurant_flavor_by_restaurant_id(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFreeGiftActivity> query_free_gift_activity(1:TFreeGiftActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodActivity> query_food_activity(1:TFoodActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_food_activity(1:TFoodActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFoodActivity get_food_activity(1:i32 food_activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFoodActivity> mget_food_activity(1:list<i32> food_activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, i32> get_food_activity_id_map(1:list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, map<i32, i32>> get_weekday_food_activity_id_map(1: list<i32> food_ids, 2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # remove this interface when better cache ready
    map<i32, map<i32, i32>> get_weekday_food_activity_id_map_no_cache(1: list<i32> food_ids, 2: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCFoodActivityWithRestaurantIds> get_food_activity_with_restaurant_ids(1:list<i32> restaurant_ids, 2:list<i32> weekdays)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 add_restaurant_certification(1:TRestaurantCertification rest_cert)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant_certification(1:TRestaurantCertification rest_cert)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void process_certification(1:i32 process_user_id, 2:i32 restaurant_id, 3:i16 to_status)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantCertification get_restaurant_certification(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i32, TRestaurantCertification> mget_restaurant_valid_certification(1:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> filter_uncertificated_restaurants(1:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantCertification> query_restaurant_certification_by_status(1:i16 status, 2:i16 offset, 3:i16 limit)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantCertification> query_restaurant_certification(1:TRestaurantCertificationQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_pre_next_restaurant_certification(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 add_restaurant_activity(1:TRestaurantActivity activity)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void update_restaurant_activity(1:i32 activity_id, 2:TRestaurantActivity activity)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> get_participatable_restaurant_activity_ids(1:i32 restaurant_id, 2:i16 activity_type)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void participate_restaurant_activity(1:i32 restaurant_id, 2:i32 activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void quit_restaurant_activity(1:i32 restaurant_id, 2:i32 activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantActivity get_restaurant_activity(1:i32 activity_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    list<TRestaurantActivity> mget_restaurant_activity(1:list<i32> activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantActivity> query_restaurant_activity_by_restaurant(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantActivity> javis_query_restaurant_activity_by_restaurant(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantActivity> query_restaurant_activity_for_admin(1:TRestaurantActivityQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    map<i16, list<i32>> get_restaurant_activity_map_group_by_type(1:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCRestaurantActivityWithRestaurantIds> get_restaurant_activity_with_restaurant_ids(1:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void save_amended_poi(1: i32 id, 2: TAmendedPoi poi)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TAmendedPoi> query_amended_poi(1: i32 city_id, 2: string keyword)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<string> get_free_gift_activity_attribute_name_by_category(1:i32 category_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCFoodCategoryWithFoods> query_food_category_with_foods(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string query_recent_removed_foods(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFood> query_gum_food_by_restaurant(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantPromotion get_restaurant_promotion(1:i32 promotion_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantPromotion> query_restaurant_promotion(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TChangelogRestaurant master_get_changelog_restaurant(1: i32 cl_rst_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TChangelogRegion master_get_changelog_region(1: i32 cl_region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TDeletelogRegion master_get_deletelog_region(1: i32 dl_region_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSeoSmPlace> query_seo_sm_place(1: TSeoSmQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSeoSmRestaurant> query_seo_sm_restaurant(1: TSeoSmQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TSeoSmCityIndex> query_seo_sm_city_index(1: TSeoSmCityIndexQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TSeoSmIndex get_seo_sm_index_by_name(1: string name)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TSaasStatus get_saas_status(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_operation_remind(1: TOperationRemindQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCOperationRemind> query_operation_remind(1: TOperationRemindQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TQuickMessage get_quick_message(1: i32 quick_message_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TFriendLink get_friend_link(1: i32 friend_link_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TFriendLink> query_friend_link()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 count_favored_user(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TCFavoredUser> mget_favored_user(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TArea> query_area_by_square(
        1: double lt_latitude,
        2: double lt_longitude,
        3: double rb_latitude,
        4: double rb_longitude
    )
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantEvaluation get_evaluation(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TPerformanceAssessmentBlock> get_all_performance_assessment_block()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    i32 add_performance_assessment_block(1: TPerformanceAssessmentBlock pab)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void delete_performance_assessment_block(1: i32 pa_block_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TWhitelist query_close_restaurant_whitelist()
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void save_close_restaurant_whitelist(1: TWhitelist whitelist_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    i32 get_restaurant_setup_step(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_restaurant_setup_step(1:i32 restaurant_id,
                                   2:i32 step)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_short_url(1:string origin_url)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool is_restaurant_mobile_location_match(1:i32 restaurant_id, 2:string mobile)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    string get_origin_url(1:string short_url_hash)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TNaposEnv get_napos_env(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool set_napos_env(1:i32 restaurant_id,
                       2:string key,
                       3:string value)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<TRestaurantDirector> query_restaurant_director(1:TRestaurantDirectorQuery query_struct)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void set_restaurant_director(1:i32 director_id, 2:list<i32> restaurant_ids,
                                 3:i16 notice_enabled, 4:i16 in_charge)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void rm_restaurant_director(1:i32 director_id, 2:list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    list<i32> query_restaurant_by_creation_time(1:Timestamp from_timestamp,
                                                2:Timestamp to_timestamp)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void add_restaurant_dist_switch(1:i32 restaurant_id,
                                    2:Mobile mobile)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void remove_restaurant_dist_switch(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantDistSwitch get_restaurant_dist_switch(1:i32 switch_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantDistSwitch get_restaurant_dist_switch_by_restaurant(1:i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    TRestaurantDistSwitch get_restaurant_dist_switch_by_mobile(1:Mobile mobile)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    #####
    # Signal APIs
    #####

    void signal_post_make_order(1: i64 order_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_update_restaurant(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_update_food_category(1: list<i32> food_category_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_update_food(1: list<i32> food_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_update_food_activity(1: list<i32> food_activity_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_post_process_food_ugc_image(1: i32 process_food_ugc_image_pr_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool any_support_for_ol_payment(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    # for compatible with old zeus async task
    void signal_menu_clear_cache(1: list<i32> restaurant_ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void signal_update_menu_cache(1: i32 restaurant_id)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),


    #####
    # Utils APIs
    #####
    void update_cache(1:string tablename,
                      2:list<i64> ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    void utils_table_cache_update(1:string tablename,
                                  2:list<i64> ids)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),

    bool utils_pk_cache_refresh(1: string api, 2: i64 pk)
        throws (1: ERSUserException user_exception,
                2: ERSSystemException system_exception,
                3: ERSUnknownException unknown_exception),
}
