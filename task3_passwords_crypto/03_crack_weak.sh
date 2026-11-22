#!/bin/bash
WORDLIST=/usr/share/wordlists/rockyou.txt

john --format=raw-md5 --wordlist="$WORDLIST" data/weak.hashes
john --format=raw-md5 --show data/weak.hashes
