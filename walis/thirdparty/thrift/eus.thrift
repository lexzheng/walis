# definr eus service
namespace php EUS
namespace py eus

/**
 * Const
 */
const i16 DEFAULT_LIST_SIZE = 20
const i16 MAX_LIST_SIZE = 200
const i16 ANONYMOUS_USER_ID = 886
const i16 DAILY_MAX_WITHDRAW_COUNT = 1
const list<i32> TEST_USER_IDS= [182506, 192927, 3215]

const string PERMISSION_MANAGE_ALL_AREA = "manage_all_area"
const string PERMISSION_WALLE_REPLACE_ORDER = "walle_replace_order"
const string DIRECTOR_MANAGE_RESTAURANT = "direct_manage_restaurant"
const string PERMISSION_MANAGE_RESTAURANT = "walle_restaurant_manage"
const string PAY_METHOD_ALIPAY_MOBILE_APP = "ALIPAY_MOBILE_APP"
const string PAY_METHOD_ALIPAY_MOBILE_WEB = "ALIPAY_MOBILE_WEB"
const string PAY_METHOD_TENPAY_WEB = "TENPAY_WEB"
const string USER_ACCESS_TOKEN_KEY = "user:access_token"
const string ACCESS_TOKEN_USER_KEY = "access_token:user"
const string ANDROID_ELEME_DEVICE_ID_UNIQUE_VERSION = "2.10"
const string DRAWBACK_PROCESS_BANK_NAME_ALIPAY = "ALIPAY"

/**
 * Enums
 */
enum BankDrawbackProcessRecordConst {
    ACCOUNT_TYPE_PERSONAL = 0,
    ACCOUNT_TYPE_BUSINESS = 1,
}

enum BankDrawbackProcessStatusConst {
    STATUS_INVALID = -1,
    STATUS_ALIPAY_BANK_PROCESSING = 0,
    STATUS_ALIPAY_BANK_SUCCESS = 1,
    STATUS_ALIPAY_BANK_FAIL_I = 2,
    STATUS_ALIPAY_BANK_FAIL_F = 3,
    STATUS_MANUAL_PROCESSING = 10,
    STATUS_MANUAL_SUCCESS = 11,
}

enum DrawbackProcessStatusConst {
    STATUS_UNPROCESSED = 0,
    STATUS_PROCESSING = 1,
    STATUS_SUCCESS = 2,
    STATUS_FAIL = 3,
    STATUS_RETRY = 4,
    STATUS_MANUAL_SUCCESS = 5,
    STATUS_IGNORED = 6,
}

enum DrawbackPlatformConst {
    PAY_PLATFORM_ALIPAY = 1,
    PAY_PLATFORM_TENPAY_WEB = 2,
    PAY_PLATFORM_TENPAY_APP = 3,
    PAY_PLATFORM_QQPAY = 4,
    PAY_PLATFORM_DIANPING = 5,
}

enum PayCompanyIdConst {
    PAY_COMPANY_ID_ALIPAY_WEB = 1,
    PAY_COMPANY_ID_ALIPAY_APP = 2,
    PAY_COMPANY_ID_TENPAY_WEB = 3,
    PAY_COMPANY_ID_TENPAY_APP = 4,
    PAY_COMPANY_ID_ALIPAY_BANK = 5,
    PAY_COMPANY_ID_QQPAY = 10,
    PAY_COMPANY_ID_DIANPING = 11,
}

enum PayComeFromConst {
    COME_FROM_WEB = 1,
    COME_FROM_WEB_MOBILE = 2,
    COME_FROM_APP_IOS = 3,
    COME_FROM_APP_ANDROID = 4,
}

enum UserNoticeConst {
    TYPE_EMAIL = 1,
    TYPE_SMS = 2,
}

enum SNSType {
    WEIBO = 1,
    RENREN = 2,
    WEIXIN = 3,
    QQ = 4,
}

enum SNSShareHongbaoConsts {
    AVAILABLE = 0,
    USED_UP = 1,
    ALREADY_GOT = 2,
    ISSUED_TO_PHONE = 3,
    ISSUED_TO_ELEME = 4,
    NOT_ALLOWED = 5,
    ORDER_CANCEL = 6,
}

enum DeviceType {
    IOS = 1,
    ANDROID = 2,
    WEB = 3,
    MOBILE_WEB = 4,
}


enum DopUserProcessType {
    NO_ORDER = 0,
    NORMAL_ORDER = 1,
    TPD_ORDER = 2,
    TERMINAL_ORDER = 3,
    ELEME_ORDER = 4,
    REFUND_ORDER = 5,
    NONE_REFUND_ORDER = 6,
    TPD_ELEME = 7,
}

enum DopUserCallType {
    GATEWAY = 1,
    SIP = 2
}

enum HongbaoConst {
    STATUS_UNUSED = 0,
    STATUS_USED = 1,
    STATUS_ORDER_CANCEL = 2,
    STATUS_INVALID = 3,
}

enum SharedHongbaoConst {
    STATUS_PENDING = 0,
    STATUS_ISSUED = 1,
    STATUS_ORDER_CANCEL = 2,
}

enum HongbaoGroupConst {
    STATUS_PENDING = 0,
    STATUS_VALID = 1,
    STATUS_USED_UP = 2,
    STATUS_ORDER_CANCEL = 3,
}

enum HongbaoExchangeConst {
    STATUS_UNUSED = 1,
    STATUS_USED = 2,
    STATUS_INVALID = 3,
}

enum ReferConst {
    STATUS_WAITING = 0,
    STATUS_VALID = 1,
    STATUS_AWARDED = 2,
    STATUS_INVALID = 3,
    STATUS_REFERER_AWARDED = 4,
}

enum UserMessageConst {
    TYPE_ORDER_PROCESS = 0,
    TYPE_ORDER_RATE = 1,
    TYPE_ORDER_INVALID = 2,
    TYPE_FEEDBACK_REPLY = 101,
    TYPE_COMMENT_REPLY = 102,
    TYPE_REFUND_SUCCESS = 201,
    TYPE_REFUND_FAIL = 202,
    TYPE_REFUND_RESTAURANT_REPLY = 203,
}

enum PointChangeRecordConst {
    TYPE_MAKE_ORDER = 0,
    TYPE_VALID_ORDER = 1,
    TYPE_INVALID_ORDER = 2,
    TYPE_RATE_ORDER = 3,
    TYPE_RATE_FOOD = 4,
    TYPE_EXCHANGE_GIFT = 5,
    TYPE_SYSTEM = 6,
    TYPE_ADMIN = 7,
    TYPE_UPLOAD_IMAGE = 8,
    TYPE_RATE_SERVICE = 9,
}

enum BalanceChangeConst {
    TRADE_TYPE_CHARGE = 0,
    TRADE_TYPE_CONSUME = 1,
    TRADE_TYPE_PRODUCE = 2,
    TRADE_TYPE_REFUND = 3,
    TRADE_TYPE_WITHDRAW_APPLY = 4,
    TRADE_TYPE_WITHDRAW_FAIL = 5,
    TRADE_TYPE_BONUS = 6,
    TRADE_TYPE_DRAWBACK = 7,
    TRADE_TYPE_PAY_AUTO_FAIL = 8,
    TRADE_TYPE_DIRECT_CONSUME = 9,
    TRADE_TYPE_CONTRACT = 10,
    TRADE_TYPE_INVALID_INCOME = 11,
    TRADE_TYPE_ANONYMOUS_DRAWBACK = 12,

    TRADE_TYPE_CLAIM_CHARGE = 20000,
    TRADE_TYPE_CLAIM_CONSUME = 20001,
    TRADE_TYPE_CLAIM_REFUND = 20002,

    PAY_METHOD_ELEME = 0,
    PAY_METHOD_ALIPAY = 1,
}

enum WithdrawRecordConst {
    STATUS_UNPROCESSED = 1
    STATUS_GENERATED = 2
    STATUS_SUBMITTED = 3
    STATUS_SUCCESS = 4
    STATUS_WARNING_FAIL = 5
    STATUS_FATAL_FAIL = 6
}

enum UserGiftConst {
    STATUS_UNPROCESSED = 0,
    STATUS_PROCESSED = 1,
    STATUS_PROCESSING = 2,
}

enum UserGiftObjStatusConst {
    OBJ_STATUS_APPLY = 0,
    OBJ_STATUS_WAIT_SYSTEM_CHECK = 1,
    OBJ_STATUS_IN_SYSTEM_CHECK = 2,
    OBJ_STATUS_END_SYSTEM_CHECK = 3,
    OBJ_STATUS_WAIT_HUMAN_CHECK = 4,
    OBJ_STATUS_CHECK_PASS = 6,
    OBJ_STATUS_CHECK_FAIL = 7,
    OBJ_STATUS_RECEIVED = 8,
    OBJ_STATUS_FINISHED = 9,
}

enum PayRecordConst {
    PAY_CO_ID_ALIPAY = 1,
    PAY_CO_ID_TENPAY = 2,
    PAY_CO_ID_CHARGE_BONUS = 3,
    PAY_CO_ID_DIANPING = 9,
    PAY_METHOD_ALIPAY_MOBILE_APP = 4,
    PAY_METHOD_ALIPAY_MOBILE_WEB = 5,
}

enum OrderPaymentConstitutionConst {
    PAY_TYPE_BALANCE = 1,
    PAY_TYPE_DIRECTLY = 2,
    PAY_TYPE_ECREDIT = 3,
    PAY_TYPE_HONGBAO = 4,
}

enum SfGroupCategoryConst {
    MARKET = 1,
    CUSTOMER_SERVICE = 2,
    RESTAURANT = 3,
    OTHER = 4,
    AUTO = 5,
}

enum UserBankcardStatus{
    INVALID = -1,
    PENDING = 0,
    VALID = 1,
}

enum WithdrawProcessRecordConst {
    STATUS_SUBMITTED = 3
    STATUS_SUCCESS = 4
    STATUS_WARNING_FAIL = 5
    STATUS_FATAL_FAIL = 6
}

enum FeedbackConst  {
    TYPE_OTHER = 0,
    TYPE_USER = 1,
    TYPE_BUG = 2,
    TYPE_SUGGESTION = 3,
    TYPE_COMPLAINT = 4,
    TYPE_NEW_PAGE = 5,
    TYPE_REQUEST_FOR_ORDER = 10,
}

enum TerminalValidationConst {
    TYPE_MOBILE = 0,
    TYPE_EMAIL = 1,
}

enum UserCertificationConst {
    STATUS_PEND = 0,
    STATUS_PASS = 1,
    STATUS_FAIL = -1,

    TYPE_NONE = 0,
    TYPE_PERSONAL = 1,
    TYPE_BUSINESS = 2,
}

enum SSOTypeConst {
    TYPE_NORMAL = 1
    TYPE_TEMP = 2
}

enum SSOAppConst {
    APP_NONE = 0,
    APP_NOCHECK = 99,
    APP_ELEME = 101,
    APP_ELEME_MOBILE = 102,
    APP_ELEME_IOS = 103,
    APP_ELEME_ANDROID = 104,
    APP_NAPOS = 201,
    APP_NAPOS_MOBILE = 202,
    APP_NAPOS_IOS = 203,
    APP_NAPOS_ANDROID = 204,
    APP_NAPOS_KAIDIAN = 210,
    APP_INTRA_WALLE_JAVIS = 301,
    APP_INTRA_SPECTRE = 302,
    APP_INTRA_EVILEYE = 303,
}

enum SSODestroyActionConst {
    USER_LOGOUT = 11,
    USER_REMOVE_BY_SELF = 12,
    ADMIN_REMOVE_BY_ADMIN = 21,
    SYSTEM_EXPIRE = 31,
    SYSTEM_USER_INACTIVE = 32,
    SYSTEM_PASSWORD_CHANGE = 33
}

enum UCBDestroyActionConst {
    USER_REMOVE_BY_SELF = 11,
    ADMIN_REMOVE_BY_ADMIN = 21,
    SYSTEM_EXPIRE = 31,
    SYSTEM_USER_INACTIVE = 32
}

enum UMBDestroyActionConst {
    ADMIN_REMOVE_BY_ADMIN = 21,
    SYSTEM_EXPIRE = 31,
    SYSTEM_SUSPICIOUS_ORDER = 32
}

enum MCBDestroyActionConst {
    ADMIN_REMOVE_BY_ADMIN = 21,
    SYSTEM_EXPIRE = 31,
    SYSTEM_SUSPICIOUS_ORDER = 32
}

enum UserCustomMenuCategoryConst {
    OTHER = 0,
    INSTANCE = 1,
    OBJECTS = 2,
}
enum UserAddressTagTypeConst {
    UNKNOWN,
    TAG_TYPE_HOME = 1,
    TAG_TYPE_SCHOOL = 2,
    TAG_TYPE_COMPANY = 3,
}

enum QRHongbaoType {
    LEAFLET = 0,
    PARTNER = 1,
}

enum QRHongbaoAlgoType {
    NEW_USER_ONLY = 0,
    ALL_MAX_AMOUNT = 1,
    NEW_USER_PREFERED = 2,
}

enum CheckoutCounterPayChannel {
    WEIXIN = 0,
    QQ = 1,
    ALIPAY = 2,
    ALIPAY_WEB = 3,
}

/**
 * Types and Structs
 */
typedef i64 Timestamp
typedef i64 Geohash
typedef string Mobile
typedef list<string> FieldList
typedef string DeviceId
typedef string Json

struct TCAlipayRefundApplyInfo {
    1: required string url,
    2: required map<string, string> form_data,
}

struct TCDrawbackProcessNotify {
    1: required string batch_no,
    2: required i16 success_num,
    3: required string remark,
}

struct TCBankDrawbackProcessNotify {
    1: required string out_refund_id,
    2: required string out_trade_no,
    3: required string status,
    4: required string batch_no,
    5: required string remark,
    6: optional string bank_account,
    7: optional string bank_name,
    8: optional double amount,
}

struct TCAlipayBatchInfo {
    1: required i32 id,
    2: required Timestamp created_at,
}

struct TCBankDrawbackProcessRecord {
    1:optional string bank_name,
    2:optional string bank_branch,
    3:optional string bank_account,
    4:optional string account_holder,
    5:optional i16 account_type,
    6:optional string city,
    7:optional string image_hash,
    8:optional i16 status,
}

struct TCDrawbackProcessRecord {
    1: required i32 id,
    2: required i32 batch_no,
    3: required i32 drawback_id,
    4: required i32 pay_record_id,
    5: required string out_trade_no,
    6: required double amount,
    7: required i16 status,
    8: required i16 pay_platform,
    9: optional i64 order_id,
    10: optional string phone,
    11: optional string user_name,
    12: optional Timestamp failed_at,
    13: optional Timestamp retry_at,
    14: optional Timestamp succeeded_at,
    15: optional i32 process_user_id,
    16: optional Timestamp processing_at,
    17: optional TCBankDrawbackProcessRecord bank_drawback_process_record,
}

struct TCQueryDrawbackProcessRecordResult {
    1: required i32 count,
    2: required list<TCDrawbackProcessRecord> drawback_process_records,
}

struct TCPayReturnInfo {
    1:i32 pay_record_id,
    2:string trade_no,
    3:i32 pay_co_id,
    4:double total_fee,
    5:string customer_pay_id,
    6:string remark,
}

struct TUserProfile {
    1: required i32 id,
    2: required i32 current_address_id,
    3: required double balance,
    4: required i32 point,
    5: required string email,
    6: required i16 is_email_valid,
    7: optional Mobile mobile,
    8: required i16 is_mobile_valid,
    9: required string validate_string,
    10: required string avatar,
    11: optional i32 current_invoice_id,
    12: required i32 user_id,
    13: required i32 payment_quota,
    14: required string payment_password,
    15: required string name,
    16: required i32 certification_type,
    17: required string referal_code,
}

struct TUserPaymentAccount {
    1: required i32 id,
    2: required i32 user_id,
    3: required double balance,
    4: required i32 payment_quota,
}

struct TCheckoutCounterParams {
    1: required list<string> counter_promotions,
    2: required map<i32, list<string>> channel_promotions_map,
    3: required list<i32> channel_sequence,
    4: required list<i32> hidden_channels,
    5: required i32 default_channel,
}

struct TUserPlace {
    1: optional i32 id,
    2: optional i32 user_id,
    3: optional i64 place_id,
    4: optional string place_name,
    5: optional Timestamp created_at,
    6: optional Timestamp last_visit,
    7: optional string pguid,
    8: optional string poi_name,
    9: optional string psn,
}


struct TUser {
    1: required i32 id,
    2: required string username,
    3: optional Timestamp last_login,
    4: optional Timestamp created_at,
    5: required i16 is_active,
    6: required i16 is_super_admin,
}

struct TAutoGeneratedUser {
    1: required i32 user_id,
    2: required i16 is_username_autogenerated,
    3: required i16 is_password_autogenerated,
}


struct TSignupExtendParam {
    1: optional string referal_code,
    2: optional string refer_url,
    3: optional string user_agent,
    4: optional string device_id,
}


struct TBank {
    1: required i16 id,
    2: required string bank_name,
    3: required string cgb_name,
    4: required string cgb_id,
}


struct TMobileLocation {
    1: required i32 id,
    2: required i32 mobile_seg,
    3: required string province,
    4: required string city,
    5: required string carrier,
}

struct TThirdUserSession {
    1: required i32 id,
    2: required string user_id,
    3: required string session_id,
    4: required i16 type,
    5: required Timestamp created_at,
}


struct TUserMessage{
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 type,
    4: required string msg_abstract,
    5: required string content,
    6: required string target_id,
    7: required string url,
    8: required i16 is_read,
    9: optional Timestamp created_at,
    10: optional Timestamp begin_at,
    11: optional Timestamp end_at,
    12: optional Timestamp read_at,
}


struct TFullUser {
    1: required TUser user,
    2: required TUserProfile profile,
}


struct TAddress {
    1: required i32 id,
    2: required i32 user_id,
    3: required string address,
    4: required string phone,
    5: required i16 is_valid,
    6: optional Timestamp created_at,
    7: optional i32 entry_id,
    8: required string phone_bk,
    9: required i64 geohash,
    10: required string name,
    11: optional string st_geohash,
}


struct TAnonymousAddress {
    1: required i32 id,
    2: required string unique_id,
    3: required string address,
    4: required string phone,
    7: optional i32 tag_type,
    8: required string phone_bk,
    9: required i64 geohash,
    10: required string name,
    11: optional string st_geohash,
}


struct TDopUser {
    1: required i32 id,
    2: required i32 user_id,
    3: required string call_user,
    4: required string call_pwd,
    5: required i32 call_status,
    6: required i16 is_online,
    7: required i16 process_type,
    8: optional Timestamp created_at,
    9: optional double weight,
    10: required i32 call_type,
}

struct TInvoice {
    1: required i32 id,
    2: required i32 user_id,
    3: required string invoice_pay_to,
    4: required Timestamp created_at,
}

struct TGift {
    1: required i32 id,
    2: required string name,
    3: required string description,
    4: required string image_url,
    5: required i32 price,
    6: required Timestamp created_at,
    7: required i16 is_valid,
    8: required i16 amount,
    9: optional string thumb_url,
    10: required i16 is_new,
    11: required i16 is_apple_product,
    12: required string image_hash,
    13: required string thumb_hash,

    14: optional i32 weight,
    15: optional string detail,
    16: optional string limitation,
    17: optional i16 gift_type,
    18: optional i16 exchange_type,
    19: optional Timestamp begin_datetime,
    20: optional Timestamp end_datetime,
    21: optional string begin_time,
    22: optional string end_time,
    23: optional double bingo_rate,
}

const string POINT_MALL_GIFT_DAY_LIMIT = 'gift_day_limit'
const string POINT_MALL_USER_DAY_LIMIT = 'user_day_limit'

enum GiftType {
    PHYSICAL = 0,
    EXCHANGE_CODE = 1,
}

enum GiftExchangeType {
    DIRECT = 0,
    LUCK = 1,
}

struct TDeliveryAddress {
    1: optional i32 id,
    2: optional i32 user_id,
    3: optional string name,
    4: optional string address,
    5: optional string phone,
    6: optional string note,
}

struct TGroup {
    1: required i32 id,
    2: required string name,
    3: required string description,
    4: required i32 rank,
    5: required i32 category,
    6: required i32 is_eleme,
}

struct THongbao {
    1: optional i32 id,
    2: optional string sn,
    3: optional i32 user_id,
    4: optional double amount,
    5: optional double used_amount,
    6: optional Timestamp created_at,
    7: optional Timestamp used_at,
    8: optional Timestamp updated_at,
    9: optional string begin_date,
    10: optional string end_date,
    11: optional i32 sum_condition,
    12: optional i32 status,
    13: optional string name,
    14: optional string source,
    15: optional string tag,
    16: optional string phone,
}

struct THongbaoGroup {
    1: required i32 id,
    2: required string sn,
    3: required i64 order_id,
    4: required i16 status,
    5: optional i32 total_count,
    6: optional i32 used_count,
    7: optional double amount,
    8: optional string name,
    9: optional string source,
    10: optional i32 duration,
    11: optional Json url_params,
    12: optional Timestamp created_at,
    13: optional Timestamp updated_at,
}

struct TQRHongbaoGroup {
    1: required i32 city_id,
    2: required string group_source,
    3: required QRHongbaoType group_type,
    4: required double amount,
    5: optional string sn,
    6: optional i16 amount_algo,
    7: optional  i16 status,
    8: optional  i32 duration,
    9: optional  string name,
    10: optional  string source,
    11: optional Timestamp created_at,
    12: optional string expire_date,
    13: optional string logo,
}

struct THongbaoIssuedRecord{
    1: required string sns_username,
    2: required string sns_avatar,
    3: required i32 amount,
    4: required Timestamp created_at,
}

struct TSharedHongbao {
    1: required i32 id,
    2: required string sn,
    3: required string group_sn,
    4: required string sns_uid,
    5: required string sns_username,
    6: required string sns_avatar,
    7: required string phone,
    8: required double amount,
    9: required double sum_condition,
    10: required i16 status,
    11: required string name,
    12: required string source,
    13: required Timestamp created_at,
    14: required Timestamp updated_at,
    15: required string user_id,
}

struct TShareHongbaoResult {
    1: required TSharedHongbao hongbao,
    2: required i16 ret_code,
    3: required list<THongbaoIssuedRecord> hongbao_records,
    4: required string account,
}

struct TSNSPhoneCheckResult {
    1: required Mobile phone,
    2: required bool is_hongbao_used_up,
    3: required list<THongbaoIssuedRecord> hongbao_records,
    4: optional TSharedHongbao hongbao,
}

struct TSNSPhoneCheckResultNew {
    1: required Mobile phone,
    2: required i16 is_hongbao_available,
    3: required list<THongbaoIssuedRecord> hongbao_records,
    4: optional TSharedHongbao hongbao,
}

struct TRefer {
    1: required i32 id,
    2: required i32 from_user_id,
    3: required i32 to_user_id,
    4: required string from_ip,
    5: required string to_ip,
    6: required string from_username,
    7: required string to_username,
    8: required string mobile,
    9: required i16 mobile_status,
    10: required i64 order_id,
    11: required i16 order_status,
    12: required Timestamp created_at,
    13: required string remark,
    14: required string refer_url,
    15: required string user_agent,
    16: required string from_city,
    17: required string to_city,
    18: required string mobile_city,
    19: required string device_id,
}

struct TReferQuery {
    1: optional i32 from_user_id,
    2: optional i32 offset,
    3: optional i32 limit,
    4: optional string from_username,
    5: optional string to_username,
    6: optional string mobile,
}

struct TPermission {
    1: required i32 id,
    2: required string name,
    3: required string description,
    4: required i32 rank,
}

struct TGroupPermission {
    1: required i32 group_id,
    2: required i32 permission_id,
}

struct TUserGift {
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 gift_id,
    4: required string delivery_name,
    5: required string delivery_address,
    6: required string delivery_phone,
    7: required string delivery_note,
    8: required Timestamp created_at,
    9: required i16 processed,
    10: required i16 is_valid,
    11: required string note,

    12: optional string gift_name,
    13: optional i16 gift_type,
    14: optional i16 exchange_type,
    15: optional string attribute,
    16: optional i64 exchange_code_id,
    17: optional i16 bingo,

    18: optional bool need_delivery,
}

enum UserGiftStatus {
    UNPROCESSED = 0,
    PROCESSED = 1,
    PROCESSING = 2,
}


struct TWeiboUserMap {
    1: required i32 id,
    2: required i64 weibo_uid,
    3: required i32 user_id,
    4: required i16 is_bound,
    5: optional Timestamp created_at,
}


struct TWeixinUserMap {
    1: required i32 id,
    2: required string weixin_uid,
    3: required i32 user_id,
    4: optional Timestamp created_at,
}

struct TQQUserMap {
    1: required i32 id,
    2: required string qq_uid,
    3: required i32 user_id,
    4: optional Timestamp created_at,
}

struct TRenrenUserMap {
    1: required i32 id,
    2: required i64 renren_uid,
    3: required i32 user_id,
    4: required i16 is_bound,
    5: optional Timestamp created_at,
    6: required i16 enable_publish,
    7: required i16 publish_order,
    8: required i16 publish_dianping,
}

struct TSNSMapStruct {
    1: required i32 user_id,
    2: required i64 sns_uid,
    3: required SNSType sns_type,
}

struct TSNSMapStructNew {
    1: required i32 user_id,
    2: required string sns_uid,
    3: required SNSType sns_type,
}

struct TGiftQuery {
    1: optional i16 is_apple_product,
    2: optional i16 is_new,
    3: optional i16 is_valid,
    4: optional i16 min_amount,
    5: optional i16 offset,
    6: optional i16 limit,
    7: optional string name,
}

struct TDrawbackProcessRecordQuery {
    1: optional i16 status,
    2: optional i64 order_id,
    3: optional i32 offset,
    4: optional i32 limit,
    5: optional i16 pay_platform,
}

struct TPointChangeRecordQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string sort_key,
    4: optional string sort_type,
    # Filters
    5: required i32 user_id,
    6: optional string start_date,
    7: optional string end_date,
    8: optional i16 delta,
}

struct TWallePointChangeQuery {
    1: required i32 user_id,
    2: optional Timestamp from_datetime,
    3: optional Timestamp to_datetime,

    4: optional i32 offset,
    5: optional i32 limit,
}

struct TPointChangeRecord {
    1:optional i32 id,
    2:optional i32 user_id,
    3:optional Timestamp created_at,
    4:optional i32 delta,
    5:optional string reason,
    6:optional i64 relevant_id,
    7:optional i16 change_type,
}

struct TUserGiftQuery {
    1: optional i16 processed,
    2: optional i16 is_valid,
    3: optional i16 offset,
    4: optional i16 limit,
    5: optional string keyword,
    6: optional i16 obj_status,
}

struct TUserQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string keyword,
    # Filters
    4: optional bool is_active,
    5: optional bool is_super_admin,
    6: optional list<i32> group_ids,
    7: optional i16 category,
    8: optional string mobile,
    9: optional string email,
    10: optional string name,
    11: optional list<i32> region_ids,
    12: optional list<i32> region_group_ids,
    13: optional list<i32> city_ids,
    14: optional list<i32> user_ids,
}

struct TFullUserQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string keyword,
    # Filters
    4: optional bool is_active,
    5: optional bool is_super_admin,
}

struct TFeedbackQuery {
    1: optional list<i32> comment_types,
    # deprecated
    2: optional i32 entry_id,
    # deprecated
    3: optional i32 zone_id,
    # deprecated
    4: optional i32 district_id,
    5: optional i32 city_id,
    6: optional i32 offset,
    7: optional i32 limit,
    8: optional i32 feedback_id,
    9: optional i32 is_processed,
    10:optional i16 is_valid,
    11:optional Timestamp created_at_start,
    12:optional Timestamp created_at_end,
    13:optional string username,
}

struct TFeedbackReplyQuery {
    1: optional i32 user_id,
    2: optional string username,
    3: optional i16 is_valid,
    4: optional i16 is_processed,
    5: optional i16 is_from_admin,
    6: optional i32 offset,
    7: optional i32 limit,
    8: optional Timestamp created_at_start,
    9: optional Timestamp created_at_end,
}

struct TWallePayStatsQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional string sort_key,
    4: optional string sort_type,
    # Filters
    5: optional string date_start,
    6: optional string date_end,
}

struct TBlockedDeviceUserQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i32 user_id,
    4: optional i32 come_from,
    5: optional i32 operator_user_id,
    6: optional string device_id,
}

struct TBlockedDeviceUser {
    1: required i32 id,
    2: required string device_id,
    3: required i32 come_from,
    4: optional string reason,
    5: optional i32 operator_user_id,
    6: optional i32 user_id,
}

struct TDeviceUserQuery {
    1: required string device_id,
    2: required i32 user_id,
    3: optional string version_name,
    4: optional i32 type,
    5: optional string eleme_device_id,
}

struct TDeviceUser {
    1: required i32 come_from,
    2: required i32 id,
    3: required string device_id,
    4: optional i32 user_id,
    5: required double version,
    6: required string version_name,
    7: required i32 type,
    8: required Timestamp created_at,
    9: optional string eleme_device_id,
}

struct THongbaoQuery {
    1: optional i32 user_id,
    2: optional list<i16> statuses,
    3: optional string begin_date_from,
    4: optional string begin_date_to,
    5: optional string end_date_from,
    6: optional string end_date_to,
    7: optional Timestamp created_at_from,
    8: optional Timestamp created_at_to,
    9: optional Timestamp used_at_from,
    10: optional Timestamp used_at_to,
    11: optional i32 limit,
    12: optional i32 offset,
    13: optional string order_by,
    14: optional i32 sum_condition,
    15: optional string source,
    16: optional double amount,
}

struct THongbaoSum {
    1: optional i32 user_id,
    2: optional list<i16> statuses,
    3: optional Timestamp used_at_from,
    4: optional Timestamp used_at_to,
    5: optional string source,
}

struct TOrderPaymentConstitution{
    1: required i32 id,
    2: required i64 order_id,
    3: required i32 user_id,
    4: required i32 trade_record_id,
    5: required i32 balance_or_pay_id,
    6: required i32 pay_type,
    7: required double amount,
    8: required i32 status
}

struct TPayError{
    1: required i32 id,
    2: required string fail_from,
    3: required string ip,
    4: required string description,
    5: required string request_content,
    6: required Timestamp created_at,
}

struct TPayRecord {
    1: required i32 id,
    2: required i32 user_id,
    3: required string trade_no,
    4: required i32 pay_purpose,
    5: required i32 pay_co_id,
    6: required double total_fee,
    7: required string customer_pay_id,
    8: required i32 pay_status,
    9: required string remark,
    10: required Timestamp created_at,
    11: required Timestamp succeeded_at,
    12: required i16 pay_company_id,
    13: required i16 come_from,
    14: required string pay_bank,
    15: required i64 order_id,
    16: required double discount,
}

struct TFeedback {
    1: required i32 id,
    2: required i32 user_id,
    3: required string username,
    4: required Timestamp created_at,
    5: required string content,
    6: required i16 is_valid,
    7: required i16 is_processed,
    8: required i32 entry_id,
    9: required i32 type,
    10: required i32 district_id,
    11: required i32 zone_id,
    12: required i32 city_id,
    13: required i64 geohash,
    14: optional string user_agent,
}

struct TFeedbackReply{
    1: required i32 id,
    2: required i32 feedback_id,
    3: required i32 user_id,
    4: required string username,
    5: required string content,
    6: required i16 is_valid,
    7: required Timestamp created_at,
    8: required i16 is_from_admin,
}

struct TCFeedbackWithReplies{
    1: required TFeedback feedback,
    2: required list<TFeedbackReply> feedback_replies,
}

struct TCFeedbackInfo {
    1: required i32 feedback_id,
    2: required Timestamp feedback_at,
    3: required i16 city_id,
    4: required Geohash geohash,
    5: required i32 reply_id,
    6: required Timestamp reply_at,
    7: required i32 reply_by,
}


struct TWithdrawRecord {
    1: required i32 id,
    2: required i32 user_id,
    3: required double amount,
    4: required i16 status,
    5: required Timestamp created_at,
    6: required string remark,
}

struct TCWithdrawRecord {
    1:required double amount,
    2:required i32 bank_id,
    3:required string cgb_id,
    4:required string card_id,
    5:required string bank_name,
    6:required string cardholder_name,
    7:required i32 withdraw_id,
}

struct TCDrawbackRecord {
    1:required string username,
    2:required double amount,
    3:required string out_trade_no,
    4:required string trade_no
}

struct TCDrawbackResultInfoQuery {
    1:optional string username,
    2:optional i64 order_id,
}

struct TCPrettyPayRecord {
    1:required string pay_company_name,
    2:required string trade_no,
    3:required string out_trade_no,
}

struct TCDrawbackResultInfo {
    1:required string username,
    2:required double amount,
    3:required Timestamp created_at,
    4:required Timestamp processed_at,
    5:required list<TCPrettyPayRecord> pay_records,
}

struct TCDrawbackResultInfoNew {
    1: required string username,
    2: required double amount,
    3: required Timestamp created_at,
    4: required Timestamp processed_at,
    5: required i16 status,
    6: required list<TCDrawbackProcessRecord> drawback_process_records,
}



struct TCDrawbackReport {
    1:required list<TCDrawbackRecord> mobile_records,
    2:required string batch_report,
    3:required string tenpay_app_report,
    4:required string tenpay_web_report,
    5:required list<TCDrawbackRecord> shengpay_records,
    6:required string shengpay_report,
}

struct TWalleWithdrawApplyQuery {
    1: optional list<i16> statuses,
    2: optional i32 restaurant_id,
    3: optional i32 offset,
    4: optional i32 limit,
    5: optional Timestamp from_created_at,
    6: optional Timestamp to_created_at,
}

struct TWalleWithdrawRecordQuery {
    1: optional list<i16> statuses,
}

struct TCWalleWithdrawApply {
    1:required i32 id,
    2:required i32 user_id,
    3:required double amount,
    4:required i16 status,
    5:required Timestamp created_at,
    6:required string remark,

    7:required string card_id,
    8:required string bank_name,
    9:required string cardholder_name,
    10:required i32 restaurant_id,
    11:required string restaurant_name,
    12:required string username,
    13:required i32 bank_id,
}

struct TTerminalValidation
{
   1: required i32 id,
   2: required i32 user_id,
   3: required string terminal,
   4: required i16 terminal_type,
   5: required string validate_code,
   6: required i16 is_valid,
   7: required i16 lives,
   8: required Timestamp created_at,
   9: required i16 is_success,
   10: required Timestamp succeeded_at,
   11: required i16 is_used,
   12: required string ip,
}

struct TTerminalValidationQuery
{
    1: optional i32 user_id,
    2: optional i16 is_valid,
    3: optional i16 is_success,
    4: optional i16 is_used,
    5: optional string ip,
    6: optional i16 terminal_type,
    7: optional string terminal,
    8: optional Timestamp created_at,
    9: optional i16 lives,
    10: optional i32 offset,
    11: optional i32 limit,
    12: optional string orderby,
}

struct TRestaurantAdmin {
    1: required i32 restaurant_id,
    2: required i32 user_id,
}

struct TSfGuardRememberKey {
    1: required i32 user_id,
    2: required string remember_key,
    3: required string ip_address,
    4: required Timestamp created_at,
}

struct TUserBankcard {
    1:required i32 id,
    2:required i32 user_id,
    3:required string card_id,
    4:required i32 bank_id,
    5:required string cardholder_name,
    6:required i16 status,
    7:required Timestamp created_at,
    8:optional string city_name,
    9:optional string branch_name,
}

struct TUserMetaData {
    1:required i32 id,
    2:required i32 user_id,
    3:required string username,
    4:required i32 refer_count,
    5:required Timestamp succeeded_at
}

struct TUserMetaDataQuery {
    1:optional i32 offset,
    2:optional i32 limit,
}

struct TUserReferRank {
    1:optional i32 rank,
    2:optional string prize,
}

struct TWalleOnlinePaymentApplyQuery {
    1:optional i16 status,
    2:optional i32 bank_id,
    3:optional string search,
    4:optional list<i32> region_ids,

    5:optional i32 offset,
    6:optional i32 limit,
}

struct TCWalleOnlinePaymentApply {
    1:required i32 id,
    2:required i32 user_id,
    3:required string card_id,
    4:required i32 bank_id,
    5:required string cardholder_name,
    6:required i16 status,
    7:required Timestamp created_at,

    8:required i32 restaurant_id,
    9:required string restaurant_name,
    10:required string username,
    11:required string bank_name,
}

struct TCUserBankCard {
    1:required i32 id,
    2:required i32 user_id,
    3:required string card_id,
    4:required i32 bank_id,
    5:required string cardholder_name,
    6:required string username,
    7:required string bank_name,
}

struct TUserProfileQuery {
    1:optional string email,
    2:optional i16 is_email_valid,
    3:optional Mobile mobile,
    4:optional i16 is_mobile_valid,
    5:optional string referal_code,
}

struct TCAccountDailyStats {
    1:required i32 type,
    2:required double amount,
    3:required i32 count,
    4:required string date
}

struct TTradeRecordQuery {
    1:optional Timestamp from_datetime,
    2:optional Timestamp to_datetime,
    3:optional list<i32> categories,
    4:optional list<i32> statuses,
    5:optional i32 user_id,
    6:optional i32 offset,
    7:optional i32 limit,
    8:optional i16 asc,
}

struct TTradeRecord {
    1:required i32 id,
    2:required i32 user_id,
    3:required i32 type,
    4:required string trade_no,
    5:required double amount,
    6:required i32 status,
    7:required string remark,
    8:required Timestamp created_at,
    9:required Timestamp finished_at,
}

struct TLoginStruct {
    1:required i32 user_id,
    2:required string ip,
    3:optional string key,
}

struct TLoginInfo {
    1:required i32 id,
    2:required i32 user_id,
    3:required Timestamp created_at,
    4:required string username,
    5:required string ip,
}

struct TLoginInfoQuery {
    1:optional i32 user_id,
    2:optional Timestamp from_datetime,
    3:optional Timestamp to_datetime,
    4:optional string ip,
    5:optional i32 offset,
    6:optional i32 limit,
}

struct TUserBalanceChangeQuery {
    1:optional list<i32> user_ids,
    2:optional list<i32> trade_types,
    3:optional i32 pay_method,
    4:optional Timestamp from_datetime,
    5:optional Timestamp to_datetime,
}

struct TCWalleBalanceChange {
    1:optional i32 id,
    2:optional i32 user_id,
    3:optional double balance,
    4:optional double balance_change,
    5:optional string  trade_no,
    6:optional i16 trade_type,
    7:optional i16 pay_method,
    8:optional Timestamp created_at,
    9:optional string alipay_trade_no,
}

struct TCWalleUserHongbao {
    1: required string hongbao_sn,
    2: optional Timestamp created_at,
    3: optional double amount,
    4: optional double sum_condition,
    5: optional string begin_date,
    6: optional string end_date,
    7: optional i16 status,
    8: optional string name,
    9: optional string username,
    10: optional string phone,
    11: optional i64 order_id,
}

struct TCWalleHongbaoExchange {
    1: required string exchange,
    2: optional double amount,
    3: optional double sum_condition,
    4: optional Timestamp created_at,
    5: optional string end_date,
    6: optional i16 status,
    7: optional string hongbao_sn,
    8: optional string phone,
}

struct TCWalleHongbaoGroup {
    1: optional i64 order_id,
    2: optional string phone,
    3: optional i16 total_count,
    4: optional i16 used_count,
    5: optional i16 status,
    6: optional string source,
    7: optional Timestamp updated_at,
}

struct TCWallePayStatsOverview {
    1:optional i32 count,
    2:optional double amount,
}

struct TCWallePayStatsDetail {
    1:optional i32 count,
    2:optional double amount,
    3:optional string user_name,
}


struct TWalleBalanceChangeQuery {
    1:required i32 user_id,
    2:optional list<i16> trade_types,
    3:optional list<i16> pay_methods,
    4:optional Timestamp from_datetime,
    5:optional Timestamp to_datetime,
    6:optional i32 offset,
    7:optional i32 limit,
}

struct TWalleHongbaoQuery {
    1: optional i32 user_id,
    2: optional string phone,
    3: optional string sn,
    4: optional i64 order_id,
    5: optional i16 status,
    6: optional string source,
    7: optional Timestamp from_datetime,
    8: optional Timestamp to_datetime,
    9: optional i32 offset,
    10: optional i32 limit,
}

struct TUserPlaceQuery
{
    1:optional i32 user_id,
    2:optional i64 place_id,
    3:optional i32 limit,
    4:optional string psn,
}

struct TAlipayInfo {
    1:optional i32 id,
    2:optional string seller_account,
    3:optional string callback_url,
    4:optional string web_notify_url,
    5:optional string app_notify_url,
    6:optional string sign_url,
    7:optional string verify_url,
    8:optional string decrypt_url,
    9:optional string v2_callback_url,
}

struct TWithdrawProcessRecord {
    1:optional i32 id,
    2:optional string batch_id,
    3:optional i32 withdraw_id,
    4:optional string card_id,
    5:optional i32 bank_id,
    6:optional string cardholder_name,
    7:optional double amount,
    8:optional i16 status,
    9:optional Timestamp processed_at,
    10:optional Timestamp finished_at,
    11:optional string reason,
}

struct TCWithdrawProcessBatch {
    1:optional string batch_id,
    2:optional i16 total,
    3:optional i16 success,
    4:optional i16 warning_fail,
    5:optional i16 fatal_fail,
    6:optional Timestamp time,
    7:optional i16 is_finished,
}

struct TUserCertification {
    1:optional i32 id,
    2:optional i32 user_id,
    3:optional i32 certification_type,
    4:optional string person_name,
    5:optional string person_certification_id,
    6:optional string person_certification_image_front,
    7:optional string person_certification_image_back,
    8:optional string corporation_name,
    9:optional string business_license_id,
    10:optional string business_license_location,
    11:optional string business_license_expiration_date,
    12:optional string business_license_image,
    13:optional string address,
    14:optional string phone,
    15:optional i16 status,
    16:optional string corporation_phone,
    17:optional Timestamp created_at,
}

struct TUserCertificationApply {
    1:optional i32 certification_type,
    2:optional string person_name,
    3:optional string person_certification_id,
    4:optional string person_certification_image_front,
    5:optional string person_certification_image_back,
    6:optional string corporation_name,
    7:optional string business_license_id,
    8:optional string business_license_location,
    9:optional string business_license_expiration_date,
    10:optional string business_license_image,
    11:optional string address,
    12:optional string phone,
    13:optional string corporation_phone,
}

struct TUserCertificationQuery{
    1:optional list<i32> certification_types,
    2:optional list<i32> statuses,
    3:optional Timestamp from_created_at,
    4:optional Timestamp to_created_at,
    5:optional i32 offset,
    6:optional i32 limit,
    7:optional i32 user_id,
}

struct TCUserCertificationProcessRecord {
    1:optional i32 id,
    2:optional i32 user_id,
    3:optional i16 from_status,
    4:optional i16 to_status,
    5:optional string remark,
    6:optional i32 process_user_id,
    7:optional Timestamp created_at,
    8:optional string description,
    9:optional string username,
}

struct TUserChangeRecord {
    1: required i32 id,
    2: required i32 user_id,
    3: required i32 admin_user_id,
    4: required string description,
    5: required string process_type,
    6: required string from_value,
    7: required string to_value,
    8: required Timestamp created_at,
}

struct TUserChangeRecordQuery {
    1: optional i32 limit,
    2: optional i32 offset,
    3: optional i32 user_id,
    4: optional i32 admin_user_id,
    5: optional string process_type,
}

struct TUserCustomMenu {
    1: optional i32 id,
    2: optional i32 user_id,
    3: optional string name,
    4: optional string category,
    5: optional i32 rank,
    6: optional string rule,
    7: optional i32 is_valid,
    8: optional Timestamp created_at,
}

/**
 * Exceptions
 */
enum EUSErrorCode {
    UNKNOWN_ERROR = 0,
    ADDRESS_NOT_FOUND = 1,
    ALIPAY_ACCOUNTS_INVALID = 2,
    ALREADY_BIND_EMAIL = 3,
    ALREADY_BIND_MOBILE = 4,
    ANDROID_MESSAGE_NOT_FOUND = 5,
    ANONYMOUS_USER_CANT_CHARGE = 6,
    BANKCARD_BIND_RECORD_NOT_FOUND = 7,
    BANK_DRAWBACK_PROCESS_RECORD_NOT_FOUND = 8,
    BANK_NOT_FOUND = 9,
    BATCH_LOG_WRONG_FORMAT = 10,
    BATCH_NOT_FOUND = 11,
    CANT_PAY_FOR_ORDER = 12,
    CANT_PAY_FOR_CONTRACT = 13,
    CGB_ACCOUNTS_INVALID = 14,
    CUSTOMER_SERVICE_NOT_FOUND = 15,
    DOP_USER_NOT_FOUND = 16,
    DRAWBACK_RECORD_NOT_FOUND = 17,
    DRAWBACK_PROCESS_RECORD_NOT_FOUND = 18,
    DRAWBACK_PROCESS_BATCH_NOT_FOUND = 19,
    DUPLICATED_BANKCARD = 20,
    DUPLICATED_BIND_CARD_REQUEST = 21,
    DUPLICATED_DRAWBACK_ANONYMOUS_ORDER = 22,
    EMAIL_OCCUPIED = 23,
    EMAIL_VALIDATION_TOO_FREQUENT = 24,
    EPAY_WRONG_AMOUNT = 25,
    FEEDBACK_NOT_FOUND = 26,
    FEEDBACK_TOO_FREQUENT = 27,
    GENERATED_RECORD_NOT_FOUND = 28,
    HONGBAO_AMOUNT_NOT_ENOUGH = 31,
    HONGBAO_INVALID = 32,
    HONGBAO_NOT_FOUND = 33,
    HONGBAO_OTHER_PEOPLES = 34,
    HONGBAO_USED = 35,
    HONGBAO_USE_LIMIT_EXCEED = 36,
    HONGBAO_GENERATE_LIMIT_EXCEED = 37,
    HONGBAO_MOBILE_NOT_MATCH = 38,
    HONGBAO_GROUP_NOT_FOUND = 39,
    QRHONGBAO_GROUP_NOT_FOUND = 40,
    QRHONGBAO_GROUP_EXPIRED = 41,
    QR_AMOUNT_ALGO_NOT_VALID = 42,
    QRHONGBAO_EXPIRE_TOO_LONG = 43,
    USER_NOT_ALLOWED = 44,
    HONGBAO_GROUP_TIME_OUT = 45,
    INSUFFICIENT_BALANCE = 46,
    INVALID_BANKCARD_ID = 47,
    INVALID_EMAIL = 48,
    INVALID_BACKUP_PHONE = 49,
    INVALID_DATE = 50,
    INVALID_HONGBAO_EXCHANGER = 51,
    INVALID_EXCHANGE_FREQUENCY = 52,
    INVALID_MOBILE = 53,
    INVALID_PASSWORD = 54,
    INVALID_PAY_COME_FROM = 55,
    INVALID_PAY_COMPANY_ID = 56,
    INVALID_PAY_METHOD_REMARK = 57,
    INVALID_PAY_RECORD = 58,
    INVALID_PAY_RETURN_INFO = 59,
    INVALID_RESTAURANT = 60,
    INVALID_TIME_RANGE = 61,
    INVALID_USER = 62,
    INVALID_USERNAME = 63,
    INVALID_VALIDATE_REQUEST = 64,
    INVALID_VERIFY_CODE = 65,
    INVOICE_NOT_FOUND = 66,
    IOS_MESSAGE_NOT_FOUND = 67,
    IP_CHANGED = 68,
    IP_PARSER_NOT_WORK = 69,
    MESSAGE_USER_NOT_MATCH = 70,
    MOBILE_AUTH_FAIL = 71,
    MOBILE_LOCATION_NOT_FOUND = 72,
    MOBILE_OCCUPIED = 73,
    MOBILE_VALIDATE_QUOTA_OUT = 74,
    NO_COUPON_SOURCE = 75,
    NO_EMAIL_BOUND = 76,
    NO_MOBILE_BOUND = 77,
    ONLINE_PAYMENT_RESTAURANT_MUST_HAVE_ADMIN = 78,
    ORDER_PAYMENT_CONSTITUTION_NOT_FOUND = 79,
    PAY_FOR_ORDER_TIMEOUT = 80,
    PAY_RECORD_MAKE_TOO_FREQUENTLY = 81,
    PAY_RECORD_NOT_FOUND = 82,
    PAY_RECORD_TRADE_NO_DUPLICATED = 83,
    PERMISSION_DENIED = 84,
    PROFILE_CHANGE_QUOTA_OUT = 86,
    REMEMBER_KEY_NOT_FOUND = 87,
    RENREN_USER_MAP_NOT_FOUND = 88,
    RESTAURANT_ADMIN_NOT_FOUND = 89,
    RESTAURANT_ALREADY_HAVE_ADMIN = 90,
    SNS_ALREADY_BOUND_OTHER = 91,
    SNS_OCCUPIED = 92,
    THIRD_USER_SESSION_NOT_FOUND = 93,
    TRADE_RECORD_NOT_FOUND = 94,
    USERNAME_ALREADY_USED = 95,
    USER_ALREADY_RESTAURANT_ADMIN = 96,
    USER_AUTH_FAIL = 97,
    MOBILE_LOGIN_AUTH_FAIL = 98,
    USER_BALANCE_CHANGE_NOT_FOUND = 99,
    USER_BANKCARD_NOT_FOUND = 100,
    USER_BANKCARD_ALL_INVALID = 101,
    USER_CERTIFICATION_NOT_FOUND = 102,
    USER_CERTIFICATION_APPLY_TYPE_INVALID = 103,
    USER_CERTIFICATION_APPLY_TYPE_NOT_FOUND = 104,
    USER_CERTIFICATION_APPLY_PASS_EDIT = 105,
    USER_CERTIFICATION_FIRST = 106,
    USER_CERTIFICATION_PROCESS_RECORD_NOT_FOUND = 107,
    USER_CERTIFICATION_DUPLICATE = 108,
    CARDHOLDER_NAME_NOT_MATCH = 109,
    USER_GROUP_NOT_FOUND = 111,
    USER_MESSAGE_NOT_FOUND = 112,
    USER_META_DATA_NOT_FOUND = 113,
    USER_NOT_FOUND = 114,
    USER_DOES_NOT_EXIST = 115,
    USER_PLACE_NOT_FOUND = 116,
    USER_PROFILE_NOT_FOUND = 117,
    MOBILE_BINDED = 118,
    MOBILE_NOT_BINDED = 119,
    ERROR_SNS_ID = 120,
    USERNAME_READONLY = 121,
    PASSWORD_UPDATE_ONLY = 122,
    VALIDATE_CODE_EXPIRED = 123,
    VALIDATE_CODE_QUOTA_OUT = 124,
    WEIBO_USER_MAP_NOT_FOUND = 125,
    WEIXIN_USER_MAP_NOT_FOUND = 126,
    WITHDRAW_RECORD_NOT_FOUND = 127,
    WITHDRAW_RECORD_CANT_SUBMIT = 128,
    WITHDRAW_RECORD_ALREADY_SUBMITTED = 129,
    WITHDRAW_PROCESS_RECORD_NOT_FOUND = 130,
    WITHDRAW_TOO_FREQUENTLY = 131,
    WITHDRAW_TOO_MUCH = 132,
    DAILY_WITHDRAW_OUT_OF_LIMIT = 133,
    WRONG_ACTIVE_CODE = 134,
    WRONG_AMOUNT = 135,
    WRONG_PASSWORD_RETRIEVAL_TOKEN = 136,
    ALREADY_BIND_BANKCARD = 137,
    USER_EXISTED_BUT_NOT_RESTAURANT_ADMIN = 138,
    NOT_TESTER_USER = 139,
    MENU_NOT_FOUND = 140,
    USER_AUTH_OLD_PASSWORD_ERROR = 141,
    USER_NOT_AUTOGENERATED = 142,
    VALIDATION_ERROR = 143,
    VALIDATION_NONEXIST_ERROR = 144,
    SNS_RECORD_NOT_FOUND = 145,
    SNS_UNBIND_ERROR = 146,
    USER_PAYMENT_ACCOUNT_NOT_FOUND = 147,
    NO_CHECKOUT_COUNTER_PARAMS = 148,
    EES_CLIENT_ERROR = 149,
    EOS_CLIENT_ERROR = 150,
    ERS_CLIENT_ERROR = 151,
    SMS_CLIENT_ERROR = 152,
    GEOS_CLIENT_ERROR = 153,

    DATABASE_ERROR = 154,
    INVALID_PARAMETERS = 155,
    USERNAME_ALL_NUMBER = 156,
    USERNAME_CONTAIN_SPECIAL_CHARACTER = 157,
    UNSAFE_PASSWORD = 158,
    // Append New Error Code Here..

    # point_mall error between 1000 - 1099
    GIFT_EXCHANGE_TOO_BUSY = 1000,
    USER_GIFT_NOT_FOUND = 1001,
    GIFT_NOT_FOUND = 1002,
    GIFT_REMAIN_NONE = 1003,
    POINT_NOT_ENOUGH = 1004,
    GIFT_LIMIT_ERROR = 1005,
    BINGO_RATE_TOO_LARGE = 1006,
}

exception EUSUserException {
    1: required EUSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EUSSystemException {
    1: required EUSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EUSUnknownException {
    1: required EUSErrorCode error_code,
    2: required string error_name,
    3: required string message,
}

/**
 * Services
 */
service ElemeUserService {
    /**
     * Base services
     */
    bool ping()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void clear_cache(1:string api_name,
                     2:list<string> params)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_cache_for_replicator(1:string name, 2:list<i64> ids, 3: string type_)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_cache(1:string tablename,
                      2:list<i64> ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    i32 auth(1:string username,
             2:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # weibo and renren only, use sns_auth_new for all sns type
    i32 sns_auth(1:i64 sns_uid,
                 2:SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 sns_auth_new(1:string sns_uid,
                     2:SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 signup(1:string username,
               2:string email,
               3:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 web_signup(1:string username,
                   2:string email,
                   3:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 sync_new_user(1:string username,
                      2:string name,
                      3:string email,
                      4:Mobile mobile,
                      5:i32 group_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 extend_signup(1:string username,
                      2:string email,
                      3:TSignupExtendParam extend_param,
                      4:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TMobileLocation get_mobile_location(1:string mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 mobileclient_signup(1:Mobile mobile,
                            2:string validation_code,
                            3:TSignupExtendParam extend_param,
                            4:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 hermes_mobileclient_signup(1:Mobile mobile,
                            2:string validation_code,
                            3:TSignupExtendParam extend_param,
                            4:string password
                            5:string sender_key)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 napos_mobileclient_signup(1:Mobile mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 mobileclient_validation_code_login(1:Mobile mobile,
                                           2:string validation_code)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 hermes_mobileclient_validation_code_login(1:Mobile mobile,
                                                  2:string validation_code,
                                                  3:string sender_key)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    i32 mobileclient_mobile_login(1:Mobile mobile
                                  2:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mobileclient_set_username(1:i32 user_id,
                                   2:string username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mobileclient_set_password(1:i32 user_id,
                                   2:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 mobileclient_reset_password(1:Mobile mobile,
                                    2:string validation_code,
                                    3:string new_password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    i32 hermes_mobileclient_reset_password(1:Mobile mobile,
                                    2:string validation_code,
                                    3:string new_password,
                                    4:string sender_key)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mobileclient_update_password(1:i32 user_id,
                                      2:string validation_code,
                                      3:string new_password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void hermes_mobileclient_update_password(1:i32 user_id,
                                      2:string validation_code,
                                      3:string new_password,
                                      4:string sender_key)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 mobileclient_sns_login(1:i32 sns_type,
                               2:string sns_uid,
                               3:string sns_username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 mobileclient_sns_login_new(1:i32 sns_type,
                                   2:string sns_uid,
                                   3:string sns_username,
                                   4:i16 device_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAutoGeneratedUser get_auto_generated_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<map<i32, list<TRefer>>> get_pending_refer()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    list<map<i32, list<TRefer>>> get_suspicious_refer()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    string get_user_referal_code(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool is_user_refered(1:i32 user_id, 2:string mode)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void temp_super_user_bind(1:string username,
                              2:string mobile,
                              3:i32 restaurant_id,
                              4:i32 bank_id,
                              5:string card_id,
                              6:string cardholder_name,
                              7:i32 process_user_id,
                              )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void third_signup(1:string user_id,
                      2:string session_id,
                      3:i32 user_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool is_username_available(1:string username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void save_dop_user(1:i32 nid,
                       2:TDopUser save_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # deprecated, use force_reset password instead
    void reset_password(1:i32 user_id,
                        2:string new_password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void force_reset_password(1: i32 user_id,
                              2: i32 admin_user_id,
                              3: string new_password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void user_reset_password(1: i32 user_id,
                             2: string new_password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_password(1:i32 user_id,
                         2:string old_password,
                         3:string new_password
                         4:string current_session)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void clean_session(1:i32 user_id,
                       2:string current_session)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void post_login(1:TLoginStruct login_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_avatar(1:i32 user_id,
                    2:string avatar)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bind_sns(1:i32 user_id,
                  2:i64 sns_uid,
                  3:SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bind_sns_new(1:i32 user_id,
                      2:string sns_uid,
                      3:SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void renren_purify(1:i32 user_id,
                       2:string username,
                       3:string email,
                       4:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void unbind_sns(1:i32 user_id,
                    2:SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bind_device(1:i32 user_id,
                     2:DeviceId device_id,
                     3:DeviceType device_type,
                     4:double version,
                     5:i32 come_from,
                     6:DeviceId eleme_device_id,
                     7:string version_name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void unbind_device(1:i32 user_id,
                       2:DeviceId device_id,
                       3:DeviceType device_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # deprecated, use update_user_email instead
    void update_email(1:i32 user_id,
                      2:string email)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_user_email(1: i32 user_id,
                           2: i32 admin_user_id,
                           3: string email)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_tester_user_profile(1: i32 tester_user_id,
                                    2: double balance,
                                    3: i32 point,
                                    4: Mobile mobile,
                                    5: i32 payment_quota,
                                    6: i32 is_mobile_valid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool update_username(1: i32 user_id,
                         2: i32 op_user_id,
                         3: string username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_mobile(1:i32 user_id,
                       2:Mobile mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_update_mobile_and_name(1:i32 user_id,
                                      2:Mobile mobile,
                                      3:string name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bind_mobile(1:i32 user_id,
                     2:Mobile mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # to be deprecated
    i32 add_address(1:i32 user_id,
                    2:i32 entry_id,
                    3:Geohash geohash,
                    4:string phone,
                    5:string address,
                    6:string phone_bk)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 add_address_new(1:i32 user_id,
                        2:string address,
                        3:string phone,
                        4:string phone_bk,
                        5:string name,
                        6:Geohash geohash)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAddress update_address_new(1:i32 user_id,
                            2:i32 address_id,
                            3:string address,
                            4:string phone,
                            5:string phone_bk,
                            6:string name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # deprecated
    TAddress update_address(1:i32 user_id,
                        2:i32 address_id,
                        3:string phone,
                        4:string address,
                        5:string phone_bk)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 add_address_with_tag(1:TAddress address)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAddress add_anonymous_address(1:TAnonymousAddress address)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAddress update_address_with_tag(1:TAddress address)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAddress update_anonymous_address(1:TAnonymousAddress address)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_address(1:i32 user_id,
                        2:i32 address_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_anonymous_address(1:i32 address_id,
                                  2:string unique_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_default_address(1:i32 user_id,
                             2:i32 address_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_groups(1:i32 user_id,
                    2:list<i32> group_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 add_invoice(1:i32 user_id,
                    2:string invoice_pay_to)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_invoice(1:i32 user_id,
                        2:i32 invoice_id,
                        3:string invoice_pay_to)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_invoice(1:i32 user_id,
                        2:i32 invoice_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_default_invoice(1:i32 user_id,
                             2:i32 invoice_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_unprocessed_user_gift()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mset_user_gift_status(1:list<i32> user_gift_ids,
                               2:i16 processed)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mset_user_gift_valid(1:list<i32> user_gift_ids,
                              2:bool is_valid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void reject_exchange_gift(1:list<i32> user_gift_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mset_feedback_reply_valid(1:list<i32> reply_ids,
                                   2:bool valid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_bankcard(1: i32 bankcard_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_user_gift(1:TUserGift update_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 save_gift(1: i32 gift_id,
                  2: TGift save_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TDeliveryAddress save_delivery_address(1: TDeliveryAddress save_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void exchange_gift(1:i32 user_id,
                       2:i32 gift_id,
                       3:string delivery_name,
                       4:string delivery_address,
                       5:string delivery_phone,
                       6:string delivery_note)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserGift exchange_gift2(1:i32 user_id,
                             2:i32 gift_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void add_delivery_address_for_user_gift(1:i32 user_gift_id
                                            2:TDeliveryAddress t_delivery_address)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void analyse_user_gift(1:i32 user_gift_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 change_point(1:i32 user_id,
                     2:i32 point_change,
                     3:string reason,
                     4:i64 relevant_id,
                     5:i16 change_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_rate_message_read(1:string target_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool check_restaurant_admin(1:i32 user_id,
                                2:i32 restaurant_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool check_service_admin(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_unread_message(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mark_message_as_read(1:i32 user_id,
                              2:i32 message_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mark_all_message_as_read(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<string> get_user_permission(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_pay_record_method(1:i32 user_id,
                               2:i32 pay_record_id,
                               3:string method_json)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 add_feedback(1:i32 user_id,
                     2:string content,
                     3:i32 comment_type,
                     4:i32 entry_id,
                     5:i32 zone_id,
                     6:i32 district_id,
                     7:i32 city_id,
                     8:i64 geohash,
                     9:string user_agent)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TFeedback> mget_feedback(1:list<i32> feedback_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_feedback(1:TFeedbackQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TFeedback> query_feedback(1:TFeedbackQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCFeedbackWithReplies> query_feedback_with_replies(
        1:TFeedbackQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_feedback_reply(1:TFeedbackReplyQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TFeedbackReply> query_feedback_reply(1:TFeedbackReplyQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    void feedback_reply(1:i32 feedback_id,
                        2:i32 user_id,
                        3:string content)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void add_restaurant_admin(1:i32 restaurant_id,
                              2:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_restaurant_admin(1:i32 restaurant_id,
                                 2:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void modify_payment_quota(1:i32 user_id,
                              2:i16 payment_quota,
                              3:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string generate_email_validate_str(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool validate_old_mobile(1:i32 user_id,
                             2:string mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string send_validate_code(1:i32 user_id,
                              2:string terminal,
                              3:i32 terminal_type,
                              4:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool validate_terminal(1:i32 user_id,
                           2:string terminal,
                           3:i32 terminal_type,
                           4:string validate_code,
                           5:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool unbind_terminal(1:i32 user_id,
                         2:i32 terminal_type,
                         3:string validate_code,
                         4:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void send_notice(1: i32 user_id,
                     2: i16 type_code,
                     3: string title,
                     4: string content)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void send_unsent_notice()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void send_unsent_notice_by_user(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # deprecated, use send_coupon_by_sms2 instead
    string send_coupon_by_sms(1:i64 mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string send_coupon_by_sms2(1:i64 mobile, 2:string source)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bind_email(1: i32 user_id,
                    2: string email)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void active_email(1: string active_code)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string generate_retrieval_password_final_token(1:string email)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 reset_forgetted_password(1:string final_token
                                 2:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool check_password_retrieval_token(1:string final_token)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),


    i32 get_user_point_change_except_order(1:i32 user_id,
                                           2:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void save_pay_error(1:i32 error_id, 2:TPayError t_error)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TPayRecord get_pay_record(1:i32 record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TPayRecord get_pay_record_by_unique_id(1:i64 unique_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 get_pay_record_id_by_order_id(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i64 get_order_id_by_pay_record_id(1:i32 pay_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool check_function_blocked(1:i32 user_id,
                                2:i32 func)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_trade_record(1:TTradeRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string parse_ip(1:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    double sum_balance_change(1:TUserBalanceChangeQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 set_user_place(1: TUserPlace set_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void delete_user_place(1: list<i32> id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    /**
     * App services
     */
    list<TCAccountDailyStats> account_get_stats(1:i32 user_id,
                                                2:Timestamp begin_datetime,
                                                3:Timestamp end_datetime)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    double account_get_stats_by_type(1:i32 user_id,
                                     2:i32 type_code)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGroup> walle_get_all_groups()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TPermission> walle_get_all_permissions()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGroupPermission> walle_get_all_group_permissions()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_add_group_permission(1:i32 group_id,
                                    2:i32 permission_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_remove_group_permission(1:i32 group_id,
                                       2:i32 permission_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_save_group(1:i32 group_id,
                          2:TGroup group_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_save_permission(1:i32 permission_id,
                               2:TPermission permission_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_balance_change(1:TWalleBalanceChangeQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleBalanceChange> walle_query_balance_change(1:TWalleBalanceChangeQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_user_hongbao(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleUserHongbao> walle_query_user_hongbao(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_hongbao_exchange(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleHongbaoExchange> walle_query_hongbao_exchange(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_hongbao_group(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleHongbaoGroup> walle_query_hongbao_group(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_weixin_hongbao_record(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TSharedHongbao> walle_query_weixin_hongbao_record(1: TWalleHongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_withdraw_apply(1:TWalleWithdrawApplyQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleWithdrawApply> walle_query_withdraw_apply(1:TWalleWithdrawApplyQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_withdraw_record(1:TWalleWithdrawRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_mset_withdraw_process_record_batch_id(
        1:list<i32> ids,
        2:string batch_id
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TWithdrawRecord> walle_query_withdraw_record(1:TWalleWithdrawRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TWithdrawRecord> walle_mget_withdraw_record(1:list<i32> ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_mset_withdraw_record_status(1:list<i32> ids, 2:i16 status)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TWithdrawProcessRecord walle_get_latest_withdraw_process_record_by_withdraw_id(
        1: i32 withdraw_id,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_bind_email(1: i32 user_id,
                          2: i32 admin_user_id,
                          3: string email)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TDopUser> walle_get_online_sev(1:list<i16> process_types)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string walle_get_point_change_list(1:TPointChangeRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string walle_get_user_list(1:TUserQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string walle_get_user_gift_list(1:TUserGiftQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string walle_get_user_gift_list_by_ids(1:list<i32> user_gift_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    # deprecated, use walle_set_user_active instead
    void walle_set_active(1:i32 user_id,
                          2:bool is_active)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_set_user_active(1: i32 user_id,
                               2: i32 admin_user_id,
                               3: i32 is_active,
                               4: string description)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_set_name(1:i32 user_id,
                        2:string name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_set_super_admin(1:i32 user_id,
                               2:bool is_super_admin)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_delete_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_unbind_email(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_unbind_mobile(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool walle_change_mobile(1: i32 user_id,
                             2: i32 admin_user_id,
                             3: Mobile new_mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_online_payment_apply(
        1:TWalleOnlinePaymentApplyQuery query_struct
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWalleOnlinePaymentApply> walle_query_online_payment_apply(
        1:TWalleOnlinePaymentApplyQuery query_struct
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TPointChangeRecord> walle_query_point_change(1:TWallePointChangeQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_point_change(1:TWallePointChangeQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_get_pay_stats_detail_count(
        1:TWallePayStatsQuery query_struct,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCWallePayStatsOverview walle_get_pay_stats_overview(
        1:TWallePayStatsQuery query_struct,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWallePayStatsDetail> walle_get_pay_stats_detail(
        1:TWallePayStatsQuery query_struct,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_mset_feedback_processed(
        1:list<i32> feedback_ids,
        2:bool is_processed,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWithdrawProcessBatch> walle_query_withdraw_process_batch(
        1: list<i16> statuses,
        2: string batch_id
        3: i32 offset,
        4: i32 limit,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void walle_mset_feedback_valid(
        1:list<i32> feedback_ids,
        2:bool is_valid,
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_count_withdraw_process_batch(
        1: list<i16> statuses,
        2: string batch_id
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TWithdrawProcessRecord> walle_get_withdraw_process_record_by_batch_id(
        1: string batch_id
    )
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<i32> dms_get_dop_user_list()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string mobile_third_signup(1:string third_user_id,
                               2:string session_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TDeviceUser> query_device_user(1:TDeviceUserQuery query)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TBlockedDeviceUser> mobile_query_blocked_device_user_list(1:TBlockedDeviceUserQuery query)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TSNSMapStruct> mobile_get_sns_map(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TSNSMapStructNew> mobile_get_sns_map_new(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mobile_save_food_image(1:i32 user_id,
                                2:i32 food_id,
                                3:string image_hash)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void mobile_add_feedback(1:i32 user_id,
                             2:string username,
                             3:string content,
                             4:i16 feedback_type,
                             5:string version,
                             6:string description,
                             7:string contact)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_upload_alipay_accounts(1:string raw_accounts_str)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_upload_cgb_accounts(1:string raw_accounts_str)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool is_able_to_pay_with_hongbao(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 pay_for_order_new(1:i32 user_id,
                          2:i64 order_id,
                          3:i16 pay_company_id,
                          4:i16 come_from,
                          5:string pay_bank,
                          6:string hongbao_sn,
                          7:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 update_pay_method_for_order(1:i64 order_id,
                                    2:i16 pay_company_id,
                                    3:i16 come_from,
                                    4:string pay_bank)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 walle_pay_for_order(1:i32 user_id,
                            2:i64 order_id,
                            3:double original_total,
                            4:string hongbao_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_for_contract(1:i32 user_id,
                          2:string contract_sn,
                          3:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_for_contract_direct(1:string contract_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_success(1:TCPayReturnInfo pay_return_info,
                     2:string from_action,
                     3:string ip)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_manually_success(1:i32 pay_record_id,
                              2:i32 user_id,
                              3:i32 admin_user_id,
                              4:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 pay_record_make(1:i32 user_id,
                        2:i32 pay_co_id,
                        3:double total_fee,
                        4:string remark)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 pay_record_make_new(1:i32 user_id,
                            2:i16 pay_company_id,
                            3:i16 come_from,
                            4:string pay_bank,
                            5:double total_fee)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_record_fail(1:i32 pay_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void direct_order_pay_fail(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void direct_order_pay_fail_new(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void user_cancel_payment(1:i64 order_id, 2:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool pay_is_success(1:i32 pay_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAlipayInfo pay_get_alipay_info()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    double pay_get_today_payment(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void withdraw_set_fatal(1:i32 withdraw_id, 2:string remark)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCWithdrawRecord> withdraw_get_apply_records()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 withdraw_restaurant_apply(1:i32 restaurant_id,
                                  2:i32 process_user_id,
                                  3:double amount,
                                  4:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void submit_withdraw_record(1:i32 withdraw_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void check_withdraw_record(1:i32 withdraw_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool is_user_drawback_out_of_limit(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void withdraw_user_manually_drawback(1:i32 user_id, 2:double amount)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void withdraw_user_drawback(1:i32 user_id
                                2:i32 process_user_id,
                                3:double amount)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void anonymous_user_drawback(1:string order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCAlipayRefundApplyInfo get_alipay_refund_apply_info(1: i32 batch_no)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCAlipayBatchInfo> query_alipay_unprocessed_batch()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void alipay_drawback_process_notify(1:TCDrawbackProcessNotify drawback_process_notify)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void alipay_bank_drawback_process_notify(1:TCBankDrawbackProcessNotify bank_drawback_process_notify)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCQueryDrawbackProcessRecordResult query_drawback_process_record(1: TDrawbackProcessRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void revoke_drawback_process(1:i32 drawback_process_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void retry_drawback_process(1:i32 drawback_process_id,
                                2:i32 process_user_id,
                                3:i16 account_type,
                                4:string bank_account,
                                5:string bank_name,
                                6:string bank_branch,
                                7:string account_holder,
                                8:string city)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void ignore_drawback_process(1:i32 drawback_process_id, 2:string reason)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void drawback_process_manually_success(1:i32 drawback_process_id, 2:string image_hash)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string get_alipay_refund_url(1:i32 batch_no)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCDrawbackReport get_drawback_report()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCDrawbackResultInfo get_drawback_result_info(1: string username, 2:string order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCDrawbackResultInfoNew get_drawback_result_info_new(1: string username, 2: string order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 bankcard_bind_apply(1:i32 user_id,
                            2:string card_id,
                            3:i32 bank_id,
                            4:string cardholder_name,
                            5:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bankcard_bind_update(1:i32 user_id,
                              2:string card_id,
                              3:i32 bank_id,
                              4:string cardholder_name,
                              5:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bankcard_bind_approve(1:i32 record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bankcard_bind_overrule(1:i32 record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void bankcard_bind(1:i32 user_id,
                       2:string card_id,
                       3:i32 bank_id,
                       4:string cardholder_name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void balance_reconciliation()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<string> generate_hongbao_exchange(1:string batch_sn,
                                   2: i32 count,
                                   3: double value,
                                   4: double sum_condition,
                                   5: i32 duration,
                                   6: string expire_date,
                                   7: string phone,
                                   8: string name,
                                   9: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void generate_hongbao(1: list<i32> user_ids,
                          2: THongbao query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void generate_hongbao_for_tester(1: i32 tester_user_id,
                                     2: double amount,
                                     3: Timestamp begin_date,
                                     4: Timestamp end_date,
                                     5: i32 sum_condition)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void generate_restaurant_activity_hongbao(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void generate_first_order_hongbao(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string exchange_hongbao(1: i32 user_id,
                          2: string exchange_code)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void charge_hongbao(1: i32 pay_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void new_user_hongbao(1: i32 user_id
                          2: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string walle_hongbao(1: i32 creator_user_id,
                         2: THongbao hongbao)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void award_refer_hongbao(1:list<i32> refer_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void punish_refers(1:list<i32> refer_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void award_refer_bind_mobile_hongbao(1:i32 refer_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void user_certification_apply(1: i32 user_id,
                                  2: TUserCertificationApply user_certification_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_user_certification(1:i32 user_id,
                                    2:i32 to_status,
                                    3:string remark,
                                    4:i32 process_user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserCertification get_user_certification(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCUserCertificationProcessRecord> query_user_certification_process_records(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void post_process_user_certification(1:i32 record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void new_user_bankcard_apply(1:i32 user_id,
                                 2:string card_id,
                                 3:i32 bank_id,
                                 4:string cardholder_name,
                                 5:string city_name,
                                 6:string branch_name)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_user_bankcard(1:i32 user_id,
                              2:string card_id,
                              3:i32 bank_id,
                              4:string cardholder_name,
                              5:string city_name,
                              6:string branch_name,
                              7:i32 process_user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void update_user_bankcard_by_user(1:i32 user_id,
                                      2:string card_id,
                                      3:i32 bank_id,
                                      4:string cardholder_name,
                                      5:string city_name,
                                      6:string branch_name,
                                      7:string password)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserCertification> query_user_certification(1:TUserCertificationQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_user_certification(1:TUserCertificationQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_for_dianping_order(1: i64 order_id, 2: string dianping_order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void dianping_order_pay_success(1: i64 order_id,
                                    2: string dianping_order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void pay_for_openapi_order(1: i64 order_id, 2: string tp_order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void openapi_order_pay_success(1: i64 order_id,
                                    2: string tp_order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void evileye_send_order_pay_success_noti(1: i64 order_id,
                                             2: i16 pay_company_id,
                                             3: string customer_pay_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    /**
     * Fingerprint
     */

    string sso_create(1:i32 user_id,
                      2:SSOTypeConst sso_type,
                      3:Json info_raw,
                      4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool sso_is_tfauthed(1:string sso_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool sso_tfauth(1:string sso_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool sso_destroy(1:string sso_id,
                     2:SSODestroyActionConst action,
                     3:i32 user_id,
                     4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool sso_destroy_admin(1:string sso_id,
                           2:SSODestroyActionConst action,
                           3:i32 op_user_id,
                           4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool sso_destroy_system(1:string sso_id,
                            2:SSODestroyActionConst action)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 sso_check(1:string sso_id,
                  2:SSOAppConst sso_app,
                  3:Json info_raw,
                  4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 sso_count_valid(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    Json sso_mget(1:i32 user_id,
                  2:bool is_valid,
                  3:Timestamp start_date,
                  4:Timestamp end_date)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string ucb_create(1:i32 user_id,
                      2:Json info_raw,
                      3:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool ucb_destroy(1:string ucb_id,
                     2:UCBDestroyActionConst action,
                     3:i32 user_id,
                     4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool ucb_destroy_admin(1:string ucb_id,
                           2:UCBDestroyActionConst action,
                           3:i32 admin_user_id,
                           4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool ucb_destroy_system(1:string ucb_id,
                            2:UCBDestroyActionConst action)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool ucb_check(1:list<string> ucb_ids,
                   2:i32 user_id,
                   3:Json info_raw,
                   4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    Json ucb_mget(1:i32 user_id,
                  2:bool is_valid,
                  3:Timestamp start_date,
                  4:Timestamp end_date)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 umcb_create(1:i32 user_id,
                    2:i64 mobile,
                    3:Json info_raw,
                    4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 umcb_check(1:i32 user_id,
                   2:i64 mobile,
                   3:Json info_raw,
                   4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool umb_create(1:i32 user_id,
                    2:i64 mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool umb_destroy_admin(1:i32 umb_id,
                           2:UMBDestroyActionConst action,
                           3:i32 admin_user_id,
                           4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    Json umb_mget(1:i32 user_id,
                  2:i64 mobile,
                  3:bool is_valid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool mcb_destroy_admin(1:i32 mcb_id,
                           2:MCBDestroyActionConst action,
                           3:i32 admin_user_id,
                           4:string ip_addr)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool mcb_destroy_system(1:i32 mcb_id,
                            2:MCBDestroyActionConst action)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    Json mcb_mget(1:i64 mobile,
                  2:bool is_valid,
                  3:Timestamp start_date,
                  4:Timestamp end_date)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void add_blocked_device(1:string eleme_device_id,
                            2:i32 user_id,
                            3:i32 operator_user_id,
                            4:string reason,
                            5:i32 come_from)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    map<i16, double> get_pay_discount_map(1:i16 come_from)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),
    /**
     * Inner services
     */
    void clean_timeout_message()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void clean_outofdate_message()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void back_up_mysql_task()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void clean_timeout_mysql_task()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void signal_post_make_order(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void signal_post_process_order(1:i32 order_process_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void signal_post_process_refund(1:i32 refund_record_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_claim_order(1:i64 order_id,
                             2:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_push_android_message(1:i32 msg_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_push_ios_message(1:i32 msg_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_add_user_message(1: i32 message_type,
                                  2: string target_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_quit_online_payment(1:i32 restaurant_id,
                                     2:i32 user_id,
                                     3:Timestamp timestamp)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_post_refund_apply(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_post_settle_up_order(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void unsubscribe_order_sms(1:i64 mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_order_refund_fail(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void process_order_refund_success(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_order_income(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<i64> filter_drawbacked_anonymous_order_ids(1:list<i64> order_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool has_permissions(1:i32 user_id,
                         2:list<string> permissions,
                         3:bool is_strict)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool has_groups(1:i32 user_id,
                    2:list<string> groups,
                    3:bool is_strict)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void clean_timout_message()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void send_restaurant_daily_balance_report(1:i32 restaurant_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserReferRank get_user_refer_rank(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void send_ecredit(1: i64 order_id,
                      2: i32 user_id,
                      3: string phone,
                      4: double ecredit_amount)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    bool check_ecredit_ok(1:string phone)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    double get_ecredit_amount_by_order_id(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void add_user_payment_account(1: i64 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TCheckoutCounterParams get_checkout_counter_params()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_checkout_counter_params(1: TCheckoutCounterParams params,
                                     2: string begin_date,
                                     3: string end_date)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    /**
     * Query services
     */
    TUser get(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUser master_get(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TThirdUserSession get_third_user_session_by_user_id(1:string user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUser get_by_username(1:string username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUser get_by_mobile(1:string mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUser> mget(1:list<i32> user_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUser> mget_by_username(1:list<string> username)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TBank get_bank(1:i32 bank_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TBank> get_bank_list()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TBank> mget_bank(1:list<i32> bank_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserBankcard get_bankcard(1: i32 user_id
                               2: i16 status)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserBankcard get_bankcard_by_user(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    map<i32, TUserBankcard> mget_bankcard_by_restaurant(1: list<i32> restaurant_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TDopUser get_dop_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TDopUser> mget_dop_user(1:list<i32> user_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserProfile get_profile(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserPaymentAccount get_user_payment_account(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserProfile master_get_profile(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserProfile> mget_profile(1:list<i32> user_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserProfile> query_profile(1:TUserProfileQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TSfGuardRememberKey get_remember_key(1: string remember_key)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TFullUser get_full(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TFullUser get_full_by_valid_mobile(1:Mobile mobile)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TFullUser> query_full(1:TFullUserQuery qeury_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TAddress get_address(1:i32 address_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TInvoice get_invoice(1:i32 invoice_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TGift get_gift(1:i32 gift_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGift> mget_gift(1: list<i32> gift_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGroup> get_group_list()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserGift get_user_gift(1:i32 user_gift_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserGift> mget_user_gift(1:list<i32> user_gift_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TWeiboUserMap get_weibo_map_by_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TRenrenUserMap get_renren_map_by_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TWeixinUserMap get_weixin_map_by_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void create_empty_hongbao_group(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    THongbaoGroup get_hongbao_group_by_order(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    THongbaoGroup generate_hongbao_group(1: i64 order_id,
                                         2: string decision,
                                         3: double risk_rate,
                                         4: string hardware_id,
                                         5: string device_id,
                                         6: string track_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string generate_qr_hongbao_group(1: TQRHongbaoGroup group)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_qr_hongbao_group(1: string group_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TQRHongbaoGroup get_qr_hongbao_group(1: string group_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TQRHongbaoGroup get_valid_qr_hongbao_group(1: string group_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TShareHongbaoResult get_qr_share_hongbao(1: string group_sn,
                                             2: string phone,
                                             3: string weixin_uid,
                                             4: string weixin_username,
                                             5: string weixin_avatar,
                                             6: string decision,
                                             7: double risk_rate)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TShareHongbaoResult get_weixin_share_hongbao(1: string group_sn,
                                                 2: string weixin_uid,
                                                 3: string weixin_username,
                                                 4: string weixin_avatar,
                                                 5: string phone,
                                                 6: string decision,
                                                 7: double risk_rate)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void sns_share_hongbao_auto_exchange(1: string phone)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TSNSPhoneCheckResultNew prepare_get_weixin_hongbao(1: string sns_uid,
                                 2: SNSType sns_type
                                 3: string group_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TSNSPhoneCheckResult check_phone_by_sns_id(1: string sns_uid,
                                 2: SNSType sns_type
                                 3: string group_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    string change_sns_hongbao_phone(1: string sns_uid,
                                  2: Mobile phone,
                                  3: SNSType sns_type)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    THongbao get_hongbao(1:i32 hongbao_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    THongbao get_hongbao_by_sn(1:string hongbao_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_hongbao(1:string hongbao_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_hongbao_exchange_batch(1: string batch_sn)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_restaurant_activity_hongbao(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_first_order_hongbao(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void invalid_hongbao_group_by_order(1:i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    double sum_hongbao_amount(1:THongbaoSum query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<THongbao> query_hongbao(1:THongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_hongbao(1:THongbaoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    map<i64, list<TOrderPaymentConstitution>> get_order_payment_constitution_map(1:list<i64> order_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TAddress> query_address_by_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TAddress> query_anonymous_address(1:string unique_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TInvoice> query_invoice_by_user(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserGift> query_user_gift(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGroup> query_user_group(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 count_gift(1:TGiftQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGift> query_gift(1:TGiftQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TGift> query_available_gift()
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TDeliveryAddress> query_delivery_address(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserMessage> query_unread_user_message(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserPlace> query_user_place(1: TUserPlaceQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TRefer> query_refer(1:TReferQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TRefer master_get_refer_by_to_user_id(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TTerminalValidation> query_terminal_validation(1:TTerminalValidationQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TWeiboUserMap get_weibo_map_by_weibo_id(1:i64 weibo_uid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TRenrenUserMap get_renren_map_by_renren_id(1:i32 renren_uid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TWeixinUserMap get_weixin_map_by_weixin_id(1:string weixin_uid)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TRestaurantAdmin get_restaurant_admin(1:i32 restaurant_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TRestaurantAdmin get_restaurant_admin_by_admin(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TRestaurantAdmin> get_restaurant_admin_by_admin_new(1:i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TTradeRecord> query_trade_record(1:TTradeRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TLoginInfo> query_login_info(1:TLoginInfoQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TCUserBankCard> mget_user_bankcard(1: list<i32> record_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TUserMetaData get_user_meta_data(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserMetaData> query_user_meta_data(1: TUserMetaDataQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserChangeRecord> query_user_change_record(1: TUserChangeRecordQuery query_struct)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<TUserCustomMenu> get_user_custom_menu_by_user(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 save_user_custom_menu(1: i32 menu_id,
                              2: TUserCustomMenu menu)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    void set_user_manage_groups(1: i32 user_id,
                                2: list<i32> group_ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<i32> get_managed_user_ids(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<i32> get_managed_group_ids(1: i32 user_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TPayRecord get_pay_record_by_order_id(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    TPayRecord get_last_pay_record_by_order_id(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    i32 get_pay_failed_time_by_order_id(1: i64 order_id)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    #####
    # Utils APIs
    #####
    void utils_table_cache_update(1:string tablename,
                                  2:list<i64> ids)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),

    list<string> query_pay_record_trade_no(1: i16 pay_company_id,
                                           2: Timestamp begin_at,
                                           3: Timestamp end_at)
        throws (1: EUSUserException user_exception,
                2: EUSSystemException system_exception,
                3: EUSUnknownException unknown_exception),
}
