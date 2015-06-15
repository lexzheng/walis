# define sms service
namespace php SMS
namespace py sms

/**
 * Consts
 */
const i16 DEFAULT_LIST_SIZE = 20
const i16 MAX_LIST_SIZE = 100

/**
 * Enums
 */
enum MessagerId {
    DODOCA = 6,
    CTC = 7,
    YUNPIAN = 8,
}

enum SendStatus {
    UNSENT = 0,
    PROCESSED = 1,
    SUCCESSED = 2,
    FAILED = 3,
}

enum ReadStatus {
    NOT_READ = 0,
    IS_READ = 1,
}

enum AiStatus {
    NOT_READ = 0,
    AUTO_CONFIRMED = 1,
    ORDER_NOT_FOUND = 2,
    UNIDENTIFIED = 3,
}

enum ReceiveDistributeStatus {
    UNDISTRIBUTED = 0,
    DISTRIBUTED_TO_VACUUM = 1,
    DISTRIBUTED_TO_ADMIN = 2,
}

enum ReportStatus {
    SUCCESSED = 0,
    FAILED = 1,
}

enum PushedContentStatus {
    UNPROCESSED = 0,
    PROCESSED = 1,
    FAILED = 2,
}

enum PushedContentType {
    RECEIVE = 0,
    REPORT = 1,
}

enum SmsServiceProvider {
    CMCC = 1,
    CU = 2,
    CT = 3,
}


/**
 * Types and Structs
 */
typedef i64 Mobile
typedef i64 Timestamp
typedef string JSON

struct TSMSSend {
    1: required i32 id,
    2: optional MessagerId messager_id,
    3: required Mobile mobile,
    4: required string content,
    5: required SendStatus status,
    6: required Timestamp created_at,
    7: required string rrid,
}

struct TSMSVerifyCode {
    1: required i32 id,
    2: required Mobile mobile,
    3: required string code,
    4: required bool is_valid,
    5: required Timestamp created_at
}

struct TSMSReceive {
    1: required i32 id,
    2: required MessagerId messager_id,
    3: required Mobile mobile,
    4: required string content,
    5: required Timestamp created_at,
}

struct TSMSReport {
    1: required i32 id,
    2: required MessagerId messager_id,
    3: required Mobile mobile,
    4: required ReportStatus status,
    5: required string rrid,
    6: required Timestamp created_at,
}

struct TSMSAdmin {
    1: required i32 id,
    2: required i64 order_id,
    3: required i32 restaurant_id,
    4: required Mobile mobile,
    5: required i32 admin_id,
    6: required ReadStatus read_status,
    7: required Timestamp created_at,
    8: required i32 sms_send_id,
    9: required i32 sms_receive_id,
}

typedef list<TSMSSend> TSMSSendList
typedef list<TSMSVerifyCode> TSMSVerifyCodeList
typedef list<TSMSReceive> TSMSReceiveList
typedef list<TSMSAdmin> TSMSAdminList

typedef list<string> QueryFields


struct TSMSAdminQuery {
    1: optional i32 restaurant_id,
    2: optional Mobile mobile,
    3: optional i32 admin_id,
    4: optional ReadStatus read_status,
    5: optional Timestamp from_time,
    6: optional Timestamp to_time,
    7: optional i32 limit,
    8: optional i32 offset,
    9: optional QueryFields query_fields,
}

/**
 * Exceptions
 */
enum SMSErrorCode {
    UNKNOWN_ERROR,

    // User Errors
    INVALID_MESSAGER_ID,
    INVALID_MOBILE,
    INVALID_RESTAURANT_MOBILE,
    INVALID_RESTAURANT_NUMBER,
    SMS_ADMIN_NOT_FOUND,
    SMS_PUSHED_CONTENT_NOT_FOUND,
    SMS_RECEIVE_NOT_FOUND,
    SMS_SEND_NOT_FOUND,
    SMS_VOICE_SEND_NOT_FOUND,
    VMS_OUT_OF_LIMIT,

    MOBILE_VALIDATION_NOT_REPEAT,
    MOBILE_VALIDATION_TIMEOUT,
    MOBILE_VALIDATION_FAIL,

    VOICE_CODE_LENGTH_FAIL,

    EOS_CLIENT_ERROR,
    ERS_CLIENT_ERROR,
    EUS_CLIENT_ERROR,

    // System Errors
    DATABASE_ERROR,
    MESSAGER_ERROR,
    SMS_PUSHED_CONTENT_INVALID,
    SMS_MESSENGER_ERROR,
}

exception SMSUserException {
    1: required SMSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception SMSSystemException {
    1: required SMSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception SMSUnknownException {
    1: required SMSErrorCode error_code,
    2: required string error_name,
    3: required string message,
}


/**
 * Services
 */
service ShortMessageService {
    /**
     * Base APIs
     */
    bool ping()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void clear_cache(1:string api_name,
                     2:list<string> params)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    string balance()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void send(1: Mobile mobile,
              2: string content)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void send_with_messager(1: Mobile mobile,
                            2: string content,
                            3: i32 messager_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void send_voice(1: Mobile mobile, 2: string code)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void send_verify_code(1: Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void send_voice_verify_code(1: Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void receive(1: MessagerId messager_id,
                 2: string content)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void report(1: MessagerId messager_id,
                2: string content)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void report_voice(1: MessagerId messager_id,
                      2: string content)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception)

    map<MessagerId, i32> stats_send_count(1: i64 from_time, 2: i64 to_time)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    map<MessagerId, i32> stats_send_total(1: i64 from_time, 2: i64 to_time)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    bool verify_mobile_with_code(1: Mobile mobile, 2: string code)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    /**
     * Apps APIs
     */

    void admin_send(1: Mobile mobile,
                    2: string content,
                    3: i32 restaurant_id,
                    4: i32 admin_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void admin_order_send(1: i64 order_id,
                          2: i32 admin_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void admin_set_message_read_status(1: i32 msg_id,
                                       2: ReadStatus read_status)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void admin_set_message_restaurant(1: i32 msg_id,
                                      2: i32 rst_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    string get_validation_code(1:Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    bool confirm_validation_code(1:Mobile mobile,
                                 4:string validate_code)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void ctc_receive()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void ctc_report()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    /**
     * Inner APIs
     */
    void signal_post_make_order(1: i64 order_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_distribute(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_send(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_send_voice(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_receive(1: i32 content_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_report(1: i32 content_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_report_voice(1: i32 content_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_ai_auto_send(1: i64 order_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void process_ai_auto_confirm(1: i32 sms_receive_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void set_pushed_content_status(1: i32 sms_pushed_content_id,
                                   2: i16 status)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    /**
     * Query APIs
     */
    TSMSSend get_send(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSSendList mget_send(1: list<i32> msg_ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSSendList query_send_by_mobile(1: Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSVerifyCodeList query_verify_code_by_mobile(1: Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSReceive get_receive(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSReceiveList mget_receive(1: list<i32> msg_ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSReceiveList query_receive_by_mobile(1: Mobile mobile)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSAdmin get_admin(1: i32 msg_id)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSAdminList mget_admin(1: list<i32> msg_ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    TSMSAdminList query_admin(1: TSMSAdminQuery query_struct)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),
    JSON sms_inspect()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),
    list<i32> voice_unsend_report()
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),


    /**
     * Signal APIs
     */
    void signal_update_sms_send(1: list<i32> ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void signal_update_sms_receive(1: list<i32> ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

    void signal_update_sms_admin(1: list<i32> ids)
        throws (1: SMSUserException user_exception,
                2: SMSSystemException system_exception,
                3: SMSUnknownException unkown_exception),

}
