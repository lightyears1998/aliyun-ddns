import json
import requests
import yaml


def main():
    keyID, keySecret, domainName, recordName = load_config()
    ip = get_ipv4_address()
    update_domain_record(keyID, keySecret, domainName, recordName)


def load_config():
    with open('config.yml') as configFile:
        config = yaml.load(configFile, Loader=yaml.BaseLoader)
        keyID, KeySecret = config["access-key"]["id"], config["access-key"]["secret"]
        domainName, recordName = config["domain-name"], config["record-name"]
    return keyID, KeySecret, domainName, recordName


def get_ipv4_address():
    ip = requests.get("https://api.ipify.org").text
    assert len(ip.split(".")) == 4, "无法查询IP地址"
    return ip


def update_domain_record(keyID, keySecret, domainName, recordName):
    record = get_domain_record(keyID, keySecret, domainName, recordName)
    recordID = record["RecordId"]


def get_domain_record(keyID, keySecret, domainName, recordName):
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest

    client = AcsClient(keyID, keySecret, 'cn-hangzhou')

    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_DomainName(domainName)
    request.set_RRKeyWord(recordName)

    response = client.do_action_with_exception(request)
    
    records = json.loads(str(response, encoding='utf-8'))["DomainRecords"]["Record"]
    records = filter(lambda record: record["RR"]==recordName and record["Type"]=="A", records)
    records = list(records)
    assert len(records) == 1, "找不到域名%s的A记录%s" % (domainName, recordName)

    return records[0]

if __name__ == "__main__":
    main()
