# coding=utf-8

"""
virtualenv定制脚本接受3个扩展函数
extend_parser(optparse_parser):添加额外的选项
adjust_options(optioins, args): 改变当前的选项
after_install: 在默认的环境安装好之后，执行其他工作，通过这个函数定制
"""
import os
import logging
import subprocess
import virtualenv


virtualenv_path = subprocess.check_output(['which', 'virtualenv']).strip()
EXPORT_TEXT = ''
ROOT_PATH = '/home/python/venv'

def extend_parse(parser):
    parser.add_option('-r', '-req', action='append', type='string', dest='reqs',
                      help="specify additional required packages", default=[])

def adjust_options(options, args):
    if not args:
        return
    base_dir = args[0]
    args[0] = os.path.join(ROOT_PATH, base_dir)

def after_install(options, home_dir):
    if not options.reqs:
        logging.warning('Warn:You maybe need specify some required packages!')
    for req in options.reqs:
        subprocess.call(['{} /bin/pip'.format(home_dir), 'install', req])

def main():
    text = virtualenv.create_bootstrap_script(EXPORT_TEXT,python_version='3.5')
    print('%s' % virtualenv_path)
    with open(virtualenv_path, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()


"""
创建一个自动安装了Django, Flask的虚拟环境
>virtualenv -r django -r flask
"""