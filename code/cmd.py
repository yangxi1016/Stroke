# -*-coding:utf8-*-
import subprocess
import os,time







start = time.clock()
def execute_command(cmd):
  
		GADextraction.write('start executing cmd...')
    		s = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    		stderrinfo, stdoutinfo = s.communicate()
    		GADextraction.write('stderrinfo is -------> %s and stdoutinfo is -------> %s' % (stderrinfo, stdoutinfo))
    		GADextraction.write('finish executing cmd....')
    		return s.returncode
		print('Run over  (%s)...' % ( os.getpid()))
		result = execute_command(cmd)

for i in range(0, 1):
        e1 = time.time()
	JAVARUN = r'java -Xms2048m -cp .:./bin:./lib/* edu.yonsei.test.GADExtractor ./data/cnv/10sen-herbs-drugs.txt'
	cmd=JAVARUN
        relation='10-herbs-dr.txt'
        GADextraction=open(relation,'wb')
	result = execute_command(cmd)
        e2 = time.time()
	print('result:------>', result)
	print i,float(e2-e1)
end = time.clock()
print 'Running time: %s Seconds'% float(end-start)
