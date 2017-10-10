# -*- coding: UTF-8 -*-
import sys
reload(sys)
import MySQLdb
import os
import uniout
sys.setdefaultencoding("utf-8")

def findidmax():

   # find how many 500's we need
   qr = "SELECT count(id) FROM bingyin" #count(*) also works
   cursor.execute(qr)
   result = cursor.fetchall()
   idmx = result[0][0]
   return idmx
def selects(idmax):
   matchlist = {}
   #for i in range(0, idmax):
   #   matchlist.append("":)
   x = 0 # x = # of times
   os.system("mkdir dbfiles")
   while 1000*x < idmax:
      write1000(x, matchlist)
      x += 1
   return matchlist
def writeonefile(article, num):
   f = open(("dbfiles/a_" + str(num) + ".txt"),"w")
   f.write(article)
   f.close()
def write1000(x, matchlist):
   sql = "SELECT * FROM bingyin where id > "+str(x*1000)+ " and id <= "+str((x+1)*1000)
   #sql = "SELECT * FROM bingyin limit = 1000"
   str1 = "\n//<![CDATA[\nac_as_id = 2586;\nac_format = 0;\nac_mode = 1;\nac_group_id = 1;\nac_server_base_url = \"d-test.39.net/\";\n//]]>\n\nvar cpro_id=\"u1546723\";\n(window[\"cproStyleApi\"] = window[\"cproStyleApi\"] || {})[cpro_id]={at:\"3\",rsi0:\"200\",rsi1:\"300\",pat:\"6\",tn:\"baiduCustNativeAD\",rss1:\"#FFFFFF\",conBW:\"1\",adp:\"1\",ptt:\"0\",titFF:\"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91\",titFS:\"13\",rss2:\"#000000\",titSU:\"0\",ptbg:\"90\",piw:\"0\",pih:\"0\",ptp:\"0\"}\n"
   str2 = "\nif (!window.jQuery)\n  document.write(\"<script language=\'javascript\' src=\'http://image.39.net/hits/jquery-1.4.2.min.js\'><\/script>\");\n\n\n\n   jQuery(\'a[keycmd]\').art_ContentEvent({keycmd:\'keycmd\'});"
   str3 = "\n$(function(){\n    var _ktimer = null;\n    $(\"body\").on(\"mouseenter\", \".kmda\", function(event) {\n        event.preventDefault();\n        var _left = Math.floor($(this).offset().left),\n            _top = Math.floor($(this).offset().top);\n        clearTimeout(_ktimer);\n        $(\".kmdcBox\").css({\"left\":+_left+\"px\",\"top\":_top+30+\"px\"}).show();\n    }).on(\"mouseleave\", \".kmda\", function(event) {\n        event.preventDefault();\n        clearTimeout(_ktimer);\n        _ktimer = setTimeout(function(){\n            $(\".kmdcBox\").hide();\n        },200);\n    }).on(\"mouseenter\", \".kmdcBox\", function(event) {\n        event.preventDefault();\n        clearTimeout(_ktimer);\n        $(\".kmdcBox\").show();\n    }).on(\"mouseleave\", \".kmdcBox\", function(event) {\n        event.preventDefault();\n        clearTimeout(_ktimer);\n        _ktimer = setTimeout(function(){\n            $(\".kmdcBox\").hide();\n        },200);\n    });\n});"
   str4 = "\n\n$(function(){\n	var _ktimer = null;\n	$(\".kmda\").hover(function(){\n		var _left = Math.floor($(this).offset().left),\n			_top = Math.floor($(this).offset().top);\n		clearTimeout(_ktimer);\n		$(\".kmdcBox\").css({\"left\":+_left+\"px\",\"top\":_top+30+\"px\"}).show();\n	},function(){\n		clearTimeout(_ktimer);\n		_ktimer = setTimeout(function(){\n			$(\".kmdcBox\").hide();\n		},200);\n	});\n	$(\".kmdcBox\").hover(function(){\n		clearTimeout(_ktimer);\n		$(\".kmdcBox\").show();\n	},function(){\n		clearTimeout(_ktimer);\n		_ktimer = setTimeout(function(){\n			$(\".kmdcBox\").hide();\n		},200);\n	});\n});"
   try:
      # 执行SQL语句
      cursor.execute(sql)
      # 获取所有记录列表
      results = cursor.fetchall()

      for row in results:
         fid = row[0]
         ftitle = row[1]
         fdate = row[2]
         article = row[3].strip().replace(str1, '').replace(str2, '').replace(str3, '').replace(str4, '')
         ftype = row[4]

         writeonefile(article, fid)
         matchlist[str(fid-1)] = ftitle
         print fid
   except:
      #print "x = ", x
      print "Error: unable to fetch data"
      return 0
def main():
   matchlist = selects(findidmax())
   f1 = open("matchlist.txt", "w")
   for k,v in matchlist.iteritems():
      f1.write("a_"+str(k)+".txt"+"\t")
      f1.write(v.decode("utf8")+"\n")
   f1.close()


try:
   db = MySQLdb.connect("rm-2ze4ecy67dzly1rvao.mysql.rds.aliyuncs.com", "yutao", "Pa88word", "39tnbdata", charset="utf8")
   cursor = db.cursor()
except:
   print "unable to connect db"
main()
db.close()



