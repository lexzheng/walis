namespace php fuss2
namespace py fuss2

const string FUSS_ORIGIN_FILENAME = ""

exception InvalidValueException {
   1: i32 error_code,
   2: string error_msg
}

enum FussCategory {
    RESTAURANT_LOGO = 1,
    FOOD = 2,
    ORDER_RECEIPT = 3,
}

exception FussException {
    1: i32 id,
    2: string name = ""
    3: string message = ""
}

typedef string FussHash

struct Meta {
    1:optional string file_name,
    2:optional string file_size
}

struct FussFile {
    1:required binary content,
    2:required string extension,
    3:optional string category,
}

service FussService {
    bool ping(),

    FussHash file_upload(1:FussFile fuss_file) throws (1:FussException e),

    # size: [[width, height], [width, height], ...]
    FussHash file_upload_sized(1:FussFile fuss_file, 2:list<list<i32>> size) throws (1:FussException e),

    FussHash file_upload_sized_with_watermarker(1:FussFile fuss_file, 2:list<list<i32>> size) throws (1:FussException e),

    string file_get_sized(1:FussHash hash, 2:string size) throws(1:FussException e),

    string file_get(1:FussHash hash) throws(1:FussException e),

    void file_delete(1:FussHash hash) throws(1:FussException e),

    void file_delete_sized(1:FussHash hash, 2:string size) throws(1:FussException e),

    void file_delete_all(1:FussHash hash) throws(1:FussException e),

    void produce_food_images(1:FussHash hash) throws(1:FussException e),

    FussHash avatar_upload(1:FussFile fuss_file) throws (1:FussException e),
}

