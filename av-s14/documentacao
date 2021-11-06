enviar as bases para o hadoop

hadoop fs -copyFromLocal /home/Disciplinas/FundamentosBigData/RelacaoComercial/Cliente.csv /databases/
hadoop fs -copyFromLocal /home/Disciplinas/FundamentosBigData/RelacaoComercial/Empresa.csv /databases/

enviar os arquivos py para o hadoop

cd /home2/ead2021/SEM1/l.silva17/PycharmProjects/av-s14
scp -P 2222 -r empresa_4/* l.silva17@localhost:s14/Empresa5 && scp -P 2222 -r empresa_5/* l.silva17@localhost:s14/Empresa5



No shell do hadoop

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q1/Mapper.py -mapper ~/s14/Empresa5/q1/Mapper.py -file ~/s14/Empresa5/q1/Reducer.py -reducer ~/s14/Empresa5/q1/Reducer.py -input /databases/Cliente.csv -output /databases/resultado_empresa5_q1 && hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q2/Mapper.py -mapper ~/s14/Empresa5/q2/Mapper.py -file ~/s14/Empresa5/q2/Reducer.py -reducer ~/s14/Empresa5/q2/Reducer.py -input /databases/Cliente.csv -output /databases/resultado_empresa5_q2 && hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q3/Mapper.py -mapper ~/s14/Empresa5/q3/Mapper.py -file ~/s14/Empresa5/q3/Reducer.py -reducer ~/s14/Empresa5/q3/Reducer.py -input /databases/Cliente.csv -output /databases/resultado_empresa5_q3 && hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q4/Mapper.py -mapper ~/s14/Empresa5/q4/Mapper.py -file ~/s14/Empresa5/q4/Reducer.py -reducer ~/s14/Empresa5/q4/Reducer.py -input /databases/Cliente.csv -output /databases/resultado_empresa5_q4 && hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q5/Mapper.py -mapper ~/s14/Empresa5/q5/Mapper.py -file ~/s14/Empresa5/q5/Reducer.py -reducer ~/s14/Empresa5/q5/Reducer.py -input /databases/Empresa.csv -output /databases/resultado_empresa5_q5 && hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/s14/Empresa5/q5/Mapper2.py -mapper ~/s14/Empresa5/q5/Mapper2.py -file ~/s14/Empresa5/q5/Reducer2.py -reducer ~/s14/Empresa5/q5/Reducer2.py -input /databases/Cliente.csv -output /databases/resultado_empresa5_q5_cl


Copiando os resultados para o Hadoop

hadoop fs -copyToLocal /databases/resultado_empresa5_q1/part-00000 s14/Empresa5/q1/resultado && hadoop fs -copyToLocal /databases/resultado_empresa5_q2/part-00000 s14/Empresa5/q2/resultado && hadoop fs -copyToLocal /databases/resultado_empresa5_q3/part-00000 s14/Empresa5/q3/resultado && hadoop fs -copyToLocal /databases/resultado_empresa5_q4/part-00000 s14/Empresa5/q4/resultado && hadoop fs -copyToLocal /databases/resultado_empresa5_q5/part-00000 s14/Empresa5/q5/resultado && hadoop fs -copyToLocal /databases/resultado_empresa5_q5_cl/part-00000 s14/Empresa5/q5/resultado_cl

Imprimindo os Resultados no hadoop

cat s14/Empresa1/q2/resultado | sort --numeric-sort
cat s14/Empresa1/q2/resultado | sort -k 2n
cat s14/Empresa1/q2/resultado | sort -k 1n
cat s14/Empresa1/q2/resultado | sort -k 1n -r

cat s14/Empresa5/q1/resultado | sort -r -n > s14/Empresa5/q1/output.txt &&  cat s14/Empresa5/q2/resultado | sort -r -n > s14/Empresa5/q2/output.txt &&  cat s14/Empresa5/q3/resultado | sort -r -n > s14/Empresa5/q3/output.txt && 
cat s14/Empresa5/q4/resultado | sort -r -n > s14/Empresa5/q4/output.txt && cat s14/Empresa5/q5/resultado | sort -r -n > s14/Empresa5/q5/output.txt && cat s14/Empresa5/q5/resultado_cl | sort -r -n > s14/Empresa5/q5/output_cl.txt


&& head s14/Empresa1/q5/output_cl.txt


upload

curl --upload-file s14/Empresa5/q1/output.txt https://transfer.sh/output.txt && curl --upload-file s14/Empresa5/q2/output.txt https://transfer.sh/output.txt && curl --upload-file s14/Empresa5/q3/output.txt https://transfer.sh/output.txt && curl --upload-file s14/Empresa5/q4/output.txt https://transfer.sh/output.txt && curl --upload-file s14/Empresa5/q5/output.txt https://transfer.sh/output.txt && curl --upload-file s14/Empresa5/q5/output_cl.txt https://transfer.sh/output_cl.txt 











