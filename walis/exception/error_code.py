# coding=utf8

from __future__ import unicode_literals

##########
# Develop error code 0~99
#####
DEV_UNKNOWN_ERROR = 0
DEV_EXCEPTION_UNDEFINED_ERROR = 10
DEV_BAD_REQUEST_ERROR = 11
DEV_THRIFT_ERR = 20
DEV_CLASS_EXTENDS_ERR = 30
DEV_METHOD_VALID = 40
DEV_ARGS_ERR = 50
DEV_REDIS_LOCKED_ERR = 60
DEV_MODULE_PATH_ERR = 70
DEV_MODULE_LOAD_ERR = 71
DEV_MODULE_ATTR_ERR = 72

##########
# Server error code 100~899
#####
SERVER_UNKNOWN_ERROR = 100

DATABASE_UNKNOWN_ERROR = 200
DATABASE_MYSQL_ERROR = 201
DATABASE_MONGO_ERROR = 202
DATABASE_REDIS_ERROR = 203
DATABASE_VALIDATION_ERROR = 204

ZEUS_DATABASE_ERROR = 209

##########
# Auth error code 900~999
#####
AUTH_FAILED_ERROR = 900
AUTH_FAILED_ERROR_TO_USER = 901

AUTH_UTP_FAILED_ERROR = 902
##########
# User error code 1000~INF
#####
USER_UNKNOWN_ERROR = 1000

# Rst 10000 ~ 11999
# Rst:cert 10000 ~ 10099
CERT_NOT_EXISTS_ERR = 10000
CERT_PROC_ILL_ERR = 10001
CERT_NOT_PENDING_ERR = 10002
CERT_UPDATE_ERR = 10003
CERT_IMAGE_URL_ERR = 10004

# Rst:bankcard 10100 ~ 10199
BANKCARD_APPROVE_ERR = 10100
BANKCARD_UPDATE_ERR = 10101
BANKCARD_STATUS_INVALID = 10102

# Activity 12000 ~ 13999
# Activity:activity 12000 ~ 12099
ACTIVITY_NONE_ERR = 12000
# Activity:payment 12100 ~ 12199
ACTIVITY_PAYMENT_PROC_ILL_ERR = 12100

# Region 14000 ~ 15999
# Region:region 14000 ~ 14099
REGION_TYPE_INVALID = 14001
REGION_INVALID = 14002

# Region:city 14100 ~ 14199
CITY_TRS_CFG_NOT_EXISTS = 14100
CITY_NOT_EXISTS = 14101
CITY_NAME_EXISTS=14102
DIST_NAME_REDUNDANCE=14110
ZONE_NAME_REDUNDANCE=14120

# User 16000 ~ 16999


# Order 17000 ~ 17999


# Finance 18000 ~ 18999


# Operation 19000 ~ 19999
# Opr Banner 19000 ~ 19099
BANNER_TYPE_ERR = 19000
BANNER_ARGS_ERR = 19001
BANNER_NOT_EXISTS_ERR = 19002

# Misc 20000 ~ INF
# Misc:file 20000 ~ 20099
IMAGE_UPLOAD_ERR = 20000
FILE_UPLOAD_ERR = 20001
VOICE_CALL_NOT_FOUND = 20002

# Misc:utils 20100 ~ 20399
FORMAT_ERR = 20100

# customer service 20400-20800
CS_EVENT_NOT_EXIST = 20400
CS_EVENT_PROCESS_STATUS_INVALID = 20401
# TODO define all the user exceptions

# restaurant
RST_IDS_REQUIRED = 1201

# coupon
COUPON_SN_REQUIRED = 1202
COUPON_SN_INVALID = 1203
COUPON_COUNT_REQUIRED = 1204
COUPON_COUNT_INVALID = 1205


# error_code,msg MAP
CODE_MSG = {
    DEV_UNKNOWN_ERROR: '开发过程未知错误',
    DEV_EXCEPTION_UNDEFINED_ERROR: '异常码未定义',
    DEV_BAD_REQUEST_ERROR: '请求参数内容或格式错误: {arg}',
    DEV_THRIFT_ERR: 'Thrift 服务<{thrift_name}> 未找到',
    DEV_CLASS_EXTENDS_ERR: '抽象类<{class_name}> 必须先继承才能使用。',
    DEV_METHOD_VALID: '函数写法不符合要求。{msg}',
    DEV_ARGS_ERR: '参数错误:{args}',
    DEV_REDIS_LOCKED_ERR: '上锁失败，未知的键类型。',
    DEV_MODULE_LOAD_ERR: '模块<{path}>加载失败',
    DEV_MODULE_PATH_ERR: '模块加载路径<{path}>不是绝对路径',
    DEV_MODULE_ATTR_ERR: '模块<{module}>中未定义任何名为<{name}>的类、方法或属性',

    SERVER_UNKNOWN_ERROR: '系统未知错误',
    DATABASE_UNKNOWN_ERROR: '数据库未知错误',
    DATABASE_MYSQL_ERROR: 'MySQL数据库错误',
    DATABASE_MONGO_ERROR: 'Mongo数据库错误',
    DATABASE_REDIS_ERROR: 'Redis数据库错误',
    DATABASE_VALIDATION_ERROR: '数据库字段校验错误 {key}: {value}',
    ZEUS_DATABASE_ERROR: 'Zeus slave数据库错误',

    AUTH_FAILED_ERROR: '无权限访问',
    AUTH_FAILED_ERROR_TO_USER: '用户 {user} 无权限访问',
    AUTH_UTP_FAILED_ERROR: '无权限访问(UTP)',

    USER_UNKNOWN_ERROR: '用户未知错误',

    # Rst
    CERT_NOT_EXISTS_ERR: '餐厅<id:{restaurant_id}> 认证不存在。',
    CERT_NOT_PENDING_ERR: '餐厅认证不在审核状态。',
    CERT_PROC_ILL_ERR: '餐厅认证状态只能变更到"通过"和"不通过"。',
    CERT_UPDATE_ERR: '餐厅<id:{restaurant_id}> ，认证更新失败，无法找到认证信息。请确认认证id是否正确。',
    BANKCARD_APPROVE_ERR: '银行卡审核不通过，请检查所填信息是否满足条件。错误类型: {error_msg}',
    BANKCARD_UPDATE_ERR: '已弃用银行卡不能修改！',
    BANKCARD_STATUS_INVALID: '启用中的银行卡不能重新直接提交审核！',
    RST_IDS_REQUIRED: u'餐厅ID不能为空',
    CERT_IMAGE_URL_ERR: '餐厅<id:{restaurant_id}> 获取验证图片失败。',
    # Coupon
    COUPON_SN_REQUIRED: u'抵价券号不能为空',
    COUPON_SN_INVALID: u'非法的抵价券号',
    COUPON_COUNT_REQUIRED: u'抵价券生成张数不能为空',
    COUPON_COUNT_INVALID: u'抵价券生成张数不能超过500',

    # Activity
    ACTIVITY_NONE_ERR: '餐厅未参与任何活动或活动id为空。',
    ACTIVITY_PAYMENT_PROC_ILL_ERR: '活动打款流程错误',

    # Region
    REGION_INVALID: '区域不合法',
    REGION_TYPE_INVALID: '区域类型不合法。',
    CITY_TRS_CFG_NOT_EXISTS: '城市<id:{city_id}>配置不存在。',
    CITY_NOT_EXISTS: '城市<id:{city_id}不存在>',
    CITY_NAME_EXISTS:'城市{city_name}已经存在',
    DIST_NAME_REDUNDANCE:'已经有相同行政区名称',
    ZONE_NAME_REDUNDANCE:'已经有相同商圈名称',

    # Operation
    BANNER_TYPE_ERR: 'Banner类型不合法。',
    BANNER_ARGS_ERR: 'Banner参数不合法。',
    BANNER_NOT_EXISTS_ERR: 'Banner<id:{banner_id}> 不存在。',

    # CS
    CS_EVENT_NOT_EXIST: '客服事件不存在 {event_id}',
    CS_EVENT_PROCESS_STATUS_INVALID: '事件处理不合法 {event_id} to {status}',

    # Misc
    IMAGE_UPLOAD_ERR: '图片上传失败！',
    FILE_UPLOAD_ERR: '文件<{file_name}>上传失败!',
    VOICE_CALL_NOT_FOUND: '语音消息<id:{call_id}> 未找到!',
    FORMAT_ERR: '无法将类型或值<{src_type}>转换为类型<{target_type}>。',
}
