import requests
import yaml


def main():
    keyID, keySecret = load_config()
    ip = get_ipv4_address()


def load_config():
    with open('config.yml') as configFile:
        config = yaml.load(configFile, Loader=yaml.BaseLoader)
        keyID, KeySecret = config["access-key"]['id'], config["access-key"]['secret']
    return keyID, KeySecret


def get_ipv4_address() -> str:
    ip = requests.get("https://api.ipify.org").text
    assert len(ip.split(".")) == 4
    return ip


if __name__ == "__main__":
    main()
