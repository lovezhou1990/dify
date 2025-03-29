import sys
import os
from celery.bin.celery import main as celery_main

if (flask_debug := os.environ.get("FLASK_DEBUG", "0")) and flask_debug.lower() in {"false", "0", "no"}:
    from gevent import monkey  # type: ignore

    # gevent
    monkey.patch_all()

    from grpc.experimental import gevent as grpc_gevent  # type: ignore

    # grpc gevent
    grpc_gevent.init_gevent()

    import psycogreen.gevent  # type: ignore

    psycogreen.gevent.patch_psycopg()
# 配置 Celery worker 的参数
celery_args = [
    'celery',
    '--app', 'app.celery',
    'worker',
    '-P', 'solo',
    '--without-gossip',
    '--without-mingle',
    '-Q', 'dataset,generation,mail,ops_trace',
    '--loglevel', 'INFO'
]

# 将参数传递给 sys.argv
sys.argv = celery_args
if __name__ == '__main__':
    # 启动 Celery worker
    try:
        celery_main()
    except SystemExit as e:
        # 处理 Celery 退出异常
        print(f"Celery worker exited with code {e.code}")