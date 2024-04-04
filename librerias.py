from flask import Flask, request, jsonify, Blueprint, send_file
from flask_cors import CORS, cross_origin
import json
from datetime import datetime, timedelta
from supabase import create_client
import pandas as pd
from collections import Counter
