# 阿里云DDNS

## 安装和运行

运行环境Python 3.7，推荐使用Pipenv管理依赖。

```sh
# $Env:PIPENV_VENV_IN_PROJECT=1
pipenv install
cp config.example.yml config.yml
# 在config.yml填入必要信息
pipenv run python .
```

## 建议

1. 推荐使用[阿里云RAM](https://ram.console.aliyun.com/overview)子用户创建AccessKey。

## 参考

- [阿里云云解析DNS文档](https://help.aliyun.com/document_detail/29740.html?spm=a2c4g.11186623.6.610.7a71120a6IvKWU)
- [ipify.org](https://www.ipify.org/)
- [DescribeDomainRecords接口文档](https://help.aliyun.com/document_detail/29776.html?spm=a2c4g.11186623.6.639.5ad9124fnH3B71)
- [UpdateDomainRecord接口文档](https://help.aliyun.com/document_detail/29774.html?spm=a2c4g.11186623.2.35.4e334256TmStOV)
