

# 语法错误数据增强

针对行业语法错误数据稀缺问题，提出语法错误替换方法，可以根据领域的数据进行语法错误制作，定制化行业模型。
目前支持缺字漏字、错别字错误、缺少标点、错用标点、主语不明、谓语残缺、宾语残缺、其他成分残缺、主语多余、虚词多余、其他成分多余、语序不当、动宾搭配不当、其他搭配不当等14种细粒度错误类型的替换，也可以对一个句子进行多种错误的替换，如下：

![image](images/example.png)



### 文件目录说明
eg:

```
CGED_DAT 
├── README.md
├── cged_dat.py
├── config.py
├── /data/
│  ├── /dat_data/
│  │  ├── confuse_obj_v.json
│  │  ...
│  │  └── token_set.txt
├── /pre_model/
│  ├── /ltp_small/
│  │  

```

### 模型文件下载

pre_model下的ltp_small,下载地址：https://huggingface.co/LTP/small

### 获得2024CCL Task7 一等奖
2024CCL Task7: https://github.com/cubenlp/2024CCL_CEFE
博客经验分享：https://www.cnblogs.com/twnlp/p/18208637
评测论文：待发表







