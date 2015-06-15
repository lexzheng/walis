namespace php jvs
namespace py jvs


typedef i64 Timestamp
typedef string JsonString


enum RestaurantRecruitmentStatus {
    STATUS_UNPROCESSED = 0,
    STATUS_PROCESSED = 1,
}


struct TRestaurantRecruitment {
    1: optional i32 id,
    2: optional i32 restaurant_id,
    3: optional i32 headcount,
    4: optional double salary,
    5: optional string working_time_start,
    6: optional string working_time_end,
    7: optional i32 status,
    8: optional string comment,
    9: optional Timestamp created_at,
    10: optional i32 city_id,
}

struct TVoiceOrder {
    1: required i64 id,
    2: required i64 order_id,
    3: required i16 status_code,
    4: required i16 key_pressed,
    5: required Timestamp created_at,
    6: required i64 call_id,
    7: required i32 sequence_number,
}

struct TDirectStruct {
    1: optional list<i32> city_ids,
    2: optional list<i32> region_group_ids,
    3: optional list<i32> region_ids,
}

service JvsService {
    string ping();

    # Restaurant recruitment
    i64 restaurant_recruitment_post_t(1:TRestaurantRecruitment data);

    TRestaurantRecruitment restaurant_recruitment_get_t(1:i32 _id);

    list<TRestaurantRecruitment> restaurant_recruitment_search_t(1:JsonString q);

    bool restaurant_recruitment_put_t(1:TRestaurantRecruitment data);

    bool restaurant_recruitment_patch(1:JsonString data);

    bool restaurant_recruitment_delete(1:i32 _id);

    # Voice order
    TVoiceOrder get_voice_order(1:i64 order_id);

    map<i64, TVoiceOrder> mget_voice_order(1: list<i64> order_ids);

    bool is_suspicious_order_auditor(1:i32 auditor_id);

    # Restaurant director
    list<i32> get_restaurant_director_ids(1:i32 restaurant_id);

    void change_director_region(1:i32 user_id,
                                2:TDirectStruct old_region,
                                3:TDirectStruct new_region);

    void set_bd_restaurant_director(1:i32 user_id,
                                    2:list<i32> restaurant_ids,
                                    3:i16 notice_enabled,
                                    4:i16 in_charge);

    i32 add_cs_process_type_change_record(1:i32 user_id,
                                             2:i16 from_type,
                                             3:i16 to_type);
}
