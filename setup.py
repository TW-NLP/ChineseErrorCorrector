import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ChineseErrorCorrector",  # 模块名称
    version="1.5.0",  # 当前版本
    author="tianwei",  # 作者
    author_email="1784526116@qq.com",  # 作者邮箱
    description="Syntax Error Data Enhancement",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    url="https://github.com/TW-NLP/ChineseErrorCorrector/",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'ltp==4.2.14', 'opencc==1.1.6'
    ],

    python_requires='>=3.8',
    include_package_data=True,  # 使用MANIFEST进行数据和模型的挂载

)
