from data_provider.data_factory import data_provider
from exp.exp_basic import Exp_Basic
from utils.tools import EarlyStopping, adjust_learning_rate, visual
from utils.metrics import metric
import torch
import torch.nn as nn
from torch import optim
import os
import time
import warnings
import numpy as np


class LocalSetting():
	def __init__(self, kv):
		self.task_name=settings["task_name"]
		self.is_training=settings["is_training"]
		self.root_path=settings["root_path"]
		self.data_path=settings["data_path"]
		self.model_id=settings["model_id"]
		self.model=settings["model"]
		self.data=settings["data"]
		self.train_epochs=settings["train_epochs"]
		self.features=settings["features"]
		self.seq_len=settings["seq_len"]
		self.label_len=settings["label_len"]
		self.pred_len=settings["pred_len"]
		self.e_layers=settings["e_layers"]
		self.d_layers=settings["d_layers"]
		self.factor=settings["factor"]
		self.enc_in=settings["enc_in"]
		self.dec_in=settings["dec_in"]
		self.c_out=settings["c_out"]
		self.embed='timeF'
		self.batch_size=32
		self.freq='h'
		self.target='OT'
		self.seasonal_patterns='Monthly' 
		self.num_workers=10
		self.d_model=settings["d_model"]
		self.d_ff=settings["d_ff"]
		self.top_k=settings["top_k"]
		self.des=settings["des"]
		self.itr=settings["itr"]


settings={'task_name': 'long_term_forecast',
 'is_training': 1,
 'root_path': './dataset/electricity/',
 'data_path': 'electricity.csv',
 'model_id': 'ECL_96_96',
 'model': '$model_name',
 'data': 'custom',
 'train_epochs': 3,
 'features': 'M',
 'seq_len': 96,
 'label_len': 48,
 'pred_len': 96,
 'e_layers': 2,
 'embed' :'timeF',
 'd_layers': 1,
 'factor': 3,
 'enc_in': 321,
 'dec_in': 321,
 'c_out': 321,
 'd_model': 256,
 'd_ff': 512,
 'top_k': 5,
 'des': "'Exp'",
 'itr': 1}


args= LocalSetting(settings);

data_set, data_loader = data_provider(args,"train")

print(data_set)