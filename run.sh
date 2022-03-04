#!/bin/bash

gunicorn -b 0.0.0.0:8766 -D app:app
