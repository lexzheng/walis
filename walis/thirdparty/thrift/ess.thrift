# define ess service
namespace php ESS
namespace py ess

/**
 * Enums
 */

/**
 * Types and Structs
 */

typedef string Json

/**
 * Exceptions
 */
enum ESSErrorCode {
    UNKNOWN_ERROR = 0,
    EOS_CLIENT_ERROR = 1,
    ERS_CLIENT_ERROR = 2,
    SMS_CLIENT_ERROR = 3,
    TASK_REVOKE = 4,
    DATABASE_ERROR = 5,
    // Append New Error Code Here..
}

struct TRestaurantQuery {
    1: required string keyword,
    2: optional list<i32> restaurant_ids,
    3: optional i32 offset,
    4: optional i32 size
}

exception ESSUserException {
    1: required ESSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception ESSSystemException {
    1: required ESSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception ESSUnknownException {
    1: required ESSErrorCode error_code,
    2: required string error_name,
    3: required string message,
}

/**
 * Services
 */
service ElemeSearchService {
    /**
     * Base APIs
     */
    bool ping()
        throws (1: ESSUserException user_exception,
                2: ESSSystemException system_exception,
                3: ESSUnknownException unknown_exception),

    Json search(1: string index,
                2: Json query)
        throws (1: ESSUserException user_exception,
                2: ESSSystemException system_exception,
                3: ESSUnknownException unknown_exception),

    Json search2(1: string index,
                 2: string doc_type,
                 3: Json query)
        throws (1: ESSUserException user_exception,
                2: ESSSystemException system_exception,
                3: ESSUnknownException unknown_exception),

    Json search_old_order(1: string doc_type,
                          2: Json query)
        throws (1: ESSUserException user_exception,
                2: ESSSystemException system_exception,
                3: ESSUnknownException unknown_exception),

    Json search_restaurant(1: TRestaurantQuery query_struct)
        throws (1: ESSUserException user_exception,
                2: ESSSystemException system_exception,
                3: ESSUnknownException unknown_exception),
}
