#!/bin/bash
echo "shell level:$SHLVL"
ssh -p 2220 -i ./id_rsa_26 bandit26@176.9.9.172
