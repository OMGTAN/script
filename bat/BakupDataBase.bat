:start

rem "����Զ������IP���û��������롢�ļ�·��"
set ftphost=10.108.17.27
set username=tan
set password=123456
set filepath=/home/backup/database/3306
rem "���ñ���·��"
set Ldir=D:/��Ŀ/2020/MEB����/���ݿⱸ��
set timevar=%time:~0,2%
if /i %timevar% LSS 10 (
	set timevar=0%time:~1,1%
)
set filename=db_%date:~0,4%-%date:~5,2%-%date:~8,2%-%timevar%.sql


echo cd %filepath% >>sftp.text

echo lcd %Ldir% >>sftp.text

echo get %filename% >>sftp.text

echo bye >>sftp.text



psftp -P 22 %username%@%ftphost% -pw %password% -b sftp.text

del sftp.text