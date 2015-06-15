# define ees service
namespace php EES
namespace py ees

/**
 * Enums
 */

/**
 * Types and Structs
 */
typedef i64 Timestamp
typedef string EmailAddress

struct TEmail {
    1: optional i32 id,
    2: required EmailAddress sender,
    3: required EmailAddress receiver,
    4: required string title,
    5: required string content,
    6: optional Timestamp created_at,
    7: optional Timestamp sent_at,
}

struct TAndroidTransMessage {
    1: required i16 msg_type,
    2: required string content,
    3: required string device_id,
    4: optional string attached_content,
    5: optional string version_name,
}

enum AppMessageConst {
    DEVICE_TYPE_IOS = 1,
    DEVICE_TYPE_ANDROID = 2,

    MSG_TYPE_NONE = 0,

    # msg_types in PUSH_TYPE_NOTIFY
    MSG_TYPE_ORDER = 1,

    # msg_types in PUSH_TYPE_TRANSMISSION
    MSG_TYPE_UPDATE_APP = 1,
    MSG_TYPE_SYNC_ORDER = 2,
    MSG_TYPE_ACTIVITY_CONTRACT = 3,

    PUSH_TYPE_NONE = 0,
    PUSH_TYPE_NOTIFY = 1,
    PUSH_TYPE_TRANSMISSION = 2,
    PUSH_TYPE_TRANSMISSION_NEW = 3,

    TRANS_TYPE_NONE = 0,
    TRANS_TYPE_OPENAPP = 1,
    TRANS_TYPE_CUSTOME = 2,

    # Application.id
    APP_ID_NAPOS_IOS = 41,
    APP_ID_ELEME_IOS = 1,

    # iOS notification commands
    IOS_COMMAND_NAPOS_ORDER_SYNC = 1,
    IOS_COMMAND_NAPOS_ACTIVITY_CONTRACT = 2,
}

/**
 * Exceptions
 */
enum EESErrorCode {
    UNKNOWN_ERROR = 0,
    EMAIL_NOT_FOUND = 1,
    INVALID_EMAIL_ADDRESS = 2,
    ANDROID_MESSAGE_NOT_FOUND = 3,
    IOS_MESSAGE_NOT_FOUND = 4,
    PUSH_TIMEOUT = 5,
    SEND_TIMEOUT = 6,
    DATABASE_ERROR = 7,
    SEND_EMAIL_ERROR = 8,
    // Append New Error Code Here..
}

exception EESUserException {
    1: required EESErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EESSystemException {
    1: required EESErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EESUnknownException {
    1: required EESErrorCode error_code,
    2: required string error_name,
    3: required string message,
}

/**
 * Services
 */
service ElemeEmailService {
    /**
     * Base APIs
     */
    bool ping()
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void clear_cache(1:string api_name,
                     2:list<string> params)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void send_with_files(1: EmailAddress sender,
                         2: EmailAddress receiver,
                         3: string title,
                         4: string content,
                         5: map<string, string> files)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),


    void send(1: EmailAddress sender,
              2: EmailAddress receiver,
              3: string title,
              4: string content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void msend(1: EmailAddress sender,
               2: list<EmailAddress> receivers,
               3: string title,
               4: string content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),


    /**
     * App service
     */
    void send_notification(1: EmailAddress receiver,
                           2: string title,
                           3: string content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void msend_notification(1: list<EmailAddress> receivers,
                            2: string title,
                            3: string content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void send_alert(1: string title,
                    2: string content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),


    /**
     * Inner APIs
     */
    void process_send(1: i32 email_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void process_push_android_message(1:i32 msg_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void process_push_ios_message(1:i32 msg_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_android_notify_message(1:i16 trans_type,
                                    2:string content,
                                    3:i16 msg_type,
                                    4:string attached_content,
                                    5:string device_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_android_notify_message2(1:i16 trans_type,
                                     2:string content,
                                     3:i16 msg_type,
                                     4:string attached_content,
                                     5:string device_id,
                                     6:i64 timestamp)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_android_trans_message(1:i16 msg_type,
                                   2:string attached_content,
                                   3:string device_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_android_trans_message2(1: TAndroidTransMessage msg)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_android_trans_message_for_napos(1:i16 msg_type,
                                             2:string attached_content,
                                             3:string device_id,
                                             4:i64 timestamp)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_ios_push_message(1:string device_id,
                              2:string attached_content,
                              3:i16 app_id,
                              4:string json_content)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_ios_push_message2(1:string device_id,
                               2:string attached_content,
                               3:i16 app_id,
                               4:string json_content,
                               5:i64 timestamp)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    void add_ios_push_message_for_napos(1:string device_id,
                                        2:string attached_content,
                                        3:i16 app_id,
                                        4:string json_content,
                                        5:i64 timestamp)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),

    # deprecated
    void notify_napos_mobile_to_sync(1: i32 restaurant_id,
                                     2: bool is_new_order)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),


    void notify_napos_mobile_to_sync2(1: i32 restaurant_id,
                                      2: bool is_new_order,
                                      3: i64 timestamp)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),
    /**
     * Query APIs
     */
    TEmail get(1:i32 email_id)
        throws (1: EESUserException user_exception,
                2: EESSystemException system_exception,
                3: EESUnknownException unknown_exception),
}
