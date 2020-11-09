#!/bin/bash
pidof pd | xargs kill

systemctl stop eyesy-python.service