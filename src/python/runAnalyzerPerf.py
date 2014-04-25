# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import constants

LOGS_ROOT = os.path.join(constnats.LOG_DIR, 'analyzers')

def run(cmd):
  if os.system(cmd):
    raise RuntimeError('%s failed' % cmd)

os.chdir('/l/4x.analyzers/lucene')

run('javac -d /l/util/build -cp build/core/classes/java:build/analysis/common/classes/java /l/util/src/main/perf/TestAnalyzerPerf.java')

run('svn cleanup')
run('svn up')
run('ant clean compile > compile.log 2>&1')

t = datetime.datetime.now()
ymd = then.strftime('%Y-%m-%d')
print('\n%s' % ymd)
logFile = '%s/%s.log' % (LOGS_ROOT, ymd)
open(logFile + '.tmp', 'w').write('svnversion: %s\n' % os.popen('svnversion').read().strip())
run('java -cp /l/util/build:build/core/classes/java:build/analysis/common/classes/java perf.TestAnalyzerPerf /lucenedata/enwiki/enwiki-20130102-lines.txt >> %s.tmp 2>&1' % logFile)
os.rename(logFile+'.tmp', logFile)