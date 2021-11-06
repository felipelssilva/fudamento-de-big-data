#!/bin/bash

#FILE_MAPPER="/home2/ead2021/SEM1/l.silva17/PycharmProjects/av-s10-mapreduce/oitavo/Mapper.py"
#FILE_REDUCER="/home2/ead2021/SEM1/l.silva17/PycharmProjects/av-s10-mapreduce/oitavo/Reducer.py"
#FILE_DB="/home/Disciplinas/FundamentosBigData/OperacoesComerciais/base_100_mil.csv"

FILE_MAPPER="/home2/ead2021/SEM1/l.silva17/PycharmProjects/av-s14/empresa_1/q4/Mapper.py"
FILE_REDUCER="/home2/ead2021/SEM1/l.silva17/PycharmProjects/av-s14/empresa_1/q4/Reducer.py"
FILE_DB="/home/Disciplinas/FundamentosBigData/RelacaoComercial/Cliente.csv"
#FILE_DB="/home/Disciplinas/FundamentosBigData/RelacaoComercial/Empresa.csv"

head -1000 "$FILE_DB" | python "$FILE_MAPPER" | sort | python "$FILE_REDUCER"
#head -1000 "$FILE_DB" | python "$FILE_MAPPER" 




