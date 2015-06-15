namespace py keeper
namespace php keeper


/**
 * Typedef
 */

typedef string Date
typedef i32 TimeStamp

# represents day of week in a list range from 1 to 7
typedef list<i16> Weekdays

/** Field name to order query result:
  *
  * 'created_at' - results ordered by `created_at` field ascendently
  * '-created_at' - results ordered by `created_at` field descendently
  */
typedef list<string> OrderBy

/**
  * Regions:
  *
  * {
  *     <city_id>: {
  *         <district_id>: [
  *             <area_id>,
  *             ...
  *         ],
  *         ...
  *     },
  *     ...
  * }
  *
  */
typedef map<i32,map<i32,list<i32>>> Regions


/**
 * Const
 */


/**
 * Enum
 */

enum ErrCode {
  # Unknown error codes
  UNKNOWN_ERROR = 999,
  UNKNOWN_SERVER_ERROR = 998,
  UNKNOWN_CLIENT_ERROR = 997,
  UNKNOWN_USER_ERROR = 996,

  # System errors
  DATABASE_ERROR = 1001,

  # Permission error codes
  PERMISSION_ERROR = 1101,

  # Validation error codes
  VALIDATION_ERROR = 1201,

  # User errors
  ZEUS_USER_ERROR = 1301,
}

enum BannerType {
  NON_INTERACTIVE = 1,
  LINK = 2,
  ACTIVITY = 3,
}

enum RestaurantType {
  NORMAL = 1,
  BRANDED = 2,
}


/**
 * Struct
 */

struct Region {
  1: i32 city_id,
  2: optional i32 district_id,
  3: optional i32 area_id,
}

struct NonInteractiveBanner {
  1: string name,
  2: bool is_valid = true,
  3: string image_hash,
  4: i16 priority,
  5: Date start_date,
  6: Date end_date,
  7: Weekdays weekdays,
  8: optional Regions regions,  // no regions specified means nationwide
}

struct LinkBanner {
  1: string name,
  2: bool is_valid = true,
  3: string image_hash,
  4: i16 priority,
  5: Date start_date,
  6: Date end_date,
  7: Weekdays weekdays,
  8: optional Regions regions,  // no regions specified means nationwide
  9: string url,
}

struct ActivityBanner {
  1: string name,
  2: bool is_valid = true,
  3: string image_hash,
  4: i16 priority,
  5: Date start_date,
  6: Date end_date,
  7: Weekdays weekdays,
  8: string activity_image_hash,
  9: string description,
  10: optional Regions regions,  // no regions specified means nationwide
  11: optional RestaurantType restaurant_type,
  12: optional i32 activity_id,
  13: optional i32 activity_category_id,
  14: optional string activity_name,
  15: optional string time_desc,
  16: optional string rule_desc,
  17: optional string tip,
  18: optional string region_desc,
}

// General one including all possible attrs from all kinds
struct Banner {
  1: i32 id,
  2: string name,
  3: BannerType type,
  4: bool is_valid,
  5: string image_hash,
  6: i16 priority,
  7: string start_date,
  8: string end_date,
  9: Weekdays weekdays,
  10: optional Regions regions,  // no regions specified means nationwide
  11: optional string url,
  12: optional RestaurantType restaurant_type,
  13: optional i32 activity_id,
  14: optional string activity_name,
  15: optional i32 activity_category_id,
  16: optional string activity_image_hash,
  17: optional string description,
  18: optional string time_desc,
  19: optional string rule_desc,
  20: optional string tip,
  21: optional string region_desc,
}

struct BannerQuery {
  1: optional string name,
  2: optional Regions regions,
  3: optional bool is_valid,
  4: optional Date start_date,
  5: optional Date end_date,
  6: optional OrderBy order_by,
  7: optional Weekdays weekdays,
  8: optional Date today,
}

struct BannerQueryResult {
  1: list<Banner> banners,
  2: i32 count,
}


/**
 * Exception
 */
exception KPError {
    1: i32 err_code,
    2: string dev_msg,
    3: string user_msg,
}

/**
 * Service
 */

service BannerService {
  void ping(),

  Banner add_non_interactive_banner(1: NonInteractiveBanner banner)
    throws (1: KPError error),

  Banner add_link_banner(1: LinkBanner banner)
    throws (1: KPError error),

  Banner add_activity_banner(1: ActivityBanner banner)
    throws (1: KPError error),

  Banner get_banner(1: i32 id)
    throws (1: KPError error),

  BannerQueryResult query_banners(1: BannerQuery query)
    throws (1: KPError error),

  BannerQueryResult javis_query_banners(1: BannerQuery query)
    throws (1: KPError error),

  Banner update_non_interactive_banner(1: i32 id,
                                       2: NonInteractiveBanner attrs)
    throws (1: KPError error),

  Banner update_link_banner(1: i32 id,
                            2: LinkBanner attrs)
    throws (1: KPError error),

  Banner update_activity_banner(1: i32 id,
                                2: ActivityBanner attrs)
    throws (1: KPError error),
}
