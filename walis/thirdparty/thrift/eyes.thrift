# define evileye service
namespace php eyes
namespace py eyes

/**
 * Const
 */
const i16 DEFAULT_LIST_SIZE = 20
const i16 MAX_LIST_SIZE = 200
 
/**
 * Enums
 */
enum SuspiciousRestaurantConst {
    STATUS_DOING = 1,
    STATUS_FINISHED = 2,
}

/**
 * Types and Structs
 */
typedef i64 Timestamp
typedef string Json

struct TWalleSuspiciousOrderAmountQuery {
    1:optional i32 auditor_id,
    2:optional i16 status,
    3:optional string date,
}

struct TWalleSuspiciousOrderQuery {
    1:required i32 restaurant_id,
    2:required string date,
    3:optional i16 offset,
    4:optional i16 limit,
}

struct TWalleSuspiciousOrder {
    1:required i64 id,
    2:required i32 restaurant_id,
    3:required string restaurant_name,
    4:required double total,
    5:required i32 user_id,
    6:required string user_name,
    7:required string ip,
    8:required Timestamp created_at,
    9:required list<string> reasons,
}

struct TOrderContext {
    1:required i32 user_id,
    2:required i32 restaurant_id,
    3:required string address,
    4:required string ip,
    5:required list<string> phones,
    6:required double total,
    7:required double subsidy_amount,
    8:required bool is_online_paid,
    9:required i32 come_from,
    10:optional string device_id,
    11:optional Timestamp created_at,
    12:optional string track_id,
}

struct TEvalResult {
    1:required double val,
    2:required double valid_val,
    3:required list<string> valid_reasons,
    4:required double risk_val,
    5:required list<string> risk_reasons,
    6:required string final_decision,
}


struct TOrderAction {
    1:required i64 order_id,
    2:required i32 restaurant_id,
    3:required Timestamp created_at,
    4:required list<string> phones,
    5:required string ip,
    6:required i32 come_from,
    7:optional i32 user_id,
    8:optional string pay_account_id,
    9:optional string track_id,
    10:optional string device_id,
}


struct TPageViewAction {
    1:required string current_url,
    2:required string referer_url,
    3:optional i32 user_id,
    4:optional string track_id,
}


/**
 * Exceptions
 */
enum EYESErrorCode {
    UNKNOWN_ERROR,

    // User Errors
    ALL_SUSPICIOUS_ORDERS_DISTRIBUTED,
    AUDITOR_AMOUNT_INVALID,

    // System Errors
    DATABASE_ERROR,
}

exception EYESUserException {
    1: required EYESErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EYESSystemException {
    1: required EYESErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EYESUnknownException {
    1: required EYESErrorCode error_code,
    2: required string error_name,
    3: required string message,
}

/**
 * Services
 */
service ElemeEvilEyeService {
    /**
     * Base APIs
     */
    bool ping()
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    /**
     * App service
     */
    i32 walle_distribute_suspicious_orders(1: i32 auditor_id,
                                           2: i32 auditor_amount,
                                           3: string date)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    Json walle_filter_suspicious_orders_amount(1: TWalleSuspiciousOrderAmountQuery query_struct)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    void walle_finish_suspicious_group_auditing(1: i32 restaurant_id, 2: string date)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    list<TWalleSuspiciousOrder> walle_get_suspicious_order_detail(1: list<i64> order_ids)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    list<TWalleSuspiciousOrder> walle_get_suspicious_orders(1: TWalleSuspiciousOrderQuery query_struct)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    TEvalResult eval_order_risk(1: TOrderContext t_order_context)
        throws (1: EYESUserException user_exception,
                2: EYESSystemException system_exception,
                3: EYESUnknownException unknown_exception),

    /**
     * Inner APIs
     */

    /**
     * Query APIs
     */

    /**
     * Signal APIs
     */
}
