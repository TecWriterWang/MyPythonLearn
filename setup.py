from distutils.core import setup  # 打包发布模块
# 完成下面配置后，在当前文件夹打开终端运行 python  setup.py sdist 命令，运行后悔发现一个dist文件夹里面就是打包的压缩包

setup(
    name='PackModule',
    version='0.0.1',
    description='这是打包模块测试',
    author='TecWang',
    author_email='122',
    python_module=['package.package.py']


)