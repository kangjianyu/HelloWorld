from setuptools import setup,find_packages
import distutils
setup(
        name='kjy_HelloWorld',     # 包名字
        version='1.0',   # 包版本
        description='This is a test of the setup',   # 简单描述
        author='kjy',  # 作者
        author_email='609363537@qq.com',  # 作者邮箱
        url='https://github.com/kangjianyu/HelloWorld.git',      # 包的主页
        packages=find_packages(),                 # 包
)