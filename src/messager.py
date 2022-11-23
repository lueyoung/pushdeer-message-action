#!/usr/bin/env python

import argparse
import yaml
import json

from utils import str2bool, str2list, str2map

import requests

class Messager(object):
    server = "https://api2.pushdeer.com"
    endpoint = "/message/push"

    def __init__(self):
        self.parser = self._create_parser()
        self.args = self.parser.parse_args()

    def _create_parser(self):
        with open("/action.yaml", 'r') as f:
            action = yaml.safe_load(f)
        parser = argparse.ArgumentParser(description = action['description'])
        inputs = action['inputs']

        for key in inputs:
            input_args = inputs[key]
            default_value = input_args.get('default','')
            parser.add_argument(
                "--" + key.replace('_', '-'),
                type = str2bool if isinstance(default_value, bool) else str,
                required = input_args.get('required', False),
                default = default_value,
                help = input_args.get('description', '')
            )

        return parser

    def run(self):
        if not self.args.enable:
            print("Please set --enable to make messager work")
            return
        self.send()

    def send(self):
        #url = "https://api2.pushdeer.com/message/push?pushkey=" + self.args.pushkey + "&text=" + self.args.text
        print(len(self.args.pushkey))
        print(self.args.pushkey)
        res = requests.get(self.server + self.endpoint, params={
            "pushkey": str(self.args.pushkey),
            "text": str(self.args.text),
        })
        print(res.json())

def main():
    m = Messager()
    m.run()

if __name__ == "__main__":
    main()
