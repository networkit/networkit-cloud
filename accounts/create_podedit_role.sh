#!/bin/bash

kubectl create role podedit --verb=create,delete,deletecollection,get,list,patch,update,watch,get,list,watch --resource=pod