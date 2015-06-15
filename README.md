Walis
=====
饿了么后台业务系统服务

* [基础环境](#基础环境)
* [开发规范](#开发规范)
* [项目结构](#项目结构)
* [部署配置](#部署配置)

***

基础环境
-------

### 环境准备

1. Clone代码

2. 搭建python虚拟化环境 (推荐 [pyenv](https://github.com/yyuu/pyenv))

    ```bash
    $ pyenv install 2.7.8
    $ pyenv virtualenv 2.7.8 rizzrack@py2.7.8
    $ pyenv activate rizzrack@py2.7.8
    ```

    或者使用 virtualenv

    ```bash
    $ mkvirtualenv zeusenv
    $ workon zeusenv
    ```

3. 连接内网

    依赖内网以下资源：zeus服务、redis、mongodb、mysql及beanstalkd等（当然也可以把服务起在本地，然后修改配置文件至本地服务）

### 环境搭建

```bash
$ make develop
```

### 运行服务（在搭建好的python虚拟化环境中）

```bash
$ make server
```

***

开发规范
-------

### 代码规范

代码书写规范参考 [python style](https://github.com/eleme/walis/blob/develop/doc/style/python.rst) 及 PEP8.

### 贡献方式

1. Fork => PR => Merge  尤其修改其他committer的代码, 多人开发**禁止直接Push Master**
2. 代码review（建议结对编程review）
3. 使用发布版本号 目前格式 `vx.x.x.x` 十进一位 (e.g. v0.3.4.5)

### 文档规范

TODO @linktime

***

项目结构
-------

### 架构图

![SOA](https://github.com/eleme/walis/blob/develop/doc/SOA.png)

### 1. 基础业务模块

目录: api, model, service, thrift

下面我们就自底向上的方式详细介绍walis的技术架构

#### Model 持久化层

a. 业务持久化

使用MySQL（可疑订单数据使用MongoDB存储），MySQL使用SQLAlchemy作为ORM

新业务的model需继承WalisModel与ModelBase:

```python
class CSEvent(WalisModel, ModelBase):
    __tablename__ = 'cs_event'

    STATUS_PENDING = 0
    STATUS_REMAIN = 1

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    user_info = Column(String)
```
*可参考 walis/model 下的代码*

b. 部分业务缓存使用redis

#### Inner 基础数据层

所有基础的数据写和查询操作均在改层封装（代码应保证业务无关性）

*可参考 walis/service/xxx/inner 下的代码*

#### Service 业务层

所有业务相关的逻辑，统一返回python dict，方便上层调用方处理

*可参考 walis/service 下的代码*

#### API 通信层

该层为外部服务提供访问接口，目前有HTTP与Thrift两种形式的接口:

a. HTTP服务

使用Flask框架为前端及其他项目提供HTTP形式的访问接口，该层分API和handler两层，
其中API列举接口形式，handler负责解析与组装HTTP参数。

*可参考 walis/api 下的代码*

b. Thrift服务

使用thriftpy搭建 Thrift server，供其他项目调用

*可参考 walis/thrift 下的代码*

### 2. 框架模块

目录: core

   ```bash
   core/
      |- api.py             # provide restful api decorator
      |- app.py             # Walis flask app model, include initialize.
      |- cmd.py             # basic debug command on console.
      |- ctx.py             # basic context
      |- exc.py             # **deprecated**
      |- log.py             # logger for framework
      |- monitor.py         # statsd monitor
      |- response.py        # response generator
      |- signal.py          # signals in framework
      |- async/             # provide async methods through beanstalkd
      |- auth/              # business auth definition and check
      |- db/                # databases such as mysql, pg, redis, mongodb
   ```

### 3. 定时任务模块

目录: scheduler

a. 使用APScheduler实现任务的定时执行

b. 定时信息在 scheduler.setting.JOB_SETTINGS 中配置

c. 任务执行脚本写在 scheduler.jobs 中，其中job_deco提供耗时记录功能

### 4. 脚本任务模块

目录: scripts

定义的所有需要临时或长期执行的一次性脚本

*建议使用print输出信息，使用logging会有权限问题*

### 5. 第三方库模块

目录: thirdparty

该模块负责整理调用来自其他模块的接口，如zeus、coffee、fuss、eyes等

其中coffee使用bluelake rpc框架，zeus、fuss等使用thrift

### 6. 异常模块

目录: exception

封装了所有walis异常，包括：

    a. 用户异常，使用raise_user_exc()
    b. 权限异常，使用raise_auth_exc()
    c. 系统异常，使用raise_server_exc()
    d. Zeus异常，使用raise_zeus_exc()
    e. 开发异常，使用raise_dev_exc()

```bash
exception/
  |- __init__.py         # 各种exception类
  |- error_code.py       # 定义业务异常code
  |- util.py             # 异常使用工具类
```

### 7. 工具类模块

目录: utils

```bash
utils/
  |- data.py            # 数据操作
  |- db.py              # 数据库操作
  |- dirty.py           # 杂项
  |- format.py          # 格式化
  |- geo.py             # 地理位置
  |- http.py            # Http
  |- lock.py            # redis锁
  |- misc.py            # 杂项
  |- model.py           # 数据结构转换
  |- module.py          # 模块加载
  |- paging.py          # 分页
  |- secret.py          # 加密
  |- thrift.py          # thrift工具
  |- time.py            # 时间转换
  |- wkb.py             # WKB相关操作
```

部署配置
-------

### 配置文件

使用根目录下的walisconfig.py作为项目配置文件，可以使用以下命令生成：

```bash
$ make config
```

### 环境部署

使用fab命令（以下例子为部署到测试环境两台机器hostname1, hostname2）：

```bash
$ fab dev:hostname1,hostname2
```
