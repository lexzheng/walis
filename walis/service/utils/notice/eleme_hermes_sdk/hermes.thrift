namespace php HERMES
namespace py hermes

/**
 * Enums
 */
enum THermesTaskStatus {
    INITIAL = 0
    SENDING = 1
    SUCCESS = 2
    FAIL = 3
    PARTIAL_SUCCESS = 4
    TIMEOUT = 5
}
enum THermesTemplateVerifyStatus {
    PENDING = 0
    SUCCESS = 1
    FAIL = 2
}
enum THermesNotificationType {
    TASK_STATUS_CHANGED = 0
    TEMPLATE_STATUS_CHANGED = 1
    USER_REPLY_RECEIVED = 2
}
enum THermesAudioVerifyCodeCallType {
    OUT = 0
    IN = 1
    BOTH = 2
}


/**
 * Types and Structs
 */
typedef string JSON
typedef i64 Timestamp
typedef i64 TaskId
typedef i64 TemplateId


struct THermesMessageTask {
    1: required TaskId id
    2: required bool mass_send
    3: required string receivers
    4: required THermesTaskStatus status
    5: required Timestamp create_time
    6: required bool need_reply
    7: required string message
    8: optional i16 retry_count  /* rename from retry to avoid keyword error */
}

struct THermesTemplateTask {
    1: required TaskId id
    2: required bool mass_send
    3: required string receivers
    4: required THermesTaskStatus status
    5: required Timestamp create_time
    6: required bool need_reply
    7: required TemplateId template_id
    8: required string template_params
    9: optional i16 retry_count  /* rename from retry to avoid keyword error */
}

struct THermesUserReply {
    1: required i64 id
    2: required string phone_number
    3: required Timestamp reply_time
    4: required string message
}

struct SenderCreationParameter {
    1: required string name
    2: optional string remark
}

struct NormalTaskCreationParameter {
    1: required string receivers
    2: required string message
    3: required string sender_key
    4: optional bool need_reply
    5: optional i16 retry_count  /* rename from retry to avoid keyword error */
}

struct TemplateTaskCreationParameter {
    1: required string receivers
    2: required TemplateId template_id
    3: required string template_params
    4: required string sender_key
    5: optional bool need_reply
    6: optional i16 retry_count  /* rename from retry to avoid keyword error */
}

struct AudioTaskCreationParameter {
    1: required string receivers
    2: required string message
    3: required string sender_key
    4: optional i16 retry_count  /* rename from retry to avoid keyword error */
}

struct VerifyCodeCreationParameter {
    1: required string sender_key
    2: required string receiver
    3: optional string code
    4: optional i16 expire
    5: optional bool via_audio
    6: optional THermesAudioVerifyCodeCallType audio_call_type
}

struct EmailVerifyCodeCreationParameter {
    1: required string sender_key
    2: required string receiver
    3: optional string code
    4: optional i16 expire
}

struct VerifyCodeCreationResult {
    1: required string hash_value
    2: required string code
}

struct THermesVerifyCodeQueryResult {
    1: required i64 id
    2: required string receiver
    3: required string sender
    4: required string code
    5: required bool is_validated
    6: required Timestamp create_time
    7: required bool via_audio
}

struct THermesSMSTaskQueryResult {
    1: required TaskId id
    2: required string receiver
    3: required string sender
    4: required string message
    5: required THermesTaskStatus status
    6: required Timestamp create_time
}


/**
 * Exceptions
 */
enum HermesErrorCode {
    UNKNOWN_ERROR,
    NOT_IMPLEMENTED,
    INVALID_ARGUMENTS,

    TASK_NOT_FOUND,
    TASK_CREATION_FAILED,
    INVALID_PARAMS_ON_TASK_CREATION,
    SENDER_CREATION_FAILED,
    TEMPLATE_CREATION_FAILED,
    GET_TEMPLATE_VERIFY_STATUS_FAILED,
    QUERY_STATUS_FAILED,
    QUERY_USER_REPLY_FAILED,
    VERIFY_CODE_CREATION_FAILED,
    VERIFY_CODE_VALIDATE_FAILED,
    INVALID_PHONE_NUMBER,
    SMS_TEMPLATE_NOT_FOUND,
    VERIFY_CODE_SEND_LIMIT_REACHED,
    SENDER_NOT_FOUND,
    INVALID_EMAIL_ADDRESS,
}

exception HermesUserException {
    1: required HermesErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception HermesSystemException {
    1: required HermesErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception HermesUnknownException {
    1: required HermesErrorCode error_code,
    2: required string error_name,
    3: required string message,
}


/**
 * Services
 */
service HermesService {

    bool ping()
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    bool system_check()
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    string create_sender(1: SenderCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    TemplateId create_sms_template(1: string template_content,
                                   2: string template_params,
                                   3: string template_slug)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    THermesTemplateVerifyStatus get_sms_template_verify_status(1: string template_slug)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    TaskId create_task(1: NormalTaskCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    TaskId create_template_task(1: TemplateTaskCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    TaskId create_audio_task(1: AudioTaskCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    map<TaskId, THermesTaskStatus> get_task_status(1: list<TaskId> task_ids)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    list<THermesUserReply> get_user_reply(1: string phone_number,
                                          2: Timestamp timestamp)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    VerifyCodeCreationResult verify_code_create(1: VerifyCodeCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    VerifyCodeCreationResult email_verify_code_create(1: EmailVerifyCodeCreationParameter param)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    bool verify_code_validate(1: string hash_value,
                              2: string verify_code_to_validate)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    bool validate_verify_code_with_hash(1: string sender_key,
                                        2: string hash_value,
                                        3: string verify_code_to_validate)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    bool validate_verify_code_with_receiver(1: string sender_key,
                                            2: string receiver,
                                            3: string verify_code_to_validate)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    bool validated_within_n_minutes(1: string sender_key,
                                    2: string receiver,
                                    3: i64 minutes)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    list<THermesVerifyCodeQueryResult> query_sent_verify_code(1: string receiver
                                                              2: i16 limit)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    list<THermesSMSTaskQueryResult> query_sms_task(1: string receiver,
                                                   2: i16 limit)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),

    TemplateId get_template_id_by_slug(1: string slug)
        throws (1: HermesUserException user_exception,
                2: HermesSystemException system_exception,
                3: HermesUnknownException unknown_exception),
}
